class Student:
    def __init__(self, name, scores):
        self.name = name
        self.scores = scores

    def calculate_average(self):
        return sum(self.scores) / len(self.scores)

    def is_passing(self, passing_score=40):
        return all(score >= passing_score for score in self.scores)
class PerformanceTracker:
    def __init__(self):
        self.students = {}

    def add_student(self, name, scores):
        self.students[name] = Student(name, scores)

    def calculate_class_average(self):
        total_scores = [student.calculate_average() for student in self.students.values()]
        return sum(total_scores) / len(total_scores)

    def display_student_performance(self):
        for name, student in self.students.items():
            average = student.calculate_average()
            status = "Passing" if student.is_passing() else "Failing"
            print(f"Student: {name}, Average: {average:.2f}, Status: {status}")
def main():
    tracker = PerformanceTracker()

    while True:
        name = input("Enter student name (or 'stop' to finish): ")
        if name.lower() == 'stop':
            break

        try:
            scores = [int(input(f"Enter score for subject {i+1}: ")) for i in range(3)]
        except ValueError:
            print("Invalid input. Please enter numeric values for scores.")
            continue

        tracker.add_student(name, scores)

    tracker.display_student_performance()
    print(f"Class Average: {tracker.calculate_class_average():.2f}")

if __name__ == "__main__":
    main()
