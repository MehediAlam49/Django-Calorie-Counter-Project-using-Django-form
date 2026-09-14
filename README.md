# Django Calorie Counter

## Contents

- [Description](#description)
- [Key Features](#key-features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Environment Variables](#environment-variables)
- [Django Template Setup](#django-template-setup)
- [Context Data](#context-data)
- [Navigation Page and URL Names](#navigation-page-and-url-names)
- [Pages and Workflows](#pages-and-workflows)
- [Animated Data Flow Diagram](#animated-data-flow-diagram)
- [Usage Examples](#usage-examples)
- [Possible Future Enhancements](#possible-future-enhancements)
- [License](#license)
- [Contact](#contact)

## Question

> Develop a Calorie Counter that can be used to estimate the number of calories a person needs to consume each day. This calculator can also provide some simple guidelines for gaining or losing weight. Users can also keep track of how many calories he/she needs and how much he/she consumes in a day. To calculate calories, we have two formulas:
>
> For a male
>
> - `BMR= 66.47+(13.75 x weight in kg) + (5.003 x height in cm) - (6.755 x age in years)`
>
> For a female
>
> - `BMR=655.1+(9.563 x weight in kg)+(1.850 xheight in cm) - (4.676 x age in years)`

- Job Specification information:

  1. Create a new Django project named `Name_ID_CaloryCounter` and a `Calorie Counter app`.
  2. Define your Calorie Counter models.
  3. Create views for Login (username/email and password) and Registration (`username`, `email`, `password`, `confirm password`) pages.
  4. Create a `django-form` to take input `Name`, `Age`, `Gender`, `Height`, `Weight` etc.
  5. Create a Django form to take input daily consumed calories (`Item name`, `Calorie consumed`)
  6. Create a dashboard where the user can view the required calories for her/him and the consumed calories daily.
  7. Define URL Patterns and configure project-level URLs.
  8. Implement the required Function and Logic in the `view.py` file.

- Job Specification information:
  - Create a new Django project. (Naming Convention: `Name_ID_CaloryCounter`)
  - Run migration to create the data tables.
  - Create a superuser. (`username`: `admin`, `password`: `1234`)
  - Register your models to the Django admin.

---
[Back to Contents](#contents)

## Description

This project is a Django-based calorie tracking application built to help users register, log in, update personal profile information, calculate Basal Metabolic Rate (BMR), and track daily consumed calories. It is designed for individuals who want a straightforward web dashboard for monitoring calorie intake and understanding whether they are consuming more or fewer calories than required.

The application uses Django’s built-in authentication flow, custom forms, and template-based UI. It is a practical, template-driven project for learning and extending a full-stack Django app with user management, form handling, and CRUD operations.

[Back to Contents](#contents)

## Key Features

- **User Authentication:** Registration, login, and logout flows built with Django `UserCreationForm` and `AuthenticationForm`.
- **Profile Management:** Stores profile details such as name, age, gender, height, weight, and computed BMR.
- **Daily Calorie Tracking:** Lets authenticated users add, update, and delete consumed calorie entries.
- **Dashboard Insights:** Shows total consumed calories, required calories, difference, and a simple eat-more/eat-less suggestion.
- **Bootstrap UI:** Uses Bootstrap 5 via Django templates and `django-crispy-forms` for a clean interface.
- **SQLite Default Database:** Runs locally with the included SQLite database setup.
- **Admin Integration:** Registered models are visible in Django admin.

[Back to Contents](#contents)

## Tech Stack

| Layer | Technology |
| --- | --- |
| Backend | Django 6.1 |
| Database | SQLite |
| Frontend | Bootstrap 5, HTML, Django Templates |
| Forms | `django-crispy-forms`, `crispy-bootstrap5` |
| Image Support | Pillow |
| Environment | Python 3.x |

[Back to Contents](#contents)

## Project Structure

```text
Django-Calorie-Counter-Project-using-Django-form/
├── calorieCounter/
│   ├── Templates/
│   │   ├── calorie-list.html
│   │   ├── dashboard.html
│   │   ├── profile.html
│   │   └── master/
│   │       ├── base.html
│   │       ├── base-form.html
│   │       ├── message.html
│   │       └── nav.html
│   ├── migrations/
│   │   └── 0001_initial.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── Mehedi_2026_CalorieCounter/
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── db.sqlite3
├── manage.py
├── README.md
├── requirements.txt
└── .gitignore
```

[Back to Contents](#contents)

## Getting Started

### Prerequisites

- Python 3.10+ recommended
- `pip` and `virtualenv` or `venv`
- Git

### Installation

```bash
# Clone the repository
git clone https://github.com/MehediAlam49/Django-Calorie-Counter-Project-using-Django-form.git

# Move into the project directory
cd Django-Calorie-Counter-Project-using-Django-form

# Create a virtual environment
python -m venv .venv

# Activate the virtual environment
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Database Setup

```bash
python manage.py migrate
```

### Run the Development Server

```bash
python manage.py runserver
```

Then open:

- http://127.0.0.1:8000/

### Create a Superuser (Optional)

```bash
python manage.py createsuperuser
```

Use the admin panel at:

- http://127.0.0.1:8000/admin/

[Back to Contents](#contents)

## Environment Variables

This project does not require any custom environment variables for local development. The default configuration uses SQLite and a console email backend, so no `.env` file is needed for the current setup.

```env
# No environment variables are currently required.
```

[Back to Contents](#contents)

## Django Template Setup

This project uses Django's template system with a shared base layout and a reusable form template.

### Shared Base Layout

The main template structure comes from `calorieCounter/Templates/master/base.html`.

```html
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet">
    <title>Hello, world!</title>
  </head>
  <body>
    {% include 'master/nav.html' %}
    <div class="container">
        {% block body %}
        {% endblock body %}
    </div>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js"></script>
  </body>
</html>
```

### Reusable Form Template

The reusable form page is defined in `calorieCounter/Templates/master/base-form.html`.

```html
{% extends 'master/base.html' %}
{% load crispy_forms_tags %}

{% block body %}
<h1>{{form_title}}</h1>
{% include 'master/message.html' %}
<form method="POST" enctype="multipart/form-data">
    {% csrf_token %}
    {{form_data|crispy}}

  <button type="submit" class="btn btn-primary">{{form_btn}}</button>
</form>
{% endblock body %}
```

### Message Template

The message template is included across forms and pages for user feedback.

```html
{% if messages %}
{% for message in messages %}
<div class="alert alert-primary" role="alert">
  {{message}}
</div>
{% endfor %}
{% endif %}
```

### Page Templates

- `dashboard.html` shows daily calorie summary cards and the consumed calorie table.
- `profile.html` shows the current profile and BMR.
- `calorie-list.html` displays the complete calorie history and includes add/edit/delete actions.

[Back to Contents](#contents)

## Context Data

The views in `calorieCounter/views.py` pass data into the templates. Below are the main context structures used by the app.

### Dashboard Context

```python
context = {
    'required_calories': bmr,
    'today_consumed_data': today_consumed_data,
    'consumed_calories': total_caloire,
    'total_count': total_consumed_calories['total_count'],
    'less_more': less_more,
    'suggestion': suggestion,
}
```

This context is used by `dashboard.html` to render:

- `required_calories`
- `consumed_calories`
- `less_more`
- `suggestion`
- the current day's log list (`today_consumed_data`)

### Registration and Login Context

```python
context = {
    "form_data": form_data,
    'form_title': 'User Registration Form',
    'form_btn': 'Register'
}
```

```python
context = {
    'form_data': form_data,
    'form_title': 'User Login Form',
    'form_btn': 'Login'
}
```

### Profile Update Context

```python
context = {
    'form_data': form_data,
    'form_title': "Update Profile Info",
    'form_btn': 'Update'
}
```

### Calorie Add and Update Context

```python
context = {
    'form_data': form_data,
    'form_title': "Add Calorie Info",
    'form_btn': 'Add Calorie'
}
```

```python
context = {
    'form_data': form_data,
    'form_title': "UPdate Calorie Info",
    'form_btn': 'UPdate Calorie'
}
```

[Back to Contents](#contents)

## Navigation Page and URL Names

The navigation menu lives in `calorieCounter/Templates/master/nav.html` and uses Django URL names defined in `calorieCounter/urls.py`.

### Navigation Template

```html
<nav class="navbar navbar-expand-lg navbar-light bg-light">
  <div class="container-fluid">
    <a class="navbar-brand" href="#">CalorieCounter</a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarNav">
      <ul class="navbar-nav">
        {% if request.user.is_authenticated %}
        <li class="nav-item">
          <a class="nav-link" href="{% url 'dashboard_page' %}">Dashboard</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="{% url 'consumed_calories_list' %}">Consumed Calories</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="{% url 'profile_page' %}">Profile</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="{% url 'logout_page' %}">Logout</a>
        </li>
        {% else %}
        <li class="nav-item">
          <a class="nav-link" href="{% url 'login_page' %}">Login</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="{% url 'register_page' %}">Reigister</a>
        </li>
        {% endif %}
      </ul>
    </div>
  </div>
</nav>
```

### URL Configuration

```python
from django.urls import path
from calorieCounter.views import *

urlpatterns = [
    path('', register_page, name='register_page'),
    path('login/', login_page, name='login_page'),
    path('logout/', logout_page, name='logout_page'),

    path('dashboard/', dashboard_page, name='dashboard_page'),
    path('profile/', profile_page, name='profile_page'),
    path('update-profile/', update_profile, name='update_profile'),

    path('consumed-calorie-list/', consumed_calories_list, name='consumed_calories_list'),
    path('add-calorie/', add_calorie, name='add_calorie'),
    path('update-calorie/<int:id>/', update_calorie, name='update_calorie'),
    path('delete-calorie/<int:id>/', delete_calorie, name='delete_calorie'),
]
```

### URL Name Reference

| Page | URL Name |
| --- | --- |
| Registration | `register_page` |
| Login | `login_page` |
| Logout | `logout_page` |
| Dashboard | `dashboard_page` |
| Profile | `profile_page` |
| Update Profile | `update_profile` |
| Consumed Calories List | `consumed_calories_list` |
| Add Calorie | `add_calorie` |
| Update Calorie | `update_calorie` |
| Delete Calorie | `delete_calorie` |

[Back to Contents](#contents)

## Pages and Workflows

### 1. Registration Page

- URL: `/`
- View: `register_page`
- Form: `RegistrationForm`
- Action: registers a new user and redirects to the login page.

### 2. Login Page

- URL: `/login/`
- View: `login_page`
- Form: `LoginForm`
- Action: authenticates the user and redirects to the dashboard.

### 3. Dashboard Page

- URL: `/dashboard/`
- View: `dashboard_page`
- Functionality:
  - loads the current user's `BasicInfoModel`
  - calculates `bmr`
  - fetches today's consumed calories
  - computes total calories consumed
  - calculates `less_more` = `bmr - total_caloire`
  - displays a suggestion: `Eat more` or `Eat less`

### 4. Profile Page

- URL: `/profile/`
- View: `profile_page`
- Displays profile fields and the stored BMR value for the authenticated user.

### 5. Update Profile Page

- URL: `/update-profile/`
- View: `update_profile`
- Form: `ProfileUpdateForm`
- Action: updates profile data, recalculates BMR, and saves the profile.

### 6. Consumed Calorie List

- URL: `/consumed-calorie-list/`
- View: `consumed_calories_list`
- Displays all calorie entries associated with the logged-in user.

### 7. Add Calorie

- URL: `/add-calorie/`
- View: `add_calorie`
- Form: `ConsumedCalorieForm`
- Action: creates a `ConsumedCalories` record linked to the current user.

### 8. Update Calorie

- URL: `/update-calorie/<int:id>/`
- View: `update_calorie`
- Action: edits the selected calorie entry and then returns to the calorie list.

### 9. Delete Calorie

- URL: `/delete-calorie/<int:id>/`
- View: `delete_calorie`
- Action: deletes the selected calorie entry and redirects back to the list.

[Back to Contents](#contents)

## Animated Data Flow Diagram

The diagram below visualizes how the current Django app moves data between the browser, views, models, and templates.

```html
<svg width="100%" height="320" viewBox="0 0 1200 320" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Calorie Counter data flow diagram">
  <defs>
    <linearGradient id="lineGradient" x1="0%" x2="100%" y1="0%" y2="0%">
      <stop offset="0%" stop-color="#0ea5e9" />
      <stop offset="50%" stop-color="#8b5cf6" />
      <stop offset="100%" stop-color="#14b8a6" />
    </linearGradient>
    <style>
      .box { fill: #f8fafc; stroke: #0f172a; stroke-width: 1.5; rx: 18; }
      .label { font: 700 20px Arial, sans-serif; fill: #0f172a; }
      .small { font: 500 14px Arial, sans-serif; fill: #334155; }
      .flow { fill: none; stroke: url(#lineGradient); stroke-width: 3; stroke-dasharray: 10 10; animation: dash 11s linear infinite; }
      .flow2 { fill: none; stroke: url(#lineGradient); stroke-width: 3; stroke-dasharray: 8 10; animation: dash 8s linear infinite reverse; }
      @keyframes dash {
        to { stroke-dashoffset: -220; }
      }
    </style>
  </defs>

  <rect x="30" y="30" width="160" height="80" class="box"/>
  <text x="110" y="60" text-anchor="middle" class="label">User</text>
  <text x="110" y="85" text-anchor="middle" class="small">Browser</text>

  <rect x="260" y="30" width="180" height="80" class="box"/>
  <text x="350" y="60" text-anchor="middle" class="label">Django</text>
  <text x="350" y="85" text-anchor="middle" class="small">URLs + Views</text>

  <rect x="510" y="30" width="210" height="80" class="box"/>
  <text x="615" y="60" text-anchor="middle" class="label">Forms</text>
  <text x="615" y="85" text-anchor="middle" class="small">Registration / Login / Profile / Calorie</text>

  <rect x="810" y="30" width="190" height="80" class="box"/>
  <text x="905" y="60" text-anchor="middle" class="label">Models</text>
  <text x="905" y="85" text-anchor="middle" class="small">User / BasicInfo / ConsumedCalories</text>

  <rect x="470" y="180" width="260" height="90" class="box"/>
  <text x="600" y="215" text-anchor="middle" class="label">Templates</text>
  <text x="600" y="240" text-anchor="middle" class="small">dashboard.html / profile.html / calorie-list.html</text>
  <text x="600" y="260" text-anchor="middle" class="small">master/base.html / base-form.html</text>

  <path class="flow" d="M190 70 H260"/>
  <path class="flow2" d="M440 70 H510"/>
  <path class="flow" d="M720 70 H810"/>
  <path class="flow2" d="M905 110 V180"/>
  <path class="flow" d="M810 220 H730"/>
  <path class="flow2" d="M470 220 H230"/>

  <g>
    <circle cx="190" cy="70" r="4" fill="#0ea5e9"/>
    <circle cx="440" cy="70" r="4" fill="#8b5cf6"/>
    <circle cx="720" cy="70" r="4" fill="#8b5cf6"/>
    <circle cx="905" cy="110" r="4" fill="#14b8a6"/>
    <circle cx="810" cy="220" r="4" fill="#0ea5e9"/>
    <circle cx="470" cy="220" r="4" fill="#14b8a6"/>
  </g>
</svg>
```

### Diagram Interpretation

| Step | Description |
| --- | --- |
| 1 | The user loads the application and interacts with forms in the browser. |
| 2 | Django `urls.py` routes requests to the correct view in `views.py`. |
| 3 | Forms validate user input and prepare data for saving or rendering. |
| 4 | Data is stored in the models: `User`, `BasicInfoModel`, and `ConsumedCalories`. |
| 5 | Templates render the dashboard, profile, and calorie list using context data returned from the views. |
| 6 | The user sees live updates such as BMR, consumed calories, and suggestion messages. |

[Back to Contents](#contents)

## Usage Examples

### Run the App

```bash
python manage.py runserver
```

### Default Routes

| Route | Purpose |
| --- | --- |
| `/` | Register a new user |
| `/login/` | Sign in to the app |
| `/logout/` | End the current session |
| `/dashboard/` | View daily calorie insights |
| `/profile/` | View profile information |
| `/update-profile/` | Update profile/BMR |
| `/consumed-calorie-list/` | View all consumed calorie entries |
| `/add-calorie/` | Add a new calorie entry |
| `/update-calorie/<id>/` | Edit an existing calorie entry |
| `/delete-calorie/<id>/` | Delete a calorie entry |

### Example Interaction Flow

1. Visit `/` and create a user.
2. Go to `/login/` and sign in.
3. Open `/update-profile/` and enter personal health data.
4. The app calculates BMR automatically using the profile values.
5. Use `/add-calorie/` to record consumed items and calories.
6. Check `/dashboard/` to see total calories, required calories, and suggestions.
7. Review and manage entries in `/consumed-calorie-list/`.

### Example Data Entry

```text
Item Name: Rice
Calorie: 250
```

```text
Item Name: Chicken Salad
Calorie: 320
```

This data is stored in `ConsumedCalories` and displayed on the dashboard and calorie list.

[Back to Contents](#contents)

## Possible Future Enhancements

These are useful additions that could improve the project, but they are not currently implemented in this repository.

- **Weekly reports and charts** for calorie trends over time.
- **Date filters** to view calorie history by specific days or weeks.
- **User profile image upload** support beyond the current profile structure.
- **CSV or PDF export** for calorie logs.
- **Email notifications and reminders** for daily logging.
- **Advanced validation** for calorie values and profile inputs.
- **Search and sorting** for calorie entries.

[Back to Contents](#contents)

## License

This project is licensed under the MIT License.

```text
MIT License

Copyright (c) 2026 Mehedi Alam

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

[Back to Contents](#contents)

## Contact

- **Project Maintainer:** Mehedi Alam
- **Email:** mehedialam806@gmail.com
- **GitHub Repository:** https://github.com/MehediAlam49/Django-Calorie-Counter-Project-using-Django-form

[Back to Contents](#contents)
