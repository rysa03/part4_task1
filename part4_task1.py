class Student():
    def __init__(self, name, last_name, department, year_of_entrance):
        self.name = name
        self.last_name = last_name
        self.department = department
        self.year_of_entrance = year_of_entrance

    def get_student_info(self):
        name = self.name
        last_name = self.last_name
        department = self.department
        year_of_entrance =self.year_of_entrance
        result = f"{name.title()} {last_name.title()} поступил в {year_of_entrance} г. на факультет {department}."
        return result

go = Student("Vasya", "Ivanov", "programirovanie", "2019")
print(go.get_student_info())