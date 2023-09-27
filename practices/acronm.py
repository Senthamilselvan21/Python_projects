user_input=input("Enter text: ")
text=user_input.split()
acronym=""
for i in text:
  acronym +=i[0].upper()

print("Acorynm is: ",acronym)
