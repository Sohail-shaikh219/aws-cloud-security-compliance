import boto3
from botocore.exceptions import ClientError


def audit_iam_users():
    iam = boto3.client("iam")
    findings = []

    try:
        users = iam.list_users()["Users"]
    except ClientError as e:
        print("Error listing IAM users:", e)
        return findings

    for user in users:
        username = user["UserName"]

        # 1️⃣ MFA check
        try:
            mfa_devices = iam.list_mfa_devices(UserName=username)
            if not mfa_devices["MFADevices"]:
                findings.append([
                    username,
                    "MFA not enabled for IAM user",
                    "MEDIUM"
                ])
        except ClientError:
            pass

        # 2️⃣ Administrator access check
        try:
            policies = iam.list_attached_user_policies(UserName=username)
            for policy in policies["AttachedPolicies"]:
                if policy["PolicyName"] == "AdministratorAccess":
                    findings.append([
                        username,
                        "AdministratorAccess policy attached",
                        "HIGH"
                    ])
        except ClientError:
            pass

    return findings
