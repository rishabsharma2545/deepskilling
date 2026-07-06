from flask import Flask

from config import Config
from extensions import db


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    from routes import course_bp
    app.register_blueprint(course_bp)

    with app.app_context():
        db.create_all()

    return app


app = create_app()

@app.route("/")
def home():
    return {"service": "Course Service", "status": "running"}

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5001, debug=True)