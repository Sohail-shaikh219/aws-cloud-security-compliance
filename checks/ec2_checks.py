import boto3
from botocore.exceptions import ClientError


def audit_ec2_security_groups():
    ec2 = boto3.client("ec2")
    findings = []

    try:
        response = ec2.describe_security_groups()
        security_groups = response["SecurityGroups"]
    except ClientError as e:
        print("Error fetching security groups:", e)
        return findings

    for sg in security_groups:
        sg_id = sg["GroupId"]
        sg_name = sg.get("GroupName", "N/A")

        for rule in sg.get("IpPermissions", []):
            from_port = rule.get("FromPort")
            to_port = rule.get("ToPort")

            for ip_range in rule.get("IpRanges", []):
                cidr = ip_range.get("CidrIp")

                if cidr == "0.0.0.0/0":
                    if from_port == 22:
                        findings.append([
                            f"{sg_name} ({sg_id})",
                            "SSH (22) open to the world",
                            "HIGH"
                        ])
                    elif from_port == 3389:
                        findings.append([
                            f"{sg_name} ({sg_id})",
                            "RDP (3389) open to the world",
                            "HIGH"
                        ])
                    else:
                        findings.append([
                            f"{sg_name} ({sg_id})",
                            f"Port {from_port}-{to_port} open to the world",
                            "MEDIUM"
                        ])

    return findings
