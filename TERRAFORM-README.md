Download and install Terraform

    1. Download terraform from official site (https://www.terraform.io/downloads.html)
    
    2. Extract file
    
    3. Copy terraform to bin folder
    
        $ sudo mv terraform /usr/local/bin/
    
Setting up terraform project

    1. Create a terraform project and put my aws_instance.tf there
    
        $ mkdir project_name
        $ mv aws_instance.tf /project_name/
        $ terraform init

    2. Edit aws_instance.tf
    
        On line 3 put your aws "YOUR_AWS_ACCESS_KEY"
        
        On line 4 put your aws "YOUR_AWS_SECRET_KEY"
        
        On line 48 put your aws "YOUR_AWS_SSH_KEY_PAIR"

    3. Check terraform plan to apply:
    
        $ terraform plan
        
    4. Apply terraform plan to create AWS EC2 instance:
    
        $ terraform apply
       
    5. DONE!!!!! you can go to AWS console to check your instance EC2 ready!!!!