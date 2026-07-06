from flask import Flask, request, Response
import requests

app = Flask(__name__)

COURSE_SERVICE = "http://127.0.0.1:5001"
STUDENT_SERVICE = "http://127.0.0.1:5002"

def forward_request(base_url, path):
    url = f"{base_url}{path}"

    response = requests.request(
        method = request.method, 
        url = url,
        headers = {
            key: value
            for key, value in request.headers
            if key.lower() != "host"
        },
        json = request.get_json(silent = True),
        params = request.args
    )

    return Response(
        response.content,
        status = response.status_code,
        content_type = response.headers.get("Content-Type")
    )

@app.route("/")
def home():
    return {"service": "Course Management API Gateway", "status": "running"}


@app.route("/api/courses/", defaults={"path": ""}, methods=["GET", "POST"])
@app.route("/api/courses/<path:path>", methods=["GET", "POST", "PUT", "DELETE"])
def course_gateway(path):
    return forward_request(COURSE_SERVICE, f"/api/courses/{path}")


@app.route("/api/students/", defaults={"path": ""}, methods=["GET", "POST"])
@app.route("/api/students/<path:path>", methods=["GET", "POST", "PUT", "DELETE"])
def student_gateway(path):
    return forward_request(STUDENT_SERVICE, f"/api/students/{path}")


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)