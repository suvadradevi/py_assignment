student={'Abhi':12,'Bobby':98,'Ram':45,'Sita':67}
name=input("Enter student name: ")
marks=student.get(name)
if marks is None:
    print("This student is not present in the list")
else:
    print("Marks = ",marks)