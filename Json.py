import json

data = '''{"class":[
  
  {
      "name": "John Smith",
      "age": 30,
      "city": "New York",
      "is_student": false,
      "grades": [95, 87, 92, 88, 76]
  },
  
  {
      "name": "Emily Smith",
      "age": 20,
      "city": "New Jersey",
      "is_student": true,
      "grades": [55, 67, 82, 88, 96]
  },
  
  {
      "name": "Jacob Dum",
      "age": 10,
      "city": "New Jersey",
      "is_student": true,
      "grades": [25, 57, 42, 88, 76],
      "hobbies": [
          {
              "instruments": {
                  "guitar": "acoustic",
                  "drums": "electric"
              }
          },
          "sports",
          "games"
      ]
  }


]
}'''
#############################################################
new_data = json.loads(data)
student_info = new_data['class']

students = []

for student in student_info:
    name = student['name']
    students.append(name)

print(students)    
############################################################
student_grades = []

for grade in student_info:
    grades = grade['grades']
    student_grades.append(grades)
print(student_grades)
###############################################################
studenet_avg_grade = []
for grades in student_grades:
    average = sum(grades)/len(grades)
    studenet_avg_grade.append(average)
print(studenet_avg_grade)
###############################################################
print(student_info[2]['hobbies'][0]['instruments'])
