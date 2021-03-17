students_present = ["Shyam", "Ramesh", "Preet", "Mohan", "Sunidhi", "Priyansh", "Drashti", "Nirva"]
name_of_student = input("\nPlease enter the name of the student : \n")

if name_of_student in students_present:
    print( "\n" +name_of_student+ " was PRESENT\n")
else:
    print("\n" +name_of_student+ " was ABSENT\n")