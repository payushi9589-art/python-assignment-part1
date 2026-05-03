

# Here is how that story looks in Python code.  Task1

raw_students = [
    {"name": "  ayesha SHARMA  ", "roll": "101", "marks_str": "88, 72, 95, 60, 78"},
    {"name": "ROHIT verma",       "roll": "102", "marks_str": "55, 68, 49, 72, 61"},
    {"name": "  Priya Nair  ",    "roll": "103", "marks_str": "91, 85, 88, 94, 79"},
    {"name": "karan MEHTA",       "roll": "104", "marks_str": "40, 55, 38, 62, 50"},
    {"name": " Sneha pillai ",    "roll": "105", "marks_str": "75, 80, 70, 68, 85"},
]

# This is our new box where we will clean and store the clean and clear data from the raw data
clean_studentsData = []

for student in raw_students:
    
    #1.Give the name a clear view like making captial letter for first name & Last name
    clean_name = student["name"].strip().title()
    
    #2.Take off the stringand as instructions ays makeing into a real number
    clean_roll = int(student["roll"])
    
    #3.Use split to make makrs look nicer 
    clean_marks = []
    #We are heree to split the string where the comma and space are required to be
    for mark in student["marks_str"].split(", "): 
        clean_marks.append(int(mark))
        
    #4.Check the validaity as mentioned in requirement
    if clean_name.replace(" ", "").isalpha():
        print(f"{clean_name}: ✓ Valid name")
    else:
        print(f"{clean_name}: ✗ Invalid name")
        
    #5.Making the card using f-strings
    print("================================")
    print(f"Student : {clean_name}")
    print(f"Roll No : {clean_roll}")
    print(f"Marks   : {clean_marks}")
    print("================================\n")
    
    # Make and align the new clean student into the created clean box variable
    cleaned_students.append({
        "name": clean_name,
        "roll": clean_roll,
        "marks": clean_marks
    })

#6.As per the ask need to find student 103 and make the name appear in CAPS ALL and lowrrcase
for student in cleaned_students:
    if student["roll"] == 103:
        print(student["name"].upper()) # ALL CAPS
        print(student["name"].lower()) # lowercase letters





------------- Reloaded ------------------



student_name = "Ayesha Sharma"
subjects     = ["Math", "Physics", "CS", "English", "Chemistry"]
marks        = [88, 72, 95, 60, 78]

print(f"Grades for {student_name}")

#for loop
for i in range(len(subjects)):
    subject_name = subjects[i]
    score = marks[i]
    
    #decide grade
if score >= 90:
        grade = "A+"
    elif score >= 80:
        grade = "A"
    elif score >= 70:
        grade = "B"
    elif score >= 60:
        grade = "C"
    else:
        grade = "F"
        
    print(f"{subject_name}: {score} - {grade}")

#work the math of sum
total_marks = sum(marks)
#way to find avg
average_marks = round(total_marks / len(marks), 2)

print(f"\nTotal marks: {total_marks}")
print(f"Average marks: {average_marks}")

#use max and min
highest_mark = max(marks)
lowest_mark = min(marks)

#try to get high and low amrk
highest_index = marks.index(highest_mark)
lowest_index = marks.index(lowest_mark)

print(f"Highest scoring subject: {subjects[highest_index]} ({highest_mark})")
print(f"Lowest scoring subject: {subjects[lowest_index]} ({lowest_mark})\n")

#can add new sub
new_subjects_added = 0

while True:
    new_subject = input("Enter a new subject (or type 'done' to stop): ").strip()
    
    #stop the loop
    if new_subject.lower() == "done":
        break
        
    new_mark_text = input(f"Enter the marks for {new_subject} (0-100): ").strip()
    
    #4.save from bad input
    try:
        new_mark = int(new_mark_text) 
        
        #verify us the provided number os valid and meaninful
        if 0 <= new_mark <= 100:
            subjects.append(new_subject) #add new sub
            marks.append(new_mark)       #add new score
            new_subjects_added += 1
        else:
            print("Warning: Marks must be between 0 and 100!")
            
    except ValueError:
        #if any string is fiven CHECK
        print("Warning: That is not a real number! Try again.")

#calculate new avg
print(f"\nNew subjects added: {new_subjects_added}")
new_total = sum(marks)
new_average = round(new_total / len(marks), 2)
print(f"Updated average: {new_average}")

===============================================================================


# Task 3 — Class Summaryof th Performance

print("\n=== Task 3: Performance Summary of the Class ===\n")

class_data = [
    ("Ayesha Sharma",  [88, 72, 95, 60, 78]),
    ("Rohit Verma",    [55, 68, 49, 72, 61]),
    ("Priya Nair",     [91, 85, 88, 94, 79]),
    ("Karan Mehta",    [40, 55, 38, 62, 50]),
    ("Sneha Pillai",   [75, 80, 70, 68, 85]),
]

report = []
for name, marks in class_data:
    avg = round(sum(marks) / len(marks), 2)
    status = "Pass" if avg >= 60 else "Fail"
    report.append((name, avg, status))

print("Name              | Average | Status")
print("----------------------------------------")
for name, avg, status in report:
    print(f"{name:<16} | {avg:7.2f} | {status}")

# Summary generation
passedStatus = sum(1 for _, _, status in report if status == "Pass")
failedStatus = len(report) - passedStatus
topper = max(report, key=lambda x: x[1])
class_avg = round(sum(avg for _, avg, _ in report) / len(report), 2)

print(f"\nPassed: {passedStatus}, Failed: {failedStatus}")
print(f"Topper: {topper[0]} ({topper[1]})")
print(f"Class Average: {class_avg}")


=====================================================================


#Task 4 


essay = "  python is a versatile language. it supports object oriented, functional, and procedural programming. python is widely used in data science and machine learning.  "

#clear whitespace
cleanEssay = essay.strip().lower()
print("Clean Essay:", cleanEssay)

print("\nTitle Case:", cleanEssay.title())

print("\nPython count:", cleanEssay.count("python"))

#emoji replcament
print("\nReplaced:", cleanEssay.replace("python", "Python 🐍"))

#spliting the sentence
sentences = cleanEssay.split(". ")
print("\nSentences List:", sentences)

#print sentence
print("\nNumbered Sentences:")
for i, s in enumerate(sentences, 1):
    if not s.endswith("."):
        s += "."
    print(f"{i}. {s}")



