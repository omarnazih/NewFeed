from flask import jsonify
from flask.views import MethodView
from flask_smorest import Blueprint, abort

from schemas import PostSchema, PostUpdateSchema
from data_access.post import create_post, fetch_post_by_id, fetch_posts, update_post, delete_post


# Define a Blueprint for the API
blp = Blueprint(
    "Posts", __name__, url_prefix="/post", description="Operations on posts"
)

# Create a MethodView for the Post resource
@blp.route("/<string:post_id>")
class PostView(MethodView):
    @blp.response(200, PostSchema)
    def get(self, post_id):
        try:
            return jsonify({"message": "Success", "data": fetch_post_by_id(post_id)})            
        except KeyError:
            abort(404, message="Post not found")   
                            
    @blp.arguments(PostUpdateSchema)
    @blp.response(200, PostSchema)
    def put(self, post_data, post_id):
        try:                 
            return jsonify({"message": "Post updated successfully", "data": update_post(post_id, post_data)})
        except KeyError:
            abort(404, message="Post not found")

    def delete(self, post_id):        
        try:            
            delete_post(post_id)
            return jsonify({"message": "Post deleted successfully"})
        except KeyError:
            abort(404, message="Post not found")            


@blp.route("/")
class PostsView(MethodView):
    @blp.response(200, PostSchema(many=True))
    def get(self):     
        return jsonify({"message": "Success", "data": fetch_posts()})

    @blp.arguments(PostSchema)
    @blp.response(201, PostSchema)
    def post(self, post_data):
        post = create_post(user_id=1, post_data=post_data)
        return jsonify({"message": "Post created successfully", "data": post})
        