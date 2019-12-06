from moduly import *
# import moduly

# //todo Ładuje dict z pliku
be1 = load("dict1")  #/todo jest od 0 do 512 włącznie !!!
be2 = load("dict2")
be3 = load("dict3")





# test = ""
# for i in range(0, 1000):
# 	test += "a"
#
# test1 = []
# for i in range(0, len(test)):
# 	test1.append(ord(test[i]))
# test = test1

test = []
for i in range(0, 1000):
	ii = 0
	while ii < 512:
		test.append(ii)
		ii += 1
# test.pop(0)
# test.pop(-1)
# print(test)



# print("Przed za: ", test)
po = multi_hasz(test, 0, 0, 0, be1, be2, be3)
print("Po za: ", po)
od_po = multi_de_hasz(po, 0, 0, 0, be1, be2, be3)
od_po.reverse()
# print("Po od: ", od_po)
print("KONIEC")




