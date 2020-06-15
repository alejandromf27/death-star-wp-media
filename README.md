Launch AWS EC2 instance with Terraform:

    1. Check TERRAFORM-README.md file

Docker set up:

    1. Install Docker (https://docs.docker.com/install/linux/docker-ce/ubuntu/)
    
        Warning: On Ubuntu 20.04 Focal Fossa install docker from: (https://linuxconfig.org/how-to-install-docker-on-ubuntu-20-04-lts-focal-fossa)
    
    3. Check docker version
    
        $ docker --version    
        
    4. Install docker-compose (https://docs.docker.com/compose/install/)
    
    5. Check docker compose version
    
        $ docker-compose --version
    
    6. Check docker services status        
    
        $ sudo systemctl status docker
        
Launch Django project

    1. Clone project
        
        $ git clone https://github.com/wp-media/Angel_Garcia_task.git
        
    2. Move to project dir
    
        $ cd Angel_Garcia_task

    3. Build containers and run project with docker compose
    
        $  sudo docker-compose up --build (use this option the first time to build the containers)
        
    4. Launch Django static
    
        $ sudo docker-compose run death_star python3 manage.py collectstatic
    
    5. Create project migrations:
    
        $ sudo docker-compose run death_star python3 manage.py makemigrations
        
    6. Execute migrations:
    
        $ sudo docker-compose run death_star python3 manage.py migrate
        
    7. Create Django superuser
    
        $ sudo docker-compose run death_star python3 manage.py createsuperuser
        
    8. Load fixtures of XWings data: 
            
        $ sudo docker-compose run death_star python3 manage.py loaddata initial_data.json
        
Running Tests

    You can use pytest like we have in this project or use the Django TestCase class
    
    Pytest:
    
        $ sudo docker-compose run death_star pytest
        
For Code Quality and Security I recommend to use SONARQUBE (https://www.sonarqube.org/)

Project Postman Collection

    Here you are the file: /Death Star.postman_collection.json
    
    You can import it on Postman to have acceso to all rest apis
    
    
Additional details:

    1.I wanted to share with you a AWS EC2 as a sample, that I launched with Terraform and also I set up the django death start project there with docker.
    
    2. Here you can see on AWS my Django instance running
    
        http://3.84.126.137:8000/admin/
        