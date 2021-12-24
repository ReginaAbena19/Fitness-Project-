import unittest
import unittest.mock as mock
import pandas as pd
from src.website.quiz.written_workout import WrittenWorkout


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

if __name__ == '__main__':
    unittest.main()