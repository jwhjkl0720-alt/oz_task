from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def game_list():
    games = ["GTA3", "GTA Vice City", "GTA San Andreas", "GTA 6"]
    return render_template("game.html", games=games)

if __name__ == "__main__":
    app.run(debug=True)