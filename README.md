# Student Gradebook & Course Manager

## Project Description

Student Gradebook & Course Manager is a terminal-based Python application developed using Object-Oriented Programming (OOP). The system helps users manage students, courses, assessments, grades, and student reports through a simple command-line interface.

The project demonstrates the use of core Python concepts, including classes, objects, inheritance, encapsulation, method overriding, lists, dictionaries, functions, and input validation.

---

## Project Files

* **main.py** – Runs the application and provides the menu-driven interface.
* **student.py** – Defines the `Student` class and email validation.
* **course.py** – Defines the `Course` class.
* **assessment.py** – Defines the `Assessment` base class and the `Quiz`, `Exam`, and `Project` subclasses.
* **gradebook.py** – Defines the `Gradebook` class that manages students, courses, grades, reports, and comments.

---

## Main Features

* Register students
* View all students
* Search students by ID or name
* Update student email
* Delete students
* Create and manage courses
* Enroll students in courses
* Add quizzes, exams, and projects
* Record assessment grades
* Calculate percentages and averages
* Display pass/fail status
* Generate letter grades
* Add teacher comments
* Generate student reports
* Validate user input and prevent common errors

---

## Object-Oriented Programming Concepts

### Encapsulation

The `Student` class uses protected attributes such as `_student_id`, `_name`, and `_email`. Getter methods provide controlled access to data, while the `set_email()` method validates email addresses before updating them.

### Inheritance

The following classes inherit from the `Assessment` class:

* `Quiz`
* `Exam`
* `Project`

These subclasses reuse the common functionality provided by the parent class.

### Method Overriding

The `Quiz`, `Exam`, and `Project` classes override methods such as `display_info()` and `grade_message()` to provide behavior specific to each assessment type.

---

## Data Structures

### Lists

Lists are used to store:

* Student course registrations
* Enrolled students
* Course assessments

### Dictionaries

Dictionaries are used to manage:

* Students
* Courses
* Grades
* Teacher comments

Using dictionaries allows fast access through student IDs and course codes.

---

## Custom Features

### Letter Grade System

The application automatically converts percentage averages into letter grades such as A, B, C, D, and F.

### Teacher Comment System

Teachers can add comments to each student's course report, making the feedback more meaningful.

---

## How to Run

1. Install Python 3.
2. Download or clone this repository.
3. Open a terminal inside the project folder.
4. Run the following command:

```bash
python main.py
```

---

## Example Workflow

1. Register a student.
2. Create a course.
3. Enroll the student in the course.
4. Add an assessment.
5. Record the student's grade.
6. Add a teacher comment.
7. View the student's report.

---

## Author

**Maliha Ebrahimi**

Final Python Project – Student Gradebook & Course Manager
