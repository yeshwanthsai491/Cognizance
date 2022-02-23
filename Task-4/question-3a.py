while True:
    print("Menu Driven Program")
    print("1.Add the student")
    print("2.Edit the student")   
    print("3.Exit")
    choice=int(input("Enter your choice:"))
    if choice==1:
        lst = []
        for i in range(int(input("Enter number of students: "))):
                lst.append([input("Enter roll no: "), input("Enter name: "), int(input("Enter marks: "))])
        print("Roll No.\t Name\t\t Marks")
        for i in lst:
                print(i[0], "\t\t", i[1], "\t\t", i[2])
    
    elif choice==2:
        roll = input("Enter roll no of student whose marks to edit: ")
        for i in lst:
                if i[0] == roll:
                        i[2] = int(input("Enter new marks: "))
        print("Roll No.\t Name\t\t Marks")
        for i in lst:
                print(i[0], "\t\t", i[1], "\t\t", i[2])
    
    elif choice==3:
        break
    else:
        print("Wrong Choice")