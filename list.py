subjects = ["math", "english", "computer", "accounting", "html"]

for i, subject in enumerate (subjects, start=1):
    print(f"{i}.{subject}")  
    
subjects.insert(2, "css")
print(subjects)

scores = [54, 45, 95, 64, 98]

greater60 = [score for score in scores if score >=60]
print(greater60)

results = [
    ["Amaka", 85, "A"],
    ["Daniel", 75, "A"],
    ["Jerry", 8, "F"],    
] 

print(results[2][0])


