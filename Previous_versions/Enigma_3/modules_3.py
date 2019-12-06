from random import shuffle
import pickle

class bcolors:
	WARNING = '\033[91m'
	BOLD = '\033[1m'
	ENDC = '\033[0m'

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
		self.i = 0
		self.i_max = len(self.drum)
		if key_i:
			self.i = key_i
		
	def encrypt(self, one_char_in_list):		
		encrypt_char_plus_i = [0, 0]		
		encrypt_char_plus_i[0] = self.drum[one_char_in_list[0]] + self.i
		if encrypt_char_plus_i[0] >= self.i_max:
			encrypt_char_plus_i[0] -= self.i_max		
		self.i += 1
		if self.i == self.i_max:
			self.i = 0
			encrypt_char_plus_i[1] = 1		
		return encrypt_char_plus_i


class Drum_next_encrypt():
	def __init__(self, drum, key_i):
		self.drum = drum
		self.i_max = len(self.drum)
		self.i = 0
		if key_i:
			self.i = key_i
	
	def encrypt(self, one_char_in_list):
		encrypt_char_plus_i = [0, 0]
		encrypt_char_plus_i[0] = self.drum[one_char_in_list[0]] + self.i
		if encrypt_char_plus_i[0] >= self.i_max:
			encrypt_char_plus_i[0] -= self.i_max
		if one_char_in_list[1] == 1:
			self.i += 1
			if self.i >= self.i_max:
				self.i = 0
				encrypt_char_plus_i[1] = 1
		return encrypt_char_plus_i


class Drum_next_decrypt():	
	drum_number = 1
	def __init__(self, drum, key_i):
		self.drum_number = Drum_next_decrypt.drum_number
		Drum_next_decrypt.drum_number += 1
		self.drum = {}		
		for key, value in drum.items():
			self.drum[value] = key	
		self.i_max = len(self.drum)
		self.i = 0
		if key_i:
			self.i = key_i
	
	def decrypt(self, one_char_in_list):
		encrypt_char_plus_i = one_char_in_list
		if (len(encrypt_char_plus_i) - 1) == self.drum_number:
			encrypt_char_plus_i.append(0)
			encrypt_char_plus_i[self.drum_number] = self.i
		else:
			self.i = encrypt_char_plus_i[self.drum_number]
		encrypt_char_plus_i[0] -= self.i
		if encrypt_char_plus_i[0] < 0:
			encrypt_char_plus_i[0] += self.i_max
		encrypt_char_plus_i[0] = self.drum[encrypt_char_plus_i[0]]
		return encrypt_char_plus_i
		


class Drum_last_decrypt():
	def __init__(self, drum, key_i):
		self.drum_number = Drum_next_decrypt.drum_number
		self.drum = {}
		for key, value in drum.items():
			self.drum[value] = key
		self.i_max = len(self.drum)
		self.i = 0
		if key_i:
			self.i = key_i
	
	def decrypt(self, one_char_in_list):
		encrypt_char_plus_i = one_char_in_list
		encrypt_char_plus_i[0] -= self.i
		if encrypt_char_plus_i[0] < 0:
			encrypt_char_plus_i[0] += self.i_max
		encrypt_char_plus_i[0] = self.drum[encrypt_char_plus_i[0]]
		self.i += 1
		encrypt_char_plus_i[self.drum_number] = self.i
		for i in range(0, self.drum_number):
			if encrypt_char_plus_i[self.drum_number - i] >= self.i_max:
				encrypt_char_plus_i[self.drum_number - i] = 0
				if (self.drum_number - i - 1) > 0:
					encrypt_char_plus_i[self.drum_number - i - 1] += 1
			else:
				break
		self.i = encrypt_char_plus_i[self.drum_number]
		return encrypt_char_plus_i
	