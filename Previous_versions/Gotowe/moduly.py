import pickle


def load(name):
	with open('obj/' + name + '.pkl', 'rb') as f:
		return pickle.load(f)

def hasz(bem, my_chr_in_int):
	# print(bem, my_chr_in_int)
	for i in range (0, 513):
		if my_chr_in_int == i:
			return bem[i]
	
def de_hasz(bem, my_chr_in_int):
	for i in range(0, 513):
		if my_chr_in_int == bem[i]:
			return i

def multi_hasz(text_string, i1, i2, i3, bemb1, bemb2, bemb3):
	text_split = list(text_string)
	haszed_text = []
	while text_split:
		a0 = ord(text_split[0])
		text_split.pop(0)
		
		a0 += i1
		if a0 > 512:
			a0 -= 513
		a1 = hasz(bemb1, a0)
		
		a1 += i2
		if a1 > 512:
			a1 -= 513
		a2 = hasz(bemb2, a1)
		
		a2 += i3
		if a2 > 512:
			a2 -= 513
		a3 = hasz(bemb3, a2)
		
		i1 += 1
		if i1 == 513:
			i1 = 0
			i2 += 1
			if i2 == 513:
				i2 = 0
				i3 += 1
				if i3 == 513:
					i3 = 0
		
		haszed_text.append(a3)
	haszed_text.append(i1)
	haszed_text.append(i2)
	haszed_text.append(i3)
	return haszed_text




def multi_de_hasz(text_list, i1, i2, i3, bemb1, bemb2, bemb3):
	de_haszed_text = []
	testtttt = []
	i3 = text_list[-1]
	text_list.pop(-1)
	i2 = text_list[-1]
	text_list.pop(-1)
	i1 = text_list[-1] - 1
	text_list.pop(-1)
	print("Klucz: ", i1, i2, i3)
	
	while text_list:
		a3 = text_list[-1]
		text_list.pop(-1)
		
		a2 = de_hasz(bemb3, a3)
		a2 -= i3
		if a2 < 0:
			a2 += 513

		a1 = de_hasz(bemb2, a2)
		a1 -= i2
		if a1 < 0:
			a1 += 513
		
		a0 = de_hasz(bemb1, a1)
		a0 -= i1
		if a0 < 0:
			a0 += 513
		
		i1 -= 1
		if i1 == -1:
			i1 = 512
			i2 -= 1
			if i2 == -1:
				i2 = 512
				i3 -= 1
				if i3 == -1:
					i3 = 512
					
		de_haszed_text.append(a0)
	return de_haszed_text
		
		
		
