# Chirp - Django

## Getting Started

Follow these instructions to get your project up and running.

### Prerequisites

- Python 3.x
- Django
- PostgreSQL (via Supabase)
- Virtual Environment

### Installation (Dev)

1. **Clone the repository:**

   ```bash
   git clone <repository-url>
   cd Chirp-Django
   ```

2. **Set up a virtual environment:**

   ```bash
   python -m venv .venv
   # Activate the virtual environment based on your shell
   .venv/bin/activate.ps1              # For PowerShell
   .venv/bin/activate                  # For Bash
   .venv/Scripts/activate.bat          # For CMD
   source .venv/Scripts/activate.fish  # For Fish
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Create a Supabase project:**

   - Go to [Supabase](https://supabase.io/) and create a new project.
   - Note down the database credentials (DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT).

5. **Configure environment variables:**

   - Create a `.env` file in the root directory with the following content:

     ```bash
     DB_NAME=your_db_name
     DB_USER=your_db_user
     DB_PASSWORD=your_db_password
     DB_HOST=your_db_host
     DB_PORT=your_db_port
     ```

6. **Update `settings.py`:**

   - In `project/settings.py`, configure the database settings to use the environment variables:

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

7. **Migrate the database:**

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

8. **Run the development server:**

   ```bash
   python manage.py runserver
   ```

9. **Access the application:**

   - Open your browser and go to `http://127.0.0.1:8000/` to see the application in action.
