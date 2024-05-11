from flask import jsonify
from flask_restx import Resource, Namespace

post_ns = Namespace('post', description='Post operations')

@post_ns.route('/posts')
class PostController(Resource):
    def get(self):
        """Get all posts."""
        return jsonify({'posts': []})

@post_ns.route('/posts/<int:post_id>')
class PostDetailController(Resource):
    def get(self, post_id):
        """Get post by ID."""
        return jsonify({'post_id': post_id})
