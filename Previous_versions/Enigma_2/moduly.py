from random import shuffle
import pickle


# //todo Buduje dict i miesza
def bud_miesz_dict(size, miesz):
	dic = {}
	for i in range(0, size):
		dic[i] = i;
	if miesz:
		shuffle(dic)
	return dic

# //todo Spr. czy dict losowy
def spr_los_dict(dic):
	test = True
	for i in range(0, len(dic)):
		for ii in range(0, len(dic)):
			if ii != i:
				if dic[i] == dic[ii]:
					print(i, ii, dic[i])
					test = False
	print("Max: ", max(dic))
	print("Min:", min(dic))
	if test:
		print(dic)
		print("DICT. OK")
	
		
# //todo Zapisuje dict do pliku
def save_dict(obj, name ):
	with open('obj/'+ name + '.pkl', 'wb') as f:
		pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)



# //todo Ładuje dict z pliku
def load_dict(name):
	with open('obj/' + name + '.pkl', 'rb') as f:
		return pickle.load(f)


def hasz(bemb, my_chr_in_int):
	for i in range(0, len(bemb)):
		if my_chr_in_int == i:
			return bemb[i]


def de_hasz(bemb, my_chr_in_int):
	for i in range(0, len(bemb)):
		if my_chr_in_int == bemb[i]:
			return i



def multi_hasz(text_list, i1, i2, i3, bemb1, bemb2, bemb3):
	if (max(text_list) <= (len(bemb1) - 1) and (min(text_list) >= 0)):
		print("Słownik OK")
	else:
		print("Słownik z max lub min poza wielkością bemb")
		return
	
	haszed_text = []
	while text_list:
		a = text_list[0]
		text_list.pop(0)
		
		a = hasz(bemb1, a)
		a += i1
		if a >= len(bemb1):
			a -= len(bemb1)
		
		a = hasz(bemb2, a)
		a += i2
		if a >= len(bemb2):
			a -= len(bemb2)
		
		a = hasz(bemb3, a)
		a += i3
		if a >= len(bemb3):
			a -= len(bemb3)
		
		i1 += 1
		if i1 == len(bemb1):
			i1 = 0
			i2 += 1
			if i2 == len(bemb2):
				i3 += 1
				i2 = 0
				if i3 == len(bemb2):
					i3 = 0
				
		haszed_text.append(a)
		
	haszed_text.append(i1)
	haszed_text.append(i2)
	haszed_text.append(i3)
	# print("Klucz: ", i1, i2, i3)
	return haszed_text




def multi_de_hasz(text_list, bemb1, bemb2, bemb3):
	de_haszed_text = []
	i3 = text_list[-1]
	text_list.pop(-1)
	i2 = text_list[-1]
	text_list.pop(-1)
	i1 = text_list[-1]
	text_list.pop(-1)
	# print("Klucz: ", i1, i2, i3)
	
	while text_list:
		a = text_list[-1]
		text_list.pop(-1)
		
		i1 -= 1
		if i1 == -1:
			i1 = len(bemb1) - 1
			i2 -= 1
			if i2 == -1:
				i2 = len(bemb2) - 1
				i3 -= 1
				if i3 == - 1:
					i3 = len(bemb3) - 1
		
		a = de_hasz(bemb3, a)
		a -= i3
		if a <= -1:
			a += len(bemb3)
		
		a = de_hasz(bemb2, a)
		a -= i2
		if a <= -1:
			a += len(bemb2)
		
		a = de_hasz(bemb1, a)
		a -= i1
		if a <= -1:
			a += len(bemb1)
		
		de_haszed_text.append(a)
	return de_haszed_text



