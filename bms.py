import mysql.connector as mysql
import datetime
db = mysql.connect(host = 'bgoxeiwvhlnqsmazcbsu-mysql.services.clever-cloud.com', user = 'u4qjiz66gy3eqbzm', password = 'hNYi8XZPQIblvqXbQNVu', database = 'bgoxeiwvhlnqsmazcbsu')
cursor = db.cursor()
def openacc():
    holder_name = input("Enter Account Holder's Name : ")
    holder_contact = input("Enter Account Holder's Contact Number : ")
    holder_address = input("Enter Account Holder's Address : ")
    balance = input("Enter opening balance : ")
    query = "INSERT INTO accounts(holder_name, holder_contact, holder_address, balance) VALUES('{}','{}','{}','{}')".format(holder_name,holder_contact,holder_address,balance)
    cursor.execute(query)
    db.commit()
    x = "SELECT max(acc_id) FROM accounts"
    cursor.execute(x)
    y = cursor.fetchall()[0][0]
    query = "CREATE TABLE IF NOT EXISTS `{}`(sno INT NOT NULL AUTO_INCREMENT PRIMARY KEY, timestamp DATETIME NOT NULL, deposit VARCHAR(20) NOT NULL, withdrawl VARCHAR(20) NOT NULL)".format(y)
    cursor.execute(query)
    return None
def searchacc():
    ch = int(input("1) Search by Holder's Name\n2) Search by Holder's Contact Number\n3) Search by Account ID\nEnter choice : "))
    if ch == 1:
        name = input("Enter the Name : ")
        query = "SELECT holder_name, acc_id FROM accounts WHERE holder_name = '{}'".format(name)
        cursor.execute(query)
        y = cursor.fetchall()
        for i in["Holder's Name","Account ID"]:
            print(i.ljust(25),end="")
        print()
        for i in y:
            for j in i:
                print(str(j).ljust(25),end="")
            print()
    elif ch == 2:
        contact = input("Enter the number : ")
        query = "SELECT holder_name, holder_contact, acc_id FROM accounts WHERE holder_name = '{}'".format(contact)
        cursor.execute(query)
        y = cursor.fetchall()
        for i in["Holder's Name","Contact Number","Account ID"]:
            print(i.ljust(25),end="")
        print()
        for i in y:
            for j in i:
                print(str(j).ljust(25),end="")
            print()
    elif ch == 3:
        contact = input("Enter the Account ID : ")
        query = "SELECT holder_name, acc_id FROM accounts WHERE holder_name = '{}'".format(contact)
        cursor.execute(query)
        y = cursor.fetchall()
        for i in["Holder's Name","Account ID"]:
            print(i.ljust(25),end="")
        print()
        for i in y:
            for j in i:
                print(str(j).ljust(25),end="")
            print()
    else:
        return None
    return None
def closeacc():
    acc_id = input("Enter Account ID : ")
    query = "SELECT * FROM accounts WHERE acc_id = {}".format(acc_id)
    cursor.execute(query)
    y = cursor.fetchall()
    for i in y:
        print(i,end="\t")
    ch = int(input("Are you sure you want to delete this account?[1/0] : "))
    if ch == 1:
        cursor.execute("DELETE FROM accounts WHERE acc_id = {}".format(acc_id))
        print("Done")
    else:
        return None
    return None
def moneytransfer():
    fromacc = int(input("Enter from account number : "))
    toacc = int(input("Enter to account number : "))
    query = "SELECT holder_name, balance, acc_id FROM accounts WHERE acc_id = {}".format(fromacc)
    cursor.execute(query)
    y = cursor.fetchall()
    for i in["Holder's Name","Balance","Account ID"]:
            print(i.ljust(25),end="")
    print()
    for i in y:
        for j in i:
            print(str(j).ljust(25),end="")
        print()
    ch = int(input("Confirm from account?[1/0] : "))
    if ch == 1:
        query = "SELECT holder_name, balance, acc_id FROM accounts WHERE acc_id = {}".format(toacc)
        cursor.execute(query)
        y = cursor.fetchall()
        for i in["Holder's Name","Balance","Account ID"]:
                print(i.ljust(25),end="")
        print()
        for i in y:
            for j in i:
                print(str(j).ljust(25),end="")
            print()
        ch1 = int(input("Confirm from account?[1/0] : "))
        if ch1 == 1:
            tobetransfered = input("Enter amount to be transfered : ")
            cursor.execute("SELECT balance FROM accounts WHERE acc_id = {}".format(fromacc))
            y = cursor.fetchall()
            y3 = y[0]
            if int(y3[0]) > int(tobetransfered):
                x = int(y3[0]) - int(tobetransfered)
                cursor.execute("UPDATE accounts SET balance = {} WHERE acc_id = {}".format(x,fromacc))
                updatepassbook(fromacc,0,tobetransfered)
                cursor.execute("SELECT balance FROM accounts WHERE acc_id = {}".format(toacc))
                y1 = cursor.fetchall()
                y = int(y1[0][0])
                y5 = y + int(tobetransfered)
                cursor.execute("UPDATE accounts SET balance = {} WHERE acc_id = {}".format(y5,toacc))
                updatepassbook(toacc,tobetransfered,0)
                db.commit()
                return None
            else:
                print("Not sufficient amount!")
                return None
        else:
            return None
    else:
        return None
def addmoney():
    toacc = input("Enter the account to which money is to be added : ")
    query = "SELECT holder_name, balance, acc_id FROM accounts WHERE acc_id = {}".format(toacc)
    cursor.execute(query)
    y = cursor.fetchall()
    for i in["Holder's Name","Balance","Account ID"]:
        print(i.ljust(25),end="")
    print()
    for i in y:
        for j in i:
            print(str(j).ljust(25),end="")
        print()
    ch1 = int(input("Confirm to account?[1/0] : "))
    if ch1 == 1:
        money = int(input("Enter money to be added : "))
        cursor.execute("SELECT balance FROM accounts WHERE acc_id = {}".format(toacc))
        y1 = cursor.fetchall()
        y = int(y1[0][0])
        y5 = y + int(money)
        cursor.execute("UPDATE accounts SET balance = {} WHERE acc_id = {}".format(y5,toacc))
        updatepassbook(toacc,int(money),0)
        db.commit()
        return None
def withdraw():
    toacc = input("Enter the account from which money is to be withdrawed : ")
    query = "SELECT holder_name, balance, acc_id FROM accounts WHERE acc_id = {}".format(toacc)
    cursor.execute(query)
    y = cursor.fetchall()
    for i in["Holder's Name","Balance","Account ID"]:
        print(i.ljust(25),end="")
    print()
    for i in y:
        for j in i:
            print(str(j).ljust(25),end="")
        print()
    ch1 = int(input("Confirm to account?[1/0] : "))
    if ch1 == 1:
        money = int(input("Enter money to be withdrawed : "))
        cursor.execute("SELECT balance FROM accounts WHERE acc_id = {}".format(toacc))
        y1 = cursor.fetchall()
        y = int(y1[0][0])
        y5 = y - int(money)
        cursor.execute("UPDATE accounts SET balance = {} WHERE acc_id = {}".format(y5,toacc))
        updatepassbook(toacc,0,int(money))
        db.commit()
        return None
def updatepassbook(acc,d,p):
    query = "INSERT INTO `{}`(deposit,withdrawl) VALUES({},{})".format(acc,d,p)
    cursor.execute(query)
    db.commit()