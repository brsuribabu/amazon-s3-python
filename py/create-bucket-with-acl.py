# Create the S3 Bucket with the ACL and Public Access
import boto3

s3 = boto3.resource('s3')

bucket = s3.Bucket('awssa-dn-test4')

response = bucket.create()

print(response)