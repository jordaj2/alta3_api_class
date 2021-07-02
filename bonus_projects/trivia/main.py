from flask import Flask
from flask import redirect
from flask import request
from flask import render_template
from flask import url_for
app = Flask(__name__)


@app.route('/')
def landing_page():
    return render_template("index.html")


@app.route('/answer', methods=['POST'])
def show_results():
    if request.method == "POST":
        if request.form.get("t1"):  # if nm was assigned via the POST
            user_answer = request.form.get("t1")  # grab the value of nm from the POST
        if user_answer == "3":
            return redirect(url_for("result_correct"))
        else:
            return redirect(url_for("result_incorrect"))
    # GET would likely come from a user interacting with a browser

@app.route('/correct')
def result_correct():
    return "You answered correctly would you like another one?"
@app.route('/incorrect')
def result_incorrect():
    return "You answered incorrectly try again.."
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)  # runs the application
