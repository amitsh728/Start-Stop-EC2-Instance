import boto3

# Enter the region your instances are in.
# Include only the region without specifying Availability Zone; e.g., 'us-east-1'
REGION = 'us-west-2'
SNS_TOPIC = 'arn:aws:sns:us-west-2:123456789101:Test_Topic'


def lambda_handler(json_input, context):
    # instance_id = json.loads(json_input)
    instances = []
    instance_id = json_input["InstanceID"]
    instances.append(instance_id)
    ec2 = boto3.client('ec2', region_name=REGION)
    ec2.start_instances(InstanceIds=instances)
    sns = boto3.client("sns")
    response = sns.publish(
        TopicArn=SNS_TOPIC,
        Message=(str('Started your instance: ' + str(instances))),
        Subject="Instance Started"
    )
