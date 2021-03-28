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

resource "aws_kinesis" "aws_kinesis" {
	
}

resource "aws_kinesis_firehose" "aws_kinesis_data_firehose" {
  
}

resource "aws_s3" "aws_s3_events_bucket" {
  
}