# Project Statement

## 1. Project Title

**PYQ Quiz & Performance System**

---

## 2. Problem Statement

Students need an efficient and simple way to practice multiple-choice questions and evaluate their preparation. When practicing questions manually, students may need to check answers separately and calculate their scores and percentages themselves.

The **PYQ Quiz & Performance System** addresses this problem by providing a Python-based console application that allows students to select a subject, attempt multiple-choice questions, receive immediate feedback, and view their final performance.

The system automatically checks answers, calculates the score, percentage, and grade, and stores completed quiz results in a JSON file for future reference.

The project also demonstrates the practical application of Python programming concepts including functions, loops, conditional statements, lists, dictionaries, Object-Oriented Programming, modular programming, input validation, file handling, JSON processing, and testing.

---

## 3. Scope of the Project

The current scope of the project includes:

* Student name registration
* Student name validation
* Subject selection
* Subject choice validation
* Multiple-choice quiz questions
* Answer validation
* Automatic answer checking
* Score calculation
* Percentage calculation
* Grade calculation
* Student details
* Previous result viewing
* JSON-based result storage
* Modular Python programming
* Object-Oriented Programming
* Automated/custom testing

The current question bank contains:

* Python
* Mathematics

Each subject currently contains five multiple-choice questions.

The project is designed as a foundation that can be expanded into a larger PYQ and mock-test platform.

---

## 4. Target Users

### 4.1 Students

Students are the primary users of the application. They can use the system to practice multiple-choice questions and check their performance.

### 4.2 Learners Preparing for Examinations

The system can be expanded to include questions from different competitive and academic examinations, allowing learners to practice subject-wise questions.

### 4.3 Python Programming Learners

The project can also be useful for students learning Python because it demonstrates how different programming concepts can be combined to create a complete application.

### 4.4 Teachers and Instructors

Teachers or instructors can potentially use the project structure to create simple subject-based quizzes and question banks.

---

## 5. High-Level Features

### 5.1 Student Registration

The application accepts the student's name before the quiz begins.

### 5.2 Input Validation

The system validates:

* Student names
* Subject choices
* Quiz answers

Invalid inputs are rejected and the user is asked to provide valid input.

### 5.3 Subject Selection

Students can select from the subjects available in the question bank.

The current subjects are:

* Python
* Mathematics

### 5.4 Multiple-Choice Quiz

Each quiz contains multiple-choice questions with four options:

* A
* B
* C
* D

### 5.5 Automatic Answer Checking

The student's answer is compared with the predefined correct answer.

The system immediately displays whether the answer is correct or incorrect.

### 5.6 Score Calculation

The application counts the number of correctly answered questions and calculates the final score.

### 5.7 Percentage Calculation

The system calculates the percentage from the student's score and the total number of questions.

### 5.8 Grade Calculation

The system assigns a grade based on the final percentage:

* A+
* A
* B
* C
* D
* F

### 5.9 Student Details

The `Student` class stores student information, quiz scores, and quiz results during the program session.

### 5.10 Persistent Result Storage

Completed quiz results are saved to:

```text
results.json
```

Each saved result contains:

* Student name
* Subject
* Score
* Percentage
* Grade

### 5.11 Previous Results

Students can view previously saved quiz results through the main menu.

### 5.12 Modular Architecture

The application is divided into multiple Python files according to their responsibilities.

### 5.13 Object-Oriented Design

The project contains:

* `Student` class
* `Quiz` class

These classes organize student and quiz-related data and operations.

### 5.14 Testing

A separate `tests.py` module contains nine tests covering:

* Percentage calculation
* Grade calculation
* Total score calculation
* Name validation
* Answer validation
* Subject validation
* Student class
* Quiz class
* Question-answer consistency

---

## 6. Project Modules

The project consists of the following major modules:

| Module              | Responsibility                                                  |
| ------------------- | --------------------------------------------------------------- |
| `main.py`           | Controls the main program and menu                              |
| `models.py`         | Defines Student and Quiz classes                                |
| `quiz_data.py`      | Stores questions and correct answers                            |
| `quiz_functions.py` | Handles quiz execution, scoring, percentage, grade, and display |
| `validation.py`     | Validates user input                                            |
| `storage.py`        | Saves and loads results using JSON                              |
| `tests.py`          | Tests important project functionality                           |
| `results.json`      | Stores completed quiz results                                   |

---

## 7. Expected Outcome

The expected outcome is a working Python application that allows a student to:

1. Enter a valid name.
2. Access the main menu.
3. View available subjects.
4. Select a subject.
5. Attempt multiple-choice questions.
6. Receive immediate answer feedback.
7. View the final score.
8. View the percentage.
9. View the grade.
10. Save the result.
11. View previous results.
12. View student details.
13. Exit the application safely.

---

## 8. Future Scope

The system can be further developed into a larger examination and learning platform by adding:

* Larger PYQ question banks
* More subjects
* Examination-wise categorization
* Year-wise question filtering
* Difficulty levels
* Timed tests
* Negative marking
* Random questions
* Answer explanations
* Database integration
* User authentication
* Web interface
* Graphical user interface
* Performance analytics
* Progress tracking
* Mock examinations
