import unittest
from unittest.mock import patch

def test_get_written_workout(self):
    with patch('written_workout.requests.form') as mocked_get:
        user_1 =

        mocked_get.return_value.ok = True
        mocked_get.return_value.text = 'Success'

        workout = self.user_1.get_written_workout('')
        mocked_get.assert_called_with('muscle-group')
        self.assertEqual(workout, 'Success')

if __name__ == '__main__':
    unittest.main()
