import json

grades = {}
criteria = {}

with open('grades.json', 'r') as readfile:
    grades = json.load(readfile)
with open('criteria.json', 'r') as openfile:
    criteria = json.load(openfile)
          
def add_grade(course, category, score):
    if course not in grades: return
    if category not in grades[course]: return
    grades[course][category].append(score)

def remove_grade(course, category, score):
    if course not in grades: return
    if category not in grades[course]: return
    grades[course][category].remove(score)

def add_course(course):
    if course in grades: return
    grades[course] = {}

def remove_course(course):
    if course not in grades: return
    del grades[course]

def add_category(course, category):
    if course not in grades: return
    if category in grades[course]: return
    grades[course][category] = []

def remove_category(course, category):
    if course not in grades: return
    if category not in grades[course]: return
    del grades[course][category]

store = json.dumps(grades, indent=4)
with open('grades.json', 'w') as outfile:
    outfile.write(store)
storeC = json.dumps(grades, indent=4)
with open('criteria.json', 'w') as outfile:
    outfile.write(storeC)
