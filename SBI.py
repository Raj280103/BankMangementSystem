import mysql.connector as ms
import pickle
con=ms.connect(user='root',host='localhost',passwd='tiger', database='bankdb')

mycursor=con.cursor(buffered=True)

def menu():
    print('*'*120)
    print('STATE BANK OF INDIA'.center(140))
    print('MAIN MENU'.center(140))
    print('1. Insert record/records'.center(140))
    print('2. Display records as per account number'.center(140))
    print('    a.  sorted as per account number'.center(137))
    print('    b.  sorted as per customer number'.center(140))
    print('    c.  sorted as per customer balance'.center(140))
    print('3. Search records details as per the account number'.center(140))
    print('4. Update record'.center(140))
    print('5. Delete record'.center(140))
    print('6. Transactions/debit/withraw/ from the account'.center(140))
    print('    a.  debit/withraw from the account'.center(140))
    print('    b.  credit into the account'.center(140))
    print('7. Exit'.center(140))
    print('*'*120)

def menusort():
    print('    a.  sorted as per account number'.center(140))
    print('    b.  sorted as per customer number'.center(140))
    print('    c.  sorted as per customer balance'.center(140))
    print('    d.  back'.center(140))

def menutransaction():
    print('    a.  debit/withraw from the account'.center(140))
    print('    b.  credit into the account'.center(140))
    print('    c.  back'.center(140))

def create ():
    try:
        mycursor.execute(' create table bank(ACCNO varchar(10) ,NAME varchar(20),MOBILE varchar(10),EMAIL varchar(20),ADDRESS varchar(20),CITY varchar(10),COUNTRY varchar(20), BALANCE float(7,2)')
        mycursor.fetchall()
        print('table created')
        insert()
    except:
        print('table exist')
        insert()

def insert():

               while True:
                   acc=input('enter account no:')
                   name=input('enter name:')
                   mob=input('enter mobile:')
                   email=input('enter email:')
                   add=input('enter address:')
                   city=input('enter city:')
                   country=input('enter country:')
                   bal=float(input('enter balance:'))
                   rec=[acc,name.upper(),mob,email.upper(),add.upper(),city.upper(),country.upper(),bal]
                   cmd='insert into bank values(%s,%s,%s,%s,%s,%s,%s,%s)'
                   mycursor.execute(cmd,rec)
                   con.commit()
                   ch=input('do you want to enter more records:')
                   if ch=='N' or ch=='n':
                       break

def dispsortacc():
    try:
        cmd='select * from bank order by ACCNO'
        mycursor.execute(cmd)
        s=mycursor.fetchall()
        F='%15s,%15s,%15s,%15s,%15s,%15s,%15s,%15s'
        print(F %('ACCNO','NAME','MOBILE','ÉMAIL',' ADDRESS','CITY','COUNTRY','BALANCE'))
        print('='*134)
        for i in s:
            for j in i:
                print('%14s' % j, end=' ')
            print()
        print('='*134)
    except:
        print('table do not exist')

def dispsortname():
    try:
        cmd='select * from bank order by NAME'
        mycursor.execute(cmd)
        s=mycursor.fetchall()
        F='%15s,%15s,%15s,%15s,%15s,%15s,%15s,%15s'
        print(F %('ACCNO','NAME','MOBILE','ÉMAIL','ADDRESS','CITY','COUNTRY','BALANCE'))
        print('='*134)
        for i in s:
            for j in i:
                print('%14s' % j, end=' ')
            print()
        print('='*134)
    except:
        print('table do not exist')

def dispsortbal():
    try:
        cmd='select * from bank order by BALANCE'
        mycursor.execute(cmd)
        s=mycursor.fetchall()
        F='%15s,%15s,%15s,%15s,%15s,%15s,%15s,%15s'
        print(F %('ACCNO','NAME','MOBILE','ÉMAIL','ADDRESS','CITY','COUNTRY','BALANCE'))
        print('='*134)
        for i in s:
            for j in i:
                print('%14s' % j, end='  ')
            print()
        print('='*134)
    except:
        print('table do not exist')

def dispsearchacc():
    try:
        cmd='select * from bank order by accno'
        mycursor.execute(cmd)
        s=mycursor.fetchall()
        ch=input('enter the acountno to be searched:')
        for i in s:
            if i[0]==ch:
                print('='*134)
                F='%15s,%15s,%15s,%15s,%15s,%15s,%15s,%15s'
                print(F %('ACCNO','NAME','MOBILE','ÉMAIL','ADDRESS','CITY','COUNTRY','BALANCE'))
                print('='*134)
        
                for j in i:
                    print('%14s' % j, end='  ')
                print()
                break
        else:
            print('record not found')
    except:
        print('table do not exist')

def update():
    try:
        cmd='select * from bank'
        mycursor.execute(cmd)
        s=mycursor.fetchall()
        A=input('enter accno whose details are to be changed:')
        for i in s:
            i=list(i)
            if i[0]==A:
                ch=input('change name(Y/N)')
                if ch=='y' or ch=='Y':
                    i[1]=input('enter name')
                    i[1]=i[1].upper()

                ch=input('change mobile(Y/N)')
                if ch=='y' or ch=='Y':
                    i[2]=input('enter mobile')

                ch=input('change email(Y/N)')
                if ch=='y' or ch=='Y':
                    i[3]=input('enter email')
                    i[3]=i[3].upper()

                    
                ch=input('change address(Y/N)')
                if ch=='y' or ch=='Y':
                    i[4]=input('enter address')
                    i[4]=i[4].upper()

                ch=input('change city(Y/N)')
                if ch=='y' or ch=='Y':
                    i[5]=input('enter city')
                    i[5]=i[5].upper()

                    

                ch=input('change country(Y/N)')
                if ch=='y' or ch=='Y':
                    i[6]=input('enter country')
                    i[6]=i[6].upper()

                    
                ch=input('change balance(Y/N)')
                if ch=='y' or ch=='Y':
                    i[7]=float(input('enter balance'))
                cmd='update bank set NAME=%s,MOBILE=%s,EMAIL=%s,ADDRESS=%s,CITY=%s,COUNTRY=%s,BALANCE=%s  WHERE ACCNO=%s'
                val=(i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[0])
                mycursor.execute(cmd,val)
                mycursor.fetchall()
                con.commit()
                print('account updated')
                break

        else:
            print('record not found')
    except:
        print('no such table')


def delete():
      try:
          cmd='select * from bank'
          mycursor.execute(cmd)
          A=input('enter accno whose details are to be changed:')
          for i in mycursor:
               i=list(i)
               if i[0]==A:
                   cmd='delete from bank where accno=%s'
                   val=(i[0],)
                   mycursor.execute(cmd,val)
                   con.commit()
                   print('account deleted')
                   break

          else:
            print('record not found')
      except:
          print('no such table')

def debit(): 

                 cmd='select * from bank'
                 mycursor.execute(cmd)
                 #s=mycursor.fetchall()
                 print('money can debited only for min balance of rs 500 exists')
                 acc=input('enter account no from which money is to be debited:')
                 for i in mycursor:
                     i=list(i)
                     if i[0]==acc:
                         amt=float(input('enter the amount to be withdrawn:'))
                         if i[7]-amt>=500:
                             i[7]-=amt
                             cmd='UPDATE BANK SET BALANCE=%s WHERE ACCNO=%s'
                             val=(i[7],i[0])
                             mycursor.execute(cmd,val)
                             con.commit()
                             print('amount debited')
                             break
                         else:
                             print('there must be min balance of rs 500')
                             break
                 else:
                     print('record not found')


def credit():
        try:
                    cmd='select * from bank'
                    mycursor.execute(cmd)
                    #s=mycursor.fetchall()
                    acc=input('enter account number:')
                    for i in mycursor:
                        i=list(i)
                        if i[0]==acc:
                            amt=float(input('enter amt to be credited'))
                            i[7]+=amt
                            cmd='UPDATE BANK SET BALANCE=%s WHERE ACCNO=%s'
                            val=(i[7],i[0])
                            mycursor.execute(cmd,val)
                            #mycursor.fetchall()
                            con.commit()
                            print('amount credited')
                            break

                    else:
                        print('record not found')

        except:
                 print('table do not exist')

while True:
    menu()
    ch=input('énter your choice:')
    if ch=='1':
        create()
    elif ch=='2':
        while True:
            menusort()
            ch1=input('enter choice a/b/c/d:')
            if ch1 in ['a','A']:
                dispsortacc()
            elif ch1 in ['b','B']:
                dispsortname()
            elif ch1 in ['c','C']:
                dispsortbal()
            elif ch1 in ['d','D']:
                print('back to the main menu')
                break
            else:
                print('invalid choice')
    elif ch=='3':
        dispsearchacc()
    elif ch=='4':
        update()
    elif ch=='5':
        delete()
    elif ch=='6':
        while True:
            menutransaction()
            ch1=input('enter choice a/b/c:')
            if ch1 in ['a','A']:
                debit()
            elif ch1 in ['b','B']:
                credit()
            elif ch1 in ['c','C']:
                print('back to main menu')
                break
            else:
                print('invalid choice')
    elif ch=='7':
        print('existing.....')
        print('thankyou visit again')
        break
    else:
        print('wrong choice entered')
         


    
                        


                    
        
            
            

                    


                    


 
