import datetime
import random
import mysql.connector as db
con=db.connect(host='localhost',
               user='root',
               password='nishitha@5',
               database='nishitha',
               auth_plugin='mysql_native_password')

mycursor=con.cursor()
today=datetime.datetime.now()

print('*'*25,"WELCOME TO CITY BANK",'*'*25)
a=['1','2','3','4','5','6','7','8','9','0']
b='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
while True:
    print("1.User")
    print("2.Admin")
    print("3.Exit")
    ch=input("Enter the option:")
    if ch=='2':
        user=input("Enter the usernmae:")
        password=input("enter the password:")
        if user=='nishitha' and password=='1234':
            while True:
                print('-'*50,"WELCOME TO ADMIN FIELD",'-'*50)
                print("1.New Account")
                print("2.Account Login")
                print("3.View all users")
                print("4.Transactions of a user")
                print("5.Display User details")
                print("6.Transactions of the particular day")
                print("7.Exit")
                ch1=input("chooes the option:")
                if ch1=='1':
                    print('-'*25,"WELCOME TO NEW ACCOUNT CREATION",'-'*25)
                    while True:
                        name=input("Enter the account holder name:")
                        for i in name:
                            if i not in b:
                                print("enter the correct name it does not contain the special symbols")
                                break
                        else:
                            break
                    while True:
                        phone=input("Enter the account holder mobile number:")
                        if phone[0]>='6'and len(phone)==10:
                            for i in phone:
                                if i not in a and i in b:
                                    print("enter the correct number")
                                    break
                            else:
                                break
                        else:
                            print("enter the a correct number")
                    ch2=input("Do you have alternative number enter 1 for yes 2 for no:")
                    if ch2=='1':
                        while True:
                            alter=input("Enter the alter native number of account holder:")
                            if alter[0]>='6' and len(alter)==10 :
                                for i in alter:
                                    if i not in a and i in b:
                                        print("enter the correct number:")
                                        break
                                else:
                                    break
                            else:
                                print("enter the correct number:")
                    elif ch2=='2':
                        while True:
                            alter=input("Enter the nomini number for this account holder:")
                            if alter[0]>='6' and len(alter)==10:
                                for i in alter:
                                    if i not in a and i in b:
                                        print("enter the correct number:")
                                        break
                                else:
                                    break
                            else:
                                print("enter the correct number:")
                    else:
                        print("chooes the correct option")
                    while True:
                        addhar=input("Enter the account holder addhar card number:")
                        if len(addhar)==12:
                            break
                        else:
                            print("please enter  the valide addhar card number")
                    while True:
                        gender=input("Enter the account holder gender:")
                        if gender=='male' or gender=='female':
                            break
                    print("1.Savings Account")
                    print("2.Current Account")
                    print("3.Fixed Deposit")
                    while True:
                        atype=input("Enter the type of account:")
                        if atype=='1':
                            acctype='savings'
                            break
                        elif atype=='2':
                            acctype='current'
                            break
                        elif atype=='3':
                            acctype='fixed'
                            break
                        else:
                            print("choose the correct account")
                    while True:
                        s=phone[ : ]
                        z=random.randint(11,99)
                        accnumber=s+str(z)
                        for i in accnumber:
                            if i not in a:
                                print("give the correct number")
                                break
                        else:
                            break
                    amount=float(input("Enter the amount:"))
                    query="insert into bank(account_number,acc_name,account_type,amount,mobile_number,alternative_number,addhar_card_number,gender,account_created_date)values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                    values=(accnumber,name,acctype,amount,phone,alter,addhar,gender,today)
                    mycursor.execute(query,values)
                    con.commit()
                    print("Account is created sucessfully")


                    print('*'*25,"THIS IS YOUR BANK BOOK",'*'*25)
                    print("ACCOUNT HOLDER NAME :",name.upper())
                    print("ACCOUNY NUMBER :",accnumber)
                    print("BRANCH NAME :CITY BANK")
                    print("BRANCH ADDRESS : AMARAVTHI(CAPITAL) PALNADU (DISTRICT)1-29 ROAD NO:52")
                    print("IFSC CODE:CTYNK1252")
                    print("SIGNATURE OF THE MANAGER:                                           K.BHARGAV")
                elif ch1=='2':
                    print("1.New user to genrate pin")
                    print("2.Regular user")
                    ch=input("Enter the chooes:")
                    if ch=='2':
                        accnumber=input("Enter the account number:")
                        pin=input("Enter your four digit pin:")
                        query="select * from bank where account_number=%s and pin_number=%s"
                        values=(accnumber,pin)
                        mycursor.execute(query,values)
                        result=mycursor.fetchone()
                        if result:
                            while True:
                                print("1.Pin Genration")
                                print("2.Credite")
                                print("3.Debit")
                                print("4.Balance enquery")
                                print("5.Exit")
                                ch1=input("Enter your option:")
                                if ch1=='1':
                                    while True:
                                        a=input("Enter the your new four digit pin:")
                                        b=input("Renter your pin:")
                                        if a==b:
                                            if len(a)==4 and len(b)==4:
                                                query="update bank set pin_number=%s where account_number=%s"
                                                values=(b,accnumber)
                                                mycursor.execute(query,values)
                                                con.commit()
                                                print("PIN GENRATED SUCCESSFULLY")
                                                break
                                            else:
                                                print("PIN CAN HAVE ONLY FOUR DIGITS")
                                        else:
                                            print("Incorrect pin")
                                            print('-'*25,'GENRATE AGAIN','-'*25)
                                elif ch1=='2':
                                    a=int(input("Enter the amount to credite amount to the account:"))
                                    query="update bank set amount=amount+%s where account_number=%s"
                                    values=(a,accnumber)
                                    mycursor.execute(query,values)
                                    con.commit()
                                    query="select acc_name from bank where account_number=%s"
                                    mycursor.execute(query,(accnumber,))
                                    acc_name=mycursor.fetchone()[0]
                                    query="select amount from bank where account_number=%s"
                                    mycursor.execute(query,(accnumber,))
                                    amt=mycursor.fetchone()[0]
                                    query="insert into transaction_table(account_number,acc_name,amount,transaction_date,credite_amount)values(%s,%s,%s,%s,%s)"
                                    values=(accnumber,acc_name,amt,today,a)
                                    mycursor.execute(query,values)
                                    con.commit()
                                    print("Amount is credited successfully")
                                elif ch1=='3':
                                    b=int(input("Enter the amount to withdraw:"))
                                    query="select amount from bank where account_number=%s"
                                    mycursor.execute(query,(accnumber,))
                                    res=mycursor.fetchone()
                                    if res[0]>b:
                                        query="update bank set amount=amount-%s where account_number=%s"
                                        values=(b,accnumber)
                                        mycursor.execute(query,values)
                                        con.commit()
                                        query="select acc_name from bank where account_number=%s"
                                        mycursor.execute(query,(accnumber,))
                                        acc_name=mycursor.fetchone()[0]
                                        query="select amount from bank where account_number=%s"
                                        mycursor.execute(query,(accnumber,))
                                        amt=mycursor.fetchone()[0]
                                        query="insert into transaction_table(account_number,acc_name,amount,transaction_date,debit_amount)values(%s,%s,%s,%s,%s)"
                                        values=(accnumber,acc_name,amt,today,b)
                                        mycursor.execute(query,values)
                                        con.commit()
                                        print("Amount is debited successfully")
                                    else:
                                        print("Their is no sufficent money to withdraw")
                                        print("your account consist of amount is:",res[0])
                                elif ch1=='4':
                                    query="select amount from bank where account_number=%s"
                                    mycursor.execute(query,(accnumber,))
                                    c=mycursor.fetchone()
                                    print("TOTAL AVAILABLE BALANCE IS:",c)
                                elif ch1=='5':
                                    break
                                else:
                                    print("Enter the correct option")
                                    
                        else:
                            print("Incorrect Account number or pin you entered")
                            print('-'*25,'ENTER ACCOUNT NUMBER AGAIN','-'*25)
                    elif ch=='1':
                        accnumber=input("enter the account number:")
                        query="select * from bank where account_number=%s"
                        mycursor.execute(query,(accnumber,))
                        res=mycursor.fetchone()
                        if res:
                            while True:
                                a=input("Enter the your new four digit pin:")
                                b=input("Renter your pin:")
                                if a==b:
                                    query="update bank set pin_number=%s where account_number=%s"
                                    values=(b,accnumber)
                                    mycursor.execute(query,values)
                                    con.commit()
                                    print("PIN GENRATED SUCCESSFULLY")
                                    break
                                else:
                                    print("Incorrect pin")
                                    print('-'*25,'GENRATE AGAIN','-'*25)
                        else:
                            print("Their no account existed in bank")
                                
                elif ch1=='3':
                    query="select account_number,acc_name,amount,mobile_number from bank"
                    mycursor.execute(query)
                    res=mycursor.fetchall()
                    print(f"{'Account Number':^20} {'Account holder name':^20} {'Amount':^20}{'Mobile Number':^20}")
                    print('-'*131)
                    q=[]
                    w=[]
                    e=[]
                    r=[]
                    for i in res:
                        for j in range(0,len(i)):
                            if j==0:
                                q.append(i[j])
                            elif j==1:
                                w.append(i[j])
                            elif j==2:
                                e.append(i[j])
                            elif j==3:
                                r.append(i[j])
                            else:
                                pass
                    for t,y,u,i in zip(q,w,e,r):
                        print(f"{t:^20} {y:^15} {u:20} {i:^25}")
                    print('-'*131)
                elif ch1=='4':
                    accnumber=input("Enter the account number:")
                    query="select account_number,acc_name,amount,transaction_date,credite_amount,debit_amount from transaction_table where account_number=%s"
                    mycursor.execute(query,(accnumber,))
                    res=mycursor.fetchall()
        
                    z=[]
                    x=[]
                    c=[]
                    v=[]
                    l=[]
                    m=[]
                    if res:
                        for i in res:
                            for j  in range(0,len(i)):
                                if j==0:
                                    z.append(i[j])
                                elif j==1:
                                    x.append(i[j])
                                elif j==2:
                                    c.append(i[j])
                                elif j==3:
                                    v.append(i[j].strftime("%Y-%d-%m"))
                                elif j==4:
                                    l.append(i[j])
                                elif j==5:
                                    m.append(i[j])
                                else:
                                    pass
                        print(f"{'Account Number':^10} {'account_holder name':^10} {'Amount':^10}{'date':^10} {'credit':^10} {'debit':^10}")
                        print('-'*131)
                        for a,s,d,f,g,h in zip(z,x,c,v,l,m):
                            print(f"{a:^10} {s:^15} {d:^15} {f:^10} {g or '0':^10} {h or '0':^10}")
                        print('-'*131)
                    else:
                        print("Their no transactions are done")
                elif ch1=='5':
                    accnumber=input("Enter the account numbere here to check the details:")
                    print('-'*20,'USER DETAILS','-'*20)
                    query="select acc_name,account_number,account_type,amount from bank where account_number=%s"
                    mycursor.execute(query,(accnumber,))
                    res=mycursor.fetchall()
                    print("Account Holder Name:",res[0][0])
                    print("Account Number:",res[0][1])
                    print("Account Type:",res[0][2])
                    print("Total Amount:",res[0][3])
                    print('-'*131)
                elif ch1=='7':
                    break
                elif ch1=='6':
                    print("1.To see today transactions")
                    print("2.To see another day transactions")
                    tran=input("Enter your option:")
                    if tran=='1':
                        today = datetime.date.today()
                        query=("select * from transaction_table where transaction_date=%s")
                        mycursor.execute(query,(today,))
                        
                        data=mycursor.fetchall()
                        print(data)
                        for i in data:
                            print(i)
                    elif tran=='2':
                        date=input("Enter the date here in the formate of 'year-month-day':")
                        query="select * from transaction_table where transaction_date=%s"
                        mycursor.execute(query,(date,))
                        dates=mycursor.fetchall()

                        for i in dates:
                            for j in i:
                                print(j)
                    else:
                        print("Enter the correct option")
                else:
                    print("Please Enter the correct option")
            else:
                print("Incorrect admin details enter correctly")
    elif ch=='1':
        while True:
            print('-'*50,'WELCOME TO USER FIELD','-'*50)
            print("1.New User")
            print("2.exisit User")
            print("3.To check user details")
            print("4.Statement")
            print("5.Exit")
            ch=input("Enter your option:")
            if ch=='2':
                accnumber=input("Enter the account number:")
                pin=input("Enter your four digit pin:")
                query="select * from bank where account_number=%s and pin_number=%s"
                values=(accnumber,pin)
                mycursor.execute(query,values)
                result=mycursor.fetchone()
                if result:
                    while True:
                        print("1.Pin Genration")
                        print("2.Credite")
                        print("3.Debit")
                        print("4.Balance enquery")
                        print("5.Exit")
                        ch1=input("Enter your option:")
                        if ch1=='1':
                            while True:
                                a=input("Enter the your new four digit pin:")
                                b=input("Renter your pin:")
                                if a==b:
                                    query="update bank set pin_number=%s where account_number=%s"
                                    values=(b,accnumber)
                                    mycursor.execute(query,values)
                                    con.commit()
                                    print("Pin genrated successfully")
                                    print('-'*25,'THANK YOU','-'*25)
                                    break
                                else:
                                    print("Incorrect pin")
                                    print('-'*25,'GENRATE AGAIN','-'*25)
                        elif ch1=='2':
                            a=int(input("Enter the amount to credite amount to the account:"))
                            query="update bank set amount=amount+%s where account_number=%s"
                            values=(a,accnumber)
                            mycursor.execute(query,values)
                            con.commit()
                            query="select acc_name from bank where account_number=%s"
                            mycursor.execute(query,(accnumber,))
                            acc_name=mycursor.fetchone()[0]
                            query="select amount from bank where account_number=%s"
                            mycursor.execute(query,(accnumber,))
                            amt=mycursor.fetchone()[0]
                            query="insert into transaction_table(account_number,acc_name,amount,transaction_date,credite_amount)values(%s,%s,%s,%s,%s)"
                            values=(accnumber,acc_name,amt,today,a)
                            mycursor.execute(query,values)
                            con.commit()
                            print("Amount credited successfully")
                        elif ch1=='3':
                            b=int(input("Enter the amount to withdraw:"))
                            query="select amount from bank where account_number=%s"
                            mycursor.execute(query,(accnumber,))
                            res=mycursor.fetchone()
                            if res[0]>b:
                                query="update bank set amount=amount-%s where account_number=%s"
                                values=(b,accnumber)
                                mycursor.execute(query,values)
                                con.commit()
                                query="select acc_name from bank where account_number=%s"
                                mycursor.execute(query,(accnumber,))
                                acc_name=mycursor.fetchone()[0]
                                query="select amount from bank where account_number=%s"
                                mycursor.execute(query,(accnumber,))
                                amt=mycursor.fetchone()[0]
                                query="insert into transaction_table(account_number,acc_name,amount,transaction_date,debit_amount)values(%s,%s,%s,%s,%s)"
                                values=(accnumber,acc_name,amt,today,b)
                                mycursor.execute(query,values)
                                con.commit()
                                print("Amount debited successfully")
                            else:
                                print("Their is no suffiecnt amount to withdraw")
                                print("your account consist of amount is:",res[0])
                        elif ch1=='4':
                            query="select amount from bank where account_number=%s"
                            mycursor.execute(query,(accnumber,))
                            c=mycursor.fetchone()
                            print("TOTAL AVAILABLE BALANCE IS:",c)
                        elif ch1=='5':
                            break
                        else:
                            print("Enter the correct option")

                                    
                else:
                    print("Incorrect Account number or pin you entered")
                    print('-'*25,'ENTER ACCOUNT NUMBER AGAIN','-'*25)
            elif ch=='1':
                print('-'*20,'GENRATE YOUR PIN HERE','-'*20)
                accnumber=input("Enter the account number:")
                query="select * from bank where account_number=%s"
                mycursor.execute(query,(accnumber,))
                result=mycursor.fetchone()
                if result:
                    while True:
                        a=input("Enter the your new four digit pin:")
                        b=input("Renter your pin:")
                        if a==b:
                            query="update bank set pin_number=%s where account_number=%s"
                            values=(b,accnumber)
                            mycursor.execute(query,values)
                            con.commit()
                            print("Pin genrated successfully")
                            print('-'*25,'THANK YOU','-'*25)
                            print("YOU CAN PERFORM OPERATIONS AS EXISIT USER")
                            break
                        else:
                            print("Incorrect pin")
                            print('-'*25,'GENRATE AGAIN','-'*25)
                else:
                    print("Enter the correct number")
            elif ch=='3':
                accnumber=input("Enter the account numbere here to check the details:")
                print('-'*20,'USER DETAILS','-'*20)
                query="select acc_name,account_number,account_type,amount from bank where account_number=%s"
                mycursor.execute(query,(accnumber,))
                res=mycursor.fetchall()
                print("Account Holder Name:",res[0][0])
                print("Account Number:",res[0][1])
                print("Account Type:",res[0][2])
                print("Total Amount:",res[0][3])
                print('-'*131)
            elif ch=='4':
                accnumber=input("enter the account number:")
                query="select * from bank where account_number=%s"
                mycursor.execute(query,(accnumber,))
                res=mycursor.fetchone()
                if res:
                    print("1.10 days statement")
                    print("2.Exit")
                    op=input("Enter the option:")
                    if op=='1':
                        query="select * from transaction_table where account_number=%s and transaction_date<=%s"
                        mycursor.execute(query,(accnumber,today))
                        data=mycursor.fetchall()
                        print(data)
                    if op=='2':
                        break
                else:
                    print("Incorrect account number")
            elif ch=='5':
                break
    elif ch=='3':
        print('-'*55,"THANK YOU VISIT AGAIN",'-'*53)
        break
    else:
        print("Enter the correct option")
'''
##################### BANK MINI PROJECT ###########################



create table useraccount(accountid int,name varchar(20),account_number int,account_type varchar(10),amount float);
alter table useraccount add mobile_number int ;
select * from useraccount;
drop table useraccount;
create table bank(account_number int,name varchar(20),account_type varchar(10),amount float,mobile_number int,alternative_number int,addhar_card_number int,gender varchar(10));
select * from bank;
desc bank;
create table bank(account_number bigint,acc_name varchar(20),account_type varchar(10),amount float,mobile_number bigint,alternative_number bigint,addhar_card_number bigint,gender varchar(10));
select * from bank;
alter table bank add pin_number bigint;
alter table bank drop column pin ;
create table transaction_table (transaction_id int,account_number int,acc_name varchar(20),amount float,transaction_date date);
alter table transaction_table modify column transaction_date datetime;
select * from transaction_table;
alter table transaction_table add constraint primary key(transaction_id);
desc transaction_table;
alter table transaction_table add credite_amount float;
alter table transaction_table add debit_amount float;
alter table transaction_table modify column transaction_date datetime;
select version();
alter table transaction_table modify column account_number varchar(15);
ALTER TABLE transaction_table 
MODIFY COLUMN transaction_date DATETIME,
ALGORITHM=INSTANT;
alter table transaction_table modify transaction_id int auto_increment ;
select * from transaction_table;
select * from bank;
select * from transaction_table;
select * from transaction_table where transaction_date>='2025-07-02' and transaction_date<='2025-07-05';
desc bank;
desc transaction_table;
alter table transaction_table modify column transaction_date date;
'''












            
