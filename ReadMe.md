## Build A Blog With Django

-> Download [starter files for this project](https://github.com/Academy-Omen/django-blogx/tree/starter)

-> Create Virtual environment
```bash
# Windows
py -3 -m venv env
# Linux and Mac
python -m venv env
```

-> Activate environment
```bash
# Windows
.\env\Scripts\activate
# Linux and Mac
source env/bin/activate
```

-> Install Requirements
```bash
pip install -r requirements.txt

```

-> Create Django project in the present directory
```bash
# the '.' tells python to create the project in the present folder
django-admin startproject core .

```

-> Create Blog app
```bash
python manage.py startapp blog

```

-> Register blog app in project settings file
```py

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # register blog here
    'blog',
]

```

-> Apply migrations
```bash
python manage.py migrate

```

-> Create basic views
```py

from django.shortcuts import render


def home(request):
    return render(request, 'index.html')


def article(request):
    return render(request, 'article.html')

```

-> Create the blog app urls file
```py

from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.home, name='homepage'),
    path('post/', views.article, name='article'),
]

```

-> Register the blog urls file in the project urls file
```py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # import include and add blog urls.py
    path('', include('blog.urls', namespace='blog')),
]
```

-> Create blog app template directory in blog app directory
```html
<!-- Example Home page -->
<h1>Home Page</h1>
```

-> Configure static files in settings file
```py
import os

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

MEDIA_ROOT = os.path.join(BASE_DIR, 'static/images')
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

```
-> Place the css files in static/css, images in static/images and the html in blog/templates


-> Load the static files in the html files
```html
<!-- place this at top -->
{% load static %}

<!-- example -->
<link rel="stylesheet" href="{% static 'css/style.css' %}"">
```

-> Create Models and register to admin interface

```bash
python manage.py makemigrations
python manage.py migrate
#  create superuser
python manage.py createsuperuser
python manage.py runserver
```

-> Tell django where to get static files in development
```py
# core.urls.py
from django.conf.urls.static import static
from django.conf import settings

# .
# .

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
```

-> Add ckeditor to installed app and add the settings
```py
# settings.py
INSTALLED_APPS = [

# .
# .

    'ckeditor',
    'ckeditor_uploader',
]

# CKEditor settigs

CKEDITOR_UPLOAD_PATH = 'uploads/'

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
        'height': 300,
        'width': '100%',
    },
}
```

-> Add ckeditor urls
```py
# core.urls.py
# .
# .

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls', namespace='blog')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]

```

-> Collect statics all static so as to copy ckeditor required media files
```bash
python manage.py collectstatic
```

