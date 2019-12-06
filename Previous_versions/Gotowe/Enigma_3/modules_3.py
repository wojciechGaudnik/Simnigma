from random import shuffle
import pickle


# //todo Buduje dict i miesza
def cre_mix_dict(size, mix):
	dic = {}
	for i in range(0, size):
		dic[i] = i;
	if mix:
		shuffle(dic)
	return dic


# //todo Spr. czy dict losowy
def check_rand_dict(dic):
	test = True
	for i in range(0, len(dic)):
		for ii in range(0, len(dic)):
			if ii != i:
				if dic[i] == dic[ii]:
					print(i, ii, be[i])
					test = False
	if test:
		print(dic)
		print("Max: ", max(dic))
		print("Min:", min(dic))
		print("DICT. OK")


# //todo Zapisuje dict do pliku
def save_dict(obj, name):
	with open('obj/' + name + '.pkl', 'wb') as f:
		pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)


# //todo Ładuje dict z pliku
def load_dict(name):
	with open('obj/' + name + '.pkl', 'rb') as f:
		return pickle.load(f)


class Drum_first_encrypt():
	def __init__(self, drum, key_i):
		self.drum = drum
		self.key_i = key_i
		self.i = 0
		self.i_max = len(self.drum)
		if self.key_i:
			self.i += self.key_i
		
	def encrypt(self, one_char_in_list):
		self.encrypt_char_plus_i = []
		
		self.encrypt_char_plus_i.append(self.drum[one_char_in_list[0]] + self.i)
		if self.encrypt_char_plus_i[0] >= self.i_max:
			self.encrypt_char_plus_i[0] -= self.i_max
		
		self.i += 1
		if self.i == self.i_max:
			self.i = 0
			self.encrypt_char_plus_i.append(1)
		else:
			self.encrypt_char_plus_i.append(0)
		
		return self.encrypt_char_plus_i


class Drum_next_encrypt():
	def __init__(self, drum, key_i):
		self.drum = drum
		self.key_i = key_i
		self.i = 0
		self.i_max = len(self.drum)
		if self.key_i:
			self.i += self.key_i
	
	def encrypt(self, one_char_in_list):
		self.encrypt_char_plus_i = []
		self.encrypt_char_plus_i.append(self.drum[one_char_in_list[0]] + self.i)
		if self.encrypt_char_plus_i[0] >= self.i_max:
			self.encrypt_char_plus_i[0] -= self.i_max
		
		if one_char_in_list[1] == 1:
			self.i += 1
		if self.i == self.i_max:
			self.i = 0
			self.encrypt_char_plus_i.append(1)
		else:
			self.encrypt_char_plus_i.append(0)
		return self.encrypt_char_plus_i


class Drum_next_decrypt():
	
	nb = 1
	def __init__(self, drum, key_i):
		self.nb = Drum_next_decrypt.nb
		Drum_next_decrypt.nb += 1
		self.drum = {}
		for i in range(0, len(drum)):
			for ii in range(0, len(drum)):
				if ii == drum[i]:
					self.drum[ii] = i
			print("Decrypt dict. next ", self.nb ," optimization: ", (i / len(drum)) * 100)
		self.i_max = len(self.drum)

		self.i = 0
		if key_i:
			self.i += key_i
	
	def decrypt(self, one_char_in_list):
		self.one_char_in_list = one_char_in_list

		if (len(self.one_char_in_list) - 1) == self.nb:
			self.one_char_in_list.append(0)
			self.one_char_in_list[self.nb] = self.i
		else:
			self.i = self.one_char_in_list[self.nb]
		
		self.one_char_in_list[0] -= self.i
		if self.one_char_in_list[0] < 0:
			self.one_char_in_list[0] += self.i_max
		self.one_char_in_list[0] = self.drum[self.one_char_in_list[0]]
		
		return self.one_char_in_list
		


class Drum_last_decrypt():
	
	def __init__(self, drum, key_i):
		self.nb = Drum_next_decrypt.nb
		
		self.drum = {}
		for i in range(0, len(drum)):
			for ii in range(0, len(drum)):
				if ii == drum[i]:
					self.drum[ii] = i
			print("Decrypt dict. last optimization: ", (i / len(drum)) * 100)
		self.i_max = len(self.drum)
		
		self.i = 0
		if key_i:
			self.i += key_i
	
	def decrypt(self, one_char_in_list):
		self.one_char_in_list = one_char_in_list
		
		self.one_char_in_list[0] -= self.i
		if self.one_char_in_list[0] < 0:
			self.one_char_in_list[0] += self.i_max
		self.one_char_in_list[0] = self.drum[self.one_char_in_list[0]]
		
		self.i += 1
		self.one_char_in_list[self.nb] = self.i
		for i in range(0, self.nb):
			if self.one_char_in_list[self.nb - i] == self.i_max:
				self.one_char_in_list[self.nb - i] = 0
				if (self.nb - i - 1) > 0:
					self.one_char_in_list[self.nb - i - 1] += 1
			else:
				break
		self.i = self.one_char_in_list[self.nb]
		return self.one_char_in_list
	