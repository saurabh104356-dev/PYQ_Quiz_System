
# ==========================================================
# main.py
# PYQ Quiz & Performance System
# Main Program
# ==========================================================

from models import Student, Quiz

from quiz_data import (
    get_questions,
    get_answers,
    get_subjects
)

from quiz_functions import (
    display_header,
    start_quiz,
    display_result,
    calculate_percentage,
    calculate_grade
)

from storage import (
    save_result,
    display_previous_results
)

from validation import (
    get_valid_name,
    validate_subject_choice
)


# ----------------------------------------------------------
# MAIN PROGRAM
# ----------------------------------------------------------

def main():

    # ------------------------------------------------------
    # GET STUDENT NAME
    # ------------------------------------------------------

    display_header("Welcome to the PYQ Quiz System")

    name = get_valid_name()

    # Create Student object
    student = Student(name)

    # ------------------------------------------------------
    # MAIN MENU LOOP
    # ------------------------------------------------------

    while True:

        print("\n==========================================")
        print("                 MAIN MENU")
        print("==========================================")
        print("1. Start Quiz")
        print("2. View Previous Results")
        print("3. View Student Details")
        print("4. View Available Subjects")
        print("5. Exit")
        print("==========================================")

        choice = input("Enter your choice: ").strip()

        # --------------------------------------------------
        # OPTION 1: START QUIZ
        # --------------------------------------------------

        if choice == "1":

            subjects = get_subjects()

            print("\n========== AVAILABLE SUBJECTS ==========")

            for i, subject in enumerate(subjects, start=1):
                print(i, ".", subject)

            subject_choice = input(
                "Select subject number: "
            ).strip()

            # Validate subject choice
            if not validate_subject_choice(
                subject_choice,
                subjects
            ):
                print("Invalid subject choice.")
                continue

            # Convert choice to index
            subject_index = int(subject_choice) - 1

            # Get selected subject
            subject = subjects[subject_index]

            # Get questions and answers
            questions = get_questions(subject)
            answers = get_answers(subject)

            # Create Quiz object
            quiz = Quiz(
                subject,
                questions,
                answers
            )

            # Show quiz information
            quiz.show_information()

            # Start quiz
            score = start_quiz(quiz)

            # Calculate percentage
            percentage = calculate_percentage(
                score,
                quiz.number_of_questions()
            )

            # Calculate grade
            grade = calculate_grade(percentage)

            # Display result
            display_result(
                name,
                subject,
                score,
                quiz.number_of_questions()
            )

            # Add score to Student object
            student.add_score(score)

            # Add complete result to Student object
            student.add_result(
                subject,
                score,
                percentage,
                grade
            )

            # Save result permanently
            save_result(
                name,
                subject,
                score,
                percentage,
                grade
            )

            print("\nResult saved successfully!")

        # --------------------------------------------------
        # OPTION 2: VIEW PREVIOUS RESULTS
        # --------------------------------------------------

        elif choice == "2":

            display_previous_results()

        # --------------------------------------------------
        # OPTION 3: VIEW STUDENT DETAILS
        # --------------------------------------------------

        elif choice == "3":

            student.show_details()

        # --------------------------------------------------
        # OPTION 4: VIEW AVAILABLE SUBJECTS
        # --------------------------------------------------

        elif choice == "4":

            subjects = get_subjects()

            print("\n========== AVAILABLE SUBJECTS ==========")

            for i, subject in enumerate(subjects, start=1):
                print(i, ".", subject)

        # --------------------------------------------------
        # OPTION 5: EXIT
        # --------------------------------------------------

        elif choice == "5":

            print("\n==========================================")
            print("Thank you for using PYQ Quiz System!")
            print("Good luck with your preparation!")
            print("==========================================")

            break

        # --------------------------------------------------
        # INVALID MENU CHOICE
        # --------------------------------------------------

        else:

            print("Invalid choice. Please select 1 to 5.")


# ----------------------------------------------------------
# PROGRAM START
# ----------------------------------------------------------

if __name__ == "__main__":
    main()

