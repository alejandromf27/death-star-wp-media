provider "aws" {
    region = "us-east-1"
    access_key = "YOUR_AWS_ACCESS_KEY"
    secret_key = "YOUR_AWS_SECRET_KEY"
}

resource "aws_security_group" "death_star_allow_tls" {
  name        = "death_star_allow_tls"
  description = "Allow HTTP and SSH inbound traffic"

  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
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
    Name = "death_star_allow_tls"
  }
}

resource "aws_instance" "death_star" {
    ami = "ami-07ebfd5b3428b6f4d"
    instance_type = "t2.micro"
    security_groups = ["${aws_security_group.death_star_allow_tls.name}"]
    key_name = "YOUR_AWS_SSH_KEY_PAIR"
    tags = {
        Name = "terraform-death_star"
    }
}

output "IP" {
    value = "${aws_instance.death_star.public_ip}"
}