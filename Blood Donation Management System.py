# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 21:35:27 2021

@author: Adithya Dileep
20 BCS 005
IIIT Dharwad
"""

import sys

class user:
    name = ""
    no = ""
    bg = ""
    dist = ""

class bb:
    name = ""
    dist = ""
    bg = [0,0,0,0,0,0,0,0]

def User():
    a = int(input("1.Donate  2.Receive  3.Main Menu ... Enter your choice number : "))
    if a==1 or a==2:
        print(" 1. A+ \t 2. A- \t 3. B+ \t 4. B- \t 5. AB+ \t 6. AB- \t 7. O+ \t 8. O-")
        b = int(input("Enter the choice number of your blood group : "))
        if b not in [1,2,3,4,5,6,7,8]:
            print("Invalid input! Try again!")
            User()
    if a==1:
        file = open('DonorDetails.txt','a')
        user.name = input(" Enter your name : ")
        user.no = input(" Enter your phone number : ")
        user.dist = input("Enter your district : ")
        if b == 1:
            user.bg = "A+"
        elif b == 2:
            user.bg = "A-"
        elif b == 3:
            user.bg = "B+"
        elif b == 4:
            user.bg = "B-"
        elif b == 5:
            user.bg = "AB+"
        elif b == 6:
            user.bg = "AB-"
        elif b == 7:
            user.bg = "O+"
        elif b == 8:
            user.bg = "O-"
        file = open('DonorDetails.txt','a')
        D = [ user.name ,"\t", user.no ,"\t", user.bg ,"\t", user.dist ]
        file.writelines(D)
        file.write("\n")
        file.close()
        menu()
    elif a==2:
        print("The available Donors List\n")
        file = open('DonorDetails.txt','r')
        for details in file:
            print(details)
        file.close()
        menu()
    elif a==3:
        menu()
    else:
        print("Invalid input! Try again!")
        menu()

def add():
    bb.name = input("Enter the name of Blood Bank / Blood Donation Camp : ")
    bb.dist = input("Enter the district : ")
    file = open('BloodBank.txt','a')
    B = [ bb.name ,"\t", bb.dist ]
    file.writelines(B)
    file.close()
    admin()

def viewbb():
    print(" List of Blood Banks / Blood Donation Camps\n")
    file = open('BloodBank.txt','r')
    for details in file:
        print(details)
    file.close()
    admin()

def view():
    print(" List of Blood Donors\n")
    file = open('DonorDetails.txt','r')
    for details in file:
        print(details)
    file.close()
    admin()

def admin():
    print("/n 1.Add blood bank / blood donation camp \t 2.View Blood Donors list \t 3.View Blood Banks/Donation Camps \t 4.Main Menu")
    m = int(input("Enter the choice number : "))
    if m==1:
        add()
    elif m==2:
        view()
    elif m==3:
        viewbb()
    elif m==4:
        menu()
    else:
        print("Invalid input! Try again!")
        menu()

def menu():
    n = int(input("\n Main Menu\n\n 1. Admin \t 2. User \t 3. Exit \n Enter the appropriate input number for your role : "))
    if n==1:
        password = input(" Enter Password : ")
        if password == "password":
            admin()
        else:
            print(" Incorrect Password !")
            menu()
    elif n==2:
        User()
    elif n==3:
        print(" STAY HEALTHY")
        sys.exit()
    else :
        print(" Invalid Input !\n")
        menu()

print("\n\n BLOOD DONATION MANAGEMENT APPLICATION \n\n")
print("\n Done by  ADITHYA DILEEP \n\t 20 BCS 005 \n\t IIIT Dharwad \n")
menu()