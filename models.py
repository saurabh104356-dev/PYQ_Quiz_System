
# ==========================================================
# models.py
# Object-Oriented Programming for PYQ Quiz System
# ==========================================================


# ==========================================================
# STUDENT CLASS
# ==========================================================

class Student:

    # ------------------------------------------------------
    # Constructor
    # ------------------------------------------------------

    def __init__(self, name):

        self.name = name

        # Stores scores of all attempted quizzes
        self.scores = []

        # Stores complete quiz results
        self.results = []


    # ------------------------------------------------------
    # Add Score
    # ------------------------------------------------------

    def add_score(self, score):

        self.scores.append(score)


    # ------------------------------------------------------
    # Add Complete Result
    # ------------------------------------------------------

    def add_result(
        self,
        subject,
        score,
        percentage,
        grade
    ):

        result = {

            "subject": subject,
            "score": score,
            "percentage": percentage,
            "grade": grade

        }

        self.results.append(result)


    # ------------------------------------------------------
    # Display Student Details
    # ------------------------------------------------------

    def show_details(self):

        print("\n==========================================")
        print("           STUDENT DETAILS")
        print("==========================================")

        print(
            "Student Name:",
            self.name
        )

        print(
            "Quizzes Attempted:",
            len(self.results)
        )


    # ------------------------------------------------------
    # Display Previous Results
    # ------------------------------------------------------

    def show_previous_results(self):

        print("\n==========================================")
        print("          PREVIOUS RESULTS")
        print("==========================================")


        # Check whether the student has attempted
        # any quiz

        if len(self.results) == 0:

            print(
                "No quizzes attempted yet."
            )

            return


        # Display every stored result

        for i, result in enumerate(
            self.results,
            start=1
        ):

            print("\nQuiz", i)

            print(
                "Subject:",
                result["subject"]
            )

            print(
                "Score:",
                result["score"],
                "/ 5"
            )

            print(
                "Percentage:",
                result["percentage"],
                "%"
            )

            print(
                "Grade:",
                result["grade"]
            )


# ==========================================================
# QUIZ CLASS
# ==========================================================

class Quiz:

    # ------------------------------------------------------
    # Constructor
    # ------------------------------------------------------

    def __init__(
        self,
        subject,
        questions,
        answers
    ):

        self.subject = subject

        self.questions = questions

        self.answers = answers


    # ------------------------------------------------------
    # Return Number of Questions
    # ------------------------------------------------------

    def number_of_questions(self):

        return len(self.questions)


    # ------------------------------------------------------
    # Display Quiz Information
    # ------------------------------------------------------

    def show_information(self):

        print("\n========== QUIZ INFORMATION ==========")

        print(
            "Subject:",
            self.subject
        )

        print(
            "Number of Questions:",
            self.number_of_questions()
        )

