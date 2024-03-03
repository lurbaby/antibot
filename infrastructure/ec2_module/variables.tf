variable "ami" {
	default = "ami-0faab6bdbac9486fb"
}

variable "instance_type" {
	default = "t2.micro"
}

variable "security_group_id" {
	type = string 
}

variable "key_name" {
	default = "kali_main_rsa_aws" 
}


variable "subnet_id" {
	default = "subnet-0977cf3277542ac72" 
}
