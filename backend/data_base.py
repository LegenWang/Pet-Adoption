"""
SQLite integration file
It hanldles the createion and managment of the database
"""

import sqlite3

def initialize_database():
    """
    Initializes the SQLite database
    Creates the tables
    """
    connection = sqlite3.connect('petSite.db')
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()

    # Create the Applications table if it doesn't exist (without the new column)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Applications (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_name TEXT NOT NULL UNIQUE,
            user_age INTEGER,
            user_occupation TEXT NOT NULL,
            user_salary INTEGER,
            pet_name TEXT NOT NULL,
            pet_breed TEXT NOT NULL,
            status TEXT DEFAULT 'Pending'
        )
    """)

    # Create the Pets table if it doesn't exist
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Pets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            breed TEXT NOT NULL,
            age INTEGER NOT NULL
        )
    """)

    # Insert initial data into Pets table if not already added
    cursor.execute("""
        INSERT OR IGNORE INTO Pets (id, name, breed, age) 
        VALUES 
            (1, 'Buddy', 'Golden Retriever', 3),
            (2, 'Rex', 'Bulldog', 6),
            (3, 'Tucker', 'Mixed', 1)
    """)

    # Insert initial data into Applications table
    cursor.execute("""
        INSERT OR IGNORE INTO Applications (id, user_name, user_age, user_occupation, user_salary, pet_name, pet_breed) 
        VALUES 
            (1, 'Alice', 30, 'Engineer', 80000, 'Buddy', 'Golden Retriever'),
            (2, 'Bob', 40, 'Teacher', 50000, 'Rex', 'Bulldog'),
            (3, 'Charlie', 35, 'Artist', 60000, 'Tucker', 'Mixed')
    """)

    connection.commit()
    connection.close()

def initialize_users_managers_database():
    """
    Initializes the users_managers SQLite database
    Creates the Users and Managers tables
    """
    connection = sqlite3.connect('users_managers.db')
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()

    # Create Users table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            email TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL,
            role TEXT NOT NULL DEFAULT 'user'  -- Added role column
        )
    """)

    # Create Managers table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Managers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            manager_email TEXT NOT NULL UNIQUE,
            manager_password TEXT NOT NULL
        )
    """)

    # Insert initial data into Users with role info
    cursor.execute("""
        INSERT OR IGNORE INTO Users (username, email, password, role) 
        VALUES
            ('steven', 'steven@example.com', '1234567', 'user'),
            ('james', 'james@example.com', 'helloworld', 'user')
    """)

    # Insert initial data into Managers table
    cursor.execute("""
        INSERT OR IGNORE INTO Managers (id, manager_email, manager_password) 
        VALUES 
            (1, 'admin@example.com', 'password123')
    """)

    connection.commit()
    connection.close()

def query_all_users():
    """
    Retrieves all users from the Users table.
    """
    connection = sqlite3.connect('users_managers.db')
    connection.row_factory = sqlite3.Row
    result = connection.execute('SELECT id, username, email FROM Users').fetchall()
    connection.close()
    return result

def query_all_pets():
    """
    Retrieves all pets from the Pets table.
    """
    connection = sqlite3.connect('petSite.db')
    connection.row_factory = sqlite3.Row
    result = connection.execute('SELECT id, name, breed, age FROM Pets').fetchall()
    connection.close()
    return result

def add_new_user(username, email, password):
    """
    Adds a new user to the Users table.
    """
    connection = sqlite3.connect('users_managers.db')
    cursor = connection.cursor()
    cursor.execute("""
        INSERT INTO Users (username, email, password) 
        VALUES (?, ?, ?)
    """, (username, email, password))
    connection.commit()
    connection.close()

def add_new_pet(name, breed, age):
    """
    Adds a new pet to the Pets table.
    """
    connection = sqlite3.connect('petSite.db')
    cursor = connection.cursor()
    cursor.execute("""
        INSERT INTO Pets (name, breed, age) 
        VALUES (?, ?, ?)
    """, (name, breed, age))
    connection.commit()
    connection.close()


# Call initialize_database only on the first run of the application
if __name__ == "__main__":
    initialize_database()
    initialize_users_managers_database()
