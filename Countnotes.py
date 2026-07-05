
amount = int(input("Enter the amount to withdraw"))

note1 = amount//100
note2 = (amount%100)//50
note3 = ((amount%100)%50)//10

print("$100 =",note1)
print("$50 =",note2)
print("$10 =",note3)