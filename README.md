# asset_management
Simple Django application to track corporate assets handed out to employees

## How to run

- Clone the repository using the following command

    `git clone git@github.com:sanjibpaul59/asset_management.git`
- cd to the directory `cd asset_management`
- Create a virtual environment and activate it
- Create a .env file and fill that up following the `_env_sample` file
### Containerized version
- Make sure you have docker installed in your system and run
`docker compose up -d --build`
- The application will run in `http://localhost:3000`
- Create a superuser from the web container

    `docker exec -it <CONTAINER_ID/CONTAINER_NAME> bash`

    `python manage.py createsuperuser` 

### Localhost
- Update the settings.py, comment the 'HOST': 'db' , and uncomment 'HOST': 'localhost'
- Run the following commands
  
  `python manage.py makemigrations`

  `python manage.py migrate`

  `python manage.py runserver`