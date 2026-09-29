def display_header(title):
    print("\n==========================================")
    print("       PYQ QUIZ & PERFORMANCE SYSTEM")
    print("==========================================")
    print(title)
    print("==========================================")

def calculate_percentage(score, total=5):
    if total == 0:
        return 0


    percentage = (score / total) * 100
    return percentage


def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "F"

def display_result(name, subject, score, total=5):
    percentage = calculate_percentage(score, total)
    grade = calculate_grade(percentage)


    print("\n==========================================")
    print("              QUIZ RESULT")
    print("==========================================")
    print("Student:", name)
    print("Subject:", subject)
    print("Score:", score, "/", total)
    print("Percentage:", percentage, "%")
    print("Grade:", grade)
    print("==========================================")

    return percentage, grade


def calculate_total_scores(*scores):
    return sum(scores)

def show_details(**details):
    print("\n========== DETAILS ==========")

    for key, value in details.items():
        print(key + ":", value)


def show_student_information(name, subject):
    print("\n========== STUDENT INFORMATION ==========")
    print("Student Name:", name)
    print("Selected Subject:", subject)


from validation import get_valid_answer


def start_quiz(quiz):

    score = 0

    print("\n========== STARTING QUIZ ==========")

    for i in range(len(quiz.questions)):

        print("\nQuestion", i + 1)
        print(quiz.questions[i])

        answer = get_valid_answer()

        if answer == quiz.answers[i]:

            print("Correct!")
            score += 1

        else:

            print("Wrong!")
            print("Correct answer:", quiz.answers[i])

    print("\nQuiz completed!")
    print(
        "Your score:",
        score,
        "/",
        len(quiz.questions)
    )

    return score

