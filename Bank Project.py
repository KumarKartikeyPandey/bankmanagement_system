import random
#BankAccount class


#Function to deposite amount
def deposit(self):
    amount=float(input("Enter amount to be deposited:"))
    self.balance+=amount
    print("\n Amount Deposited:", amount)


#Funtion to withdraw the amount
    def withdraw(self):
        amount=float(input("Enter amount to be withdraw:"))
    if self.balance>=amount:
        self.balance-=amount
        print("\n You Withdrew:", amount)
    else:
        print("\n Insufficient balance:")


#Function to display amount
def display(self):
    print("\n Net Available Balance=", self.balance)


#Python program to create Bankaccount class
#with both a deposit() and a withdraw() function
class Bank_Account:
    def __init__ (self):
        self.balance=0
        print("Hello!!! Welcome to the Deposit & Withdraw ")
        return
    def deposit(self):
        amount=float(input("Enter amount to be Deposited:"))
        self.balance+=amount
  


#_____MAIN PROGRAM_____
print("\t\t\t\t\t\t\t-----------------")
print("\t\t\t\t\t\t\t*****************")
print("\t\t\t\t\t\t\t   WELCOME TO    ")
print("\t\t\t\t\t\t\t*****************")
print("\t\t\t\t\t\t\t----------------")
print("\t\t\t\t\t$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
print("\t\t\t\t\t\t     KARTIKEY RESERVE BANK       ")
print("\t\t\t\t\t$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
name=["Kumar Kartikey Pandey", "Keshav Kumar Pandey", "Reena Pandey", "Punit Mishra", "Pawan Kumar Mishra", "Pooja Mishra", "Praniti Pandey", "Shreel Mishra", "Pranshu", "Ujjawal", "Ram", "Shyam", "Laxman", "Bharat", "Ravi", "Rajesh", "Rajendra"]
account_number=100
print("Please enter the following details to proceed:-")
Name=input("Enter User's Name:")
while Name in name:
    print("User's Name Verified")
    break
while Name not in name:
    print("!!!User Name Not Verified!!!")
    break
while Name in name:
    Account_Number=int(input("Enter your Account Number:"))
    break
while Name not in name:
    break
if Name not in name:
    print("1. Want to become our member")
    print("2. Want to leave")
    ch=int(input("Enter your choice (1 or 2)"))
while ch == 2:
    print("Thanks For Giving Us A Chance to Serve for You. We will Love to Serve Service For You Again. You are Heartly Welcomed.")
    break
while ch == 1:
    print("Please Enter Following Details To proceed")
    NAME=input("Enter Your Name:")
    D_O_B=input("Enter Your Date Of Birth:")
    Age=int(input("Enter Your Age:"))
    Address=input("Enter your Permanenet Address:")
    Source=input("Enter the source from where you get  to know about our bank:")
    Addhar_Number=int(input("Enter Your Addhar Number:"))
    Introducer=input("Enter the Introducer's Name:")
    Introducers_Account=int(input("Enter the Introducer's account Number:"))
    Nominee=input("Enter the name of user of your Account in your absence:")
    Occupation=input("Enter Your Occupation:")
    Email=input("Enter Your Emai-id:")
    Contact_Number=int(input("Enter Your 10 Digit Valid Contact Number:"))
    Account_Opening_Date=input("Enter date of opening of account:") 
    Signature=input("Enter Your Valid and Authorised Signature:")
    fileout=open("Name","a")
    for i in range (1):
        Name=NAME
        
        Account_Type=input("Enter the type of your account:")
        
        rec=Name+","+Account_Type+'\n'
        fileout.write(rec)
    fileout.close()
    break
while ch == 1:
    print("\nBefore Starting Operations on Your Account Please Read the Folowing Details Carefully.")

    print("\n1. All the information provided by you will remain confedential and will be used by our authorities as per the necessity.")

    print("\n2. Appropriate documents must be produced at the time of identifcation.")

    print("\n3. Account holder should check the last balance/transactions to ensure their accuracy.")

    print("\n4. If the account remains unfunctional for two years, then it will become inoperative/dormant.")

    print("\n5. Please ignore emails that ask for your bank account details.")

    print("\n6. Please do not part with internet banking account's used-ID, password, OTP, ATM pin, etc.")
    break
while ch == 1:  
    AccountNumber=random.randint(12345678911125,98765432156745)
    print("Your Account Number is",AccountNumber)
    break
while ch == 1:
    print("Welcome Dear", Name, "Now you are ready to use your account")
    print("Choose the operations from the given list to use facilities for your account")
    initial_Balance=0.00
    break
while ch == 1:
    print("\t\t\t\t\t\t\t$$$$$$$$$$$$$")
    print("\t\t\t\t\t\t\t-------------")
    print("\t\t\t\t\t\t\t    MENU     ")
    print("\t\t\t\t\t\t\t-------------")
    print("\t\t\t\t\t\t\t$$$$$$$$$$$$$")

    print("\n\t\t\t1. Deposit money in my account.")

    print("\n\t\t\t2. Withdraw money from my account.")

    print("\n\t\t\t3. Trasfer money from my account.")

    print("\n\t\t\t4. Check my current balance.")

    print("\n\t\t\t5. Want to invest money in our schemes.")

    print("\n\t\t\t6. Want to get a loan.")

    print("\n\t\t\t7. Want to edit my details.")

    print("\n\t\t\t8. Want to close my account")

    print("\n\t\t\t9. Want to apply for a cheque book")

    print("\n\t\t\t10. Want to apply for a ATM/Debit card.")

    print("\n\t\t\t11. Display the list of members of the bank.")

    print("\n\t\t\t12. Display the details of members of the bank.")

    print("\n\t\t\t13. Exit")

    opt=int(input("Enter the option you want to activate for your account:"))

    while opt == 13:
        print("\n\n\t\t\t\t\t\t\t$$$$$$$THANK YOU VERY MUCH FOR VISITING OUR BANK$$$$$$$")
        break
        
    if opt == 1:
        Amount=float(input("\nEnter the amount you want to deposit in your account:"))
        Date_of_Deposit=input("\nEnter the date of deposition:")
        sign=input("\nEnter your signature:")
        if sign == Signature:
            balance=initial_Balance+Amount
            print("\nAn amount of",Amount,"INR is susseccfully deposited in your account",AccountNumber, "on" ,Date_of_Deposit)


    if opt == 2:
        Amount=float(input("\nEnter the amount you want to withdraw from your account:"))
        Date_of_withdrawl=input("\nEnter the date of Withdrawl:")
        sign=input("\nEnter your signature recognized by our authorities.")
        if sign == Signature:
            withdrew == balance-Amount
            print("\nAn amount of ",Amount,"INR is succcessfully withdrawn from your account",AccountNumber, "on" ,Date_of_withdrawl)


    if opt == 3:
        Acc=int(input("\nEnter the account number of account to which money is to be transfered."))
        Name_Of_Account_Holder=input("\nEnter the Name of the Account Holder:")
        Bank=input("\nEnter the name/branch of the bank in which account exixts:")
        Amount=float(input("\nEnter the amount to be transfered:"))
        Date=input("\nEnter the date of transfer:")
        sign=input("\nEnter your signature recognized by our authorities.")
        if sign == Signature:
            print("\nAn amount of",Amount,"INR is successfuly transfered from your account",AccountNumber,"to account",Acc,"belonging to",Name_Of_Account_Holder,"Of Bank/Branch",Bank,"on" ,Date)


    if opt == 4:
        print("\nCurrently your account",AccountNumber,"has",withdrew,"INR")


    if opt == 5:
        print("\nInvestment of your capital in any of our scheme of your choice will be entirely on your risk") 
        print("\n\t\t1. Scheme-1:- Property Scheme")
        print("\n\t\t2. Scheme-2:- Insurance Scheme")
        
        sch=int(input("\nEnter the scheme of your choice (1 or 2):-"))

        if sch == 1:
              print("\nConditions of the Scheme are:-")
              print("\n1. Minimum investment capital is 5 lac INR.")
              print("\n2. Your capital will be invested for  5 years.")
              print("\n3.Final returning capital of scheme will entirely depend on value of property at that time.")
              print("\nProperties are available in Varanasi, Delhi, Mumbai, Kolkata, Chennai, Surat, Ahemdabad, Jaipur, Chandigarh, Pune, Bangalore, Hyedrabad, Gwalior, Indore, London, New York City, Washington D.C., Spain, Brazil, Germany, Sydney")
              Property=input("\nSelect the place of your choice:")
              Capital=float(input("\nEnter the amount you want to invest:"))
              sign=input("\nEnter your signature recognized by our authorities.")
              if sign == Signature:
                  print("\nThank You for investing in our scheme, your",Capital,"INR has been successfully invested in",Property,"for 5 years")

        if sch == 2:
              print("\nConditions of the Scheme are:-")
              print("\n1. Insurance money will only be given to you or your nominee.")
              print("\nWhich type of insurance you want")
              print("\n1. Propery Insurance.")
              print("\n2. Life Insurance.")
              print("\n3. Vehicle Insurance.")
              Ins=int(input("\nEnter which type of insurance you want:"))

              if Ins == 1:
                  print("\nPlease enter the following details:")
                  size=float(input("\nEnter the size of the property:"))
                  Location=input("\nEnter the location of the property:")
                  Owner=input("\nEnter the name of the owner the property:")
                  sign=input("\nEnter your signature recognized by our authorities.")
                  if sign == Signature:
                      print("\nProperty Insurance Scheme is successfully activated for the property of",Owner,"at ",Location)

              if Ins == 2:
                  print("\nPlease enter the following details:")
                  Owner=input("\nEnter the name of holder of insurance:")
                  age=int(input("\nEnter the age of insurance holder:"))
                  sign=input("\nEnter your signature recognized by our authorities.")
                  if sign == Signature:
                      print("\nLife Insurance Scheme is successfully activated for the life of",Owner,"of age",age,"years")

              if Ins == 3:
                    print("\nPlease enter the following details:")
                    category=input("\nEnter the category of the vehicle:")
                    Model=input("\nEnter the name and model of the vehicle:")
                    Owner=input("\nEnter the name of the owner the vehicle:")
                    sign=input("\nEnter your signature recognized by our authorities.")
                    if sign == Signature:
                        print("\nVehicle Insurance Scheme is successfully activated for the vehicle" ,Model, "of" ,Owner)


    if opt == 6:
        print("\nLoan will be sanctioned at the rate of 12% per annum")
        R=12
        Loan=float(input("\nEnter the amount for loan desired:"))
        time=int(input("\nEnter the time for which loan is require:"))
        sign=input("\nEnter your signature recognized by our authorities.")
        
        if sign == Signature:
            print("\nLoan has been approved successfully and you have to return it our bank after the completion of" ,time)


    if opt == 7:
        NAME=input("Enter Your Name:")
        D_O_B=input("Enter Your Date Of Birth:")
        Age=int(input("Enter Your Age:"))
        Address=input("Enter your Permanenet Address:")
        Source=input("Enter the source from where you get  to know about our bank:")
        Addhar_Number=int(input("Enter Your Addhar Number:"))
        Introducer=input("Enter the Introducer's Name:")
        Introducers_Account=int(input("Enter the Introducer's account Number:"))
        Nominee=input("Enter the name of user of your Account in your absence:")
        Occupation=input("Enter Your Occupation:")
        Email=input("Enter Your Emai-id:")
        Contact_Number=int(input("Enter Your 10 Digit Valid Contact Number:"))
        Account_Opening_Date=input("Enter date of opening of account:") 
        Sign=input("Enter Your Valid and Authorised Signature:")
        if Sign == Signature:
            print("\nYour deails has been updated successfully.")


    if opt == 8:
        Acc_No=int(input("\nEnter your account number:"))
        print("\nPlease confirm your signature for closure of your account.")
        Sign=input("\nEnter your recognized signature:")
        if Sign == signature:
            print("\nYour account" ,Acc_No, "has been closed successfully and all your details will remain safe with or authorities and will be only used with your permision.")
            


    if opt == 9:
        Acc_No=int(input("\nEnter your account number:"))
        Address=input("\nEnter your Permanenet Address:")
        Contact_Number=int(input("\nEnter Your 10 Digit Valid Contact Number:"))
        sign=input("\nEnter your signature recognized by our authorities.")
        if sign == Signature:
            print("\nThanks for providing us required details, your cheque book will be posted soon to your address for account" ,Acc_No)


    if opt == 10:
        print("\nPlease fill up following details for issuing your ATM/Debit card.")
        NAME=input("\nEnter Your Name:")
        D_O_B=input("\nEnter Your Date Of Birth:")
        Occupation=input("\nEnter Your Occupation:")
        Address=input("\nEnter your Permanenet Address:")
        Salary=float(input("\nEnter your annual income:"))
        Email=input("\nEnter Your Emai-id:")
        Contact_Number=int(input("\nEnter Your 10 Digit Valid Contact Number:"))
        Signature=input("\nEnter Your Valid and Authorised Signature:")
        if sign == Signature:
            if Salary >= 50000:
                print("\nThank You for providing us details we will soon issue an ATM/Debit card for you.")
            else:
                print("\nSORRY, regarding your salary we can not provide you an/a ATM/Debit card.")

    if opt == 11:
        fileinp=open("Name","r")
        while str:
            str=fileinp.readline()
            print(str)
        fileinp.close()

    if opt == 12:
        fileinp=open("Name","r")
        while str:
            str=fileinp.readline()
            print(str)
        fileinp.close()
    


    


    
    
                                                          
            

