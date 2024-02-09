import requests
from random import choice, randint
from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)
app.config["SECRET_KEY"] = "rick&morty"

RiMo_API = "https://rickandmortyapi.com/api/character/"
response = requests.get(url=RiMo_API)
response.raise_for_status()

data = response.json()
last_page = data["info"]["pages"]


@app.route("/", methods=["GET"])
def home():
    rand_num = randint(1, last_page)

    parameters = {"page": rand_num}

    response = requests.get(url=RiMo_API, params=parameters)
    response.raise_for_status()
    data = response.json()

    characters = choice(data["results"])

    return render_template("index.html", character=characters)


if __name__ == "__main__":
    app.run(debug=True)
