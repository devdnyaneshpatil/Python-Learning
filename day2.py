bill=input("What is the total bill?")
tip=input("what percentage tip would you like to give? 10,12 or 15?")
people=input("How many people to split the bill?")
bill_as_int=int(bill)
tip_as_int=int(tip)
people_as_int=int(people)
tip_as_percent=tip_as_int/100
total_tip_amount=bill_as_int*tip_as_percent
total_bill=bill_as_int+total_tip_amount
bill_per_person=total_bill/people_as_int
final_amount=round(bill_per_person,2)
print(f"Each person should pay:${final_amount}")