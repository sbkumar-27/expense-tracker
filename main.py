import mysql.connector as sql
try:


    #Establishing a connnection to expense_tracker databse
    conn=sql.connect(host="localhost",user="root",port="3306",password="sanji",database="expense_tracker")
    cur=conn.cursor()


    #Login or Register
    #uid,uname,number integer
    #password string
    print("\t\t\t\t--------Welcome to Expense Tracker--------")
    print("1.Login")
    print("2.Register")
    choice=int(input("Enter your choice:"))
    if (choice==1):
        uid=int(input("Enter your user id:"))
        password=input("Enter your password:")
        query="SELECT password FROM USER WHERE uid=%s"
        cur.execute(query,(uid,))
        temp=cur.fetchone()
        if (temp is not None and temp[0]==password):
            print("Login Successful")
        else:
            print("Invalid user id or password")
    elif(choice==2):
        uname=input("Enter your name:")
        number=int(input("Enter your number:"))
        password=input("Enter your password:")
        query="INSERT INTO user(u_name,u_num,password,balance) VALUES(%s,%s,%s,%s)"
        values=(uname,number,password,0)
        cur.execute(query,values)
        conn.commit()
        uid=cur.lastrowid
        print("Registered Succesfully")
        print("Your user id:",uid)
        balance=int(input(("Enter your bank balance:")))
        query="UPDATE USER SET balance=%s WHERE uid=%s"
        values=(balance,uid)
        cur.execute(query,values)
        conn.commit()



except Exception as e:
    print("Error:",e)
