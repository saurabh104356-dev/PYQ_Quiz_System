# PYQ Quiz & Performance System

## 1. Project Title

**PYQ Quiz & Performance System**

---

## 2. Project Overview

The **PYQ Quiz & Performance System** is a Python-based console application designed to help students practice multiple-choice questions and evaluate their quiz performance.

The system allows a student to enter their name, select a subject, attempt a quiz, receive immediate feedback, and view the final score, percentage, and grade.

The application also stores quiz results permanently in a JSON file, allowing previously saved results to be viewed later.

The project demonstrates important Python programming concepts including:

* Functions
* Lists and dictionaries
* Conditional statements
* Loops
* Input/output
* Object-Oriented Programming
* Modular programming
* Input validation
* JSON file handling
* Exception handling
* Automated testing

---

## 3. Objectives

The main objectives of this project are:

1. To develop a simple educational quiz application using Python.
2. To provide subject-wise multiple-choice questions.
3. To automatically check student answers.
4. To calculate quiz scores.
5. To calculate percentages and grades.
6. To validate user input.
7. To store quiz results permanently.
8. To allow users to view previous quiz results.
9. To demonstrate modular and object-oriented Python programming.
10. To test important functions using custom test cases.

---

## 4. Features

### 4.1 Student Name Validation

The system asks the student to enter their name.

The name is validated to ensure that:

* It is not empty.
* It contains only letters and spaces.
* Numeric characters are not accepted.

Example:

```text
Enter your name: Saurabh Singh
```

---

### 4.2 Main Menu

After entering the name, the student receives the following menu:

```text
1. Start Quiz
2. View Previous Results
3. View Student Details
4. View Available Subjects
5. Exit
```

---

### 4.3 Subject Selection

The current question bank contains two subjects:

* Python
* Mathematics

The available subjects are retrieved dynamically from the question bank.

---

### 4.4 Multiple-Choice Questions

Each subject currently contains five multiple-choice questions.

Each question provides four options:

```text
A
B
C
D
```

The student must enter one of these options.

---

### 4.5 Answer Validation

The system validates the answer entered by the student.

Only the following answers are accepted:

```text
A
B
C
D
```

Lowercase answers such as `a` or `b` are also accepted because the input is converted to uppercase.

Invalid answers are rejected and the user is asked to enter a valid option.

---

### 4.6 Automatic Answer Checking

The student's answer is compared with the correct answer stored in the answer bank.

For a correct answer:

```text
Correct!
```

For an incorrect answer:

```text
Wrong!
Correct answer: C
```

The score is automatically updated.

---

### 4.7 Score Calculation

The system calculates the total number of correct answers.

For example:

```text
Your score: 4 / 5
```

---

### 4.8 Percentage Calculation

The percentage is calculated using the student's score and the total number of questions.

For example:

```text
Score: 4 / 5
Percentage: 80.0 %
```

---

### 4.9 Grade Calculation

The system assigns a grade according to the percentage:

|    Percentage | Grade |
| ------------: | :---- |
| 90% and above | A+    |
|       80%–89% | A     |
|       70%–79% | B     |
|       60%–69% | C     |
|       50%–59% | D     |
|     Below 50% | F     |

---

### 4.10 Student Details

The application creates a `Student` object that stores:

* Student name
* Quiz scores
* Quiz results

The Student Details option displays the student's name and the number of quizzes attempted during the current program session.

---

### 4.11 Previous Results

Quiz results are permanently stored in:

```text
results.json
```

The application can load these saved results and display:

* Student name
* Subject
* Score
* Percentage
* Grade

This allows previous quiz attempts to remain available after the program is closed.

---

### 4.12 JSON File Storage

The project uses Python's built-in `json` module to store quiz results.

The stored information has the following structure:

```json
{
    "name": "Student Name",
    "subject": "Python",
    "score": 4,
    "percentage": 80.0,
    "grade": "A"
}
```

Multiple quiz results are stored as a list of result objects.

---

### 4.13 Object-Oriented Programming

The project uses two main classes:

### `Student`

The `Student` class stores student-related information and quiz results.

Main methods include:

* `add_score()`
* `add_result()`
* `show_details()`
* `show_previous_results()`

### `Quiz`

The `Quiz` class stores:

* Subject
* Questions
* Correct answers

Main methods include:

* `number_of_questions()`
* `show_information()`

---

### 4.14 Modular Programming

The project is divided into separate Python modules.

This makes the program easier to understand, maintain, test, and modify.

---

## 5. Technologies and Tools Used

| Technology / Tool          | Purpose                                |
| -------------------------- | -------------------------------------- |
| Python 3.14                | Main programming language              |
| VS Code                    | Development environment                |
| JSON                       | Persistent result storage              |
| GitHub                     | Version control and project submission |
| Python `json` module       | Reading and writing result data        |
| Python `assert` statements | Testing program functionality          |

No external Python libraries are required for the current version.

---

## 6. Project Structure

```text
PYQ_Quiz_System/
│
├── main.py
├── models.py
├── quiz_data.py
├── quiz_functions.py
├── storage.py
├── validation.py
├── tests.py
├── README.md
├── statement.md
└── results.json
```

### File Description

| File                | Description                                                      |
| ------------------- | ---------------------------------------------------------------- |
| `main.py`           | Main program and menu system                                     |
| `models.py`         | Contains `Student` and `Quiz` classes                            |
| `quiz_data.py`      | Contains questions, answers, and subject data                    |
| `quiz_functions.py` | Contains quiz, scoring, percentage, grade, and display functions |
| `storage.py`        | Saves and loads results using JSON                               |
| `validation.py`     | Handles name, answer, and subject validation                     |
| `tests.py`          | Contains automated/custom test cases                             |
| `results.json`      | Stores quiz results permanently                                  |
| `README.md`         | Project documentation                                            |
| `statement.md`      | Project statement and scope                                      |

---

## 7. System Requirements

### Hardware

* Computer or laptop
* Keyboard
* Basic storage space

### Software

* Python 3.x
* VS Code or another Python IDE
* Command Prompt, PowerShell, or Terminal
* GitHub account for repository submission

---

## 8. Installation and Setup

### Step 1: Install Python

Install Python 3.x on your computer.

The current project was developed using Python 3.14.

Verify the installation:

```bash
python --version
```

---

### Step 2: Open the Project

Open the `PYQ_Quiz_System` folder in VS Code.

---

### Step 3: Check the Project Files

Make sure the following files are present:

```text
main.py
models.py
quiz_data.py
quiz_functions.py
storage.py
validation.py
tests.py
results.json
```

---

### Step 4: Run the Application

Open the terminal in the project directory and run:

```bash
python main.py
```

---

## 9. How to Use the System

### Step 1: Enter Student Name

The application first asks:

```text
Enter your name:
```

Enter a valid name containing letters and spaces.

---

### Step 2: Select an Option

The main menu appears:

```text
==========================================
                 MAIN MENU
==========================================
1. Start Quiz
2. View Previous Results
3. View Student Details
4. View Available Subjects
5. Exit
==========================================
```

---

### Step 3: Start a Quiz

Select:

```text
1. Start Quiz
```

The available subjects are displayed.

Currently available:

```text
1. Python
2. Mathematics
```

---

### Step 4: Attempt Questions

Select a subject and answer each question using:

```text
A
B
C
D
```

The program immediately tells the student whether the answer is correct.

---

### Step 5: View the Result

After all five questions have been attempted, the program displays:

* Student name
* Subject
* Score
* Percentage
* Grade

Example:

```text
==========================================
              QUIZ RESULT
==========================================
Student: Saurabh Singh
Subject: Python
Score: 4 / 5
Percentage: 80.0 %
Grade: A
==========================================
```

---

### Step 6: View Previous Results

Select:

```text
2. View Previous Results
```

The program reads the saved results from `results.json` and displays them.

---

### Step 7: View Student Details

Select:

```text
3. View Student Details
```

The application displays the student's name and the number of quizzes attempted during the current session.

---

### Step 8: View Available Subjects

Select:

```text
4. View Available Subjects
```

The program displays all subjects currently available in the question bank.

---

### Step 9: Exit

Select:

```text
5. Exit
```

The program terminates with a thank-you message.

---

## 10. Testing

The project includes a dedicated `tests.py` file containing nine custom test cases.

Run the tests using:

```bash
python tests.py
```

The tests cover:

1. Percentage calculation
2. Grade calculation
3. Total score calculation
4. Student name validation
5. Answer validation
6. Subject choice validation
7. Student class functionality
8. Quiz class functionality
9. Question-answer bank consistency

A successful test run displays:

```text
==========================================
       PYQ QUIZ SYSTEM - TESTING
==========================================

Test 1 passed: Percentage calculation
Test 2 passed: Grade calculation
Test 3 passed: Total score calculation
Test 4 passed: Name validation
Test 5 passed: Answer validation
Test 6 passed: Subject validation
Test 7 passed: Student class
Test 8 passed: Quiz class
Test 9 passed: Question and answer bank

==========================================
       ALL TESTS PASSED SUCCESSFULLY
==========================================
```

---

## 11. Testing Scenarios

| Test                      | Expected Result                 |
| ------------------------- | ------------------------------- |
| Valid student name        | Name accepted                   |
| Empty name                | Name rejected                   |
| Name containing numbers   | Name rejected                   |
| A/B/C/D answer            | Answer accepted                 |
| Invalid answer such as E  | Answer rejected                 |
| Valid subject number      | Subject accepted                |
| Invalid subject number    | Subject rejected                |
| Correct quiz answer       | Score increases                 |
| Incorrect quiz answer     | Score remains unchanged         |
| Completed quiz            | Result displayed                |
| Result saved              | Result stored in `results.json` |
| Previous results selected | Saved results displayed         |

---

## 12. Data Storage

The project uses a JSON file named:

```text
results.json
```

The file acts as the local storage system for quiz results.

A result contains:

```text
Name
Subject
Score
Percentage
Grade
```

The `storage.py` module handles:

* Saving results
* Loading results
* Displaying previous results

The program also handles cases where the JSON file does not exist or contains invalid JSON data.

---

## 13. Project Workflow

```text
Start
  |
  v
Enter Student Name
  |
  v
Validate Name
  |
  +---- Invalid ----> Ask Again
  |
  v
Display Main Menu
  |
  +---- Start Quiz
  |        |
  |        v
  |   Select Subject
  |        |
  |        v
  |   Validate Choice
  |        |
  |        v
  |   Load Questions
  |        |
  |        v
  |   Attempt Questions
  |        |
  |        v
  |   Check Answers
  |        |
  |        v
  |   Calculate Score
  |        |
  |        v
  |   Calculate Percentage
  |        |
  |        v
  |   Calculate Grade
  |        |
  |        v
  |   Display Result
  |        |
  |        v
  |   Save to results.json
  |
  +---- View Previous Results
  |
  +---- View Student Details
  |
  +---- View Subjects
  |
  +---- Exit
             |
             v
            End
```

---

## 14. Advantages

* Simple console-based interface.
* Easy subject selection.
* Automatic answer checking.
* Automatic score calculation.
* Percentage and grade calculation.
* Input validation prevents invalid entries.
* Results can be stored permanently.
* Previous results can be viewed.
* Uses Object-Oriented Programming.
* Uses modular program structure.
* Includes dedicated testing.
* Can be expanded with more subjects and questions.

---

## 15. Limitations

The current version has some limitations:

* The application is console-based.
* The current question bank contains only Python and Mathematics.
* Each subject currently contains five questions.
* Results are stored locally in a JSON file.
* There is no graphical user interface.
* There is no online database.
* There is no user login or authentication system.
* There is currently no timer for quizzes.
* Performance analysis is limited to basic score, percentage, and grade information.

---

## 16. Future Scope

The project can be extended in the future by adding:

1. More subjects and larger question banks.
2. Questions from actual examination years.
3. Difficulty levels.
4. Random question selection.
5. Randomized answer options.
6. Timed quizzes.
7. Negative marking.
8. Detailed explanations for answers.
9. Graphical user interface.
10. Web-based implementation.
11. Database integration.
12. Student login and authentication.
13. Detailed performance analytics.
14. Score history and progress tracking.
15. Mock-test functionality.
16. Leaderboards.
17. Question search and filtering.

---

## 17. Conclusion

The **PYQ Quiz & Performance System** is a Python-based educational application that provides students with a simple way to practice multiple-choice questions and evaluate their performance.

The project demonstrates the practical use of Python functions, lists, dictionaries, loops, conditional statements, Object-Oriented Programming, modular programming, input validation, JSON file handling, exception handling, and testing.

The use of separate modules makes the application organized and maintainable, while JSON storage allows quiz results to persist between program executions.

The current implementation provides a foundation that can be further developed into a larger PYQ and mock-test platform.

---

## 18. Author

**Student:** Saurabh Singh

**Project:** PYQ Quiz & Performance System

**Programming Language:** Python

**Development Environment:** Visual Studio Code

**Repository:** GitHub
