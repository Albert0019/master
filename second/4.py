class Student:
    def __init__(self, name: str, age: int, group_number: int, average_score: float):
        self.name = name
        self.age = age
        self.group_number = group_number
        self.average_score = average_score

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

    def calculate_scholarship(self) -> int:
        if self.average_score == 5:
            return 6000
        elif self.average_score < 5:
            return 4000
        else:
            return 0

    def compare_scholarship(self, other):
        if self.calculate_scholarship() > other.calculate_scholarship():
            return f"{self.name}'s scholarship is greater"
        elif self.calculate_scholarship() < other.calculate_scholarship():
            return f"{self.name}'s scholarship is smaller"
        else:
            return "Scholarships are equal"


class Graduate(Student):
    def __init__(self, name: str, age: int, group_number: int, average_score: float, research_project: str):
        super().__init__(name, age, group_number, average_score)
        self.research_project = research_project

    def calculate_scholarship(self) -> int:
        if self.average_score == 5:
            return 8000
        elif self.average_score < 5:
            return 6000
        else:
            return 0


# Test
student1 = Student("Alice", 20, 101, 4.5)
student2 = Student("Bob", 21, 102, 5)
graduate = Graduate("Charlie", 23, 103, 4.8, "AI Research")

print(student1.calculate_scholarship())  # 4000
print(graduate.calculate_scholarship())  # 6000
print(student1.compare_scholarship(student2))  # Alice's scholarship is smaller