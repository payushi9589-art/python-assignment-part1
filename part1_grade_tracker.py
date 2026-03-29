

# Here is how that story looks in Python code. 

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