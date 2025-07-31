# News app

## DESCRIPTION

My project provides readers with access to news articles authored by independent journalists affiliated with various publications. Subscribed individuals will receive newsletters and access articles published by the publishers or by individual journalists. Additionally, when an editor approves a news article submission, it will be shared with subscribers via email and posted on Twitter.

## INSTALLATION & SETUP

### Cloning the repository
1. Clone the repository
    ```bash
    git clone repository-url
    ```
2. Navigate into project repository
    ```bash
    cd new_app
    ```

#### Set the required envirionmental variables:
1. Rename `.env.template` to `.env`
2. Update the envionmental variables within `.env`

### Virtual Environment: 
1. Create a virtual envionment
    ```bash
    python -m venv venv 
    ```
2. Activate virtual envionment
    ```bash
    venv\Scripts\activate
    ```
3. Install project dependencies
    ```bash
    pip install -r requirements.txt
    ```
4. Apply migrations
    ```bash
    python manage.py migrate
    ```
5. Run the server
    ```bash
    python manage.py runserver
    ```

### Docker:
1. Build and start the container
    ```bash
    docker compose up -d --build
    ```
2. Apply migrations to database
    ```bash
	docker compose run django-web python manage.py migrate
    ```
	
### Usage

1. Navigate to `localhost:8000` to view the homepage



