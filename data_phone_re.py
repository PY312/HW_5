import re
a = open("src\data_phone.json","r")
b = a.read(2000000)
a.close()

c = re.compile ("(\d{13})")

found = re.findall(c,b)
total_phone=len(found)

num1= re.findall("[(]+669[)][ ]?[\d]{3}-[\d]{4}", b)
num2= re.findall("[(]+000[)][ ]?[\d]{3}-[\d]{4}", b)
num3= re.findall("[(]+699[)][ ]?[\d]{3}-[\d]{4}", b)

print(f"Total amount of phone numbers with 13 digits: {total_phone}")
print(num1)
print(num2)
print(num3)