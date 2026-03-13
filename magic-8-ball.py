from random import choice


def is_valid_question(question):

    while not question.endswith("?"):

        question = input(
            "I'm answering only YES or NO question, (If you want to exit type E): "
        )

        if question.lower() == "e":
            return False

    return True


def play(user_name, answers, continue_prompts):

    while True:

        question = input(f"Okay {user_name}, what is your question? ")
        if not is_valid_question(question):
            break

        print(choice(answers))

        print(choice(continue_prompts), "Yes: Y, No: N ", end=" ")
        answer = input()

        if answer.lower() != "y":
            print("Come back if you have any questions!")
            break


answers = [
    "Without a doubt",
    "It is predetermined",
    "No doubts whatsoever",
    "Definitely yes",
    "You can be sure of it",
    "I think so - yes",
    "Most likely",
    "Good prospects",
    "Signs point to yes",
    "Yes",
    "Not clear yet, try again",
    "Ask later",
    "Better not to tell",
    "Cannot predict right now",
    "Concentrate and ask again",
    "Don't even think about it",
    "My answer is no",
    "According to my data - no",
    "Prospects are not very good",
    "Very doubtful",
]

continue_prompts = [
    "Any more questions?",
    "Want to ask something else?",
    "Hmm, it seems like you want to ask something else?",
    "What else do you want to ask?",
]

print(
    'Hello! I am a magic ball, and I know the answer to any "yes or no" question you have.'
)
user_name = input("What is your name? ")
play(user_name, answers, continue_prompts)
