

class Course:


    def __init__(self, course_code, course_name):
        self.course_code = course_code
        self.course_name = course_name
        self.students = []
        self.assessments = []

    def add_student(self, student_id):
        if student_id not in self.students:
            self.students.append(student_id)

    def has_assessment_title(self, title):

        title = title.strip().lower()
        return any(asm.title.lower() == title for asm in self.assessments)

    def add_assessment(self, assessment):

        if self.has_assessment_title(assessment.title):
            return False
        self.assessments.append(assessment)
        return True

    def find_assessment(self, title):
        for asm in self.assessments:
            if asm.title.lower() == title.lower():
                return asm
        return None

    def display_info(self):
        print(f"Course Code: {self.course_code}")
        print(f"Course Name: {self.course_name}")
        print(f"Enrolled Students: {len(self.students)}")
        if self.assessments:
            print("Assessments:")
            for asm in self.assessments:
                print("  - " + asm.display_info())
        else:
            print("Assessments: None")
