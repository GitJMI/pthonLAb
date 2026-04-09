dict = {'prague': 20, 'jamshedpur': 500, 'delhi': 50, 'moradabad': 90}

while(True):
    print("1.add key value\n2.search by key\n3.search by value\n4.update\n5.delete value\n6. display sort\n7.exit")

    ch = int(input("enter the choice: "))

    if (ch == 1):
        print("---adding a key value pair---")
        key = input("enter the key:")
        value = int(input("enter the value:"))
        dict[key] = value

    elif (ch == 2):
        print("---search by key ---")
        key= input("enter key to search: ")
        for obj in dict:
            if (key == obj):
                print(f"key found---\nkey:{key} & value:{dict[key]}")
                break 
            print("key not found\n")

    elif(ch == 3):
        print("---seaching by value---")
        value = int(input("enter the value: "))
        for obj in dict:
            if (value == dict[obj]):
                print(f"value found!!\nkey:{obj} value:{value}")
                break
            print("Value not found")

    elif(ch == 4):
        print("---updating the dict---")
        print(f"current dictionary:{dict}")
        key = input("enter the key: ")
        value= int(input("enter the new value: "))
        dict[key] = value

    elif(ch == 5):
        print("---deleting the value---")
        value = int(input("enter the value to be deleted: "))
        for obj in dict:
            if(dict[obj] == value):
                del dict[obj]
                print("deleted the value and key")
                break
            # print("not Found the value")

    elif (ch == 6):
        print("---sorted dictionary---")
        for k , v in sorted(dict.items()):
            print((k,v),end=" ")

        print("\n-----\n")

    elif( ch == 7 ):
        print("--exiting from program---")
        break

    else:
        print("wrong input\n")
    print("\n---------------------\n")