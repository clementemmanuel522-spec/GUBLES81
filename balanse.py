def withdraw_money(current_balance, amount):
    if(current_balance >= amount):
        current_balance = current_balance - amount
    return current_balance

balance = withdraw_money(800, 50)
print(balance)

if(balance <= 50):
    print("we need to make deposit") 
else:
    print("you are free to withdraw")