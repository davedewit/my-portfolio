import boto3

import StringIO
import mimetypes

def lambda_handler(event, context):
    sns = boto3.resource('sns')
    topic = sns.Topic('arn:aws:sns:ap-southeast-2:114366766218:DeployPortfolioTopic')

    s3 = boto3.resource('s3')

    portfolio_bucket = s3.Bucket('portfolio.dewit.com.au')
    portfolio_bucket.Object(nm).Acl().put(ACL='public-read')
