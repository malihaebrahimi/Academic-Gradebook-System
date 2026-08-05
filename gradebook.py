


class Gradebook:


    def __init__(self, passing_grade=55.0):
        self.students = {}
        self.courses = {}
        self.grades = {}
        self.comments = {}
        self.passing_grade = passing_grade

    def add_student(self, student):
        s_id = student.get_id()
        if s_id in self.students:
            return False
        self.students[s_id] = student
        self.grades[s_id] = {}
        self.comments[s_id] = {}
        return True

    def add_course(self, course):
        code = course.course_code
        if code in self.courses:
            return False
        self.courses[code] = course
        return True

    def enroll_student(self, student_id, course_code):
        if student_id in self.students and course_code in self.courses:
            student = self.students[student_id]
            course = self.courses[course_code]
            student.enroll_course(course_code)
            course.add_student(student_id)
            if course_code not in self.grades[student_id]:
                self.grades[student_id][course_code] = {}
            return True
        return False

    def add_assessment(self, course_code, assessment):
        
        if course_code in self.courses:
            return self.courses[course_code].add_assessment(assessment)
        return False

    def record_grade(self, student_id, course_code, assessment_title, score):
        if student_id not in self.students:
            return "Error: Student not found."
        if course_code not in self.courses:
            return "Error: Course not found."
        student = self.students[student_id]
        if course_code not in student.courses:
            return "Error: Student is not enrolled in this course."
        course = self.courses[course_code]
        assessment = course.find_assessment(assessment_title)
        if not assessment:
            return "Error: Assessment not found in this course."
        if score < 0 or score > assessment.max_score:
            return f"Error: Score must be between 0 and {assessment.max_score}."
        self.grades[student_id][course_code][assessment.title] = score
        return f"Grade saved! Feedback: {assessment.grade_message(score)}"

    def add_comment(self, student_id, course_code, comment_text):
        
        if not isinstance(comment_text, str):
            return False
        comment_text = comment_text.strip()
        if not comment_text:
            return False
        if student_id in self.students and course_code in self.courses:
            if course_code in self.students[student_id].courses:
                self.comments[student_id][course_code] = comment_text
                return True
        return False

    def calculate_average(self, student_id, course_code):
        if student_id not in self.grades or course_code not in self.grades[student_id]:
            return None
        student_grades = self.grades[student_id][course_code]
        course = self.courses[course_code]
        if not student_grades:
            return None
        total_pct = 0.0
        for title, score in student_grades.items():
            asm = course.find_assessment(title)
            if asm:
                total_pct += asm.calculate_percentage(score)
        return total_pct / len(student_grades)

    def get_letter_grade(self, average):
        if average is None:
            return "N/A"
        if average >= 90:
            return "A"
        elif average >= 80:
            return "B"
        elif average >= 70:
            return "C"
        elif average >= 60:
            return "D"
        else:
            return "F"

    def get_pass_fail(self, average):
        if average is None:
            return "No grades yet"
        if average >= self.passing_grade:
            return "Passed"
        return "Failed"

    def show_report(self, student_id):
        if student_id not in self.students:
            print("Student not found!")
            return
        student = self.students[student_id]
        print("\n================ REPORT CARD ================")
        print(f"Student: {student.get_name()} (ID: {student.get_id()})")
        print(f"Email: {student.get_email()}")
        print("---------------------------------------------")
        if not student.courses:
            print("Not enrolled in any courses.")
            return
        for code in student.courses:
            course = self.courses[code]
            print(f"Course: {course.course_code} - {course.course_name}")
            course_grades = self.grades[student_id].get(code, {})
            for title, score in course_grades.items():
                asm = course.find_assessment(title)
                pct = asm.calculate_percentage(score) if asm else 0.0
                print(f"  * {title}: {score}/{asm.max_score} ({pct:.1f}%)")
            avg = self.calculate_average(student_id, code)
            letter = self.get_letter_grade(avg)
            status = self.get_pass_fail(avg)
            if avg is None:
                print("  Average Score: N/A")
            else:
                print(f"  Average Score: {avg:.2f}%")
            print(f"  Letter Grade:  {letter} (Custom Feature)")
            print(f"  Status:        {status}")
            comment = self.comments[student_id].get(code, "No comments.")
            print(f"  Teacher Comment: \"{comment}\"")
            print("---------------------------------------------")

    def search_student(self, query):
        print(f"\nSearching for '{query}':")
        for s_id, student in self.students.items():
            if query.lower() in s_id.lower() or query.lower() in student.get_name().lower():
                student.display_info()

    def delete_student(self, student_id):
        if student_id not in self.students:
            return False
        for course in self.courses.values():
            if student_id in course.students:
                course.students.remove(student_id)
        del self.students[student_id]
        del self.grades[student_id]
        del self.comments[student_id]
        return True
