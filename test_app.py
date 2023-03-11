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
