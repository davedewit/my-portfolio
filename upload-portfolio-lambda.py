import boto3

def lambda_handler(event, context):
    sns = boto3.resource('sns')
    topic = sns.Topic('arn:aws:sns:ap-southeast-2:114366766218:DeployPortfolioTopic')


    print "Job Done!"
    topic.publish(Subject="Test #2", Message="Portfolio deployed successfully!.")
