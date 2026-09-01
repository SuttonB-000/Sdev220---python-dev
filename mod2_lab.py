#variable declaration
lastName = ""

print("To exit program, type 'zzz' or 'ctrl + c'")

#main prog logic [as long as user does not enter 'zzz' prog will continue]
while lastName != 'zzz':
    lastName = input('What is the students last name? ')
    
    #exit statement
    if lastName == 'zzz':
        break

    firstName = input('What is the students first name? ')
    gpa = float(input(f"What is {firstName} {lastName}'s gpa? "))
    
    #gpa test conditions
    if gpa >= 3.5:
        print("student has made Dean's List")
        special = "Dean's List"
    elif gpa >= 3.25:
        print("student has made Honor Roll")
        special = "Honor Roll"
    else:
        special = ""

    data = f'{lastName} {firstName} ... {gpa} {special}'

    #write data to a file 
    with open('grades.txt', 'a') as f:
        f.write(data + '\n')

print('Here is the data you entered:')
with open('grades.txt', 'r') as f:
    for line in f:
        print(line)


