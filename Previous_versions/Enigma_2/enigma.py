from moduly import *
# from reverse import reverse

# bitow = 2
# bit = 2 ** bitow
# print(bit)

# be1 = bud_miesz_dict(5, True)
# be2 = bud_miesz_dict(5, True)
# be3 = bud_miesz_dict(5, True)
# spr_los_dict(be1)
# spr_los_dict(be2)
# spr_los_dict(be3)
#
# save_dict(be1, "be1")
# save_dict(be2, "be2")
# save_dict(be3, "be3")

be1 = load_dict("be1")
be2 = load_dict("be2")
be3 = load_dict("be3")
# spr_los_dict(be1)
# spr_los_dict(be2)
# spr_los_dict(be3)

#/todo -----------------------------------
# text_list = []
# for i in range (0, 5):
# 	for ii in range(0, 5):
# 		text_list.append(1)
#
#
# print("text przed   :\t\t",text_list)
# text_hasz = multi_hasz(text_list, 0, 0, 0, be1, be2, be3)
# print("text po      :\t\t",text_hasz)
# text_de_hasz = multi_de_hasz(text_hasz, be1, be2, be3)
# text_de_hasz.reverse()
# print("text odsz   :\t\t",text_de_hasz)
#/todo -----------------------------------


text_list =[0, 0, 0, 0, 0]
print(text_list)

i1 = 0
i2 = 0
i3 = 0

lit1 = hasz(be1, text_list[0])
lit1 += i1
if lit1 >= len(be1):
	lit1 -= len(be1)
lit1 = hasz(be2, lit1)
lit1 += i2
if lit1 >= len(be2):
	lit1 -= len(be2)
lit1 = hasz(be3, lit1)
lit1 += i3
if lit1 >= len(be3):
	lit1 -= len(be3)
print("lit1. przed i po.: ",text_list[0], " : ", lit1)
print("Wart. i(n):\t\t", i1, " : ", i2, " : ", i3)
i1 += 1
if i1 == len(be1):
	i1 = 0
	i2 += 1
	if i2 == len(be2):
		i3 += 1
		i2 = 0
		if i3 == len(be3):
			i3 = 0
print("-----------------------------------")


lit2 = hasz(be1, text_list[1])
lit2 += i1
if lit2 >= len(be1):
	lit2 -= len(be1)
lit2 = hasz(be2, lit2)
lit2 += i2
if lit2 >= len(be2):
	lit2 -= len(be2)
lit2 = hasz(be3, lit2)
lit2 += i3
if lit2 >= len(be3):
	lit2 -= len(be3)
print("lit2. przed i po.: ",text_list[1], " : ", lit2)
print("Wart. i(n):\t\t", i1, " : ", i2, " : ", i3)
i1 += 1
if i1 == len(be1):
	i1 = 0
	i2 += 1
	if i2 == len(be2):
		i3 += 1
		i2 = 0
		if i3 == len(be3):
			i3 = 0
print("-----------------------------------")


lit3 = hasz(be1, text_list[2])
lit3 += i1
if lit3 >= len(be1):
	lit3 -= len(be1)
lit3 = hasz(be2, lit3)
lit3 += i2
if lit3 >= len(be2):
	lit3 -= len(be2)
lit3 = hasz(be3, lit3)
lit3 += i3
if lit3 >= len(be3):
	lit3 -= len(be3)
print("lit3. przed i po.: ",text_list[2], " : ", lit3)
print("Wart. i(n):\t\t", i1, " : ", i2, " : ", i3)
i1 += 1
if i1 == len(be1):
	i1 = 0
	i2 += 1
	if i2 == len(be2):
		i3 += 1
		i2 = 0
		if i3 == len(be3):
			i3 = 0
print("-----------------------------------")




lit4 = hasz(be1, text_list[3])
lit4 += i1
if lit4 >= len(be1):
	lit4 -= len(be1)
lit4 = hasz(be2, lit4)
lit4 += i2
if lit4 >= len(be2):
	lit4 -= len(be2)
lit4 = hasz(be3, lit4)
lit4 += i3
if lit4 >= len(be3):
	lit4 -= len(be3)
print("lit4. przed i po.: ",text_list[3], " : ", lit4)
print("Wart. i(n):\t\t", i1, " : ", i2, " : ", i3)
i1 += 1
if i1 == len(be1):
	i1 = 0
	i2 += 1
	if i2 == len(be2):
		i3 += 1
		i2 = 0
		if i3 == len(be3):
			i3 = 0
print("-----------------------------------")


lit5 = hasz(be1, text_list[4])
lit5 += i1
if lit5 >= len(be1):
	lit5 -= len(be1)

lit5 = hasz(be2, lit5)
lit5 += i2
if lit5 >= len(be2):
	lit5 -= len(be2)

lit5 = hasz(be3, lit5)
lit5 += i3
if lit5 >= len(be3):
	lit5 -= len(be3)

print("lit5. przed i po.: ",text_list[4], " : ", lit5)
print("Wart. i(n):\t\t", i1, " : ", i2, " : ", i3)
i1 += 1
if i1 == len(be1):
	i1 = 0
	i2 += 1
	if i2 == len(be2):
		i3 += 1
		i2 = 0
		if i3 == len(be3):
			i3 = 0
print("-----------------------------------") #/todo etwertertewrtwert
print("-----------------------------------")
i1 -= 1
if i1 == -1:
	i1 = len(be1) - 1
	i2 -= 1
	if i2 == -1:
		i2 = len(be2) - 1
		i3 -= 1
		if i3 == -1:
			i3 = len(be3) - 1
print("Wart. i(n):\t\t", i1, " : ", i2, " : ", i3)

lit5 = de_hasz(be3, lit5)
lit5 -= i3
if lit5 <= -1:
	lit5 += len(be3)

lit5 = de_hasz(be2, lit5)
lit5 -= i2
if lit5 <= -1:
	lit5 += len(be2)

lit5 = de_hasz(be1, lit5)
lit5 -= i1
if lit5 <= -1:
	lit5 += len(be1)
print("lit5. od:", lit5)
print("-----------------------------------")
i1 -= 1
if i1 == -1:
	i1 = len(be1) - 1
	i2 -= 1
	if i2 == -1:
		i2 = len(be2) - 1
		i3 -= 1
		if i3 == -1:
			i3 = len(be3) - 1
print("Wart. i(n):\t\t", i1, " : ", i2, " : ", i3)

lit4 = de_hasz(be3, lit4)
lit4 -= i3
if lit4 <= -1:
	lit4 += len(be3)

lit4 = de_hasz(be2, lit4)
lit4 -= i2
if lit4 <= -1:
	lit4 += len(be2)

lit4 = de_hasz(be1, lit4)
lit4 -= i1
if lit4 <= -1:
	lit4 += len(be1)
print("lit4. od:", lit4)
print("-----------------------------------")
i1 -= 1
if i1 == -1:
	i1 = len(be1) - 1
	i2 -= 1
	if i2 == -1:
		i2 = len(be2) - 1
		i3 -= 1
		if i3 == -1:
			i3 = len(be3) - 1
print("Wart. i(n):\t\t", i1, " : ", i2, " : ", i3)

lit3 = de_hasz(be3, lit3)
lit3 -= i3
if lit3 <= -1:
	lit3 += len(be3)

lit3 = de_hasz(be2, lit3)
lit3 -= i2
if lit3 <= -1:
	lit3 += len(be2)

lit3 = de_hasz(be1, lit3)
lit3 -= i1
if lit3 <= -1:
	lit3 += len(be1)
print("lit3. od:", lit3)
print("-----------------------------------")
i1 -= 1
if i1 == -1:
	i1 = len(be1) - 1
	i2 -= 1
	if i2 == -1:
		i2 = len(be2) - 1
		i3 -= 1
		if i3 == -1:
			i3 = len(be3) - 1
print("Wart. i(n):\t\t", i1, " : ", i2, " : ", i3)

lit2 = de_hasz(be3, lit2)
lit2 -= i3
if lit2 <= -1:
	lit2 += len(be3)

lit2 = de_hasz(be2, lit2)
lit2 -= i2
if lit2 <= -1:
	lit2 += len(be2)

lit2 = de_hasz(be1, lit2)
lit2 -= i1
if lit2 <= -1:
	lit2 += len(be1)
print("lit2. od:", lit2)
print("-----------------------------------")
i1 -= 1
if i1 == -1:
	i1 = len(be1) - 1
	i2 -= 1
	if i2 == -1:
		i2 = len(be2) - 1
		i3 -= 1
		if i3 == -1:
			i3 = len(be3) - 1
print("Wart. i(n):\t\t", i1, " : ", i2, " : ", i3)

lit1 = de_hasz(be3, lit1)
lit1 -= i3
if lit1 <= -1:
	lit1 += len(be3)

lit1 = de_hasz(be2, lit1)
lit1 -= i2
if lit1 <= -1:
	lit1 += len(be2)

lit1 = de_hasz(be1, lit1)
lit1 -= i1
if lit1 <= -1:
	lit1 += len(be1)
print("lit1. od:", lit1)


