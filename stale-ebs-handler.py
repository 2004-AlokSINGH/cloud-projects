import boto3
import logging
from botocore.exceptions import ClientError

# Setup structured logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def get_active_instance_ids(ec2_client):
    """Retrieve all running EC2 instance IDs."""
    try:
        response = ec2_client.describe_instances(Filters=[
            {'Name': 'instance-state-name', 'Values': ['running']}
        ])
        instance_ids = {
            instance['InstanceId']
            for reservation in response['Reservations']
            for instance in reservation['Instances']
        }
        return instance_ids
    except ClientError as e:
        logger.error(f"Error fetching running instances: {e}")
        return set()

def is_volume_attached_to_running_instance(ec2_client, volume_id):
    """Check if a volume is attached to any instance."""
    try:
        response = ec2_client.describe_volumes(VolumeIds=[volume_id])
        attachments = response['Volumes'][0]['Attachments']
        return bool(attachments)
    except ClientError as e:
        if e.response['Error']['Code'] == 'InvalidVolume.NotFound':
            return False
        logger.error(f"Error describing volume {volume_id}: {e}")
        return False

def delete_snapshot(ec2_client, snapshot_id, reason):
    """Delete the given snapshot and log the reason."""
    try:
        ec2_client.delete_snapshot(SnapshotId=snapshot_id)
        logger.info(f"Deleted snapshot {snapshot_id}: {reason}")
    except ClientError as e:
        logger.error(f"Failed to delete snapshot {snapshot_id}: {e}")

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')
    
    try:
        # Get all snapshots owned by this account
        snapshots_response = ec2.describe_snapshots(OwnerIds=['self'])
        active_instance_ids = get_active_instance_ids(ec2)

        for snapshot in snapshots_response['Snapshots']:
            snapshot_id = snapshot['SnapshotId']
            volume_id = snapshot.get('VolumeId')

            if not volume_id:
                delete_snapshot(ec2, snapshot_id, "Not attached to any volume.")
                continue

            if not is_volume_attached_to_running_instance(ec2, volume_id):
                delete_snapshot(ec2, snapshot_id, f"Volume {volume_id} not attached to any running instance.")

    except Exception as e:
        logger.exception("Unhandled error occurred during snapshot cleanup.")
