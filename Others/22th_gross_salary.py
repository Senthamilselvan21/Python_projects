Basic_salary=int(input("Enter your Basic_salary: "))
House_rent_allowance=int(input("Enter your House_rent_allowance :"))
Leave_and_travel_allowance=int(input("Enter your Leave_and_travel_allowance: "))
special_allowance=int(input("Enter your special_allowance: "))
Total_allowances= Basic_salary + House_rent_allowance + Leave_and_travel_allowance + special_allowance
print("Total_allowances","Rs.",Total_allowances)
#Detections
Provident_fund=int(input("Enter your Provident_fund: "))
Profession_tax=int(input("Enter your Profession_tax: "))
Insurance_premiun=int(input("Enter your Insurance_premiun: "))
Total_deductions=Provident_fund + Profession_tax + Insurance_premiun
print("Total_Deductions","Rs.",Total_deductions)
Gross_salary_per_annum=Total_allowances - Total_deductions
print("Gross_salary_per_annum","Rs.",Gross_salary_per_annum)