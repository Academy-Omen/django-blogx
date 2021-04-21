## Build A Blog With Django

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

-> Create Django project
```bash
django-admin startproject core

```