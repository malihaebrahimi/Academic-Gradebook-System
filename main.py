
from student import Student, is_valid_email
from course import Course
from assessment import Quiz, Exam, Project, ASSESSMENT_TYPES
from gradebook import Gradebook


def show_menu():
    print("\n--- GRADEBOOK MENU ---")
    print("1. Register Student")
    print("2. View Registered Students")
    print("3. Create Course")
    print("4. Enroll Student in Course")
    print("5. Add Assessment")
    print("6. Record Student Score")
    print("7. Add Teacher Comment (Custom Feature)")
    print("8. View Student Report")
    print("9. Search Student")
    print("10. Remove Student")
    print("11. Update Student Info (Name/Email)")
    print("12. View Course Info")
    print("0. Exit")


def prompt_assessment_type():
    """
    Shows the assessment-type menu and returns the matching class from
    ASSESSMENT_TYPES, or None if the user's choice isn't a recognized
    type. Kept separate from the main loop so the "reject invalid
    type" logic is in exactly one place.
    """
    print("Type: (1) Quiz (2) Exam (3) Project")
    choice = input("Choice: ").strip()
    return ASSESSMENT_TYPES.get(choice)


def main():
    my_gradebook = Gradebook()

    # Seed data so the menu isn't empty on first run.
    s1 = Student("S001", "Maliha Ebrahimi", "abmaliha1@gmail.com")
    my_gradebook.add_student(s1)
    c1 = Course("PY101", "Python Programming")
    my_gradebook.add_course(c1)
    my_gradebook.enroll_student("S001", "PY101")
    my_gradebook.add_assessment("PY101", Quiz("Quiz 1", 10))
    my_gradebook.record_grade("S001", "PY101", "Quiz 1", 8)

    while True:
        show_menu()
        choice = input("Enter option (0-12): ").strip()

        if choice == "1":
            s_id = input("Student ID: ").strip()
            name = input("Name: ").strip()
            email = input("Email: ").strip()
            if not s_id or not name:
                print("ID and Name cannot be empty.")
                continue
            if not is_valid_email(email):
                print("Invalid email format. Student was not registered.")
                continue
            s = Student(s_id, name, email)
            if my_gradebook.add_student(s):
                print("Student added!")
            else:
                print("ID already exists.")

        elif choice == "2":
            if not my_gradebook.students:
                print("No students registered.")
            for student in my_gradebook.students.values():
                student.display_info()

        elif choice == "3":
            code = input("Course Code: ").strip().upper()
            name = input("Course Name: ").strip()
            if code and name:
                c = Course(code, name)
                if my_gradebook.add_course(c):
                    print("Course added!")
                else:
                    print("Course code already exists.")
            else:
                print("Course Code and Name cannot be empty.")

        elif choice == "4":
            s_id = input("Student ID: ").strip()
            c_code = input("Course Code: ").strip().upper()
            if my_gradebook.enroll_student(s_id, c_code):
                print("Student enrolled!")
            else:
                print("Failed to enroll. Check ID and Course Code.")

        elif choice == "5":
            c_code = input("Course Code: ").strip().upper()
            if c_code not in my_gradebook.courses:
                print("Course not found.")
                continue

            title = input("Assessment Title (e.g. Midterm): ").strip()
            if not title:
                print("Assessment title cannot be empty.")
                continue

            try:
                max_score = float(input("Max Score: "))
            except ValueError:
                print("Must be a number.")
                continue

            asm_class = prompt_assessment_type()
            if asm_class is None:
                print("Invalid assessment type. Assessment was not created.")
                continue

            try:
                asm = asm_class(title, max_score)
            except ValueError as exc:
                print(f"Could not create assessment: {exc}")
                continue

            if my_gradebook.add_assessment(c_code, asm):
                print("Assessment added to course!")
            else:
                print(f"An assessment titled '{title}' already exists in this course.")

        elif choice == "6":
            s_id = input("Student ID: ").strip()
            c_code = input("Course Code: ").strip().upper()
            title = input("Assessment Title: ").strip()
            try:
                score = float(input("Score: "))
            except ValueError:
                print("Must be a number.")
                continue
            print(my_gradebook.record_grade(s_id, c_code, title, score))

        elif choice == "7":
            s_id = input("Student ID: ").strip()
            c_code = input("Course Code: ").strip().upper()
            comment = input("Teacher Comment: ").strip()
            if not comment:
                print("Comment cannot be empty.")
                continue
            if my_gradebook.add_comment(s_id, c_code, comment):
                print("Comment added!")
            else:
                print("Could not add comment.")

        elif choice == "8":
            s_id = input("Student ID: ").strip()
            my_gradebook.show_report(s_id)

        elif choice == "9":
            q = input("Enter Name or ID to search: ").strip()
            my_gradebook.search_student(q)

        elif choice == "10":
            s_id = input("Student ID to delete: ").strip()
            if my_gradebook.delete_student(s_id):
                print("Student removed.")
            else:
                print("Student not found.")

        elif choice == "11":
            s_id = input("Student ID: ").strip()
            if s_id not in my_gradebook.students:
                print("Student not found.")
                continue
            student = my_gradebook.students[s_id]

            print("What would you like to update?")
            print("  1. Name")
            print("  2. Email")
            print("  3. Both")
            sub_choice = input("Choice: ").strip()

            if sub_choice in ("1", "3"):
                new_name = input("New Name: ").strip()
                if student.set_name(new_name):
                    print("Name updated!")
                else:
                    print("Invalid name (cannot be empty).")

            if sub_choice in ("2", "3"):
                new_email = input("New Email: ").strip()
                if student.set_email(new_email):
                    print("Email updated!")
                else:
                    print("Invalid email format.")

            if sub_choice not in ("1", "2", "3"):
                print("Invalid choice. Nothing updated.")

        elif choice == "12":
            c_code = input("Course Code: ").strip().upper()
            if c_code in my_gradebook.courses:
                my_gradebook.courses[c_code].display_info()
            else:
                print("Course not found.")

        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print("Invalid option!")


if __name__ == "__main__":
    main()
