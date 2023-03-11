from flask import Flask, request, render_template, jsonify
from uuid import uuid4

from boggle import BoggleGame

app = Flask(__name__)
app.config["SECRET_KEY"] = "this-is-secret"

# The boggle games created, keyed by game id
games = {} # {game_id: game}


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


#  data = response.get_json()
#             board = data['board']
#             game_id = data['gameId']
#             print(data)
#             # breakpoint()
#             # write a test for this route
#             self.assertIn('board', data.keys())
#             self.assertIn(game_id, games)
#             self.assertTrue(isinstance(game_id, str))
#             self.assertTrue(isinstance(board, list))