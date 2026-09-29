
# ==========================================================
# storage.py
# Save and Load Quiz Results
# ==========================================================

import json

FILE_NAME = "results.json"


def save_result(name, subject, score, percentage, grade):
    """Save one quiz result to a JSON file."""

    result = {
        "name": name,
        "subject": subject,
        "score": score,
        "percentage": percentage,
        "grade": grade
    }

    try:
        with open(FILE_NAME, "r") as file:
            results = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        results = []

    results.append(result)

    with open(FILE_NAME, "w") as file:
        json.dump(results, file, indent=4)


def load_results():
    """Load all previous quiz results."""

    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def display_previous_results():
    """Display all saved quiz results."""

    results = load_results()

    print("\n==========================================")
    print("          PREVIOUS QUIZ RESULTS")
    print("==========================================")

    if len(results) == 0:
        print("No previous results found.")
        return

    for i, result in enumerate(results, start=1):
        print("\nQuiz", i)
        print("Student:", result["name"])
        print("Subject:", result["subject"])
        print("Score:", result["score"])
        print("Percentage:", result["percentage"], "%")
        print("Grade:", result["grade"])


