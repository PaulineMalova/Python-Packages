class Mpesa_Account:
	def __init__(self,name,phone_number):
		self.name=name
		self.phone_number=phone_number
		self.balance=0

	def deposit(self,amount):
		self.balance = self.balance+amount
		print("Dear {}, you have deposited Ksh{}. Your new balance is Ksh{}.".format(self.name,amount,self.balance))

	def withdraw(self,amount):
		if amount<self.balance:
			self.balance = self.balance-amount
			print ("Dear {}, you have withdrawn Ksh{}. Your new balance is Ksh{}.".format(self.name,amount,self.balance))
		else:
			print("Sorry {}, you do not have enough funds to facilitate your withdrawal. Your current balance is Ksh{}.".format(self.name,self.balance))

	def check_balance(self):
		print("Hello {}, your balance for account {} is Ksh{}.".format(self.name,self.phone_number,self.balance))					