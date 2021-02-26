class bank_ac:
    def __init__(self,name,ac_no,ac_type,ac_balance):
        self.name=name
        self.ac_no=ac_no
        self.ac_type=ac_type
        self.ac_balance=ac_balance
    def depo_amount(self,amount):
        self.amount=amount
        self.ac_balance+=self.amount
    def withdraw(self,amount_):
        self.amount_=amount_
        if self.amount_<=self.ac_balance:
            self.ac_balance-=self.amount_
        else:
            print("you don't have enough money in your account")
    def disp(self):
        print("NAME:",self.name)
        print("AC.NO:",self.ac_no)
        print("AC TYPE:",self.ac_type)
        print("AC BALANCE:",self.ac_balance)
        
name=input("enter the name")
ac_no=int(input("enter your account number"))
ac_type=input("enter account type")
ac_bal=int(input("enter initial balance"))
ac=bank_ac(name,ac_no,ac_type,ac_bal)
c=0
while c!=4:
    c=int(input("enter your choice 1.deposit , 2.display , 3.withdraw , 4.exit"))
    if c==1:
        amount=int(input("enter the amount to deposit"))
        ac.depo_amount(amount)
    elif c==2:
        ac.disp()
    elif c==3:
        amount_=int(input("enter the amount to withdraw"))
        ac.withdraw(amount_)
    elif c==4:
        print("exit")
        
        
        
