from flask import Flask, render_template, request, redirect
from werkzeug.utils import secure_filename

app = Flask(__name__)


@app.route("/")
def default():
    return redirect('/upload')

@app.route("/upload")
def upload():
    return render_template("upload.html")


@app.route("/uploader", methods=["GET", "POST"])
def upload_file():
    if request.method == "GET":  # if method is a get (same as "/upload")
        return render_template("upload.html")
    if request.method == "POST":
        f = request.files["file"]
        f.save(secure_filename(f.filename))
        return "file uploaded successfully"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)
