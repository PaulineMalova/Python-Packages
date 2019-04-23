class Mpesa_Account:
	def __init__(self,name,phone_number):
		self.name=name
		self.phone_number=phone_number
		self.balance=0
		self.deposits = []
		self.withdrawals = []

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