# 📚 LITRevu

**LITRevu** is a Django application designed to manage literary reviews. Users can request critiques for books or articles, post their own reviews, and follow other users to see their activity in a personalized feed.

---

## 📚 Table of Contents

- [Features](#-features)
- [Application Architecture](#-application-architecture)
- [Installation Guide](#-installation-guide)
- [Launch the Application](#-launch-the-application)
- [Code Quality Report (Flake8)](#-code-quality-report-flake8)
- [Built With](#-built-with)
- [Releases](#-releases)
- [Author](#-author)
- [License](#-license)

---

## 🧩 Features

- User authentication with signup and login pages.
- Personalized feed showing tickets and reviews from followed users and the current user.
- Ability to create tickets requesting reviews for books or articles.
- Ability to post reviews in response to existing tickets.
- Ability to create a ticket and a review in a single step.
- Feed ordered in reverse chronological order based on latest activity.
- Follow or unfollow users.
- View the list of followed users and followers.

---

## 🧠 Application Architecture

LITRevu is a Django web application structured around Django’s MTV pattern
(Model–Template–View), which is conceptually close to MVC and promotes clear
separation of concerns.

- **Models** define the database schema and relationships (tickets, reviews, publications, user follows).
- **Views** contain the business logic that handles HTTP requests and responses.
- **Templates** render HTML pages displayed to the user.
- **Forms** centralize validation and form handling logic.
- **Static files** (CSS, JavaScript) manage the frontend behavior and styling.
- **Migrations** track database schema changes over time.
- **Development utilities** provide helper scripts for code inspection and
  version control workflows.

Here is the overall project layout:

```
LITRevu/
├── manage.py                  # Django entry point
├── db.sqlite3                 # SQLite database
├── requirements.txt           # Python dependencies
├── data/                      # Uploaded media files (ticket images)
│   └── ticket_images/
├── _dev_utils/                # Developer utility scripts
│   ├── concat.sh              # Concatenate source files
│   ├── dir.sh                 # Generate directory tree
│   ├── commit.sh              # Git helper script
│   ├── code.txt               # Generated source snapshot
│   └── directories.txt        # Generated directory listing
├── LITRevu/                   # Project configuration
│   ├── settings.py            # Global Django settings
│   ├── urls.py                # Root URL routing
│   ├── asgi.py / wsgi.py      # Deployment entry points
└── reviews/                   # Main application
    ├── models.py              # Data models
    ├── views/                 # View logic (feature-based modules)
    ├── forms/                 # Django forms
    ├── templates/reviews/     # HTML templates
    ├── static/reviews/        # CSS and JavaScript
    ├── migrations/            # Database migrations
    ├── admin.py               # Django admin configuration
    └── urls.py                # App-level URL routing
```

---

## 🚀 Installation Guide

> ⚠️ **Compatibility Note**
> This project requires **Python ≥ 3.10** and **pip ≥ 23.0** to ensure full compatibility with Flake8 and its HTML reporting plugin.

> 🐧 **Note macOS/Linux**
> On Linux/Mac, the `python` command may not be available by default.
> Use `python3` instead:

Clone the repository from GitHub:

```bash
git clone https://github.com/DomiCarr/OCR_P09_LITRevu
cd OCR_P09_LITRevu
```

### 🛠️ Set up the virtual environment

Create and activate the virtual environment before installing packages or running the application.

Create:

```bash
python -m venv env
# If python doesn't work, use python3:
python3 -m venv env
```

Activate:

- **On macOS/Linux**
  ```bash
  source env/bin/activate
  ```

- **On Windows (CMD)**
  ```cmd
  env\Scripts\activate
  ```

- **On Windows (PowerShell)**
  ```powershell
  .\env\Scripts\Activate.ps1
  ```

> 📝 **Note (PowerShell)**
> If you get an error like
> **“running scripts is disabled on this system”**,
> open PowerShell as administrator and run:
>
> ```powershell
> Set-ExecutionPolicy RemoteSigned
> ```
>
> Then confirm with `Y` to allow local scripts to run.


### 📦 Install dependencies

```bash
pip install -r requirements.txt
```

### ✅ Verify installation

Run the following to confirm packages are installed:

```bash
pip freeze
```

Expected output includes:

```text
asgiref==3.11.0
Django==5.2.8
flake8==7.3.0
flake8-html==0.4.3
Jinja2==3.1.6
MarkupSafe==3.0.2
mccabe==0.7.0
pillow==12.0.0
pycodestyle==2.14.0
pyflakes==3.4.0
Pygments==2.19.2
sqlparse==0.5.3
```

---

### 🏃 Run the Django Development Server

From the project root:

```bash
python manage.py runserver
# If python doesn't work, use python3:
python3 manage.py runserver

```

🌐 Access the application

Open your browser and go to http://127.0.0.1:8000/

---

## 🧪 Code Quality Report (Flake8)
![Flake8](https://img.shields.io/badge/code%20style-Flake8-blue)


To ensure code quality and compliance with PEP8 standards, this project uses **Flake8** with HTML reporting.

You can generate a detailed linting report by running the following command from the root of the project:

```bash
python -m flake8 src/ --format=html --htmldir=flake8_rapport
# If python doesn't work, use python3:
python3 -m flake8 src/ --format=html --htmldir=flake8_rapport
```

This will create an HTML report in the `flake8_rapport/` directory.
You can open `flake8_rapport/index.html` in your browser to review warnings, errors, and style issues.

> ⚙️ **Configuration Note**
> Flake8 is configured via a `.flake8` file located at the root of the project.
> It sets the maximum line length to 119 characters, excludes folders like `env/`, `__pycache__/`, and `flake8_rapport/`, and enables HTML output in the `flake8_rapport/` directory.

> ✅ Tip: Make sure your virtual environment is activated before running the command.

---

## 🧰 Built With

[![Made with Python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)

- **Python** — main programming language
- **MVC (Model–View–Controller)** — architectural pattern used to separate concerns between data (Model), user interface (View), and logic (Controller)
**Cross-platform compatibility** — works on 🐧 Linux, 🍎 macOS, and 🪟 Windows


---

## 📦 Releases

- **Version 1.0** — Initial release

---

## 👤 Author

**Dominique Carrasco**
GitHub: [@DomiCarr](https://github.com/DomiCarr)

---

## 📄 License

This project is licensed under the [OpenClassrooms Terms & Conditions](https://openclassrooms.com/fr/policies/terms-conditions)
