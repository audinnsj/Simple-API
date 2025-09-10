from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "API sederhana untuk mengirim file html"

@app.route("/file/<size>")
def get_file(size):
    try:
        return open(f"file_{size}.html", "r").read()
    except:
        return "File tidak ditemukan"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050)
