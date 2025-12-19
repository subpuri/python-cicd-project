variable "region" {
    description = "AWS region"
    default = "us-east-1"
}

variable "instance_type" {
    description = "Free tier EC2 instance type"
    default = "t3.micro"
}

variable "key_name" {
    description = "Existing EC2 key pair name"
    type = string
}

variable "project_name" {
    description = "Project tag/name"
    default = "infraops-k3s"
}

