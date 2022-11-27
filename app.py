# Imports and setup

from flask import Flask, render_template, redirect

# Create instance of flask app

app = Flask(__name__)

# Create route that renders index.html template

@app.route("/")
def index():
    # crypto_dict = ["Bootmen", "Rabbit-Proof Fence", "The Bank", "Paperback Hero", "The Adventures of Priscilla, Queen of the Desert"]
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
