class Mpesa_Account:
	def __init__(self,name,phone_number):
		self.name=name
		self.phone_number=phone_number
		self.balance=0
		self.deposits = []
		self.withdrawals = []
		self.loan = 0

	def deposit(self,amount):
		self.deposits.append(amount)
		self.balance = self.balance+amount
		print("Dear {}, you have deposited Ksh{}. Your new balance is Ksh{}.".format(self.name,amount,self.balance))

	def withdraw(self,amount):
		if amount<self.balance:
			self.withdrawals.append(amount)
			self.balance = self.balance-amount
			print ("Dear {}, you have withdrawn Ksh{}. Your new balance is Ksh{}.".format(self.name,amount,self.balance))
		else:
			print("Sorry {}, you do not have enough funds to facilitate your withdrawal. Your current balance is Ksh{}.".format(self.name,self.balance))

	def check_balance(self):
		print("Hello {}, your balance for account {} is Ksh{}.".format(self.name,self.phone_number,self.balance))

	def my_deposits(self):
		for x in self.deposits:
			print (x)

	def my_withdrawals(self):
		for x in self.withdrawals:
			print (x)

	def give_loan(self,amount):
		if len(self.deposits) >= 5 and self.loan == 0 and amount <= (1/3)*(sum(self.deposits)):
			self.loan = self.loan + amount
			self.balance=self.balance+amount
			print("Hello {}! You have qualified for the loan of Ksh{}. Your new balance is Ksh{}.".format(self.name,self.loan,self.balance))
		else:
			print("Sorry {}, you do not qualify for a loan at this time. To qualify, you should have depositted 5 times or more and have no existing loan. The maximum you can borrow is a third of the total deposits you have made so far.".format(self.name,len(self.deposits)))	

	def repay_loan(self,amount):
		if self.loan==0:
			print("You do not have an outstanding loan. Borrow to enjoy our services.")
		elif amount==0:
			print("You have not began clearing your loan yet.")		
		elif amount<self.loan:
			self.loan = self.loan - amount
			self.balance=self.balance-amount
			print("Hello {}, You have repaid {}and have an outstanding loan of Ksh {}. Your new account balance is Ksh{}. Continue repaying to enjoy our services.".format(self.name,amount,self.loan,self.balance))
		elif amount==self.loan:
			self.loan = self.loan-amount
			self.balance=self.balance-amount
			print("You have fully repaid your loan of {}. Your new account balance is Ksh{}. You can now borrow again.".format(amount,self.balance))	
		elif amount>self.loan:
			excess = amount - self.loan
			self.balance=self.balance-amount
			self.balance = self.balance + excess
			self.loan = (self.loan + excess) - amount
			print("Hello {}, you have succesfully repaid your loan. Your excess, {}, has been deposited into your account. Your new balance is {}. You can now borrow again.".format(self.name,excess,self.balance))
		