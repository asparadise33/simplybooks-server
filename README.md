
# SIMPLY BOOKS API:

This is an API that used Python and Django to create collections of Authors, Books and Genres for the Simply Books project at NSS.

# Postman Docs 
Please read the attached for full documentation as to how the API works and how to access the endpoints to fetch data.
https://documenter.getpostman.com/view/33499624/2sAYQXpYTU

# Loom Video of the calls being made in Postman
https://www.loom.com/share/706f0264de0a46e08de18de805f6cdc2?sid=0eb40369-c5ed-4b15-bab5-a3993da478a8

# Project Setup Instructions for first-time installation

Follow these steps to set up and run the project:

1. Install the required packages using Pipenv:
    ```sh
    pipenv install
    ```

2. Activate the virtual environment:
    ```sh
    pipenv shell
    ```

3. Create the database migrations:
    ```sh
    python manage.py makemigrations
    ```

4. Apply the migrations to the database:
    ```sh
    python manage.py migrate
    ```

5. Start the development server:
    ```sh
    python manage.py runserver
    ```


## HOW TO START THE SERVER FOR FRONT-END
1. Open Terminal:
    ```sh
    pipenv shell
    ```

2. Start Python Interpreter:
    ```sh
    CTRL + Shift + P and click Python: Select Interpreter
    ```    

3. Select the correct Python Interpreter:
    ```sh
    Python (version)(`file_name_server_randomString`:Pipenv) ~.\virtualenvs\sec...
    ```  

4. Open Terminal to Start Server:
    ```sh
    python manage.py runserver
    ```      

5. Verify server is running by clicking to open web page to see data:
    ```sh
    Starting development server at http://127.0.0.1:8000/
    ```
  
```      
