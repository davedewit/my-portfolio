import boto3
import zipfile
import StringIO
import mimetypes

def lambda_handler(event, context):
    sns = boto3.resource('sns')
    topic = sns.Topic('arn:aws:sns:ap-southeast-2:114366766218:DeployPortfolioTopic')

    try:
        s3 = boto3.resource('s3')

        portfolio_bucket = s3.Bucket('portfolio.dewit.com.au')
        build_bucket = s3.Bucket('build.dewit.com.au')

        portfolio_zip = StringIO.StringIO()
        build_bucket.download_fileobj('buildportfolio.zip', portfolio_zip)

        with zipfile.ZipFile(portfolio_zip) as myzip:
            for nm in myzip.namelist():
                obj = myzip.open(nm)
                portfolio_bucket.upload_fileobj(obj, nm, ExtraArgs={'ContentType': 'basestring'})
                portfolio_bucket.Object(nm).Acl().put(ACL='public-read')

        print "Job Done!"

        topic.publish(Subject="Test #2", Message="The medium is the message.")
    except:
        topic.publish(Subject="Portfolio Deploy failed", Message="The Portfolio was not deployed successfully!")
