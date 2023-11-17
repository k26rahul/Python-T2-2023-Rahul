marks = float(input())
num_options = int(input())

correct_options = input().split(",")
student_options = input().split(",")

correct_options = [int(option) for option in correct_options]
student_options = [int(option) for option in student_options]

num_correct_options = len(set(correct_options) & set(student_options))

if num_correct_options != len(student_options):
    print(0.0)
else:
    individual_mark = marks // len(correct_options)
    marks_obtained = num_correct_options * individual_mark
    print(marks_obtained)
