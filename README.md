<img src="https://s3-ap-south-1.amazonaws.com/amitcloud/work.amit.cloud/wp-content/uploads/2019/04/19101016/logo.svg?sanitize=true" height="50">

Checkout my profile and other projects at [amit.cloud](http://work.amit.cloud)

# Start / Stop EC2 Instances
These scripts aims to start / stop ec2 instances when triggered. 
These scripts could be triggered from events like cronjob or cloudwatch rules.
### Usage with AWS CloudWatch Rules:
1. Login to AWS Console.
2. Create Lambda Functions one each with start_ec2_instance.py and stop_ec2_instance.py  
3. Goto AWS Cloudwatch.
4. In Cloudwatch, under **Events**, click on **Rules**. 
5. Click on Create Rule.
6. Configure the event source to trigger at a particular time.
7. Configure the targets to trigger the lambda functions (to start/stop instances).
8. Configure the Input for lambda as  constant json: {"InstanceID":"<instanceID of the concerned instance>"}
     >Example:  {"InstanceID":"i-09301238312312431"}

### Use Case:
These scripts are useful when you wish to start or stop certain ec2 instances. These techniques are greatly useful to reduce the monthly bill of a project.

### Other Details
- Python Version = 3.7.2
- Boto3 Version = 1.9.188