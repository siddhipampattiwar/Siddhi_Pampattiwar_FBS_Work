# 1. Create a class Emp (eid,ename,basic)
# 2. WAP a menu driven program to perform following operations using
# files :

# a. Add a record
# b. Search for a record using id
# c. Delete a record using id
# d. Edit a record using id.
# e. Display all records.


import pickle

class Emp:
    def __init__(self, eid, ename, basic):
        self.eid = eid
        self.ename = ename
        self.basic = basic


def add_record():
    eid = int(input("Enter Employee ID: "))
    ename = input("Enter Employee Name: ")
    basic = float(input("Enter Basic Salary: "))

    emp = Emp(eid, ename, basic)

    with open("employee.dat", "ab") as f:
        pickle.dump(emp, f)

    print("Record Added Successfully!")


def search_record():
    eid = int(input("Enter Employee ID to Search: "))

    try:
        with open("employee.dat", "rb") as f:
            while True:
                emp = pickle.load(f)

                if emp.eid == eid:
                    print("ID:", emp.eid)
                    print("Name:", emp.ename)
                    print("Basic Salary:", emp.basic)
                    return

    except EOFError:
        print("Record Not Found!")

    except FileNotFoundError:
        print("File Not Found!")


def delete_record():
    eid = int(input("Enter Employee ID to Delete: "))
    records = []
    found = False

    try:
        with open("employee.dat", "rb") as f:
            while True:
                try:
                    emp = pickle.load(f)

                    if emp.eid == eid:
                        found = True
                    else:
                        records.append(emp)

                except EOFError:
                    break

        if found:
            with open("employee.dat", "wb") as f:
                for emp in records:
                    pickle.dump(emp, f)

            print("Record Deleted Successfully!")
        else:
            print("Record Not Found!")

    except FileNotFoundError:
        print("File Not Found!")


def edit_record():
    eid = int(input("Enter Employee ID to Edit: "))
    records = []
    found = False

    try:
        with open("employee.dat", "rb") as f:
            while True:
                try:
                    emp = pickle.load(f)

                    if emp.eid == eid:
                        emp.ename = input("Enter New Name: ")
                        emp.basic = float(input("Enter New Salary: "))
                        found = True

                    records.append(emp)

                except EOFError:
                    break

        if found:
            with open("employee.dat", "wb") as f:
                for emp in records:
                    pickle.dump(emp, f)

            print("Record Updated Successfully!")
        else:
            print("Record Not Found!")

    except FileNotFoundError:
        print("File Not Found!")


def display_all():
    try:
        with open("employee.dat", "rb") as f:
            while True:
                try:
                    emp = pickle.load(f)
                    print("\nEmployee ID:", emp.eid)
                    print("Employee Name:", emp.ename)
                    print("Basic Salary:", emp.basic)

                except EOFError:
                    break

    except FileNotFoundError:
        print("No Records Found!")


while True:
    print("\n1. Add Record")
    print("2. Search Record")
    print("3. Delete Record")
    print("4. Edit Record")
    print("5. Display All Records")
    print("6. Exit")

    choice = input("Enter Your Choice: ")

    if choice == "1":
        add_record()
    elif choice == "2":
        search_record()
    elif choice == "3":
        delete_record()
    elif choice == "4":
        edit_record()
    elif choice == "5":
        display_all()
    elif choice == "6":
        break
    else:
        print("Invalid Choice!")

