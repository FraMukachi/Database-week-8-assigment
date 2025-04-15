# Database-week-8-assigment

# Contact Book API with FastAPI and MySQL

# Project Description

A complete RESTful API for managing contacts, phone numbers, and tags. This project provides full CRUD (Create, Read, Update, Delete) functionality for a contact book application, built with:

- FastAPI (Python web framework)
- MySQL (Relational database)
- Pydantic (Data validation)
- MySQL Connector (Database connectivity)

Key features include:
- Contact management with full details
- Multiple phone numbers per contact
- Tagging system for contact categorization
- Search and filtering capabilities
- Comprehensive error handling
- Interactive API documentation

# Setup Instructions

# Prerequisites

- Python 3.7+
- MySQL Server
- pip (Python package manager)

# 1. Database Setup

1. Create the database by running the SQL script:


mysql -u root -p < contact_book.sql


2. Create a `.env` file in the project root with your database credentials:

env
DB_HOST=localhost
DB_USER=your_username
DB_PASSWORD=your_password
DB_NAME=contact_book


# 2. Python Environment Setup

1. Create and activate a virtual environment:


python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate


2. Install dependencies:


pip install -r requirements.txt


# 3. Running the Application

Start the FastAPI development server:


uvicorn app.main:app --reload


The API will be available at http://localhost:8000

