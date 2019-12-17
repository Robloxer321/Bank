import banking

acct1 = banking.Account ('Nicholas', 1000)
acct2 = banking.Account ('Myles', 10000000)

acct1.deposit (200)
acct1.withdrawl(700)
acct2.deposit(1100)
acct2.withdrawl(700)

print (acct1.owner, acct1.balance)
print (acct2.owner, acct2.balance)
acct1.deposit(20.23*1.22)
print(acct1.__str__())
print(acct2.__str__())
