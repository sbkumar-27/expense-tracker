# Expense Tracker

A simple, menu-driven expense tracker built with Python and MySQL. The project currently includes user registration, login, and bank balance setup.

## Features

- User registration with name, phone number, and password
- Automatically generated user ID
- Login using user ID and password
- Store and update a user's balance in MySQL
- MySQL database integration using `mysql-connector-python`

## Tech Stack

- **Language:** Python
- **Database:** MySQL
- **Python package:** `mysql-connector-python`

## Project Structure

```text
expense-tracker/
├── database/
│   └── schema.sql
├── main.py
└── README.md
```

## Requirements

- Python 3
- MySQL Server
- `pip` (Python package installer)

## Setup and Installation

### 1. Clone the repository

```bash
git clone https://github.com/sbkumar-27/expense-tracker.git
cd expense-tracker
```

### 2. Install the Python dependency

```bash
python -m pip install mysql-connector-python
```

### 3. Create the database and tables

Open MySQL and run the SQL commands in `database/schema.sql`.

If the SQL file does not create the database, create it first:

```sql
CREATE DATABASE expense_tracker;
```

Then select the database and run the table definitions from `database/schema.sql`.

### 4. Configure the database connection

Update the connection settings in `main.py` to match your local MySQL setup:

- Host: `localhost`
- Port: `3306`
- Username: your MySQL username
- Password: your MySQL password
- Database: `expense_tracker`

**Security:** Do not commit real database passwords or other secrets to GitHub. For a public repository, move credentials into environment variables or a local configuration file excluded by `.gitignore`.

### 5. Run the application

Run the program from a terminal so you can enter menu choices:

```bash
python main.py
```

## Usage

When the program starts, choose an option:

1. **Login** — enter your user ID and password.
2. **Register** — enter your name, phone number, and password. The application creates a user ID and lets you enter your starting balance.

## Current Scope

This is an early version of the project. Expense recording, income tracking, transaction history, and reports can be added in future updates.

## Contributing

Suggestions and improvements are welcome. For larger changes, create a branch and open a pull request.

## License

No license has been specified yet.
