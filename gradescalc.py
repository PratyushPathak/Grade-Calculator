import json
from fractions import Fraction

default_grades = {"Homework": [],
         "Quiz": [],
         "Exam": [],
         "Participation": []}

try:
    with open("grades.json", "r") as openfile:
        grades = json.load(openfile)

        for category in default_grades.keys():
            if category not in grades:
                grades[category] = []
except FileNotFoundError:
    grades = default_grades.copy()
except json.JSONDecodeError:
    grades = default_grades.copy()

add = input("Do you have grades to input: \n1. Yes\n2. No\n")
hasInput = (int(add) == 1)

if hasInput:
    print("Input grades for each category one after another, enter -1 when done to move to next category")
    for category in grades.keys():
        if(category != "Averages"):
            print(f"{category}:")
            currGrade = float(Fraction(input("Enter grade or -1 to move on:\n")))
            while currGrade >= 0:
                if(category != "Quiz"): currGrade /= 100
                grades[category].append(currGrade)
                currGrade = float(Fraction(input()))

    storeData = json.dumps(grades, indent=4)

    with open("grades.json", "w") as outfile:
        outfile.write(storeData)

    print(grades)

with open("grades.json", "r") as openfile:
    finG = json.load(openfile)

if(int(input("Calculate Averages?\n1. Yes\n")) == 1):
    averages = {}
    for category in finG:
        if category != "Averages":
            if finG[category]:
                if(category != "Quiz"): 
                    catSum = sum(finG[category])
                    averages[category] = catSum / len(finG[category])
                else: 
                    catSum = sum(finG[category]) - min(finG[category])
                    averages[category] = catSum / (len(finG[category]) - 1)
            else:
                averages[category] = 0
    
    finG["Averages"] = averages

    strAvg = json.dumps(finG, indent = 4)

    with open("grades.json", "w") as outfile:
        outfile.write(strAvg)
    
    print(averages)

print("\n\n\n\n\n")

weights = {"Homework": 45,
           "Quiz": 15,
           "Exam": 35,
           "Participation": 5}

weightedAvg = 0

for category in finG["Averages"]:
    weightedAvg += (finG["Averages"][category])*weights[category]

print(weightedAvg)
