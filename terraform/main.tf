terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = "us-east-1"
}

resource "aws_security_group" "api_sg" {
  name        = "developer-toolkit-api-sg"
  description = "Allow SSH and API access"

  ingress {
    description = "SSH access"
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    description = "API access"
    from_port   = 8000
    to_port     = 8000
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "developer-toolkit-api-sg"
  }

}
terraform $ cat ec2.tf
data "aws_ami" "amazon_linux" {
  most_recent = true
  owners      = ["amazon"]

  filter {
    name   = "name"
    values = ["al2023-ami-*-x86_64"]
  }
}

resource "aws_instance" "api_server" {
  ami                    = data.aws_ami.amazon_linux.id
  instance_type          = "t2.micro"
  vpc_security_group_ids = [aws_security_group.api_sg.id]

  user_data = <<-EOF
    #!/bin/bash
    yum install -y docker git
    systemctl start docker
    systemctl enable docker
    git clone https://github.com/MeelahMe/developer-toolkit-api.git /home/ec2-user/app
    cd /home/ec2-user/app
    docker build -t developer-toolkit-api .
    docker run -d -p 8000:8000 --name dev-tools-api developer-toolkit-api
  EOF

  tags = {
    Name = "developer-toolkit-api-instance"
  }
}

output "instance_public_ip" {
  value       = aws_instance.api_server.public_ip
  description = "Public IP address of the running API instance"
}
terraform $ cat main.tf 
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = "us-east-1"
}

resource "aws_security_group" "api_sg" {
  name        = "developer-toolkit-api-sg"
  description = "Allow SSH and API access"

  ingress {
    description = "SSH access"
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    description = "API access"
    from_port   = 8000
    to_port     = 8000
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "developer-toolkit-api-sg"
  }

}
