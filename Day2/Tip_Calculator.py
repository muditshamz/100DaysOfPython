#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: You might need to do some research in Google to figure out how to do this.

bill = int(input("Give the bill amount?\n$"))
tip_amount = int(input("What is the amount you prefer for tip? 10%, 12%, 15% \n"))
people = int(input("Among how many members you want to split?\n"))

each_person_pay = (bill/people) * (1+(tip_amount/100))

final_contribution_eachHead = "{:.2f}".format(each_person_pay)
print("Every person will pay:$",final_contribution_eachHead)
