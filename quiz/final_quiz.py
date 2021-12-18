from generate_random_workout import get_random_workout # Delia's random workout
from user_questions_and_answers import user_id # assigned this object to the quiz class to call its methods
from youtube_utils import get_workout_results_from_youtube # Yasmine's results function
from written_workout import get_written_workout # Yasmine's Exercise DB function

# User decides whether they want a random workout or input their preferences


def main(): #Regina's function
    first_move = input("Hello!, What would you like to do today? Options are: A) Random Workout\n B) Specific Workout\n C) Written Workout?"
                       "\n Answer:")
    if first_move == "A" or first_move == "Random Workout":
        get_random_workout()
    elif first_move == "B" or first_move == "Specific Workout": # calling the quiz methods
        user_id.exercise_goals()
        user_id.body_parts_training()
        user_id.workout_location()
        get_workout_results_from_youtube() # calling Yasmine's video results function
    elif first_move == "C" or first_move == "Written Workout":
        user_id.exercise_goals()
        user_id.body_parts_training()
        user_id.workout_location()
        written_workout() # calling Yasmine's Exercise DB results function
    else:
        print("Please pick a valid option.")


if __name__ == "__main__":
    main()
    
