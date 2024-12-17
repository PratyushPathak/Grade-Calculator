import json
import copy

grades = {}
criteria = {}
    
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
    criteria[course] = {}

def remove_course(course):
    if course not in grades: return
    del grades[course]
    del criteria[course]

def add_category(course, category, weight, numDropped):
    if course not in grades: return
    if category in grades[course]: return
    grades[course][category] = []
    criteria[course][category] = [weight, numDropped]

def remove_category(course, category):
    if course not in grades: return
    if category not in grades[course]: return
    del grades[course][category]
    del criteria[course][category]

def calculate_avg(course, category):
    if criteria[course][category][1] == 0:
        return sum(grades[course][category]) / len(grades[course][category])
    if len(grades[course][category]) <= criteria[course][category][1]: return sum(grades[course][category]) / len(grades[course][category])
    
    temp = copy.copy(grades[course][category])
    avg = sum(temp)
    for i in range(criteria[course][category][1]):
        avg = avg - min(temp)
        temp.remove(min(temp))
    
    return avg / len(temp)


def calculate_courseavg(course):
    courseavg = 0
    for category in grades[course]:
        print(f"{calculate_avg(course, category)} x {criteria[course][category][0]}")
        courseavg += (calculate_avg(course, category)/100) * criteria[course][category][0]
    return courseavg





store = json.dumps(grades, indent=4)
with open('grades.json', 'w') as outfile:
    outfile.write(store)
storeC = json.dumps(criteria, indent=4)
with open('criteria.json', 'w') as outfile:
    outfile.write(storeC)
