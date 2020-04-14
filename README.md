# Django Tutorial from [The Net Ninja](https://www.youtube.com/playlist?list=PL4cUxeGkcC9ib4HsrXEYpQnTOTZE1x0uc)
- All code for the project can be found on [iamshaunjp's GitHub django-playlist repo](https://github.com/iamshaunjp/django-playlist/tree/master)

---

## Project Set-up
- After navigating to desired directory and activating the `django_env` conda environment, create the application using the following command:
    `django-admin startproject djangonautic`
- `cd djangonautic` to get into the project's directory
- in a new console tab (don't forget to activate the `django_env` again), `python manage.py runserver` to get the app server running locally
- navigate to `localhost:8000` to see the app running
- the `manage.py` script hold a lot of key tasks including spinning up servers, making migrations, enter an interactive shell to interact with the database, etc.
- Recall, Django comes packaged and set-up to have a **SQLite3** database on the backend, for which the data is save in the `db.sqlite3` file

---
## Django Set-up
- Refer to the MDN diagram on the interaction between key Django components
- It is important to not that requests made to the application by the browser are handled by **URLS** (`urls.py`), and the final response it provided the the browser by a **View** (`views.py`)
