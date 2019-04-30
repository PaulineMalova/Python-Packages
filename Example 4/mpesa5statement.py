from datetime import datetime

class Mpesa_Account:
	def __init__(self,name,phone_number):
		self.name=name
		self.phone_number=phone_number
		self.balance=0
		self.deposits = []
		self.withdrawals = []
		self.loan = 0
		self.loans = []
		self.loanspaid = []

	def deposit(self,amount):
		now=datetime.now()
		object={"time":now,"amount":amount}
		self.deposits.append(object)
		self.balance = self.balance+amount
		print("Dear {}, you have deposited Ksh{}. Your new balance is Ksh{}.".format(self.name,amount,self.balance))

	def withdraw(self,amount):
		if amount<self.balance:
			now=datetime.now()
			object={"time":now,"amount":amount}
			self.withdrawals.append(object)
			self.balance = self.balance-amount
			print ("Dear {}, you have withdrawn Ksh{}. Your new balance is Ksh{}.".format(self.name,amount,self.balance))
		else:
			print("Sorry {}, you do not have enough funds to facilitate your withdrawal. Your current balance is Ksh{}.".format(self.name,self.balance))

	def check_balance(self):
		print("Hello {}, your balance for account {} is Ksh{}.".format(self.name,self.phone_number,self.balance))

	def my_deposits(self):
		for x in self.deposits:
			time=x["time"]
			amount=x["amount"]
			print("On {} you deposited Ksh{}.".format(time.strftime("%A %d %B %Y"),amount))

	def my_withdrawals(self):
		for x in self.withdrawals:
			time=x["time"]
			amount=x["amount"]
			print("On {} you withdrew Ksh{}.".format(time.strftime("%A %d %B %Y"),amount))

	def give_loan(self,amount):
		total=0
		for x in self.deposits:
			amt=x["amount"]
			total+=amt
		if len(self.deposits) >= 5 and self.loan == 0 and amount <= (total/3):
			now = datetime.now()
			object = {"time":now,"amount":amount}
			self.loans.append(object)
			self.loan = self.loan + amount
			self.balance=self.balance+amount
			print("Hello {}! You have qualified for the loan of Ksh{}. Your new balance is Ksh{}.".format(self.name,self.loan,self.balance))
		else:
			print("Sorry {}, you do not qualify for a loan at this time. To qualify, you should have deposited 5 times or more and have no existing loan. The maximum you can borrow is a third of the total deposits you have made so far.".format(self.name))	

	def repay_loan(self,amount):
		if self.loan==0:
			print("You do not have an outstanding loan. Borrow to enjoy our services.")
		elif amount==0:
			print("You have not began clearing your loan yet.")		
		elif amount<self.loan:
			now = datetime.now()
			object = {"time":now,"amount":amount}
			self.loanspaid.append(object)
			self.loan-=amount
			self.balance=self.balance-amount
			print("Hello {}, You have repaid {} and have an outstanding loan of Ksh {}. Your new account balance is Ksh{}. Continue repaying to enjoy our services.".format(self.name,amount,self.loan,self.balance))
		elif amount==self.loan:
			now = datetime.now()
			object = {"time":now,"amount":amount}
			self.loanspaid.append(object)
			self.loan = self.loan-amount
			self.balance=self.balance-amount
			print("You have fully repaid your loan of {}. Your new account balance is Ksh{}. You can now borrow again.".format(amount,self.balance))	
		elif amount>self.loan:
			now = datetime.now()
			object = {"time":now,"amount":amount}
			self.loanspaid.append(object)
			excess = amount - self.loan
			self.balance=self.balance-amount
			self.balance = self.balance + excess
			self.loan = (self.loan + excess) - amount
			print("Hello {}, you have succesfully repaid your loan. Your excess, {}, has been deposited into your account. Your new balance is {}. You can now borrow again.".format(self.name,excess,self.balance))
	
	def myloans(self):
		for x in self.loans:
			time = x["time"]
			loan = x["amount"]
			print("{} - {}".format(time.strftime("%A %d %B %Y"),loan))

	def mypaidloans(self):
		for x in self.loanspaid:
			time = x["time"]
			loanpaid = x["amount"]
			print("{}-{}".format(time.strftime("%A %d %B %Y"),loanpaid))

	def statement(self):
		for x in self.deposits:
			time=x["time"]
			amount=x["amount"]
			print("On {}, you deposited Ksh{}.".format(time.strftime("%A, %d %B, %Y"),amount))
		for x in self.withdrawals:
			time=x["time"]
			amount=x["amount"]
			print("On {}, you withdrew Ksh{}.".format(time.strftime("%A, %d %B, %Y"),amount))	
		for x in self.loans:
			time = x["time"]
			loan = x["amount"]
			print("On {}, you got a loan of Ksh{}".format(time.strftime("%A, %d %B, %Y"),loan))	
		for x in self.loanspaid:
			time = x["time"]
			loanpaid = x["amount"]
			print("On {}, you paid a loan of Ksh{}".format(time.strftime("%A, %d %B, %Y"),loanpaid))	