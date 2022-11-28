from Account import Account
from Customer import Customer
from Bank import Bank

def main():
    b1 = Bank("CIMB NIAGA")
    b1.addCustomer("Shaan", "Gunwani")
    b1.addCustomer("Shaima", "Zebian")
    b1.addCustomer("Kishore", "Kumar")
    print(b1.getNumOfCust())

    b1.getCustomer(0).setAccount(Account(500000))
    b1.getCustomer(1).setAccount(Account(500000))
    b1.getCustomer(2).setAccount(Account(500000))
    print(b1.getCustomer(2).getAccount().getBalance())

    if b1.getCustomer(2).getAccount().deposit(1000000):
        print(b1.getCustomer(2).getAccount().getBalance())
    else:
        print("IT IS WRONG!!")

    info = eval(input("HELLO, PLEASE ENTER YOUR ACCOUNT NUMBER:- "))
    print('WELCOME TO THE CIMB NIAGA BANK, ', b1.getCustomer(info).getFirstName(), b1.getCustomer(info).getLastName(), ',')

    print('PLEASE ENTER A NUMBER ACCORDINGLY:')
    action = eval(input(('\n1. ACCOUNT INFORMATION \n2. MAKE A NEW ACCOUNT \n3. DEPOSIT MONEY FROM YOUR ACCOUNT \n4. WITHDRAW MONEY TO YOUR ACCOUNT\n')))

    if action == 1:
        print('\nACCOUNT INFORMATION:\n\n\nYOUR ACCOUNT NUMBER IS=', info, '\n\nYOUR ACCOUNT NAME IS =',
              b1.getCustomer(info).getFirstName(), b1.getCustomer(info).getLastName(), '\n\n')

    elif action == 2:

        print("    MAKE A NEW ACCOUNT    \n")
        fn = input('\n\n PLEASE ENTER YOUR FIRST NAME:\n\n')
        ln = input('\n\n PLEASE ENTER YOUR LAST NAME\: \n\n')
        NewAccNo = b1.getNumOfCust()

        b1.addCustomer(fn, ln)
        depositAmount = eval(input('\n\nPLEASE ENTER THE DEPOSIT AMOUNT (THE MINIMUM AMOUNT TO DEPOSIT IS 1000)\n\n'))

        if depositAmount in (range(1000)):
            print("THE AMOUNT YOU WANT TO DEPOSIT IS VERY LOW! YOU CAN'T DEPOSIT LESSER THAN 1000!!\n")
            exit()

        else:
            print("\n AMOUNT TO DEPOSIT :- ", depositAmount)

        b1.getCustomer(NewAccNo).setAccount(Account(depositAmount))
        print("\n\nPLEASE ENTER YOUR FULL NAME FOR YOUR NEW ACCOUNT: \n", fn, ln, "\n\n PLEASE ENTER YOUR NEW ACCOUNT NUMBER: \n\n",
              b1.getNumOfCust(), "\n\n THANK YOU VERY MUCH!!", fn, ln, '!\n\n')
        print('YOUR BALANCE IS:\n', b1.getCustomer(NewAccNo).getAccount().getBalance(), '\n\n')

    elif action == 3:
        print("    DEPOSIT MONEY   \n\n")
        SecondWithdrawAmt = eval(input("YOUR DEPOSIT AMOUNT IS :-\n"))
        b1.getCustomer(info).getAccount().deposit(SecondWithdrawAmt)
        print("\nCONGRATULATIONS!! YOUR DEPOSIT WAS SUCCESFULL  :", b1.getCustomer(info).getAccount().getBalance(), "\n\n")


    elif action == 4:
        print("\n    WITHDRAW MONEY FROM YOUR ACCOUNT   \n\n")
        WithdrawAmt = eval(input("WITHDRAWAL AMOUNT IS:- \n"))
        b1.getCustomer(info).getAccount().withdraw(WithdrawAmt)
        print("\nCONGRATULATIONS! YOUR WITHDRAW IS SUCCESSFULL!! YOUR BALANCE NOW IN YOUR BANK ACCOUNT IS:", b1.getCustomer(info).getAccount().getBalance(), "\n\n")
    else:
            print('OOPS!! YOU DID SOMETHING WRONG!!')

if __name__=="__main__":
    main()
    
