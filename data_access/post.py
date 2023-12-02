from flask import g

def create_post(user_id, post_data):    

    try:
        cursor = g.db.cursor()
        cursor.execute('INSERT INTO Posts (user_id, title, content) VALUES (%s, %s, %s)', (user_id, *post_data.values()))
        g.db.commit()
        cursor.close()

        # Return the created post (assuming you have a function to fetch a post by ID)        
        created_post_id = cursor.lastrowid
        created_post = fetch_post_by_id(created_post_id)
        
        return created_post

    except Exception as e:        
        print(f"Error creating post: {e}")
        raise e

def update_post(post_id, post_data):
    try:
        cursor = g.db.cursor()
        cursor.execute('UPDATE Posts SET title = %s, content = %s WHERE post_id = %s', (*post_data.values(), post_id))
        g.db.commit()
        cursor.close()

        # Return the updated post (assuming you have a function to fetch a post by ID)
        updated_post = fetch_post_by_id(post_id)
        return updated_post

    except Exception as e:        
        print(f"Error updating post: {e}")
        raise e

def delete_post(post_id):
    try:
        cursor = g.db.cursor()
        cursor.execute('DELETE FROM Posts WHERE post_id = %s', (post_id,))
        g.db.commit()
        cursor.close()

        # Return a success message or any relevant data
        return {"message": "Post deleted successfully"}

    except Exception as e:        
        print(f"Error deleting post: {e}")
        raise e


def fetch_post_by_id(post_id):
    try:
        cursor = g.db.cursor()
        cursor.execute('SELECT * FROM Posts WHERE post_id = %s', (post_id,))
        result = cursor.fetchone()
        cursor.close()

        # Return the post
        return result

    except Exception as e:        
        print(f"Error fetching post: {e}")
        raise e
    

def fetch_posts():
    try:
        cursor = g.db.cursor()
        cursor.execute('SELECT * FROM Posts')
        result = cursor.fetchall()
        cursor.close()

        # Return the posts
        return result

    except Exception as e:        
        print(f"Error fetching posts: {e}")
        raise e