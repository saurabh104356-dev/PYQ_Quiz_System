
# ==========================================================
# validation.py
# Input Validation for PYQ Quiz & Performance System
# ==========================================================


def validate_name(name):
    """
    Checks whether the student name is valid.
    """

    name = name.strip()

    if name == "":
        return False

    if not name.replace(" ", "").isalpha():
        return False

    return True


def validate_subject_choice(choice, subjects):
    """
    Checks whether the selected subject exists.
    """

    if choice.isdigit():
        choice = int(choice)

        if choice >= 1 and choice <= len(subjects):
            return True

    return False


def validate_answer(answer):
    """
    Checks whether the quiz answer is A, B, C or D.
    """

    answer = answer.strip().upper()

    if answer in ["A", "B", "C", "D"]:
        return True

    return False


def validate_menu_choice(choice):
    """
    Checks whether the menu choice is a valid number.
    """

    if choice.isdigit():
        choice = int(choice)

        if choice >= 1 and choice <= 6:
            return True

    return False


def get_valid_answer():
    """
    Keeps asking until the user enters A, B, C or D.
    """

    while True:
        answer = input("Enter your answer (A/B/C/D): ").strip().upper()

        if validate_answer(answer):
            return answer

        print("Invalid answer. Please enter A, B, C or D.")


def get_valid_name():
    """
    Keeps asking until the user enters a valid name.
    """

    while True:
        name = input("Enter your name: ").strip()

        if validate_name(name):
            return name

        print("Invalid name. Please enter letters and spaces only.")

