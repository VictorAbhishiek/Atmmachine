print("welcome to state bank of india ATM")
restart=('Y')
chance=3
balance=1000
while chance>=0:
     pin=int(input("enter 4 digit pin number "))
     if (pin==1234):
         print("you entered your pin currectly\n")
         while restart not in ('n','NO','no','N'):
             print("please press 1 for bank balance:\n ")
             print("please press 2 for money withdrawl:\n ")
             print("please press 3 to pay in:\n ")
             print("please press 4 to return card:\n ")
             option=int(input("please select your option" ))
             if option == 1:
                 print("your balance is",balance,"\n")
                 restart = input("would you like to go back?")
                 if restart in('n','NO','no','N'):
                     print("thank you")
                     break
             elif option == 2:
                 option2=('y')
                 withdrawl=float(input("how much would you like to withdraw: "))
                 if withdrawl in[10,20,30,40,50,60,70,80,90,100]:
                     balance=balance-withdrawl
                     print('\nYour balance is now',balance)
                     restart = input("would you like to go back? ")
                     if restart in ('n','no','NO','N'):
                         print("thank you")
                         break
                 elif withdrwal !=[10,20,30,40,50,60,70,80,90,100]: 
                    print("invalid amount, please re-enter\n")
                    restart=('y') 
                 elif withdrawl == 1:
                    withdrawl=float(input("please enter desired amount: "))

                 elif option == 3:
                    pay_in= float(input("how much would you like to pay: "))
                    balance =balance+pay_in
                    print("\nYour balance is now", balane)
                    restart=input("would you like to go back: ")
                    if restart in ('n','no','NO','N'):
                        print("thank you")
                        break
                 elif option == 4:
                    print("please wait your card is returned....\n")
                    print("thank you visit again")
                    break
                 else:
                    print("please enter a correct number.\n")
                    restart =('y')
     elif pin !=('1234'):
         print("incorrect pin ")
         chance = chance-1
         if chance==0:
             print('\n No more tries')
         break 