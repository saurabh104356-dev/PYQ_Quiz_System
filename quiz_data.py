
# ==========================================================
# quiz_data.py
# Question Bank for PYQ Quiz & Performance System
# ==========================================================


# ==========================================================
# PYTHON QUESTIONS
# ==========================================================

python_questions = [

    """1. What is the output of 10 + 5?
A. 5
B. 10
C. 15
D. 50""",

    """2. Which function is used to take input from the user?
A. print()
B. input()
C. scan()
D. read()""",

    """3. Which symbol is used for comments in Python?
A. //
B. /*
C. #
D. <!-- -->""",

    """4. Which data type is used to store True or False?
A. int
B. str
C. bool
D. float""",

    """5. Which operator is used for exponentiation in Python?
A. ^
B. **
C. //
D. %%"""

]


python_answers = [
    "C",
    "B",
    "C",
    "C",
    "B"
]


# ==========================================================
# MATHEMATICS QUESTIONS
# ==========================================================

math_questions = [

    """1. What is the value of 5 × 6?
A. 20
B. 25
C. 30
D. 35""",

    """2. What is the square of 12?
A. 124
B. 144
C. 154
D. 164""",

    """3. What is the value of 15 + 25?
A. 30
B. 35
C. 40
D. 45""",

    """4. What is the HCF of 36 and 60?
A. 6
B. 12
C. 18
D. 24""",

    """5. What is the value of 10²?
A. 20
B. 50
C. 100
D. 1000"""

]


math_answers = [
    "C",
    "B",
    "C",
    "B",
    "C"
]


# ==========================================================
# QUESTION BANK
# ==========================================================

question_bank = {

    "Python": python_questions,

    "Mathematics": math_questions

}


# ==========================================================
# ANSWER BANK
# ==========================================================

answer_bank = {

    "Python": python_answers,

    "Mathematics": math_answers

}


# ==========================================================
# FUNCTIONS
# ==========================================================


def get_questions(subject):

    return question_bank.get(
        subject,
        []
    )


def get_answers(subject):

    return answer_bank.get(
        subject,
        []
    )


def get_subjects():

    return list(question_bank.keys())

