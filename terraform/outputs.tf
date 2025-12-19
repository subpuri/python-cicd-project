output "ec2_public_ip" {
  value = aws_instance.k3s_node.public_ip
}

output "ssh_command" {
  value = "ssh ubuntu@${aws_instance.k3s_node.public_ip}"
}
