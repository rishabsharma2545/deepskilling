from flask import Flask, jsonify
from config import Config
from courses import courses_bp

# 37. In app.py, create the Flask app using the application factory pattern.
def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # 40. Register the blueprint in create_app() with app.register_blueprint(courses_bp).
    app.register_blueprint(courses_bp)
    
    # 45. Add Flask error handlers for 404 and 500 using @app.errorhandler(404). 
    # Return JSON error responses (not HTML) — APIs should never return HTML error pages.
    @app.errorhandler(404)
    def not_found_error(error):
        """Handles 404 Not Found errors globally across the app."""
        return jsonify({
            'status': 'error',
            'message': 'The requested URL or resource could not be found.'
        }), 404

    @app.errorhandler(500)
    def internal_error(error):
        """Handles 500 Internal Server Error exceptions globally."""
        return jsonify({
            'status': 'error',
            'message': 'An unexpected internal server error occurred.'
        }), 500
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run()

