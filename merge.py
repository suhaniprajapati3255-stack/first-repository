d1={"sonia":"verma"}
d2={"suhani":"prajapati"}
print("before merge=",d1,d2)

d3=d1|d2

print("after merge=",d3)
#print(d1)
#print(d2)
#print(d3)

d1.update(d2)
print(d1)
#print(d2)