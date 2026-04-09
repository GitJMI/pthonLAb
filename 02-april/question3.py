dict = {
    'raju':{
        "maths":99,
        "science":96,
        "english":98
    }
}
#maths , english , science

while(True):
    print("1.entry of a student's marks\n2.name & percentage\n3.who more than 75%\n4.name of topper of subject\n")

    ch = int(input("enter the choice: "))

    if (ch == 1):
        flag = 1
        while(flag):
            print("for exit student entry press 0")
            name =input("enter the student'name: ")
            Ms = int(input("enter marks of science"))
            Me = int(input ("enter the marks of english "))
            Mm = int (input("enter the marks of maths"))

            dict[name]["maths"] = Mm
            dict[name]["english"] = Me
            dict[name]["science"] = Ms

            ex = int(input("do you want to exit(0):"))
            if(ex == 0):
                print("---ended---\n")
                break

    elif (ch ==2):
        sum = 0
        name = input("enter name for percentage")
        for sub in dict[name]:
                sum = sum + dict[name][sub]
        percent = (sum/3)
        print(f"{name}:{percent}")
    
    elif (ch == 3):
        sum = 0
        percentdict ={
            
        }
        
        name = input("enter name for percentage")
        for student in dict:
            for sub in dict[student]:
                sum = sum + dict[student][sub]
            percent = (sum/3)
            percentdict[student] = percent

        for student in percentdict:
            if (percentdict[student] > 75 ):
                print(f"{percentdict[student]}")

        