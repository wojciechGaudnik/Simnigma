for i in range(0,380):
	print(chr(i))
print("-----------")

for i in tekst_split:
	print(i,(ord(i)))
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
def szyfr_bem1(be1, str):
	haszstr = []
	for i in range(0, len(str)):
		for ii in range (0, 512):
			if ord(str[i]) == ii: #//todo
				haszstr.append(be1[ii])
	b = []
	for i in range(0, len(haszstr)):
		b.append(chr(haszstr[i]))
	return b

a = szyfr_bem1(be, tekst_split)
print(a)

def deszyfr_bem1(be1, str):
	dehaszstr = []
	for i in range(0, len(str)):
		for ii in range (0, 512):
			if ord(str[i]) == be1[ii]:
				dehaszstr.append(ii)
	b = []
	for i in range(0, len(dehaszstr)):
		b.append(chr(dehaszstr[i]))
	return b

b = deszyfr_bem1(be, a)
print(b)














#/todo szyfrowanie
a1 = szyfr_bem(be1, tekst_split)
print("Po be1:\t\t\t ", a1, ord(a1[0]))
a1 = chr(ord(a1[0]) + 1)
if ord(a1) > 512:
	a1 = 0
print("Po + 1:\t\t\t\t", a1, ord(a1))


a2 = szyfr_bem(be2, a1)
print("Po be2:\t\t\t ", a2, ord(a2[0]))
a2 = chr(ord(a2[0]) + 1)
if ord(a2) > 512:
	a2 = 0
print("Po + 1:\t\t\t\t", a2, ord(a2))


a3 = szyfr_bem(be3, a2)
print("Po be3:\t\t\t ", a3, ord(a3[0]))
a3 = chr(ord(a3[0]) + 1)
if ord(a3) > 512:
	a3 = 0
print("Po + 1:\t\t\t\t", a3, ord(a3))



#/todo deszyfrowanie
# 512 + 1 = 513 ---> 0
# 0 - 1 = -1 ---> 512

print("Przed:\t\t\t\t ",a3, ord(a3[0]))

a3 = chr(ord(a3[0]) - 1)
if ord(a3) < 0:
	a3 = 512
print("Po - 1:\t\t\t\t", a3, ord(a3))
a2 = deszyfr_bem(be3, a3)
print("Po be3:\t\t\t ", a2, ord(a2[0]))


a2 = chr(ord(a2[0]) - 1)
if ord(a2) < 0:
	a2 = 512
print("Po - 1:\t\t\t\t", a2, ord(a2))
a1 = deszyfr_bem(be2, a2)
print("Po be2:\t\t\t ", a1, ord(a1[0]))


a1 = chr(ord(a1[0]) - 1)
if ord(a1) < 0:
	a1 = 512
print("Po - 1:\t\t\t\t", a1, ord(a1))
a0 = deszyfr_bem(be1, a1)
print("Po be1:\t\t\t ", a0, ord(a0[0]))














