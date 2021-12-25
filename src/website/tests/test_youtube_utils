# testing YoutubeWorkout
import unittest
from src.website.youtube.youtube_utils import YoutubeWorkout
from unittest.mock import patch


class TestYoutubeWorkout(unittest.TestCase):
    def test_connect_to_api(self):
        return_list = ("youtube", "v3", "AIzaSyB5YfBeSnx_VnIDCmfkJHp5lzci9wNe4-E")
        response = YoutubeWorkout.connect_to_api(self)
        self.assertEqual(response, return_list)

    def test_get_youtube_api_result(self):
        response = YoutubeWorkout(workout_type='yt', number_of_videos=20).get_youtube_api_result('youtube', 'v3','AIzaSyB5YfBeSnx_VnIDCmfkJHp5lzci9wNe4-E')
        self.assertEqual(response['kind'], 'youtube#searchListResponse')

    def test_randomise_result(self):
        items_list = ["a", "b", "c"]
        data = {"items": items_list}
        response = YoutubeWorkout(workout_type='yt', number_of_videos=2).randomise_results(data)
        self.assertIn(response[0], items_list)
        self.assertIn(response[1], items_list)

    @patch('test_youtube_utils.YoutubeWorkout.url_to_db')
    def test_create_urls_list_in_db(self, url_to_db):
        input_items = [{
            "id": {
                "videoId": "36"
            }
        }]
        response = YoutubeWorkout(workout_type='yt', number_of_videos=3).create_urls_list_in_db(input_items)
        self.assertEqual(response, None)

    @patch('src.website.youtube.youtube_utils.render_template')
    @patch('src.website.youtube.youtube_utils.YoutubeWorkout.connect_to_api')
    @patch('src.website.youtube.youtube_utils.YoutubeWorkout.get_youtube_api_result')
    @patch('src.website.youtube.youtube_utils.YoutubeWorkout.randomise_results')
    @patch('src.website.youtube.youtube_utils.YoutubeWorkout.create_urls_list_in_db')
    def test_get_workout_results_from_youtube(self, create_url, rend_res, get_video, connect_api, render):
        render.return_value = 'render'
        connect_api.return_value = ['yt', 're', 'auth']
        rend_res.return_value = 'text'
        get_video.return_value = 'vdo'
        create_url.return_value = 'out'
        response = YoutubeWorkout(workout_type='yt', number_of_videos=2).get_workout_results_from_youtube('type', 'number')
        self.assertEqual(response, 'render')

if __name__ == '__main__':
    unittest.main()
