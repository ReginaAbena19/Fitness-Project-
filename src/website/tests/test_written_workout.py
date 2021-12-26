import unittest
import unittest.mock as mock
import pandas as pd
from src.website.quiz.written_workout import WrittenWorkout

"""
This tests whether the URL for the API request is correctly generated based
on the input from the html form
"""


class TestWrittenWorkout(unittest.TestCase):
    def test_generate_url_for_api(self):
        self.assertEqual(WrittenWorkout.generate_url_for_api(self, "Back"),
                         "https://exercisedb.p.rapidapi.com/exercises/bodyPart/Back")
        self.assertEqual(WrittenWorkout.generate_url_for_api(self, "Abs"),
                         "https://exercisedb.p.rapidapi.com/exercises/bodyPart/Abs")
        self.assertEqual(WrittenWorkout.generate_url_for_api(self, "Legs"),
                         "https://exercisedb.p.rapidapi.com/exercises/bodyPart/Legs")

    def test_connect_to_exercisedb_api(self):
        return_list = ({
                           'x-rapidapi-host': "exercisedb.p.rapidapi.com",
                           'x-rapidapi-key': "6491b9bedamsh60d64359f44595dp19a013jsn596072484b13"
                       }, {})
        response = WrittenWorkout.connect_to_exercisedb_api(self)
        self.assertEqual(response, return_list)


"""
These are some tests that we attempted but couldn't get to pass successfully.
"""
# def test_make_request_to_api(self):
#   response = WrittenWorkout().make_request_to_api(
#       url = "https://exercisedb.p.rapidapi.com/exercises/bodyPart/Abs",
#       headers = {
#           'x-rapidapi-host': "exercisedb.p.rapidapi.com",
#           'x-rapidapi-key': "6491b9bedamsh60d64359f44595dp19a013jsn596072484b13"
#       },
#       payload= {})
#   self.assertEqual(response, )

# def test_randomise_api_result(self):
#    items_list = {}
#    data = {}
#    response = WrittenWorkout(dd,5).randomise_api_result(data)
#    self.assertIn(response[0], items_list)
#    self.assertIn(response[1], items_list)

# def test_append_results_to_lists(self):

# def test_create_workout_csv(self):
#    d = {'bodyPart': 'Legs',
#         'equipment': 'Gym',
#         'gifUrl': '',
#         'id': '',
#         'name': '',
#         'target': ''}

#    test_df = pd.DataFrame(d)
#    with mock.patch.object(test_df, "to_csv") as to_csv_mock:
#        WrittenWorkout.create_workout_csv(test_df, "workout.csv")
#        to_csv_mock.assert_called_with("workout.csv")


if __name__ == '__main__':
    unittest.main()
