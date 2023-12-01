from flask import g, jsonify, request
from flask.views import MethodView
from flask_smorest import Blueprint, abort

from schemas import PostSchema, PostUpdateSchema


# Define a Blueprint for the API
blp = Blueprint(
    "Posts", __name__, url_prefix="/post", description="Operations on posts"
)

# Create a MethodView for the Post resource
@blp.route("/<string:post_id>")
class PostView(MethodView):
    @blp.response(200, PostSchema)
    def get(self, post_id):
        """Get Post"""
        
        cursor = g.db.cursor()
        cursor.execute('SELECT * FROM Users')
        result = cursor.fetchall()
        cursor.close()
        
        print(result)
        return jsonify({"message": "Get Post"})

    @blp.arguments(PostUpdateSchema)
    @blp.response(200, PostSchema)
    def put(self, post_data, post_id):
        """Update Post"""
        data = post_data.get_json()                

        return jsonify({"message": "Post updated successfully"})

    def delete(self, post_id):
        """Delete Post"""
        return jsonify({"message": "Delete Post"})


@blp.route("/")
class PostsView(MethodView):
    @blp.response(200, PostSchema(many=True))
    def get(self):
        """Get Posts"""
        return jsonify({"message": "Get Posts"})

    @blp.arguments(PostSchema)
    @blp.response(201, PostSchema)
    def post(self, post_data):
        """Create Post"""
        data = post_data    
        
        print(post_data)

        return jsonify({"message": "Post created successfully", "data": post_data})