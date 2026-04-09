dict = {
    "january":31,
    "february":28,
    "march":31,
    "april":30,
    "may":31,
    "june":30,
    "july":31,
    "august":31,
    "september":30,
    "october":31,
    "november":30,
    "december":31
}
print("---dictionary whose keys are month name , and values are no. of days---")

while(True):
    print("1.to know days in a month\n2.to display months and days in alphabetical order\n3.to print 31days month\n4.print months sorted by no. days in a month\n5.exit")
    
    ch = int(input("enter the choice: "))

    if (ch == 1):
        key = input("enter the month name: ")
        for obj in dict:
            if(obj == key.lower()):
                print(f"{key}:{dict[obj]}\n")
                break
            print("not found\n")
    
    elif (ch == 2):
        print("---alphabetical order---- \n")
        
        for k , v in sorted(dict.items()):
            print((k,v),end=" ")

        print("\n-----\n")

    elif (ch == 3):
        print("---31 days month---\n")
        for obj in dict:
            if (dict[obj] == 31):
                print(f"{obj}  ")
        print("------------\n")
    elif (ch == 4):
        for k , v in sorted(dict.items(),key = lambda x:x[1]):
            print(k,":",v)
        print("---------------\n")

    elif (ch == 5):
        break