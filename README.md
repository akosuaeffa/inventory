# CE Delights Inventory Management System

## Table of Contents
1. Introduction
2. Features
3. Technologies Used
4. Setup Instructions
5. Usage
6. API Endpoints
7. Contributing

## Introduction
CE Delights Inventory Management System is a web application designed to help restaurant owners manage their inventory, recipes, and sales efficiently. It allows users to add new recipes with their respective ingredients, update inventory levels, and log customer purchases, ensuring smooth restaurant operations.

## Features
- **Inventory Management:** Add, update, and delete ingredients with available quantities and prices.
- **Recipe Management:** Create and manage recipes by specifying required ingredients and their quantities.
- **Purchase Logging:** Record customer purchases, automatically adjusting inventory levels.
- **Reporting:**  View total inventory costs, daily revenue, purchase logs, and restock requirements.

## Technologies Used
- **Backend:** Django
- **Frontend:** HTML, CSS, JavaScript
- **Database:** SQLite (default for development, can be switched to PostgreSQL/MySQL for production)
- **Version Control:** Git, GitHub

## Setup Instructions
### Prerequisites
- Python 3.x
- pip (Python package installer)
- venv

### Installation Steps
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/akosuaeffa/inventory.git
   cd inventory

2. **Create and Activate Virtual Environment:**
   ```bash
   venv venv
   venv\Scripts\activate

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt

4. **Apply Migrations:**
   ```bash
   python manage.py migrate

5. **Run the Development Server:**
   ```bash
   python manage.py runserver

6. **Access the Application:**
   Open your web browser and enter the url `http://127.0.0.1:8000/`
   
