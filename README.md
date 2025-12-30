# AWS Cloud Security Compliance & Risk Assessment Tool

## 📌 Overview
This project is a Python-based AWS Cloud Security Compliance and Risk Assessment tool designed to audit AWS accounts for common security misconfigurations.  
It helps identify security risks across AWS services and generates a structured compliance report.

The tool is built using **AWS SDK (boto3)** and follows real-world cloud security auditing practices used in enterprises.

---

## 🎯 Key Features
- 🔐 Audits **IAM users** for security best practices
- 🪣 Scans **S3 buckets** for public access misconfigurations
- 🌐 Analyzes **EC2 security groups** for open ports
- ⚠️ Assigns **risk levels** (LOW / MEDIUM / HIGH)
- 📊 Calculates an **overall risk score**
- 📁 Generates a **CSV security compliance report**
- 🧩 Modular and extensible architecture

---

## 🛠️ AWS Services Used
- AWS IAM
- Amazon S3
- Amazon EC2
- AWS STS

---

## 🧰 Tech Stack
- Python 3
- AWS CLI
- boto3 (AWS SDK for Python)
- Linux (Ubuntu)
- Git & GitHub

---

## 📂 Project Structure
aws-cloud-security-compliance/
│
├── checks/
│ ├── iam_checks.py
│ ├── s3_checks.py
│ └── ec2_checks.py
│
├── risk/
│ └── risk_engine.py
│
├── reports/
│ └── report_generator.py
│
├── output/
│ └── security_report.csv
│
├── config.py
├── main.py
├── requirements.txt
└── README.md

---

## ⚙️ How It Works
1. The tool authenticates with AWS using configured IAM credentials
2. Security checks are performed on IAM, S3, and EC2 resources
3. Findings are classified based on severity
4. A cumulative risk score is calculated
5. Results are exported as a CSV compliance report

---

## 🚀 How to Run the Project

### 1️⃣ Configure AWS CLI
```bash
aws configure
2️⃣ Install Dependencies
bash
Copy code
pip install -r requirements.txt
3️⃣ Run the Audit
bash
Copy code
python main.py
4️⃣ View Report
bash
Copy code
cat output/security_report.csv
📈 Sample Findings
IAM user without MFA enabled

S3 bucket with public access block disabled

EC2 security group allowing public access on sensitive ports

🔐 Security Note
No AWS credentials are hardcoded

.gitignore prevents sensitive data from being committed

Uses least-privilege IAM access

📌 Use Case
Cloud Security Audits

DevOps & Cloud Internships

Security Compliance Checks

Learning AWS Security Best Practices

🧠 Future Enhancements
CloudWatch & Config rule integration

JSON & HTML report formats

Multi-account scanning

CI/CD security integration

Email or Slack alerts
