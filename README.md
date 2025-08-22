# 🚀 Provisioning EC2 Instances using AWS Lambda + API Gateway

The project demonstrates provisioning of AWS EC2 using a serverless architecture using:
- AWS Lambda - which is a serverless service that allows users to run code without managing servers. Once run, AWS handles the underlying infrastructure, including server provisioning, patching and maintainence.
- API Gateway - which allows us to create, publish, monitor and secure APIs. Here, HTTP API is used to send request to AWS Lambda.
- Boto3 - which is a Python module that allows us to interact with AWS and has the ability to perform operations such as creating and managing EC2 instances, S3 buckets, Lambda functions, etc.
  
## 📌 Objective

To  build a serverless API endpoint that provisions a new EC2 instance when a POST request is made. 

## Tools and Services 
- AWS Lambda
- AWS API Gateway
- AWS IAM
- AWS EC2
- Postman
- Python 3 (boto3)

## Steps 
### Step 1: Create Ec2 Key Pair
