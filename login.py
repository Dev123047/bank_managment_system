import csv
from bms import *
def login():
    while True:
        print("Choose Login Type:\n\t1) Admin Login\n\t2) User Login\n\t3) Forgot User Login Password")
        ch = int(input("Your choice : "))
        if ch == 1:
            adminlogin()
        elif ch == 2:
            userlogin()
        elif ch == 3:
            forgotpass()
        else:
            break
def adminlogin():
    user = input("Enter User ID : ")
    userpass = dict(zip(fetchadminlogin(0),fetchadminlogin(1)))
    if user in fetchadminlogin(0):
        password = input("Enter password : ")
        if userpass[user] == password:
            print("Success")
            adminmenu()

def userlogin():
    user = input("Enter User ID : ")
    userpass = dict(zip(fetchuserlogin(0),fetchuserlogin(1)))
    if user in fetchuserlogin(0):
        password = input("Enter password : ")
        if userpass[user] == password:
            print("Success")
            usermenu()
def createuserlogin(): #done
    username = input("Enter User ID : ")
    if username in fetchuserlogin(0):
        print("User already exists!")
        return None
    password = input("Enter Password : ")
    secques = input("Enter Security Question : ")
    secans  = input("Enter Security Question's Answer : ")
    rec = [username,password,secques,secans]
    with open('./logindetails/user.csv','a',newline='') as det:
        writer = csv.writer(det)
        writer.writerow(rec)
    return None
def fetchuserlogin(x): #done
    det = open("./logindetails/user.csv","r")
    reader = csv.reader(det)
    existing = []
    column = []
    for row in reader:
        for i in row:
            existing.append(i)
            continue
    for i in range(x,len(existing),4):
        column.append(existing[i])
    det.close()
    return column
def fetchadminlogin(x): #done
    det = open("./logindetails/admin.csv","r")
    reader = csv.reader(det)
    existing = []
    column = []
    for row in reader:
        for i in row:
            existing.append(i)
            continue
    for i in range(x,len(existing),2):
        column.append(existing[i])
    det.close()
    return column
def forgotpass():
    user = input("Enter User ID : ")
    if user in fetchuserlogin(0):
        userpass = dict(zip(fetchuserlogin(0),fetchuserlogin(1)))
        usersecques = dict(zip(fetchuserlogin(0),fetchuserlogin(2)))
        secquesans = dict(zip(fetchuserlogin(2),fetchuserlogin(3)))
        ans = input("Security Question : {}\nSecurity Question's Answer : ".format(usersecques[user]))
        givensecques = usersecques[user]
        if ans == secquesans[givensecques]:
            print("Password is : {}".format(userpass[user]))
        else:
            print("Fail")
    return None
def adminmenu():
    while True : 
        print("Options :\n\t1) Open New Account\n\t2) Search a Account\n\t3) Close an existing account\n\t4) Intra Bank Money Tranfer\n\t5) Add Money to Account\n\t6) Withdraw Money from Account\n\t7) Logout")
        ch = int(input("Enter choice : "))
        if ch == 1:
            openacc()
        elif ch == 2:
            searchacc()
        elif ch == 3:
            closeacc()
        elif ch == 4:
            moneytransfer()
        elif ch == 5:
            addmoney()
        elif ch == 6:
            withdraw()
        else:
            print("You have been logged out!")
            break
def usermenu():
    while True:
        print("1) Search Account")
        ch = int(input("Enter Choice : "))
        if ch == 1:
            searchacc()
        else:
            print("You have been logged out!")
            break