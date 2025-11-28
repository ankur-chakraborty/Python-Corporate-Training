
def write_quiz(questions, filename="quiz.txt"):
    """
    Writes a list of questions into a file with question numbers and blank lines for answers.

    :param questions: List of question strings
    :param filename: Name of the output file (default: quiz.txt)
    """
    try:
        with open(filename, "w", encoding="utf-8") as file:
            for i, question in enumerate(questions, start=1):
                file.write(f"{i}. {question}\n")
                file.write("\n")
                file.write("\n")
        print(f"Quiz written successfully to {filename}")
    except Exception as e:
        print(f"An error occurred: {e}")



questions = [
    "What is the capital of France?",
    "Who wrote 'To Kill a Mockingbird'?",
    "What is 2 + 2?"
]

write_quiz(questions)
