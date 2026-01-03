# AWS utility


## Build Amazon EC2 AMI using Packer
```bash
# Switch to AWS utility directory.
$ cd <PROJECT_ROOT_DIR>

# Initialize Packer module.
$ packer init aws/ec2/ami/amazon-linux-2023.pkr.hcl

# Validate Packer module.
$ packer validate aws/ec2/ami/amazon-linux-2023.pkr.hcl

# Build VM image using Packer module.
$ packer build aws/ec2/ami/amazon-linux-2023.pkr.hcl
```


## Manage Amazon EC2 instances using Python AWS SDK.
```bash
# Switch to AWS utility directory.
$ cd <PROJECT_ROOT_DIR>

# Start Amazon EC2 instance.
$ python aws/ec2/instance/manage.py start <INSTANCE_ID>

# Stop Amazon EC2 instance.
$ python aws/ec2/instance/manage.py stop <INSTANCE_ID>

# Terminate Amazon EC2 instance.
$ python aws/ec2/instance/manage.py terminate <INSTANCE_ID>
```