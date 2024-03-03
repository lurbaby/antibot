
module "ec2_module" {
	source = "./ec2_module"
	security_group_id = module.sg_module.security_group_id 	 
}

module "sg_module" {
	source = "./sg_module"
}
#resource "aws_ecr_repository" "lurbaby-ecr" {
#  name = "lurbaby-ecr" 
#}

#run with -backend-config="backends/dev.tfvars"
#terraform import aws_ecr_repository.lurbaby-ecr lurbaby-ecr one-time

