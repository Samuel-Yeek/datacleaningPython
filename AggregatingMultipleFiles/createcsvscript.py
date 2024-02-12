import csv
import random
#use this to generate random data for this mini project.
#This script will generate 12 csv files, each containing a list of students, their test scores, and their grade level. Name isnt included because I didnt want to code that plus its "anonymous" data.
def generate_student_id():   
    return random.randint(111111, 999999) # 6-digit student ID, ik this probably isnt unique but im only making this data for the AggregateGrades.py project and did this instead of just downloading some .csv files or copying the ones from the site I used to learn this. (I use iteration in the next file tho)


def generate_test_score():
    return round(random.gauss(78, 10)) # Mean score of around 78

def generate_grade():
    return random.randint(1, 12)

def generate_students(num_students):
    students = []
    for _ in range(num_students):
        student_id = generate_student_id()
        test_score = generate_test_score()
        grade = generate_grade()
        students.append((student_id, test_score, grade))
    return students

def write_to_csv(filename, data):
    with open(f'AggregatingMultipleFiles/{filename}', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['StudentID', 'Test Score', 'Grade'])
        writer.writerows(data)

def main():
    for grade in range(1, 13):
        num_students = random.randint(80, 120)
        students = generate_students(num_students)
        filename = f'exams{grade}.csv'
        write_to_csv(filename, students)
        print(f'{filename} created with {num_students} students.')


main()
