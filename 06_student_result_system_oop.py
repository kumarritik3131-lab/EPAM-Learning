# Student result manager demonstrating inheritance and polymorphism.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def describe(self):
        print(f"{self.name}, age {self.age}")


class Student(Person):
    PASS_MARK = 40

    def __init__(self, name, age, roll_number):
        super().__init__(name, age)
        self.roll_number = roll_number
        self.marks = {}

    def add_marks(self, subject, score):
        if not 0 <= score <= 100:
            print("Marks must be between 0 and 100.")
            return
        self.marks[subject] = score

    def total_marks(self):
        return sum(self.marks.values())

    def average(self):
        if not self.marks:
            return 0
        return self.total_marks() / len(self.marks)

    def result(self):
        if not self.marks:
            return "No marks entered"
        if all(score >= self.PASS_MARK for score in self.marks.values()):
            return "PASS"
        return "FAIL"

    def describe(self):
        # Overrides Person.describe(): an example of polymorphism.
        print(f"Student: {self.name} | Roll no.: {self.roll_number}")

    def report(self):
        self.describe()
        print("-" * 35)
        for subject, score in self.marks.items():
            print(f"{subject}: {score}")
        print(f"Total: {self.total_marks()}")
        print(f"Average: {self.average():.2f}")
        print(f"Result: {self.result()}")


def main():
    student = Student("Meera", 19, "AIML-024")
    student.add_marks("Mathematics", 86)
    student.add_marks("Python", 92)
    student.add_marks("Physics", 78)
    student.report()


if __name__ == "__main__":
    main()
