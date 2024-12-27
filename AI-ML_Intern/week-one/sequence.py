a = ["vijay","Dhanush","Suriya","SK","Ragava","Allu Arjun","Ajith"]
print(a)
a.append("STR")
print(a)
b = "Ajith","Vikram","Vishal"
a.extend(b)
print(a)
a.insert(1,"Kenny")
print("lists :",a)
a[1:3] = "prabhu","karthick","Atharwa"
print(a)


'''
for loop
'''

for i in a:
   
    if i == "Ragava":
        continue
    print(i)

