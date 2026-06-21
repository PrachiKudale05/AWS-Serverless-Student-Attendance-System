# AWS-Serverless-Student-Attendance-System

## Project Summary

Designed and implemented a serverless attendance management system on AWS that automatically records student attendance, generates attendance confirmation audio, and stores attendance records in the cloud.

The solution leverages event-driven and serverless AWS services to automate attendance processing, reduce manual effort, and demonstrate real-world cloud application development.

---

## Key Highlights

* Built a fully serverless architecture using AWS services
* Automated attendance recording through REST APIs
* Implemented request processing using AWS Lambda
* Stored attendance records in Amazon DynamoDB
* Generated attendance confirmation audio using Amazon Polly
* Stored MP3 audio files in Amazon S3
* Configured IAM roles and CloudWatch monitoring
* Eliminated manual attendance tracking through automation

---

## Architecture

User Request → Amazon API Gateway → AWS Lambda → Amazon DynamoDB

AWS Lambda → Amazon Polly → Amazon S3 (MP3 Storage)

AWS Lambda → Amazon CloudWatch (Monitoring & Logs)

---

## Technologies Used

### AWS Services

* Amazon API Gateway
* AWS Lambda
* Amazon DynamoDB
* Amazon Polly
* Amazon S3
* AWS IAM
* Amazon CloudWatch

### Programming Language

* Python

### Database

* Amazon DynamoDB

---

## Workflow

1. User submits Student ID and Student Name through an API request.
2. Amazon API Gateway receives the request.
3. AWS Lambda processes the attendance request.
4. Student attendance information is stored in Amazon DynamoDB.
5. Amazon Polly generates an attendance confirmation audio message.
6. Lambda saves the generated MP3 file in Amazon S3.
7. CloudWatch logs capture execution and monitoring details.

---

## Sample Output

### Attendance Record

Student ID: 105

Student Name: Prachi

### Generated Audio File

105_Prachi.mp3

### Audio Message

"Attendance verification completed successfully. Student Prachi has been marked present."

---

## Skills Demonstrated

* Serverless Computing
* Event-Driven Architecture
* Cloud Automation
* AWS Security & IAM
* API Development
* Database Integration
* Python Development
* Cloud Monitoring
* Text-to-Speech Integration
* AWS Service Integration

---

## Business Value

This solution demonstrates how cloud-native architectures can automate attendance management, improve operational efficiency, reduce manual record keeping, and provide scalable attendance tracking without managing servers.

---

## Future Enhancements

* Face Recognition Attendance Verification
* Attendance Analytics Dashboard
* Email & SMS Notifications
* Mobile Application Integration
* Multi-Class Attendance Management

---

## Author

**Prachi Kudale**

AWS Cloud | Python Developer | DevOps Enthusiast
