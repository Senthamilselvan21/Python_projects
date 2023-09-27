"""empdetails={'name':'muniraj','empid':900,'salary':5000}
for keys in empdetails.keys():
        print(empdetails[keys])"""

empdetails={}
for record in range(2):
        name = input("Enter a name: ")
        salary = input("Enter salary: ")
        empdetails[name] = salary


print(empdetails)


