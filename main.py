from checks.s3_checks import audit_s3_buckets
from checks.ec2_checks import audit_ec2_security_groups
from checks.iam_checks import audit_iam_users
from risk.risk_engine import calculate_risk_score
from reports.report_generator import generate_csv_report


def main():
    findings = []

    print("Starting AWS Cloud Security Audit...\n")

    findings.extend(audit_s3_buckets())
    findings.extend(audit_ec2_security_groups())
    findings.extend(audit_iam_users())

    generate_csv_report(findings)
    risk_score = calculate_risk_score(findings)

    print("Audit Completed Successfully")
    print(f"Total Findings: {len(findings)}")
    print(f"Overall Risk Score: {risk_score}")
    print("Report generated: output/security_report.csv")


if __name__ == "__main__":
    main()
