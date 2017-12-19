from random import shuffle
import pickle

# print("Buduje dict i miesza-----------")
be = {}
for i in range(0, 513):
	be[i] = i;
shuffle(be)


# //todo Spr. czy dict losowy
# for i in range(0, 512):
# 	for ii in range(0, 512):
# 		if ii != i:
# 			if be[i] == be[ii]:
# 				print(i, ii, be[i])
# print("Koniec spr. czy dict różny-----------")


# //todo Zapisuje dict do pliku
# def save_dict(obj, name ):
# 	with open('obj/'+ name + '.pkl', 'wb') as f:
# 		pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)
# 	save_dict(be, "dict3")
# print(be)



# //todo Ładuje dict z pliku
def load_load(name):
	with open('obj/' + name + '.pkl', 'rb') as f:
		return pickle.load(f)


be1 = load_load("dict1")
be2 = load_load("dict2")
be3 = load_load("dict3")


def szyfr_bem(be, str):
	haszstr = []
	for i in range(0, len(str)):
		for ii in range(0, 512):
			if ord(str[i]) == ii:
				haszstr.append(be[ii])
	b = []
	for i in range(0, len(haszstr)):
		b.append(chr(haszstr[i]))
	return b


def deszyfr_bem(be, str):
	dehaszstr = []
	for i in range(0, len(str)):
		for ii in range(0, 512):
			if ord(str[i]) == be[ii]:
				dehaszstr.append(ii)
	b = []
	for i in range(0, len(dehaszstr)):
		b.append(chr(dehaszstr[i]))
	return b


test = "a"
a1 = szyfr_bem(be1, test)
b = deszyfr_bem(be1, a1)


# print(test)
# print(a1[0])
# print(b[0])


# tekst = "a" #""/aąbcćdeęfghijklłmnńoóprsśtuwxyz żź"
# tekst_split = list(tekst)
# print("Przed:\t\t\t ",tekst_split, ord(tekst_split[0]))


# /todo 512 + 1 = 513 ---> 0
# /todo 512 + 12 = 524 ---> 11
# /todo 70 + 442 = 512 ---> 512
# /todo 70 + 443 = 513 ---> 0     513 - 512 -1
# /todo 70 + 444 = 514 ---> 1     514 - 512 -1

# /todo 0 - 12 = -12 ---> 501
# /todo 0 - 1 = -1 ---> 512




# /todo szyfrowanie
def pierwsze_trzy(text_string):
	text_split = list(text_string)
	i1 = 0
	i2 = 0
	i3 = 0
	gotowe = ""
	while text_split:
		a0 = text_split[0]
		text_split.pop(0)
		
		if i1 == 513:
			i1 = 0
			i2 += 1
		a1 = szyfr_bem(be1, a0)
		# print("Po be1:\t\t\t ", a1, ord(a1[0]))
		a1 = chr(ord(a1[0]) + i1)
		if ord(a1) > 512:
			a1 = i1 - 1
		# print("Po + 1:\t\t\t\t", a1, ord(a1))
		i1 += 1
		
		if i2 == 513:
			i2 = 0
			i3 += 1
		a2 = szyfr_bem(be2, a1)
		# print("Po be2:\t\t\t ", a2, ord(a2[0]))
		a2 = chr(ord(a2[0]) + i2)
		if ord(a2) > 512:
			a2 = i2 - 1
		# print("Po + 1:\t\t\t\t", a2, ord(a2))
		
		
		if i3 == 513:
			i3 = 0
		a3 = szyfr_bem(be3, a2)
		# print("Po be3:\t\t\t ", a3, ord(a3[0]))
		a3 = chr(ord(a3[0]) + i3)
		if ord(a3) > 512:
			a3 = i3 - 1
		# print("Po + 1:\t\t\t\t", a3, ord(a3))
		
		gotowe += a3
	# print(a0, " : ", a3)
	return gotowe


test = ""
for i in range(0, 280):
	test += "a"
print(test)
print(pierwsze_trzy(test))




# /todo deszyfrowanie
#
#
# print("Przed:\t\t\t\t ",a3, ord(a3[0]))
#
# a3 = chr(ord(a3[0]) - 1)
# if ord(a3) < 0:
# 	a3 = 512
# print("Po - 1:\t\t\t\t", a3, ord(a3))
# a2 = deszyfr_bem(be3, a3)
# print("Po be3:\t\t\t ", a2, ord(a2[0]))
#
#
# a2 = chr(ord(a2[0]) - 1)
# if ord(a2) < 0:
# 	a2 = 512
# print("Po - 1:\t\t\t\t", a2, ord(a2))
# a1 = deszyfr_bem(be2, a2)
# print("Po be2:\t\t\t ", a1, ord(a1[0]))
#
#
# a1 = chr(ord(a1[0]) - 1)
# if ord(a1) < 0:
# 	a1 = 512
# print("Po - 1:\t\t\t\t", a1, ord(a1))
# a0 = deszyfr_bem(be1, a1)
# print("Po be1:\t\t\t ", a0, ord(a0[0]))






