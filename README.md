# A Django E-commerce project for batch b420 of ITVedant institute, Bengaluru branch


For every new project,
- Create a dedicated folder for the new project and open that directory in visual studio.
- Create the virtual environment
    - `python -m venv <virt_env_name>`
- Activate the virtual env
    - `<virt_env_folder>/Scripts/activate`
- Install django and other required dependencies.
    - `pip install django`
    - `pip install pillow`
- Freeze the requirements (Repeat this step whenever new dependencies are installed or updated)
    - `pip freeze > requirements.txt`
---
## Start the project
- Ensure the virtual environment is activated.
- `django-admin startproject <django_proj_name>`
- Move into the django project directory
    - `cd <django-project-folder-name>`
- Let's test the django installation
    - Migrate the schema of the project into db
        - `python manage.py migrate`
    - Run the server
        - `python manage.py runserver`
### Django Admin panel
- Every django project comes packed with a pre-built admin page under the path `/admin`.
- To get access to this, first we need an admin account.
- Run `python manage.py createsuperuser` and follow instructions
- Run the server and go to the path `<hosted_ip>:<port>/admin`
- Log-in using the credentials we setup in the previous step.
---
### A Django project's logic is divided into re-usable packages called `apps`
- Let's create our first app
- **For each new app**: 
---
Ensure you are inside django project folder

1. Start the app
    - `python manage.py startapp <app_name>`
2. Go to `settings.py` inside the project root folder and look for the list `INSTALLED_APPS`.
    - Add the new app name at the end of the list.
    - This let's the django project register the app while running and also helps track schema designed inside the app.
3. Create a new `urls.py` file inside the **app** folder.
    - Go to the `urls.py` file inside **project root folder**
    - This file will have a path listed as `path('admin/', admin.site.urls),`
    - Let's link the new app urls to the list `urlpatterns`.
    1. Add `include` function to the import `from django.urls import path, include`
    2. Add new pattern in the urlpatterns.
        - `path('<path in which app sub-paths should be available>', include('<app_name>.urls'))`
        - For example, if the app name is `mainapp` and I want the sub paths to be available in the path `products/`, I would write
            - `path('products/', include('mainapp.urls'))`
    3. ### Model the schema for entity types handled by the app
        - Go to `models.py` inside app folder and design a class inheriting the `models.Model` class from the imported module `django.db.models`
        - After making any schema changes inside `models.py`
            - Run `python manage.py makemigrations <app_name>` to track the schema changes and generate scripts to update those changes in the db.
            - Run `python manage.py migrate` to run the generated scripts and execute the updates. 
        - In case you want to access CRUD operations on a model inside the pre-built django admin panel,
            - Go to admin.py inside the app folder
            - import the model that you require into the admin module
            - append a new line to the file
                - `admin.site.register(<ModelName>)`
    4. ### Set-up the View function (or Class based view) in the app's views.py
        - Import the app's models to this file using `from .models import <Classname1>, <Classname2`
        - Create FBVs or CBVs to handle the requests
        - In case we are serving rendered templates,
            - Create a new `templates` folder inside the app folder.
            - Create the necessary templates and link it to the respective Views
    5. ### Set-up the app `urls.py`
        - Do necessary imports: 
            ```python
                from django.urls import path
                from . import views
            ```
        - Set-up the list `urlpatterns`
        - Add new paths linking the views we created inside `views.py`.
        - For each view, add the following to the list
            - ```path('<path-for-accessing-view>', views.<view-name>, name = '<path-name>'),```
        - Each path defined inside the urlpatterns can be linked to hyperlinks in the templates using the following django tag `{% url '<path_name>' <arguments_if_necessary> %}`
        - For example : 
            ```html
            <a href="{% url 'home_page' %}">Home</a>

            <a href = "{% url 'prod_details' prod.pk %}">

   
            ```
    ### Repeat the above steps for each new app
---