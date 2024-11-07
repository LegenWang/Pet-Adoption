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

    # Create Users table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )
    """)

    #Create application table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Applications (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_name TEXT NOT NULL UNIQUE,
            user_age INTEGER,
            user_occupation TEXT NOT NULL,
            user_salary INTEGER,
            pet_name TEXT NOT NULL,
            pet_breed TEXT NOT NULL
                   )
                   """)

    # Create Pets table
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

    # Insert initial data into Pets table if not already added
    cursor.execute("""
        INSERT OR IGNORE INTO Pets (name, breed, age) 
        VALUES 
            ('Buddy', 'Golden Retriever', 3),
            ('Rex', 'Bulldog', 6),
            ('Tucker', 'Mixed', 1)
    """)

    #Insert initial data into application table
    cursor.execute("""
        INSERT OR IGNORE INTO Applications (id, user_name, user_age, user_occupation, user_salary, pet_name, pet_breed) 
        VALUES 
            (1, 'Alice', 30, 'Engineer', 80000, 'Buddy', 'Golden Retriever'),
            (2, 'Bob', 40, 'Teacher', 50000, 'Rex', 'Bulldog')
    """)

    #Insert initial data into manager table
    cursor.execute("""
        INSERT OR IGNORE INTO Managers (id, manager_email, manager_password) 
        VALUES 
            (1, 'admin@example.com', 'password123')
    """)

    # Insert initial data into Users
    cursor.execute("""
        INSERT OR IGNORE INTO Users (username, password) 
        VALUES
            ('steven', '1234567'),
            ('james', 'helloworld')
    """)

    # Commit the changes and close the connection
    connection.commit()
    connection.close()

def query_all_users():
    """
    Retrieves all users from the Users table.
    """
    connection = sqlite3.connect('petSite.db')
    connection.row_factory = sqlite3.Row
    result = connection.execute('SELECT id, username FROM Users').fetchall()
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

def add_new_user(username, password):
    """
    Adds a new user to the Users table.
    """
    connection = sqlite3.connect('petSite.db')
    cursor = connection.cursor()
    cursor.execute("""
        INSERT INTO Users (username, password) 
        VALUES (?, ?)
    """, (username, password))
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
