student_id = input('enter student id:')
name = input('enter student name:')
placeofbirth = input('enter place of birth:')
dateofbirth = input('enter date of birth:')
address = input ('enter student address:')
gender = input ('enter student gender:')

student_data = f"{student_id}#{name}#{placeofbirth}#{dateofbirth}#{address}#{gender}"

fo = open("d:/studentprofile.txt", "a")
data = fo.write("student_data")
print(data)


