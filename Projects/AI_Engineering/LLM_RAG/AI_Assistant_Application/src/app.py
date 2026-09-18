
from flask import Flask, request, render_template
from rag import answer_question

app = Flask(__name__, template_folder="../templates")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/generate", methods=["POST"])
def generate():

    question = request.form["prompt"]

    response = answer_question(question)

    return render_template(
        "index.html",
        prompt=question,
        response=response
    )


if __name__ == "__main__":
    app.run(debug=True)

