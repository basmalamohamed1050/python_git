incom=float(input("Enter your monthly income: "))
rent=float(input("Enter rent cost: "))
food=float(input("Enter rent cost: "))
transport = float(input("Enter transport cost: "))
extra = float(input("Enter extra expenses: "))
total_expenses=rent+food+transport+extera
remaining_money=incom-total_expenses

print("--- Budget Report ---")
print(f"Incom    :{incom:,.2f}")
print(f"Food            :{food:,.2f}")
print(f"transport       :{transport:,.2f}")
print(f"etera           :{extra:,.2f}")
print(f"Remaining Money :{remaining_money:,.2f}")