import re

a =open("src\data_corey.txt ","r")
b =a.read(5000000)
a.close()
c = re.compile ("(\d{3}\D{0,3}\d{3}\D{0,3}\d{4})")
found = re.findall(c,b)

num7 = len ([i for i in found[:-1] if i[-1]=="7"])
total_numbers = len(found)

mail1=re.compile("([a-zA-Z]+@[a-zA-Z]+.com)")
mail_com=re.findall(mail1,b)
mail2=re.compile("([a-zA-Z]+@[a-zA-Z]+.net)")
mail_net=re.findall(mail2,b)

total_mail_com=len(mail_com)
total_mail_net=len(mail_net)


univers=re.compile("\w+@\w+.\w{3}")
univers_mail=re.findall(univers,b)


print(f"Total amount of phone numbers: {total_numbers}")
print(f"Total amount of phone numbers with ending 7: {num7}")
print(f"Total amount of @***.com: {total_mail_com}")
print(f"Total amount of @***.net: {total_mail_net}")
print(mail_net, mail_com)
print(univers_mail)


