from flask import Flask

app = Flask(__name__)

@app.get("/")
def hello():
    return "Hello, world!"

if __name__ == "__main__":
    # 关键:host=0.0.0.0让容器外能访问
    app.run(host="0.0.0.0", port=5000, debug=False)