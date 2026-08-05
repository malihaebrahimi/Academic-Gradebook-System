
def is_valid_email(email):

    if not isinstance(email, str):
        return False
    email = email.strip()
    if email.count("@") != 1:
        return False
    local, _, domain = email.partition("@")
    if not local or not domain:
        return False
    if "." not in domain:
        return False
    if domain.startswith(".") or domain.endswith("."):
        return False
    return True


class Student:

    def __init__(self, student_id, name, email):
        self._student_id = student_id
        self._name = name
        self._email = email
        self.courses = []

    def get_id(self):
        return self._student_id

    def get_name(self):
        return self._name

    def get_email(self):
        return self._email

    def set_name(self, new_name):

        if not isinstance(new_name, str):
            return False
        new_name = new_name.strip()
        if not new_name:
            return False
        self._name = new_name
        return True

    def set_email(self, new_email):

        if not isinstance(new_email, str):
            return False
        new_email = new_email.strip()
        if not is_valid_email(new_email):
            return False
        self._email = new_email
        return True

    def enroll_course(self, course_code):
        if course_code not in self.courses:
            self.courses.append(course_code)

    def display_info(self):
        print(f"ID: {self._student_id} | Name: {self._name} | Email: {self._email} | Enrolled in: {self.courses}")
