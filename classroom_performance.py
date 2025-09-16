class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def average(self):
        if not self.marks:
            return 0
        return sum(self.marks) / len(self.marks)

def calculate_averages(students_dict):
    averages = {}
    for name, marks in students_dict.items():
        student = Student(name, marks)
        averages[name] = round(student.average(), 2)
    return averages

def find_top_performer(averages):
    return max(averages, key=averages.get)

def main():
    students = {
        "John": [85, 78, 92],
        "Alice": [88, 79, 95],
        "Bob": [70, 75, 80]
    }
    averages = calculate_averages(students)
    top_performer = find_top_performer(averages)
    print("Average Marks:", averages)
    print("Top Performer:", top_performer)
if __name__ == "__main__":
    main()
