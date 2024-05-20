import sys
import random

# write your code here
party_number = int(input("Enter the number of friends joining (including you): "))

if party_number < 1:
    print("No one is joining for the party")
    sys.exit()
else:
    print("Enter the name of every friend (including you), each on a new line: ")
    
party_list = {}
i = 0

for i in range(party_number):
    x = str(input())
    party_list.update({x:0})

print(party_list)

total_bill = int(input("Enter the total bill value: "))

use_feature = input('Do you want to use the "Who is lucky?" feature? Write Yes/No: ')
if use_feature == "Yes":   
    lucky_one = random.choice(list(party_list.keys()))
    print(f"{lucky_one} is the lucky one! ")   
    #lucky one doesn't split bill, others pay
    equal_billing = float(round(total_bill / (party_number - 1), 2))
    for key, value in party_list.items():
        party_list[key] = equal_billing
    party_list[lucky_one] = 0.0
    print(party_list)

else:  
    print("No one is going to be lucky")
    equal_billing = float(round(total_bill / (party_number), 2))
    for key, value in party_list.items():
        party_list[key] = equal_billing
    print(party_list)
