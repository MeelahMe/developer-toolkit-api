# Deployment

Infrastructure is provisioned with Terraform, defining an EC2 instance and a security group in AWS. The instance runs Amazon Linux, installs Docker on boot, clones this repository, builds the application image, and starts the container automatically.

## Provisioning

```bash
cd terraform
terraform init
terraform plan
terraform apply
```

`terraform plan` displays every resource that would be created before any changes are made. `terraform apply` requires explicit `yes` confirmation before creating real infrastructure.

## What gets created

- **A security group** allowing inbound traffic on port 22 (SSH) and port 8000 (API access), with unrestricted outbound traffic.
- **A `t2.micro` EC2 instance** running the most recent Amazon Linux 2023 AMI, with a startup script (`user_data`) that installs Docker, clones this repository, builds the Docker image, and runs the container on port 8000.

## Verified behavior

This configuration was applied to a real AWS account and verified end-to-end:

- The root endpoint (`/`) responded correctly over the public internet at the instance's assigned IP address.
- An authenticated endpoint correctly returned `500 Server API key is not configured` when queried without an `API_KEY` environment variable set on the instance. This confirms the authentication safeguard added in [authentication.md](authentication.md) behaves correctly on real infrastructure, not only in local development and CI.

## Security group scope

The security group allows SSH access from any IP address (`0.0.0.0/0`). This is a deliberate scope decision for a short-lived demo instance, not a production configuration. A production deployment would restrict SSH access to specific known IP ranges, or remove direct SSH access entirely in favor of AWS Systems Manager Session Manager.

## Teardown

Infrastructure was destroyed immediately after verification to avoid ongoing cost:

```bash
terraform destroy
```

Terraform displays every resource to be destroyed and requires explicit `yes` confirmation. Deletion was confirmed both through Terraform's own output and independently through the AWS EC2 console.

## Planned improvements

- Pass `API_KEY` into the instance securely (for example, through AWS Systems Manager Parameter Store) rather than leaving it unconfigured.
- Use an Elastic IP or a load balancer, so the public address does not change between deployments.
- Replace the direct GitHub clone in `user_data` with a pre-built image pulled from a container registry (for example, Amazon ECR).
