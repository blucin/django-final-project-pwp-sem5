# Python and Web Programming Final Project: Chirp (Twitter Clone)

<!-- metadata (use pandoc) 
% title: Python and Web Programming Final Project: Chirp (Twitter Clone)
% author: Akshar Patel (12102110501003) CSE-IoT Batch A
% date: October 04, 2023
-->

## 1. Setting up venv 

- Enter the following command based on your shell to create a virtual environment named .venv in the current directory

```bash
python -m venv .venv
# Only run one of the following commands
.venv/bin/activate.ps1              # For PowerShell
.venv/bin/activate                  # For Bash
.venv/Scripts/activate.bat          # For CMD
source .venv/Scripts/activate.fish  # For Fish
```

## 2. Installing dependencies

- Use the requirements.txt file to install all the dependencies provided in this project

```bash
pip install -r requirements.txt
```

## 3. Make a project in the current directory

- Make sure you are in the root directory of the project and run the following command

```bash
django-admin startproject project .
```

## 4. Make an app in the project

- Make sure you are in the root directory of the project and run the following command which will create an app named app

```bash
python manage.py startapp app
```

## 5. Start a supabase project

- Create a supabase project to use their postgres database.

![Creating a supabase project](assets/supabase_creating_project.png)


## 6. Change project `settings.py` file

- Your .env format should be like this

```bash
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=your_db_host
DB_PORT=your_db_port
```

- Go to settings.py file and change the following

```python
from decouple import config

...

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST'),
        'PORT': config('DB_PORT'),
    }
}

...
```

## 7. Migrate the database

- Run the following command to migrate the database

```bash
python manage.py makemigrations
python manage.py migrate
```