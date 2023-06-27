from flask import Flask, request, render_template, jsonify
from uuid import uuid4

from boggle import BoggleGame

app = Flask(__name__)
app.config["SECRET_KEY"] = "this-is-secret"

# The boggle games created, keyed by game id
games = {}  # {game_id: game}


@app.get("/")
def homepage():
    """Show board."""

    return render_template("index.html")


@app.post("/api/new-game")
def new_game():
    """Start a new game and return JSON: {game_id, board}."""

    # get a unique string id for the board we're creating
    game_id = str(uuid4())
    game = BoggleGame()
    games[game_id] = game
    print(games)

    game_info = {'gameId': game_id, 'board': game.board}

    return jsonify(game_info)


@app.post("/api/score-word")
def handle_word():
    """
    input: word - string
    output:
        - if not a word return json{result: "not-word"}
        - if not on board return json{result: "not-on-board"}
        - if a valid word return json{result: "ok"}
    """

    word = request.json['word'].upper()
    game_id = request.json['gameId']
    game_instance = games[game_id]
    print(game_instance)

    if not game_instance.is_word_in_word_list(word):
        return jsonify({"result": "not-word"})
    elif not game_instance.check_word_on_board(word):
        return jsonify({"result": "not-on-board"})
    else:
        return jsonify({"result": "ok"})
