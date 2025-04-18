import boto3

client = boto3.client('s3')


def deploy_s3(bucket_name):
    response = client.create_bucket(
    Bucket = bucket_name
)

bucket_name = input("Give a unique S3 bucket you want to create: ")
deploy_s3(bucket_name)
