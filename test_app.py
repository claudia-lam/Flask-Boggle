from unittest import TestCase

from app import app, games, BoggleGame

# Make Flask errors be real errors, not HTML pages with error info
app.config['TESTING'] = True

# This is a bit of hack, but don't use Flask DebugToolbar
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']


class BoggleAppTestCase(TestCase):
    """Test flask app of Boggle."""

    def setUp(self):
        """Stuff to do before every test."""

        self.client = app.test_client()
        app.config['TESTING'] = True

    def test_homepage(self):
        """Make sure information is in the session and HTML is displayed"""

        with self.client as client:
            response = client.get('/')
            html = response.get_data(as_text=True)
            ...
            # test that you're getting a template
            self.assertEqual(response.status_code, 200)
            self.assertIn(
                "<!-- boggle-board to be checked in test_homepage() -->", html)
            # consider searching instead
            # for a comment to make it less brittle

    def test_api_new_game(self):
        """Test starting a new game."""

        with self.client as client:
            response = client.post("/api/new-game")

            data = response.get_json()
            board = data['board']
            game_id = data['gameId']
            print(data)
            # breakpoint()
            # write a test for this route
            # self.assertIn('board', data.keys())
            self.assertIn(game_id, games)
            self.assertTrue(isinstance(game_id, str))
            self.assertTrue(isinstance(board, list))

    def test_score_word(self):
        """Make sure word is legal, not on board, or not a word"""

        with self.client as client:
            new_game = client.post("/api/new-game")
            new_game_decoded = new_game.get_json()

            game_id = new_game_decoded["gameId"]

            current_game = games[game_id]

            # change the random board to a fixed board
            current_game.board = [['A', 'B', 'C'],
                                  ['D', 'A', 'D'],
                                  ['C', 'A', 'T']]

            current_game.board_size = 3

            # if not a word in the english language
            response = client.post(
                "/api/score-word",
                json={'gameId': game_id, 'word': 'asdfasdf'})
            data = response.get_json()

            self.assertEqual(data, {"result": "not-word"})

            # if word not on board
            response = client.post(
                "/api/score-word",
                json={'gameId': game_id, 'word': 'DOG'})
            response_data = response.get_json()

            self.assertEqual(response_data, {
                             "result": "not-on-board"})

            # if word is valid
            response = client.post(
                "/api/score-word",
                json={'gameId': game_id, 'word': 'DAD'})
            response_data = response.get_json()

            self.assertEqual(response_data, {
                             "result": "ok"})
