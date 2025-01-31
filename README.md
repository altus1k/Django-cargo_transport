# Cargo Transport System

## Description

A cargo transport management system that allows users to create orders, add drivers, and manage their profiles.

## Installation

1. Clone the repository:

   bash
   git clone https://github.com/yourusername/cargo_transport.git
   cd cargo_transport


2. Create and activate a virtual environment:

   bash
   python3 -m venv myenv
   source myenv/bin/activate
   

3. Install the dependencies:

   bash
   pip install -r requirements.txt

4. Apply the database migrations:

   bash
   python3 manage.py makemigrations
   python3 manage.py migrate

5. Create a superuser for accessing the admin panel:

   bash
   python3 manage.py createsuperuser

6. Run the development server:

   bash
   python3 manage.py runserver

7. Open your browser and go to `http://127.0.0.1:8000/`.

## Usage

### Home Page

The home page displays buttons for registration and login. After logging in, users can access their profile, view orders, and add drivers.

### Order Management

Users can create, update, and delete orders. Each order has a status: "Not Started", "In Progress", or "Completed".

### User Profile

Users can update their profile information, including their image and bio.

### Add Driver

Users can add drivers through the corresponding form.

## Project Structure

cargo_transport/
├── manage.py
├── cargo_transport/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
├── orders/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── signals.py
│   ├── urls.py
│   ├── views.py
│   ├── templates/
│       ├── orders/
│           ├── home.html
│           ├── create_order.html
│           ├── update_order.html
│           ├── delete_order.html
│           ├── orders_list.html
│           ├── add_driver.html
│   ├── migrations/
│       ├── __init__.py
├── templates/
│   ├── base.html
│   ├── registration/
│       ├── login.html
│       ├── signup.html
│   ├── users/
│       ├── profile.html


## License

This project is licensed under the MIT License. See the LICENSE file for details.
