terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 3.27"
    }
  }
}

variable "access_key" {}
variable "secret_key" {}

provider "aws" {
  profile = "default"
  region  = "us-east-1"
  access_key = "${var.access_key}"
  secret_key = "${var.secret_key}"
}

resource "aws_lambda_function" "user_event_lambda" {
	
}

resource "aws_lambda_function" "user_utm_lambda" {
  
}

resource "aws_sns" "tracking_events_sns" {
  
}

resource "aws_sqs" "sns_user_event_dead_letter_queue" {
  
}

resource "aws_sqs" "sns_user_utm_dead_letter_queue" {
  
}


resource "aws_sqs" "user_event_backup_dead_letter_queue" {
  
}

resource "aws_sqs" "user_event_backup_queue" {
  
}

resource "aws_sqs" "user_utm_backup_dead_letter_queue" {
  
}

resource "aws_sqs" "user_utm_backup_queue" {
  
}

resource "aws_redshift" "redshift_cluster_1" {
  
}

resource "aws_iam" "iam_user" {
  
}