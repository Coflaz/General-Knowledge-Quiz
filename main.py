from data import question_data
import time
import random
from prettytable import PrettyTable
import os

class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

class Player:
    def __init__(self, name, score=0, pass_question=False):
        self.name = name
        self.score = score
        self.pass_question = pass_question

question_bank = [Question(question["text"], question["answer"]) for question in question_data]

class Quiz:
    def __init__(self, quiz_name, players=None):
        self.quiz_name = quiz_name
        self.players = players or []
        self.question_bank = question_bank.copy()
        self.question_number = 0

    def start(self):
        print("\nWelcome to the {} quiz!".format(self.quiz_name))
        time.sleep(1)
        print("\nYou will be asked a series of True or False questions.")
        time.sleep(1)
        print("\nPlease enter 'True' or 'False' for each question.")
        time.sleep(1)
        print("\nType 'pass' to skip a question that will give 0 points.")
        time.sleep(1)
        print("\nGood luck!\n")

    def determine_users(self):
        while True:
            users_amount = int(input("Enter the number of players (up to 10): "))
            if 1 <= users_amount <= 10:
                break
            else:
                print("Please enter a number between 1 and 10.")

        for i in range(1, users_amount + 1):
            player_name = input("\nUser #{}'s username: ".format(i))
            self.players.append(Player(player_name))

        print("This is a {} player quiz.".format(len(self.players)))

    def display_player_scores(self):
        player_table = PrettyTable(["Player #", "Nickname", "Score"])
        for i, player in enumerate(self.players, start=1):
            player_table.add_row([i, player.name, player.score])
        print(player_table)
        time.sleep(3)
        if self.should_end_quiz():
                os.system("cls" if os.name == "nt" else "clear")
                print("Thank you for playing!")
                print("\nFinal scores:\n")
                print(player_table)
                exit()
        time.sleep(2)

    def reveal_answer(self, correct_answer):
        time.sleep(1)
        print("\nThe correct answer was: {}".format(correct_answer))
        time.sleep(1)
    

    def ask_question(self):
        os.system("cls" if os.name == "nt" else "clear")
        self.question_number += 1
        random_question = self.question_bank.pop(random.randint(0, len(self.question_bank) - 1))
        print("\nQuestion #{}:".format(self.question_number))
        time.sleep(1)
        print(random_question.prompt)
        time.sleep(1)

        active_players = [player for player in self.players if not player.pass_question]

        if not active_players:
            print("All players have passed. Quiz ends.")
            return

        for player in active_players:
            if player.pass_question:
                print("{} has passed this question.".format(player.name))
            else:
                answer = input("\n{}'s answer: ".format(player.name)).lower()
                if self.check_answer(answer, random_question.answer) == "pass":
                    player.pass_question = True
                elif self.check_answer(answer, random_question.answer):
                    player.score += 1
                else:
                    player.score -= 1


        self.reveal_answer(random_question.answer)

    def should_end_quiz(self):
        end_input = input("\nDo you want to end the quiz? (y/n): ").lower()
        return end_input == "y"

    def check_answer(self, answer, correct_answer):
        answer = answer.lower()  
        correct_answer = correct_answer.lower()  

        if answer == "pass":
            return "pass"
        elif answer in {"true", "false"}:
            return answer == correct_answer
        else:
            print("\nInvalid input. Please try again.\n")
            return False

    def play(self):
        os.system("cls" if os.name == "nt" else "clear")
        self.start()
        self.determine_users()

        while True:
            self.ask_question()
            self.display_player_scores()

            if any(player.score >= 15 for player in self.players):
                print("Quiz ends. A player has reached a score of 15.")
                break

            if all(player.pass_question for player in self.players):
                print("All players have passed. Quiz ends.")
                break

if __name__ == "__main__":
    quiz = Quiz("General Knowledge Quiz")
    quiz.play()
