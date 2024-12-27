provider "aws" {
  region = var.aws_region
}

module "vpc" {
  source = "terraform-aws-modules/vpc/aws"
  name = "threat-intel-vpc"
  cidr = "10.0.0.0/16"
  azs = ["us-east-1a", "us-east-1b"]
  private_subnets = ["10.0.1.0/24", "10.0.2.0/24"]
  public_subnets  = ["10.0.101.0/24", "10.0.102.0/24"]
  enable_nat_gateway = true
}

module "ecs" {
  source = "terraform-aws-modules/ecs/aws"
  name = "threat-intel-cluster"
  container_insights = true
  capacity_providers = ["FARGATE"]
  default_capacity_provider_strategy = [
    {
      capacity_provider = "FARGATE"
      weight = 1
    }
  ]
}

module "rds" {
  source = "terraform-aws-modules/rds/aws"
  identifier = "threat-intel-db"
  engine = "postgres"
  engine_version = "13.7"
  instance_class = "db.t3.medium"
  allocated_storage = 20
  db_name = "threat_intel"
  username = var.db_username
  password = var.db_password
  vpc_security_group_ids = [aws_security_group.rds.id]
  subnet_ids = module.vpc.private_subnets
}