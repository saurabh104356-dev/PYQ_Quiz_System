
# ==========================================================
# tests.py
# Testing Module for PYQ Quiz & Performance System
# ==========================================================

from models import Student, Quiz

from quiz_data import (
    get_questions,
    get_answers,
    get_subjects
)

from quiz_functions import (
    calculate_percentage,
    calculate_grade,
    calculate_total_scores
)

from validation import (
    validate_name,
    validate_answer,
    validate_subject_choice
)


# ==========================================================
# TEST 1
# ==========================================================

def test_percentage():

    result = calculate_percentage(4, 5)

    assert result == 80.0

    print("Test 1 passed: Percentage calculation")


# ==========================================================
# TEST 2
# ==========================================================

def test_grade():

    result = calculate_grade(85)

    assert result == "A"

    print("Test 2 passed: Grade calculation")


# ==========================================================
# TEST 3
# ==========================================================

def test_total_scores():

    result = calculate_total_scores(5, 4, 3)

    assert result == 12

    print("Test 3 passed: Total score calculation")


# ==========================================================
# TEST 4
# ==========================================================

def test_name_validation():

    assert validate_name("Saurabh Singh") == True

    assert validate_name("") == False

    assert validate_name("Saurabh123") == False

    print("Test 4 passed: Name validation")


# ==========================================================
# TEST 5
# ==========================================================

def test_answer_validation():

    assert validate_answer("A") == True

    assert validate_answer("b") == True

    assert validate_answer("E") == False

    print("Test 5 passed: Answer validation")


# ==========================================================
# TEST 6
# ==========================================================

def test_subject_validation():

    subjects = get_subjects()

    assert validate_subject_choice("1", subjects) == True

    assert validate_subject_choice("100", subjects) == False

    print("Test 6 passed: Subject validation")


# ==========================================================
# TEST 7
# ==========================================================

def test_student_class():

    student = Student("Saurabh Singh")

    student.add_score(5)

    assert student.name == "Saurabh Singh"

    assert student.scores == [5]

    print("Test 7 passed: Student class")


# ==========================================================
# TEST 8
# ==========================================================

def test_quiz_class():

    questions = get_questions("Python")

    answers = get_answers("Python")

    quiz = Quiz(
        "Python",
        questions,
        answers
    )

    assert quiz.subject == "Python"

    assert quiz.number_of_questions() == len(questions)

    print("Test 8 passed: Quiz class")


# ==========================================================
# TEST 9
# ==========================================================

def test_question_answer_bank():

    subjects = get_subjects()

    for subject in subjects:

        questions = get_questions(subject)

        answers = get_answers(subject)

        assert len(questions) == len(answers)

    print("Test 9 passed: Question and answer bank")


# ==========================================================
# RUN ALL TESTS
# ==========================================================

def run_all_tests():

    print("\n==========================================")
    print("       PYQ QUIZ SYSTEM - TESTING")
    print("==========================================")

    test_percentage()

    test_grade()

    test_total_scores()

    test_name_validation()

    test_answer_validation()

    test_subject_validation()

    test_student_class()

    test_quiz_class()

    test_question_answer_bank()

    print("\n==========================================")
    print("       ALL TESTS PASSED SUCCESSFULLY")
    print("==========================================")

# ==========================================================
# PROGRAM START
# ==========================================================

if __name__ == "__main__":
    run_all_tests()




