provider "aws" {
    region = var.region
}






data "aws_vpc" "default" {
    default = true
}






data "aws_subnets" "default" {
    filter {
        name   = "vpc-id"
        values = [data.aws_vpc.default.id]
    }
}








resource "aws_security_group" "k3s_sg" {
    name        = "${var.project_name}-sg"
    description = "Allow SSH, k3s, and NodePort"
    vpc_id      = data.aws_vpc.default.id


    ingress {
        description = "SSH"
        from_port   = 22
        to_port     = 22
        protocol    = "tcp"
        cidr_blocks = ["0.0.0.0/0"]
    }

    ingress {
        description  = "Kubernetes NodePort"
        from_port    = 30000
        to_port      = 32767
        protocol     = "tcp"
        cidr_blocks  = ["0.0.0.0/0"]
    }


    ingress {
        description  = "k3s API"
        from_port    = 6443
        to_port      = 6443
        protocol     ="tcp"
        cidr_blocks  = ["0.0.0.0/0"]
    }


    egress {
        from_port = 0
        to_port   = 0
        protocol  = "-1"
        cidr_blocks  = ["0.0.0.0/0"]
    }
}









resource "aws_iam_role" "ec2_role" {
    name = "${var.project_name}-role"


    assume_role_policy = jsonencode({
        Version       = "2012-10-17"
        Statement     = [{
            Effect    = "Allow"
            Principal = {Service = "ec2.amazonaws.com"}
            Action    = "sts:AssumeRole"
        }]
    })
}





resource "aws_iam_role_policy_attachment" "ecr_read" {
  role       = aws_iam_role.ec2_role.name
  policy_arn = "arn:aws:iam::aws:policy/AmazonEC2ContainerRegistryReadOnly"
}






resource "aws_iam_instance_profile" "ec2_profile" {
  name = "${var.project_name}-profile"
  role = aws_iam_role.ec2_role.name
}



data "aws_ami" "ubuntu" {
  most_recent = true
  owners      = ["099720109477"]

  filter {
    name   = "name"
    values = ["ubuntu/images/hvm-ssd/ubuntu-jammy-22.04-amd64-server-*"]
  }
}




resource "aws_instance" "k3s_node" {
  ami                    = data.aws_ami.ubuntu.id
  instance_type          = var.instance_type
  subnet_id              = data.aws_subnets.default.ids[0]
  vpc_security_group_ids = [aws_security_group.k3s_sg.id]
  key_name               = var.key_name

  iam_instance_profile = aws_iam_instance_profile.ec2_profile.name

  tags = {
    Name = var.project_name
  }
}





