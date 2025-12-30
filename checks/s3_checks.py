import boto3
from botocore.exceptions import ClientError


def audit_s3_buckets():
    s3 = boto3.client("s3")
    findings = []

    try:
        buckets = s3.list_buckets()["Buckets"]
    except ClientError as e:
        print("Error listing S3 buckets:", e)
        return findings

    for bucket in buckets:
        bucket_name = bucket["Name"]

        # 1️⃣ Check ACL for public access
        try:
            acl = s3.get_bucket_acl(Bucket=bucket_name)
            for grant in acl["Grants"]:
                if "AllUsers" in str(grant) or "AuthenticatedUsers" in str(grant):
                    findings.append([
                        bucket_name,
                        "Public ACL detected on S3 bucket",
                        "HIGH"
                    ])
                    break
        except ClientError:
            pass

        # 2️⃣ Check Public Access Block
        try:
            pab = s3.get_public_access_block(Bucket=bucket_name)
            config = pab["PublicAccessBlockConfiguration"]

            if not all(config.values()):
                findings.append([
                    bucket_name,
                    "S3 Public Access Block not fully enabled",
                    "MEDIUM"
                ])
        except ClientError:
            findings.append([
                bucket_name,
                "S3 Public Access Block not configured",
                "MEDIUM"
            ])

    return findings
