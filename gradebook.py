last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

# Your code below: 

subjects = ["Physics", "Calculus", "Poetry", "History"]
grades = [98, 97, 85, 88]
gradebook = [["Physics", 98], ["Calculus", 97], ["Poetry", 85], ["History", 88]]
print(gradebook)

gradebook.append(["CompSci", 100])
gradebook.append(["VisArts", 93])
print(gradebook)

gradebook[-1][-1] += 5
print(gradebook)

gradebook[2].remove(85)
gradebook[2].append("Pass")
print(gradebook)

print("\n")

full_gradebook = last_semester_gradebook + gradebook
print(full_gradebook)