# Polls Website

### A full-featured polling application built with Django that allows users to create, vote on, and view poll results with real-time visualizations. 
# 📗 Table of Contents

- [📖 About the Project](#about-project)
  - [🛠 Built With](#built-with)
    - [Tech Stack](#tech-stack)
    - [Key Features](#key-features)
- [💻 Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Setup & Install](#setup)
  - [Usage](#usage)
- [🤝 Contributing](#contributing)
- [⭐️ Show your support](#support)
- [📝 License](#license)

<!-- PROJECT DESCRIPTION -->

# 📖 Django Polls Website <a id="about-project"></a>

Django polls website implementing models, views, templates, forms, and authentication for voting and adding questions 

## 🛠 Built With <a id="built-with"></a>

### Tech Stack <a id="tech-stack"></a>

- **Language**: Python (recommendation: `Python 3.13+`)
- **Libraries**: Django 6+, SQLite, 

<!-- Features -->

### Key Features <a id="key-features"></a>

- User Authentication: Register, login, logout, and password reset functionality
- Poll Management:
    - Create polls with multiple choice questions
    - Set poll duration and visibility
    - Edit and delete your own polls

- Voting System:
    - Single vote per user per poll
    - Anonymous voting option
    - Real-time results visualization

<!-- GETTING STARTED -->

## 💻 Getting Started <a name="getting-started"></a>

### Prerequisites

```sh
 git
 python 3.13+
 Django 6.0+
```

### Setup & Install

Follow these steps to run project locally.

Clone this repository to your desired folder:

```sh
  # 1. Clone
  git clone https://github.com/Dimah-code/polls-django.git
  cd polls-django
  # 2. create a virtual environment
  python -m venv venv

  # 3. Activate it:
  # macOS / Linux (bash / zsh)
  source venv/bin/activate

  # Windows
  .\venv\Scripts\Activate.ps1

  # 3. Install dependencies
  pip install -r requirements.txt
```

Make migrations:

```shell
python3 manage.py makemigrations
```

Now migrate:

```shell
python3 manage.py migrate
```

Create a superuser:

```shell
python3 manage.py createsuperuser
```

### Usage

To run the project, execute the following command:

Run server on localhost:

```shell
python3 manage.py runserver
```

Open it on browser:
```text
Go to http://127.0.0.1:8000/ on your favorite web-browser
```

<!-- CONTRIBUTING -->

## 🤝 Contributing <a name="contributing"></a>

Contributions are welcome! see <a href="CONTRIBUTING">here</a> for more information.

<!-- SUPPORT -->

## ⭐️ Show your support <a name="support"></a>

If this repo helped you practice Django, please give it a ⭐ and share with others learning **Django**. Issues, PRs and suggestions are welcome!

## 📝 License <a name="license"></a>

This project is [MIT](/LICENSE) licensed.