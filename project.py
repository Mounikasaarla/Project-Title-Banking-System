import datetime
class Sbi:
    bank_name="SBI"
    bank_loc="Chaitanyapuri"
    ifsc_code="Sbi00123"
    bank_manager="rahul"
    pin_code=500060
    no_of_customers=0
    customer_details={}
    transaction_details={}
    def __init__(self,name,phone,age,adhaar,address,balance,pin):
        self.name=name
        self.phone=self.validate_phone(phone)
        self.age= self.validate_age(age)
        self.adhaar=self.validate_adhaar(adhaar)
        self.address=address
        self.balance=balance
        self.pin=self.validate_pin(pin)

        self.increment_account_num()
        acc_num=1000+self.no_of_customers

        self.store_customer_data(acc_num,self)


    @classmethod
    def increment_account_num(cls):
        cls.no_of_customers+=1
    @classmethod
    def store_customer_data(cls,acc_num_data,customer_data):
        cls.customer_details[acc_num_data]=customer_data
    @staticmethod
    def validate_phone(mobile_num):
        if len(str(mobile_num))==10 and str(mobile_num).isdigit():
            return mobile_num
        else:
            raise Exception ("ENTER VALID NUMBER")
    @staticmethod
    def validate_adhaar(adhaar_num):
        if len(str(adhaar_num))==12 and str(adhaar_num).isdigit():
            return adhaar_num
        else:
            raise Exception("ENTER VALID ADHAAR NUMBER")
    @staticmethod
    def validate_age(age_num):
        if age_num>=18 :
            return age_num
        else:
            raise Exception("YOUR NOT ELIGIBLE TO CREATE A ACCOUNT")
    @staticmethod
    def validate_pin(pin_num):
        if len(str(pin_num))==4 and str(pin_num).isdigit():
            return pin_num
        else:
            raise Exception(" ENTER VALID PIN")
    @classmethod
    def check_balnce(cls):
        print("\n ........BALANCE PAGE.......\n")
        user_acc_num=int(input("ENTER YOUR ACC NUMBER : "))
        user_pin=int(input("ENTER YOUR PIN NUMBER : "))
        if user_acc_num in cls.customer_details and user_pin==cls.customer_details[user_acc_num].pin:
            print(f"The Current balance is: {cls.customer_details[user_acc_num].balance}")
        elif user_acc_num in cls.customer_details and user_pin!=cls.customer_details[user_acc_num].pin:
            print("INVALID PIN NUMBER")
        else:
            print("INVALID USER")
    @classmethod
    def deposite(cls,count=0):
        if count==3:
            print("attemps are over")
            return
        print("\n ........DEPOSITE PAGE.......\n")
        user_acc_num = int(input("ENTER YOUR ACC NUMBER : "))
        user_pin = int(input("ENTER YOUR PIN NUMBER : "))
        if user_acc_num in cls.customer_details and user_pin == cls.customer_details[user_acc_num].pin:
            amount=int(input("Enter the amount to deposite: "))
            if amount>0:
                cls.customer_details[user_acc_num].balance+=amount
                print(f"RS.{amount} has been credited to your account and your current balance is: {cls.customer_details[user_acc_num].balance} ")
                if user_acc_num not in cls.transaction_details:
                    cls.transaction_details[user_acc_num]=[{"DATE_TIME":datetime.datetime.now(),"TYPE":"CREADITED","AMOUNT":amount,"BALANCE":cls.customer_details[user_acc_num].balance}]
                else:
                    cls.transaction_details[user_acc_num]+=[{"DATE_TIME":datetime.datetime.now(),"TYPE":"CREADITED","AMOUNT":amount,"BALANCE":cls.customer_details[user_acc_num].balance}]

            else:
                print("ENTER VALID AMOUNT")
        elif user_acc_num in cls.customer_details and user_pin!=cls.customer_details[user_acc_num].pin:
            print("INVALID PIN NUMBER")
        else:
            print("INVALID USER")
            cls.deposite(count+1)
    @classmethod
    def withdraw(cls):
        print("\n ........WITHDRAW PAGE.......\n")
        user_acc_num = int(input("ENTER YOUR ACC NUMBER : "))
        user_pin = int(input("ENTER YOUR PIN NUMBER : "))
        if user_acc_num in cls.customer_details and user_pin == cls.customer_details[user_acc_num].pin:
            amount = int(input("Enter the amount to withdraw: "))
            if amount<=cls.customer_details[user_acc_num].balance and amount>0:
                cls.customer_details[user_acc_num].balance-=amount
                print(f"RS.{amount} has been debited to your account and your current balance is: {cls.customer_details[user_acc_num].balance}")
                if user_acc_num not in cls.transaction_details:
                    cls.transaction_details[user_acc_num]=[{"DATE_TIME":datetime.datetime.now(),"TYPE":"DEBITED","AMOUNT":amount,"BALANCE":cls.customer_details[user_acc_num].balance}]
                else:
                    cls.transaction_details[user_acc_num]+=[{"DATE_TIME":datetime.datetime.now(),"TYPE":"DEBITED","AMOUNT":amount,"BALANCE":cls.customer_details[user_acc_num].balance}]
            else:
                print("INSUFFICIENT BALANCE")
        elif user_acc_num in cls.customer_details and user_pin!=cls.customer_details[user_acc_num].pin:
            print("INVALID PIN NUMBER")
        else:
            print("INVALID USER")
    @classmethod
    def change_pin(cls):
        print("\n ........CHANGE PIN.......\n")
        user_acc_num = int(input("ENTER YOUR ACC NUMBER : "))
        user_pin = int(input("ENTER YOUR PIN NUMBER : "))
        if user_acc_num in cls.customer_details and user_pin == cls.customer_details[user_acc_num].pin:
            new_pin=int(input("ENTER NEW PIN : "))
            confirm_pin=int(input("CONFIRM THE NEW PIN : "))
            if new_pin==user_pin:
                print("you already used this pin")
            elif new_pin==confirm_pin:
                cls.validate_pin(new_pin)
                cls.customer_details[user_acc_num].pin=new_pin
                print("New pin has been updated succefully ****")
            else:
                print("new pin and confirm pin not matched")
        elif user_acc_num in cls.customer_details and user_pin != cls.customer_details[user_acc_num].pin:
            print("INVALID PIN NUMBER")
        else:
            print("INVALID USER")
    @classmethod
    def modify_customer_details(cls):
        print("\n ........MODIFY PAGE.......\n")
        user_acc_num = int(input("ENTER YOUR ACC NUMBER : "))
        user_pin = int(input("ENTER YOUR PIN NUMBER : "))
        if user_acc_num in cls.customer_details and user_pin == cls.customer_details[user_acc_num].pin:
            while True:
                print("\nSELECT 1 TO CHANGE THE NAME","SELECT 2 TO CHANGE THE ADDRESS","SELECT 3 TO CHANGE THE MOBILE NUM","SELECT 4 FOR EXIT\n",sep="\n")
                select=int(input("ENTER A NUMBER TO CHANGE DETAILS:"))
                match select:
                    case 1:
                        print("\n..........MODIFY NAME..............")
                        new_name=input("ENTER YOUR NEW NAME: ")
                        confirm_name=input("CONFIRM YOUR NEW NAME: ")
                        if new_name==confirm_name:
                            cls.customer_details[user_acc_num].name=new_name
                            print("your name  changed successfully")
                        else:
                            print("your new name and confirm name are not matching")
                    case 2:
                        print("\n..........MODIFY ADDRESS..............")
                        new_address = input("ENTER YOUR NEW ADDRESS: ")
                        confirm_address = input("CONFIRM YOUR NEW ADDRESS: ")
                        if new_address==confirm_address:
                            cls.customer_details[user_acc_num].address=new_address
                            print("your address  changed successfully")
                        else:
                            print(" your new address and confirm address are not matching")
                    case 3:
                        print("\n..........MODIFY MOBILE NUMBER..............")
                        new_mobile_num = input("ENTER YOUR NEW MOBILENUM: ")
                        confirm_mobile_num = input("CONFIRM YOUR NEW MOBILENUM: ")
                        if new_mobile_num == confirm_mobile_num:
                            cls.validate_phone(new_mobile_num)
                            cls.customer_details[user_acc_num].phone = new_mobile_num
                            print("your mobile number  changed successfully")
                        else:
                            print(" your new mobile number and confirm mobile number are not matching")
                    case 4:
                        print("\n.......... EXIT..............")
                        print("you have done with modification thank you")
                        break
                    case _:
                        print(" boss there are only 1 2 3 4 options select in between them ")
        elif user_acc_num in cls.customer_details and user_pin != cls.customer_details[user_acc_num].pin:
            print("INVALID PIN NUMBER")
        else:
            print("INVALID USER")
    @classmethod
    def transfer_money(cls):
        print(f".............TRANSFER MONEY PAGE........")
        sender_acc_num=int(input("ENTER YOUR ACC NUMBER: "))
        sender_pin_num=int(input("ENTER YOUR PIN NUMBER: "))
        if sender_acc_num in cls.customer_details and sender_pin_num==cls.customer_details[sender_acc_num].pin:
            receiver_acc_num=int(input("ENTER RECEIVER ACC NUMBER:"))
            receiver_ifsc=input("ENTER RECEIVER IFSC CODE:")
            if receiver_acc_num in cls.customer_details and receiver_ifsc==cls.ifsc_code:
                amount=int(input("ENTER THE AMOUNT TO TRANSFER: "))
                if amount<=cls.customer_details[sender_acc_num].balance:
                    cls.customer_details[sender_acc_num].balance-=amount
                    cls.customer_details[receiver_acc_num].balance+=amount
                    print(f"RS:{amount} transferd successfully")

                    # print("after")
                    # print(cls.customer_details[sender_acc_num].balance)
                    # print(cls.customer_details[receiver_acc_num].balance)

                else:
                    print("INSUFFICENT AMOUNT")
            else:
                print("RECEIVER NOT FOUND")
        elif sender_acc_num in cls.customer_details and sender_pin_num != cls.customer_details[sender_acc_num].pin:
            print("INVALID PIN NUMBER")
        else:
            print("INVALID USER")
    @classmethod
    def mini_statement(cls):
        print("................MINI STATEMENT.........")
        user_acc_num = int(input("ENTER YOUR ACC NUMBER : "))
        user_pin = int(input("ENTER YOUR PIN NUMBER : "))
        if user_acc_num in cls.customer_details and user_pin == cls.customer_details[user_acc_num].pin:
            print("DATE_TIME".ljust(35),"TYPE".center(30),"AMOUNT".center(20),"BALANCE".center(10),sep="|")
            transaction_history=cls.transaction_details[user_acc_num]
            for d in transaction_history:
                print(str(d["DATE_TIME"]).ljust(35),d["TYPE"].center(30),str(d["AMOUNT"]).center(20),str(d["BALANCE"]).center(10),sep="|")





c1=Sbi("raju",9876543210,25,987676554444,"55/2 kothapet",1000,8888)
c2=Sbi("sandhya",8765432190,21,123456789012,"haythnagar",1500,7777)
print(c1.customer_details)
print(c2.customer_details)
c1.check_balnce()
c1.deposite()
c1.withdraw()
c1.change_pin()
c1.modify_customer_details()
c1.transfer_money()
c1.deposite()
c1.deposite()
print(Sbi.transaction_details)
c1.withdraw()
c1.withdraw()
print(Sbi.transaction_details)
c1.deposite()
c1.withdraw()
c1.mini_statement()

