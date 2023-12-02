from flask import g
from mysql.connector import connect, Error

def get_db(app):  
    if 'db' not in g:
        try:
            g.db = connect(
                host=app.config["DATABASE_HOST"],
                user=app.config["DATABASE_USER"],
                password=app.config["DATABASE_PASSWORD"],
                database=app.config["DATABASE_NAME"],
            )
        except Error as e:
            print(f"Error: {e}")
            g.db = None
    return g.db

def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()
     
def init_db(app):
    db = get_db(app)
    cursor = db.cursor()

    # Create Users table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Users (
            user_id INT PRIMARY KEY AUTO_INCREMENT,
            username VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL
        )
    """)

    # Create Posts table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Posts (
            post_id INT PRIMARY KEY AUTO_INCREMENT,
            user_id INT,
            title VARCHAR(255) NOT NULL,
            content TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES Users(user_id)
        )
    """)

    # Create Comments table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Comments (
            comment_id INT PRIMARY KEY AUTO_INCREMENT,
            user_id INT,
            post_id INT,
            content TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES Users(user_id),
            FOREIGN KEY (post_id) REFERENCES Posts(post_id)
        )
    """)

    # Create Likes table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Likes (
            like_id INT PRIMARY KEY AUTO_INCREMENT,
            user_id INT,
            post_id INT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES Users(user_id),
            FOREIGN KEY (post_id) REFERENCES Posts(post_id)
        )
    """)

    # Create Shares table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Shares (
            share_id INT PRIMARY KEY AUTO_INCREMENT,
            user_id INT,
            post_id INT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES Users(user_id),
            FOREIGN KEY (post_id) REFERENCES Posts(post_id)
        )
    """)

    # Create Follows table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Follows (
            follower_id INT,
            followee_id INT,
            PRIMARY KEY (follower_id, followee_id),
            FOREIGN KEY (follower_id) REFERENCES Users(user_id),
            FOREIGN KEY (followee_id) REFERENCES Users(user_id)
        )
    """)
    
    #Insert Admin user for testing
    cursor.execute("""
        Insert into Users (username, email) values ('admin', 'admin@localhost')
    """)    

    db.commit()
    cursor.close()        
