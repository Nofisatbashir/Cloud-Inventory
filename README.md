# Cloud-Based Inventory-Management-WebApp
The Cloud-Based Inventory Management Application is a scalable web application designed to help businesses efficiently manage stock levels in real time. The system enables users to track inventory, monitor low-stock thresholds, and receive automated alerts, all hosted on cloud infrastructure for reliability and scalability.

## Key Features
Real-time inventory tracking
Low-stock threshold configuration
Automated email notifications for low inventory
Secure cloud-hosted backend
Containerized application for portability
Managed database for persistent data storage
Scalable deployment on AWS

## System Architecture
The application is built using a containerized microservice architecture and deployed on Amazon Web Services (AWS).
Core Components:
Docker for containerization
Amazon Elastic Container Registry (ECR) for image storage
Amazon ECS (Fargate) for container orchestration
Amazon RDS (MySQL) for inventory data storage
Amazon SNS for email notifications
Amazon S3 for asset storage
AWS IAM for access control
Amazon CloudWatch for monitoring and logging

## Deployment Workflow
Develop and test the application locally.
Containerize the application using Docker.
Push Docker images to Amazon ECR.
Deploy containers using Amazon ECS (Fargate).
Configure database using Amazon RDS.
Set up low-stock alert triggers using AWS SNS and Lambda.
Monitor application performance with CloudWatch.

## Low-Stock Alert Logic
Inventory levels are continuously monitored.
When stock falls below the defined threshold:

A trigger is activated.

An email notification is sent to the admin via AWS SNS




