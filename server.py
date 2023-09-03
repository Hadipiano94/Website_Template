from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def get_home_page():
    return render_template("index.html")


@app.route("/portfolio_details")
def get_details_page():
    return render_template("portfolio-details.html")


if __name__ == "__main__":
    app.run(debug=True)
