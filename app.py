from flask import Flask, render_template, request
from logic.excuse_generator import generate_excuse
from utils.validators import validate_input

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    scenario = request.form.get("scenario")
    tone = request.form.get("tone")
    reason = request.form.get("reason")
    language = request.form.get("language", "en")

    if not validate_input(scenario, tone, reason):
        return render_template("result.html", excuse="Invalid input.", tone="formal")

    excuse = generate_excuse(scenario, tone, reason, language)
    return render_template("result.html", excuse=excuse, tone=tone)
if __name__ == "__main__":
    app.run(debug=True)
