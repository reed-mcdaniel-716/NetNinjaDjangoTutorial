# Django Tutorial from [The Net Ninja](https://www.youtube.com/playlist?list=PL4cUxeGkcC9ib4HsrXEYpQnTOTZE1x0uc)
- All code for the project can be found on [iamshaunjp's GitHub django-playlist repo](https://github.com/iamshaunjp/django-playlist/tree/master)

---

## 2. Project Set-up
- After navigating to desired directory and activating the `django_env` conda environment, create the application using the following command:
    `django-admin startproject djangonautic`
- `cd djangonautic` to get into the project's directory
- in a new console tab (don't forget to activate the `django_env` again), `python manage.py runserver` to get the app server running locally
- navigate to `localhost:8000` to see the app running
- the `manage.py` script hold a lot of key tasks including spinning up servers, making migrations, enter an interactive shell to interact with the database, etc.
- Recall, Django comes packaged and set-up to have a **SQLite3** database on the backend, for which the data is save in the `db.sqlite3` file

---
## 3. URLs and Views
- Refer to the MDN diagram on the interaction between key Django components
- It is important to not that requests made to the application by the browser are handled by **URLS** (`urls.py`), and the final response it provided the the browser by a **View** (`views.py`)

---
## 4. HTML templates
- Remember: add `os.path.join(BASE_DIR, 'templates')` to the `TEMPLATE DIRS` array in `settings.py` so that Djamgo knows to look in the `templates/` directory of each app for our Templates

---
## 5. Apps
- When we initialize the project, Django creates the root app found in the folder with the same name as the project, in this case **djangonautic**
- In Django, you want to split your project into sections by creating logically separate "apps", each contained within its own folder with separate URLs (`urls.py`), Views (`views.py`), and template directories (`/templates/{app name}/`)
- You create new apps in the root folder using the command `python manage.py startapp {app name}`
    - will need to add `urls.py` file yourself to each app
- Remember: any apps created must be added to the `INSTALLED_APPS` array in `settings.py`
- Remember: All newly created URLs in the differnt apps must be registered in the list of URLs for the root app (i.e. **djangonautic**)
- The structure for this project is as follows, with the apps being **djangonautic**, **articles**, and **accounts**

---
## 6. Models
- Models in Django are python classes which represent a table in a database
    - The class name is the table's name
- Each type of data class we'll have (i.e. Articles, Users, etc.) is represented by its own model
- Each model maps to a single table in a database, which may contain multiple instances of a given model

---
## 7. Migrations
- Migrations do just that, they migrate our Models to the database, creating the appropriate tables with the specified fields that we've created
- To do this, we must first create a migration file, which tracks all changes made to our models (can be found in the `migrations/` folder of each app), and then run a migration via the `manage.py` script (done each time we wish to update our database)
- The commands to do this is, in the root directory:
    - `python manage.py makemigrations`
    - `python manage.py migrate`

---
## 8. ORM
- Object-relational mapping (ORM) in computer science is a programming technique for converting data between incompatible type systems using object-oriented programming languages. [Wikipedia](https://en.wikipedia.org/wiki/Object-relational_mapping)
    - This creates, in effect, a "virtual object database" that can be used from within the programming language.
- The Django Object-Relational Mapping (ORM) (look more into ORMs in general) bridges the code between the code and the database, allowing us to interact with the database using the Model
    - This includes saving, retrieving ,and updating instances of the Model in the database
- Will do the following exercises in a interactive python shell within the application as not to mess up the application
    - command to start interactive python shell in application is : `python manage.py shell`
    ```
    In [1]: # importing Article model                                                                   
    In [2]: from articles.models import Article                                                         
    In [3]: # check import                                                                              
    In [4]: Article                                                                                     
    Out[4]: articles.models.Article
    In [5]: # query for all rows (objects) in the Article table                                         
    In [6]: Article.objects.all()                                                                       
    Out[6]: <QuerySet []>
    In [7]: # creating a new Article instance                                                           
    In [8]: article= Article()                                                                          
    In [9]: article                                                                                     
    Out[9]: <Article: Article object (None)>
    In [10]: # adding a title to our instance                                                            
    In [11]: article.title= "hello, world"                                                              
    In [12]: article.title                                                                              
    Out[12]: 'hello, world'
    In [13]: # saving new instance to the database table                                                
    In [14]: article.save()                                                                             
    In [15]: # query Article table again                                                                
    In [16]: Article.objects.all()                                                                      
    Out[16]: <QuerySet [<Article: Article object (1)>]>
    In [17]: # one object now in query set                                                               
    In [18]: # indexed retrieval                                                                        
    In [19]: Article.objects.all()[0]                                                                   
    Out[19]: <Article: Article object (1)>
    In [20]: Article.objects.all()[0].title                                                             
    Out[20]: 'hello, world'
    In [21]: # to get a more descriptive query set, must define override __str__ function of Article model     
    In [22]: quit()    
    ```
    - once `__str__` defined in Article model:
    ```
    In [1]: from articles.models import Article                                                                
    In [2]: # querying for all rows as Article now that string representation                                  
    In [3]: Article.objects.all()                                                                              
    Out[3]: <QuerySet [<Article: hello, world>]>
    In [4]: # adding additional article                                                                        
    In [5]: article2= Article()                                                                                
    In [6]: article2.title= "Django Rules!"                                                                    
    In [7]: article2.save()                                                                                    
    In [8]: # query for all again                                                                              
    In [9]: Article.objects.all()                                                                              
    Out[9]: <QuerySet [<Article: hello, world>, <Article: Django Rules!>]>
    In [10]: quit()                                                       
    ```

---
## 9. Admin
- The Django Admin area is a area for site admins to control the content and accessibility of their website
    - It comes baked in and acts as a CMS (content management system)
    - Admins can create instances of models, create users, and other such tasks
- To get started you must first create a superuser using the command: `python manage.py createsuperuser`, and enter the information you're prompted for (e-mail address is optional)
    - for this project using default username and `admin_pass` as password
    - to test, run the server, navigate to `localhost:8000/admin` and try out credentials
    - superuser automatically granted "staff status"
- To make a Model accessible in the Admin area, must register the Model in the `admin.py` file of the root app (**djangonautic**)
- In the Admin area you can click on each registered Model to view existing instances and add new ones

---
## 10. Template Tags
- In Django, a template is a text file that can generate any text-based format (HTML, XML, CSV, etc.)
- A template contains variables, which get replaced with values when the template is evaluated, and tags, which control the logic of the template.

---
## 11. Model Methods
- Within each Model class, you may define functions (methods) just like you would in any python class

---
## 12. Static Files and Images
- Files like images, CSS files, and JavaScript scripts that can be serve to the client via the browser are considered static files
- In production, these files would likely be stored by a cloud service like AWS S3 for efficiency, but for local development we can store them locally
- Note that the way static files are configured to be served in development is often very insecure and, as such, should be changed before the application is put into production

---
## 13. Extending (HTML) Templates
- We may want to make a base HTML template and extend it when you want multiple HTML templates to have some components in common
    - For example, we may want all of our HTML templates to have the same head and footer
    - See the `base_layout.html` in the root folder's `template/` folder

---
## 14. URL parameters
- While some url route names maybe static, at other times you may want them to be more dynamic, including variable fields
