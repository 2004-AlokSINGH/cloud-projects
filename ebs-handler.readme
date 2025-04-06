
# 🧹 AWS Lambda: EBS Snapshot Cleanup Automation

This project contains an AWS Lambda function that automatically identifies and deletes unused **EBS snapshots** to help reduce unnecessary storage costs and keep your AWS environment clean and efficient.

---

## 📌 Overview

Amazon EBS (Elastic Block Store) snapshots are often created during backups or by automation tools. Over time, unused or orphaned snapshots accumulate, consuming storage and increasing AWS billing costs.

This Lambda function safely deletes:

- 📦 Snapshots not associated with any volume  
- 🔌 Snapshots of volumes not attached to any running EC2 instance  

This ensures only meaningful snapshots are retained.

---

## ✨ Features

- ✅ Automated cleanup of unused EBS snapshots  
- ✅ Supports snapshots associated with deleted or unused volumes  
- ✅ Filters out volumes not attached to any **running** EC2 instance  
- ✅ Modular code with clean logging  
- ✅ Industry-standard structure and error handling  
- ✅ Easy to deploy using the AWS Lambda console  

---

## 📁 Project Structure

```
ebs-snapshot-cleanup/
├── lambda_function.py    # Main Lambda code
├── README.md             # This documentation
```

---

## 🛠️ Setup Guide

### 1. ✅ Create IAM Role for Lambda

Assign the following IAM policy to the Lambda's execution role:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "ec2:DescribeInstances",
        "ec2:DescribeVolumes",
        "ec2:DescribeSnapshots",
        "ec2:DeleteSnapshot"
      ],
      "Resource": "*"
    }
  ]
}
```

---

### 2. 🚀 Create Lambda Function

- Go to [AWS Lambda Console](https://console.aws.amazon.com/lambda/)
- Click **Create Function**
- Choose **Author from scratch**
- Set the following:
  - **Function name**: `ebs-snapshot-cleaner`
  - **Runtime**: `Python 3.9` (or latest)
  - **Execution role**: Choose the IAM role created above

---

### 3. 📤 Upload the Code

- Replace the default function code with the contents of `lambda_function.py`
- Set **Handler name**: `lambda_function.lambda_handler`
- Click **Deploy**

---

### 4. ⏰ Automate with Schedule (Optional)

To run the Lambda periodically:

- Go to **Amazon EventBridge (CloudWatch Events)**
- Create a **Rule**
- Choose **Schedule**:
  - Expression example: `rate(1 day)`
- Add the Lambda function as the target

---

## 📜 Sample Log Output

Captured in **CloudWatch Logs**:

```
Deleted EBS snapshot snap-0123456789abcdef0 as it was not attached to any volume.
Deleted EBS snapshot snap-0fedcba9876543210 as its associated volume was not attached to any running instance.
```

---

## 📦 Requirements

- AWS Lambda (Python Runtime)  
- AWS IAM Role with EC2 read/delete snapshot permissions  
- Boto3 (comes pre-installed in Lambda)

---

## 🔮 Possible Enhancements

- [ ] Add SNS or email notification for deleted snapshots  
- [ ] Add support for tag-based exclusion  
- [ ] Add dry-run mode  
- [ ] Export deletion report to Amazon S3  
- [ ] Multi-region cleanup support

---
