class QuizApp:
    def __init__(self):
        self.score = 0
        self.questions = {
            "What is the capital of France?": {
                "A": "Berlin",
                "B": "Paris",
                "C": "London",
                "D": "Rome",
                "correct": "B"
            },
            "What is the largest planet in our solar system?": {
                "A": "Earth",
                "B": "Saturn",
                "C": "Jupiter",
                "D": "Uranus",
                "correct": "C"
            },
            "Who painted the Starry Night?": {
                "A": "Leonardo da Vinci",
                "B": "Vincent van Gogh",
                "C": "Claude Monet",
                "D": "Pablo Picasso",
                "correct": "B"
            }
        }

    def ask_questions(self):
        for question, answers in self.questions.items():
            print(question)
            for option, answer in answers.items():
                if option != "correct":
                    print(f"{option}: {answer}")
            user_answer = input("Choose the correct option: ").upper()
            if user_answer == answers["correct"]:
                self.score += 1
                print("Correct answer!\n")
            else:
                print(f"Wrong answer. The correct answer is {answers['correct']}\n")

    def display_score(self):
        print(f"Your final score is {self.score} out of {len(self.questions)}")


def main():
    quiz_app = QuizApp()
    quiz_app.ask_questions()
    quiz_app.display_score()


if __name__ == "__main__":
    main()
