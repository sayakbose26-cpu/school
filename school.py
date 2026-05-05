import mysql.connector as msql
mycon=msql.connect(host="localhost",user="root",passwd="",database="sayak")
def entrystud():
    cursor=mycon.cursor()
    n=int(input("enter how many entries\t"))
    for i in range(n):
        a=int(input("enter roll:\t"))
        b=input("enter the name:")
        c=int(input("enter the marks:"))
        t="insert into stud(roll,name,marks) values('{}','{}','{}')".format(a,b,c)
        cursor.execute(t)
        mycon.commit()
    print("------------------------------------------------------------")
    print("entry complete")
    print("---------------------------------------------------------------")
def updatestud():
    cursor=mycon.cursor()
    m=int(input("enter which roll is to be updates:\t"))
    n=int(input("enter new marks:\t"))
    st="update stud set marks={} where roll={}".format(n,m)
    cursor.execute(st)
    mycon.commit()
    print("------------------------------------------------------------")
    print("complete")
    print("------------------------------------------------")
def check():
    cursor=mycon.cursor()
    m=int(input("enter the roll you want to check:\t"))
    t="select * from stud where roll={}".format(m)
    cursor.execute(t)
    d=cursor.fetchone()
    print(d)
    print("------------------------------------------------------------")
    print("complete")
    print("-------------------------------------------------")
def entrytech():
    cursor=mycon.cursor()
    p=int(input("enter how many entries:\t"))
    for k in range(p):
        a=input("enter the teacher name:\t")
        b=int(input("enter the teacher id:\t"))
        c=input("enter the subject:\t")
        t="insert into techer(name,id,subject) values('{}','{}','{}')".format(a,b,c)
        cursor.execute(t)
        mycon.commit()
    print("------------------------------------------------------------")
    print("entry complete")
    print("-----------------------------------------------------")
def updatetech():
    cursor=mycon.cursor()
    j=int(input("enter the teacher id:\t"))
    y=input("enter the subject:\t")
    t="update techer set subject={],where id={}"
    cursor.execute(t)
    mycon.commit()
    print("------------------------------------------------------------")
    print("completed")
    print("------------------------------------------------------------")
print("-------------------------------------")
print("welcome to student management system")
print("-------------------------------------")
print("your options:")
print("1.student")
print("2.techer")
x=int(input("enter the choice:\t"))
if(x==1):
    print("1.entry")
    print("2.update")
    print("3.check")
    z=int(input("enter the choice:\t"))
    if(z==1):
        entrystud()
    elif(z==2):
        updatestud()
    elif(z==3):
        check()
elif(x==2):
    print("1.entry")
    print("2.update")
    q=int(input("enter the choice:\t"))
    if(q==1):
        entrytech()
    elif(q==2):
        updatetech()
else:
    print("wrong")
        
    
