print("======= Expense Tracker =======")
print("   Track your spending easily \n")

expenses = []
purposes = []

while True:
	entry = input("Enter expense amount(or type 'done'):")
	if entry == "done":
		break

	try:
		expenses.append(float (entry))
	except:
		print("Please enter a valid number")

	what_for = input("What was it for? ")

	purposes.append(str(what_for))


total = sum(expenses)

print("Total spent: ", total)

with open("expenses.txt", "w") as file:
	"""for item in expenses:
		file.write(str(item)+ "\n") """

	for i in range (len(expenses)):
		file.write(str(expenses[i])+ "\t" + purposes[i] + "\n")
		
	file.write("Total:" + str(total))


print("\nYou spent a total of: ", total)
print("Data saved to expenses.txt")