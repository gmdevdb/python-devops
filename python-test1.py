import boto3
from botocore.exceptions import ClientError

# Set the IAM username you want to inspect
username = "devops-user2"

# Create an IAM client
iam = boto3.client("iam")

try:
    # Fetch the list of access keys
    response = iam.list_access_keys(UserName=username)['AccessKeyMetadata']
    print(response)
    for key in response:
            print(f" access key {key['AccessKeyId']}")

except Exception as e:
    print("Oops, something went wrong:", e)
