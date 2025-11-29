# buildDjango

This repository contains several Django projects used for learning and tutorials.

## Projects

The repository is organized into the following independent projects:

### 1. LittleLemon
Located in `LittleLemon/`, this is a Django project structured for the Little Lemon restaurant application. It includes a `LittleLemonDRF` app, which is a Django Rest Framework application skeleton.

**Setup and Run:**
```bash
cd LittleLemon
python manage.py runserver
```

### 2. myproject
Located in `myproject/`, this is a basic Django project containing a `myapp` application with a simple home view.

**Setup and Run:**
```bash
cd myproject
python manage.py runserver
```

### 3. mappingURLs
Located in `mappingURLs/myproject/`, this is a project demonstrating URL parameter mapping. It contains a `drinks` view that accepts a drink name as a URL parameter.

**Setup and Run:**
```bash
cd mappingURLs/myproject
python manage.py runserver
```

## Setup Instructions

1.  **Clone the repository:**
    ```bash
    git clone <repository_url>
    cd <repository_name>
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Navigate to a project directory and run the server.**

## Documentation

Each project is fully documented with docstrings following the Google Python Style Guide. You can inspect the source code for detailed information about modules, classes, and functions.
