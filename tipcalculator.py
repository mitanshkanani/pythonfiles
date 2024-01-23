print("Welcome to the tip calculator.")
total=float(input("What was the total bill?$"))
tip=float(input("what percentage tip would you like to give ? 10, 12 or 15 ?"))
peeps=float(input("How many people to split the bill?"))
totaltip=(total)*(tip/100)
cost=totaltip+total
perpeep=cost/peeps
x=round(perpeep,2)
print(f"Each person should pay :${x}")