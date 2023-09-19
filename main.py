from BankAcct import BankAccount

ba1 = BankAccount(24601, "Jean Valjean", 3_456)
ba2 = BankAccount(2, "Number 2", 1_000)
ba3 = BankAccount(8913, "Rocket Raccoon", 2_000)

# Print account particulars for account 1
ba1.print_acct_info()
# Deposit 10_000 into account 2
ba2.make_deposit(10_000)
# Withdraw 5,000 from account 3 - this should fail
ba3.make_withdrawal(5_000)
# Transfer 10_000 from account 1 to account 2 - this should fail
ba1.transfer(10_000, ba2)
# Transfer 10_000 from account 1 to account 3 - this should fail
ba1.transfer(10_000, ba3)
# Transfer 10_000 from account 1 to account 3 
ba1.transfer(1_000, ba3)
# Print info for account 3
ba3.print_acct_info()