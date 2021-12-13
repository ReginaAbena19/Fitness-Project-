from generate_random_workout import get_random_workout # Delia's random workout
from user_QA_and_workouts import user_id # assigned this object to the quiz class to call its methods
from views import main # Yasmine's results function

# User decides whether they want a random workout or input their preferences


def main():
    first_move = input("Hello!, What would you like to do today? Options are: A) Random Workout\n B) Specific Workout?"
                       "\n Answer:")
    if first_move == "A" or first_move == "Random Workout":
        get_random_workout()
    elif first_move == "B" or first_move == "Specific Workout": # calling the quiz methods
        user_id.exercise_goals()
        user_id.body_parts_training()
        user_id.workout_location()
        main() # calling Yasmine's video results function
    else:
        print("Please pick a valid option.")


if __name__ == "__main__":
    main()
    
