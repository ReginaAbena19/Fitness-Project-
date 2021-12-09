
# Creating the Quiz class

class Quiz:
    def __init__(self):
        self.user_preferences = []

    # Question 1- exercise goals( 4 options- strength training, build muscle, endurance
    def exercise_goals(self):
        user_question1_answer = input("What are your exercise goals? Options are: A. Weightloss\n B. Strength training"
                                      "\n C. Muscle building\n, D. Endurance\n ")
        fitness_goals = ["A. Weightloss", "B. Strength training", "C. Muscle building", "D. Endurance"]
        if user_question1_answer in fitness_goals:
            self.user_preferences.append(user_question1_answer)
        else:
            error_message = input("Please pick one of the options provided.")

        print("Click 'Next Question'")

    def body_parts_training(self):
        user_question2_answer = input( "What do you want to train today? Options are: A. Legs\n B. Arms \n, C. Abs \n, "
                                       "D. Back\n ")
        body_training = ["A. Legs", "B. Arms", "C. Abs", "D. Back"]
        if user_question2_answer in body_training:
            self.user_preferences.append(user_question2_answer)
        else:
            error_message = input("Please pick one of the options provided.")

        print("Click 'Next Question'")

    def workout_location(self):
        user_question3_answer = input( "Where do you want to train today? Options are: A. Home\n B. Gym\n")
        location = ["A. Home", "B. Gym"]
        if user_question3_answer in location:
            self.user_preferences.append(user_question3_answer)
        else:
            error_message = input("Please pick one of the options provided.")

        print("Your results will be displayed soon.")

    def get_results(self):
        print(self.user_preferences)


user = Quiz()


#W/out based on quiz
import os
import googleapiclient.discovery


def quiz_based_workout():
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = "AIzaSyB5YfBeSnx_VnIDCmfkJHp5lzci9wNe4-E"
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey=DEVELOPER_KEY)
    requests = youtube.search().list(
        part="snippet",
        maxResults=3,
        q=user.get_results(),
    )
    response = requests.execute()
    items = response["items"]

    videos = []
    for item in items:
        videos.append(item['id']['videoId'])

    print(videos)

    return render_template('results.html', len=len(videos), videos=videos)



