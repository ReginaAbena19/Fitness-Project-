# import unittest
# from unittest.mock import patch

# def test_get_written_workout(self):
#     with patch('written_workout.requests.form') as mocked_get:
#         user_1 =

#         mocked_get.return_value.ok = True
#         mocked_get.return_value.text = 'Success'

#         workout = self.user_1.get_written_workout('')
#         mocked_get.assert_called_with('muscle-group')
#         self.assertEqual(workout, 'Success')

# if __name__ == '__main__':
#     unittest.main()


# testing the website
import unittest
from src.main import app
from flask import session, request
from src.website.youtube.youtube_utils import YoutubeWorkout


class WebsiteTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        app.config['SECRET_KEY'] = 'cfgfitnessproject'
        self.app = app.test_client()
        self.assertEqual(app.debug, False)

# test to check if connection is successful
    def test_sign_up_path(self):
        response = self.app.get("/sign-up")
        self.assertEqual(response.status_code, 200)

# test to check that user cannot see home page if they are not logged in
    def test_home_logged_out(self):
        response = self.app.get("/home")
        self.assertEqual(response.status_code, 404)

# test to check if user can see their profile page when logged in
    def test_profile_logged_in(self):
        if session:
            response = self.app.get("/profile")
            self.assertEqual(response.status_code, 200)

# test to check if home page loads the quiz form
    def test_home_quiz(self):
        if session:
            response = self.app.get("/home")
            self.assertIn('<form method="post">'.encode(), response.data)

# tests to check if user picks a written workout, then the website redirects user to written workout page
    def test_written_results_page(self):
        if session:
            if request.form['submit-button'] == "written":
                response = self.app.get("/results-written")
                self.assertEqual(response.status_code, 200)

# test to check if the personalised workout pick displays 3 videos on results page
    def test_show_3_videos(self):
        if session:
            if request.form['submit-button'] == "personalised-youtube":
                response = self.app.get("/results")
                self.assertIn('<iframe src="https://www.youtube.com/embed/{{videos[i]["id"]["videoId"]}}"> len=3'.encode(),
                              response.data)

# test to check if personalised user query will render personalised response on results page
    def test_personalised_video_query(self):
        if session:
            if request.form['workout-location'] == "home" and request.form['muscle-group'] == "abs" and "workout" and \
                    request.form['submit-button'] == "personalised-youtube":
                youtube_class = YoutubeWorkout(workout_type="home+abs+workout", number_of_videos=3)
                response = youtube_class.get_workout_results_from_youtube(workout_type="home+abs+workout", number_of_videos=3)
                self.assertIn(response, "/results")
                
