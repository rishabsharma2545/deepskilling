from flask import Flask
from config import Config
from courses import courses_bp

# 37. In app.py, create the Flask app using the application factory pattern.
def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # 40. Register the blueprint in create_app() with app.register_blueprint(courses_bp).
    app.register_blueprint(courses_bp)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run()

