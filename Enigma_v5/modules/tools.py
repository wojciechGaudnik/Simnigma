# only functions to generate, load, save, check itp..
import decimal
import time
from random import randint

import sys

from math import log

import pickle

from .__tools_single import __cre_rotor, __save_rotor, __load_rotor, __check_rand_rotor, generate_from_64b_inter_key, bcolors
from .core import EncryptNextRotor, EncryptSet, DecryptNextRotor, DecryptSet





def create_rotors(size_in_bit, mix, number_of_rotors): # todo daj mix Tru i na koncu
	size = 2 ** size_in_bit
	return ([__cre_rotor(size, mix) for _ in range(0, number_of_rotors)])
	
	
def save_rotors(rotors, name):
	i = 1
	for rotor in rotors:
		__save_rotor(rotor, name + '_' + str(i))
		i += 1
	
		
def load_rotors(name, number):
	return ([__load_rotor(x) for x in (name + '_' + str(x) for x in range(1, number + 1))])
	

def save_rotors_in_one_file(rotors, name):
	name += ".rotors" if ".rotors" not in name[-7:] else ""
	with open(name, 'wb') as f:
		pickle.dump(rotors, f, pickle.HIGHEST_PROTOCOL)


def load_rotors_from_one_file(name):
	name += ".rotors" if ".rotors" not in name[-7:] else ""
	with open(name, 'rb') as f:
		return pickle.load(f)


def save_key(name, key):
	name += ".key" if ".key" not in name[-4:] else ""
	f = open(name, "wb")
	try:
		f.write(bytes(key + "\n", 'ascii'))
	finally:
		f.close()


def load_key(name, show=False):
	name += ".key" if ".key" not in name[-4:] else ""
	# f = open(name, "rb")
	# try:
	# 	key_list = f.read()
	# finally:
	# 	f.close()
	try:
		f = open(name, 'rb')
		key_list = f.read()
		print('Loaded key:   ', name)
		f.close()
	except:
		exit(bcolors.WARNING +  "Error: Can't open key file {}".format(name) + bcolors.ENDC)
	
	
	
	key = ""
	key_ret = ""
	for c in key_list:
		key += chr(c)
	key_ret = key_ret.join(key)
	return key_ret[:-1]
	
	
def save_file(name, file):
	f = open(name, "wb")
	file.append(10)
	try:
		f.write(bytes(file))
	finally:
		f.close()
	
	
def load_file(name):
	f = open(name, "rb")
	try:
		file = f.read()
	finally:
		f.close()
	file = list(file)
	return file[:-1]

def check_rand_rotors(rotors):
	__key_min = min(rotors[0])
	__key_max = max(rotors[0])
	__value_min = min(rotors[0].values())
	__value_max = max(rotors[0].values())
	__len = len(rotors[0])
	__random = __check_rand_rotor(rotors[0])
	
	for rotor in rotors:
		if __key_min != min(rotor) or __key_max != max(rotor) or __len != len(rotor) or __random != __check_rand_rotor(rotor)\
				or __value_min != min(rotor.values()) or __value_max != max(rotor.values()):
			return False, __random
	return True, __random


# todo I know what you mean :) but it's only to see if it's possible.
# todo In any case, how to find "statement with out any effect"
def gen_text(char_max, ran, size_triple, rotor_for_gen, *char_size):
	print("Dorób proces postępu gen_text ")
	x = []
	if len(char_size) == 1:
		char = char_size[0]
		size = 1
	else:
		if len(char_size) == 2:
			char = char_size[0]
			size = char_size[1]
		else:
			char = 0
			size = 1
	
	rotor_for_gen = dict(rotor_for_gen)
	[[[x.append(randint(0, len(rotor_for_gen) - 1) if ran else char) for _ in range(3 * len(rotor_for_gen))]
	  if not char_max else [x.append(len(rotor_for_gen) - 1) for _ in range(3 * len(rotor_for_gen))]]
	 if size_triple else [[x.append(randint(0, len(rotor_for_gen) - 1) if ran else char) for _ in range(size)]
	                      if not char_max else [x.append(len(rotor_for_gen) - 1) for _ in range(size)]]]
	return x


def check_text_const(text_before):
	for i in range(1, len(text_before)):
		if text_before[0] != text_before[i]:
			return False
	return True


def encrypt(rotors, key_enc, text_before):
	# internal_key_enc = __generate_inter_key(key_enc, rotors)
	encrypt_rotors = [EncryptNextRotor(rotor) for rotor in rotors]
	encrypt_first = EncryptSet(key_enc[:], text_before[:], rotors)
	
	enc = [True]
	while True:
		enc = encrypt_first.set_enc_chain(enc)
		for encrypt_rotor in encrypt_rotors:
			enc = encrypt_rotor.encrypt(enc)
		if not enc[-1]:
			break
	text_encrypt = encrypt_first.get_encrypt_list()
	return text_encrypt


def decrypt(rotors, key_dec, text_encrypt):
	# internal_key_dec = __generate_inter_key(key_dec, rotors)
	decrypt_rotors = [DecryptNextRotor(rotor) for rotor in rotors]
	decrypt_first = DecryptSet(key_dec[:], text_encrypt[:], rotors)
	
	dec = [True]
	while True:
		dec = decrypt_first.set_dec_chain(dec)
		for decrypt_rotor in reversed(decrypt_rotors):
			dec = decrypt_rotor.decrypt(dec)
		if not dec[-1]:
			break
	text_decrypt = decrypt_first.get_decrypt_list()
	return text_decrypt


def check_all_patterns(text_encrypt, min_pattern, max_pattern, max_num_patterns=1, number_of_check_patterns=0,
                       del_patterns=[], show=False,
                       mark=-1):  # todo make optimizations, chyba przelatuje zakres jak sprawdzalem DNA !!!
	t_i = text_encrypt[:]  # text internal
	min_p = min_pattern  # min length pattern
	max_p = max_pattern  # 300 #len(t_i) // 2
	stop_if = max_pattern
	p_l = []  # pattern list
	min = 0
	pf = 0
	ps = 0
	i_m = mark  # internal mark
	
	if del_patterns:
		for i in del_patterns:
			p_len = i[0]
			i.pop(0)
			i.pop(0)
			for ii in i:
				t_i[ii: p_len + ii] = [i_m for _ in range(ii, p_len + ii)]
	
	while True:
		if number_of_check_patterns != 0:
			if stop_if - max_p >= number_of_check_patterns:
				print(("\rPatterns shorter, only {} first:".format(max_num_patterns) + " " * 20)[:49] + str(
					[p_l if p_l else "[None]"])[2:-2]) if show else None
				sys.stdout.write("\r")
				return p_l
		# sys.stdout.write(str((str("\rPatterns 3 shorter in progres ..." + " " * 15,),
		#                  str(([patt for patt in p_l])[1:])[:-1], str((len(t_i[min + pf: max_p + pf]), min + pf, max_p + pf + ps)))))
		
		# sys.stdout.write(("\rPatterns 3 shorter in progres ..." + " " * 15 + str((len(t_i[min + pf: max_p + pf]), min + pf, max_p + pf + ps))))
		# time.sleep(0.1)
		sys.stdout.write(("\rPatterns shorter, only {} first in progress ...".format(max_num_patterns) + " " * 7)[:49] +
		                 str(p_l)[1:-1] + str([', ' if p_l else ""])[2:-2] + str(
			list([len(t_i[min + pf: max_p + pf]), min + pf, max_p + pf + ps]))) \
			if show else None
		# sys.stdout.write(("\r" + "Patterns over, only {} first in progress ...".format(num_of_pat) + " " * 7)[:49])
		# sys.stdout.write(("\r" + "Patterns over, only first in progres ..." + " " * 8 + str(list_of_patterns)[1:-1] +
		#                   str([len(text_to_check_inter[0: m + i]), nr_del, nr_del + (m + i),
		#                        nr_del + (m + i) * 2])))  # [0:82])
		
		# print(str(([patt for patt in p_l])[1:])[:-1], "\b", len(t_i[min + pf: max_p + pf]), min + pf, max_p + pf + ps)
		if len(p_l) >= max_num_patterns:
			print(("\rPatterns shorter, only {} first:".format(max_num_patterns) + " " * 20)[:49] + str(
				[p_l if p_l else "[None]"])[1:-1]) if show else None
			sys.stdout.write("\r")
			return p_l
		# -1 in Stały ?
		if i_m not in t_i[min + pf: max_p + pf]:
			# -1 in Ruchomy ?
			if i_m not in t_i[max_p + pf + ps: 2 * max_p + pf + ps]:
				# Stały == Ruchomy ?
				if t_i[min + pf: max_p + pf] == t_i[max_p + pf + ps: 2 * max_p + pf + ps]:
					# Save and zamień na -1
					p_l.append([len(t_i[min + pf: max_p + pf]), min + pf, max_p + pf + ps])
					t_i[max_p + pf + ps: 2 * max_p + pf + ps] = [i_m for _ in
					                                             range(max_p + pf + ps, 2 * max_p + pf + ps)]
			# Ruchomy END ?
			if t_i[max_p + pf + ps: 2 * max_p + pf + ps] == t_i[-len(t_i[max_p + pf + ps: 2 * max_p + pf + ps]):]:
				# Stały END ?
				if t_i[min + pf: max_p + pf] + t_i[max_p + pf + ps: 2 * max_p + pf + ps] == t_i[-2 * len(
						t_i[max_p + pf + ps: 2 * max_p + pf + ps]):]:
					# Len min ?
					if len(t_i[min + pf: max_p + pf]) < min_p:
						# STOP
						print(
							("\rPatterns shorter, only {} first:".format(max_num_patterns) + " " * 20)[:49] + str(p_l)[
							                                                                                  1:-1]) if show else None
						sys.stdout.write("\r")
						return p_l
					# Stały -1, Ruchomy - 1, Stały << p, Ruchomy << p
					else:
						max_p -= 1
						pf = 0
						ps = 0
				# stały >> 1, Ruch << p
				else:
					pf += 1
					ps = 0
			# ruch >> 1
			else:
				ps += 1
		else:
			if t_i[min + pf: max_p + pf] + t_i[max_p + pf + ps: 2 * max_p + pf + ps] == t_i[-2 * len(
					t_i[max_p + pf + ps: 2 * max_p + pf + ps]):]:
				# Len min ?
				if len(t_i[min + pf: max_p + pf]) < min_p:
					# STOP
					print(("\rPatterns shorter, only {} first:".format(max_num_patterns) + " " * 20)[:49] +
					      str(p_l)[1:-1]) if show else None
					sys.stdout.write("\r")
					return p_l
				# Stały -1, Ruchomy - 1, Stały << p, Ruchomy << p
				else:
					max_p -= 1
					pf = 0
					ps = 0
			# stały >> 1, Ruch << p
			else:
				pf += 1
				ps = 0


def check_patterns(text_to_check, min_len = 4, max_num_patterns = 1, show = False): #todo https://www.tutorialspoint.com/python/string_find.htm
	p_l = []        # pattern list
	m = min_len
	nr_del = 0
	text_to_check_inter = text_to_check[:]
	while True:
		for i in range(0, len(text_to_check_inter)):
			# print("test")
			if show:
				# time.sleep(0.01)
				sys.stdout.write((("\rPatterns over, only {} first in progress ...".format(max_num_patterns) + " " * 7)[:49] + str(p_l)[1:-1] + str([', ' if p_l else ""])[2:-2] +
				                  str([len(text_to_check_inter[0: m + i]), nr_del, nr_del + (m + i), nr_del + (m + i) * 2])))# + ", "))#[0:82])
			# time.sleep(0.001)
			# if len(p_l) <= num_of_pat:
			# 	if p_l:
			# 		# len_patt = len(p_l)
			# 		sys.stdout.write("\rProgress :\t\t\t\t\t\t\t\t %s " % [i for i in p_l])
					# sys.stdout.flush()
			# print(p_l)
			# print("\rProgress decrypt:\t\t\t\t\t\t\t\t[100 %]")
			# else:
			# 	# sys.stdout.write("\rProgress decrypt:\t\t\t\t\t\t\t\t[%.4f %%]    " % (progress))
			
			
			if (m + i) * 3 > len(text_to_check_inter):
				break
			if text_to_check_inter[0: m + i] == text_to_check_inter[m + i: (m + i) * 2] == \
					text_to_check_inter[(m + i) * 2: (m + i) * 3]:
				p_l.append([len(text_to_check_inter[0: m + i]), nr_del, nr_del + (m + i), nr_del + (m + i) * 2])
				if len(p_l) == max_num_patterns:
					if show:
						print(str("\rPatterns over, first {}:".format(max_num_patterns) + " " * 30)[:49] + str(p_l)[1:-1])
					return p_l
		if len(text_to_check_inter) >= 1:
			text_to_check_inter.pop(0)
			nr_del += 1
		else:
			break
		if p_l:
			if show:
				print(str("\rPatterns over, first {}:".format(max_num_patterns) + " " * 30)[:49] + (str(p_l))[1:-1])
			return p_l
	sys.stdout.write("\r")
	return False

# todo do usunięcia ?!?!?
def create_key(key_my, rotors):
	dic_64b_1 = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "a": 10,
	             "b": 11, "c": 12, "d": 13, "e": 14, "f": 15, "g": 16, "h": 17, "i": 18, "j": 19, "k": 20,
	             "l": 21, "m": 22, "n": 23, "o": 24, "p": 25, "q": 26, "r": 27, "s": 28, "t": 29, "u": 30,
	             "v": 31, "w": 32, "x": 33, "y": 34, "z": 35, "A": 36, "B": 37, "C": 38, "D": 39, "E": 40,
	             "F": 41, "G": 42, "H": 43, "I": 44, "J": 45, "K": 46, "L": 47, "M": 48, "N": 49, "O": 50,
	             "P": 51, "Q": 52, "R": 53, "S": 54, "T": 55, "U": 56, "V": 57, "W": 58, "X": 59, "Y": 60,
	             "Z": 61, "+": 62, "/": 63}
	
	if isinstance(key_my, str):
		key_my = key_my.lower()
		number_in_32b = 0
		i = 0
		while key_my:
			number_in_32b += dic_64b_1[key_my[-(1 + i)]] * (32 ** i)
			i += 1
			if len(key_my) == i:
				break
		i = 0
		key = [0, ]
		while number_in_32b:
			key[i] = number_in_32b % (len(rotors[0]))
			number_in_32b //= (len(rotors[0]))
			i += 1
			if number_in_32b < (len(rotors[0])):
				key += [number_in_32b, ]
				break
			key += [0, ]
		key = reversed(key)
		return list(key)
	else:
		return key_my

# change key if 64b to DEC
def key_from_64b_to_dec(key_my):
	dic_32b = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "a": 10,
	           "b": 11, "c": 12, "d": 13, "e": 14, "f": 15, "g": 16, "h": 17, "i": 18, "j": 19, "k": 20,
	           "l": 21, "m": 22, "n": 23, "o": 24, "p": 25, "r": 26, "s": 27, "t": 28, "u": 29, "v": 30, "w": 31}

	number_in_32b = 0
	if isinstance(key_my, str):
		key_my = key_my.lower()
		i = 0
		while key_my:
			number_in_32b += dic_32b[key_my[-(1 + i)]] * (32 ** i)
			i += 1
			if len(key_my) == i:
				break
	return number_in_32b


# def __generate_inter_key(key, rotors, show=False):
# 	dic_64b_1 = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "a": 10,
# 	             "b": 11, "c": 12, "d": 13, "e": 14, "f": 15, "g": 16, "h": 17, "i": 18, "j": 19, "k": 20,
# 	             "l": 21, "m": 22, "n": 23, "o": 24, "p": 25, "q": 26, "r": 27, "s": 28, "t": 29, "u": 30,
# 	             "v": 31, "w": 32, "x": 33, "y": 34, "z": 35, "A": 36, "B": 37, "C": 38, "D": 39, "E": 40,
# 	             "F": 41, "G": 42, "H": 43, "I": 44, "J": 45, "K": 46, "L": 47, "M": 48, "N": 49, "O": 50,
# 	             "P": 51, "Q": 52, "R": 53, "S": 54, "T": 55, "U": 56, "V": 57, "W": 58, "X": 59, "Y": 60,
# 	             "Z": 61, "+": 62, "/": 63}
#
# 	# 64b transformed to DEC
# 	rand_num_in_DEC_from_64b = 0
# 	exponent = 0
# 	num_in_64b = key[:]
# 	for i in num_in_64b:
# 		rand_num_in_DEC_from_64b += (dic_64b_1[i] * (64 ** exponent))
# 		exponent += 1
# 	if show:
# 		print("Random number in DEC from 64b: ")
# 		for i in range(0, len(str(rand_num_in_DEC_from_64b)) + 60, 60):
# 			if str(rand_num_in_DEC_from_64b)[i: 60 + i]:
# 				print(str(rand_num_in_DEC_from_64b)[i: 60 + i])
# 			else:
# 				# print("")
# 				break
# 	# print(str(rand_num_in_DEC_from_64b)[i: 60 + i])
# 	# rand_num_in_DEC_from_64b_save = rand_num_in_DEC_from_64b
#
# 	# Generate internal key from DEC
# 	i = 0
# 	inter_key = [0, ]
# 	while rand_num_in_DEC_from_64b:
# 		inter_key[i] = rand_num_in_DEC_from_64b % (len(rotors[0]))
# 		rand_num_in_DEC_from_64b //= (len(rotors[0]))
# 		i += 1
# 		if rand_num_in_DEC_from_64b < (len(rotors[0])):
# 			inter_key += [rand_num_in_DEC_from_64b, ]
# 			break
# 		inter_key += [0]
# 	# inter_key = inter_key[::-1]   # the number in the correct order, without this number, is invert
# 	if len(inter_key) % len(rotors) != 0:
# 		add_zeros = abs((len(inter_key) % len(rotors)) - len(rotors))
# 		for _ in range(0, add_zeros):
# 			inter_key.insert(0, 0)
#
# 	if show:
# 		print("\nInternal key: ")
# 		for i in range(0, len(str(inter_key)) + 60, 60):
# 			if str(inter_key)[i: 60 + i]:
# 				print(str(inter_key)[i: 60 + i])
# 			else:
# 				# print("")
# 				break
# 		print(str(inter_key)[i: 60 + i])
# 		if (len(inter_key) % len(rotors) != 0):
# 			print("\nFail")
# 			return False
# 		else:
# 			print("\nPass")
# 	return inter_key


#
def create_random_64b_key(size_in_bit = 2, rotors = [], show = False): #todo usuń rotors !!!
	dic_64b_1 = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "a": 10,
	             "b": 11, "c": 12, "d": 13, "e": 14, "f": 15, "g": 16, "h": 17, "i": 18, "j": 19, "k": 20,
	             "l": 21, "m": 22, "n": 23, "o": 24, "p": 25, "q": 26, "r": 27, "s": 28, "t": 29, "u": 30,
	             "v": 31, "w": 32, "x": 33, "y": 34, "z": 35, "A": 36, "B": 37, "C": 38, "D": 39, "E": 40,
	             "F": 41, "G": 42, "H": 43, "I": 44, "J": 45, "K": 46, "L": 47, "M": 48, "N": 49, "O": 50,
	             "P": 51, "Q": 52, "R": 53, "S": 54, "T": 55, "U": 56, "V": 57, "W": 58, "X": 59, "Y": 60,
	             "Z": 61, "+": 62, "/": 63}
	
	dic_64b_2 = {}
	for inter_key, value in dic_64b_1.items():
		dic_64b_2[value] = inter_key
	
	# Random number in DEC
	rand_num_in_DEC = randint(2 ** size_in_bit, (2 ** (size_in_bit + 1)) - 1)
	if show:
		print("Size of the number in bit: ", int(log(rand_num_in_DEC, 2)))
		print("Random number in DEC: ")
		for i in range(0, len(str(rand_num_in_DEC)) + 60, 60):
			if str(rand_num_in_DEC)[i: 60 + i]:
				print(str(rand_num_in_DEC)[i: 60 + i])
			else:
				print("")
				break
	rand_num_in_DEC_save = rand_num_in_DEC
	
	# DEC transformed to 64b
	rand_num_in_64b = ""
	while rand_num_in_DEC:
		mod = rand_num_in_DEC % 64
		one_64b = dic_64b_2[mod]
		rand_num_in_64b += one_64b
		rand_num_in_DEC //= 64
	if show:
		print("Random number in 64b: ")
		for i in range(0, len(str(rand_num_in_64b)) + 60, 60):
			if str(rand_num_in_64b)[i: 60 + i]:
				print(str(rand_num_in_64b)[i: 60 + i])
			else:
				print("")
				break
	
	# return __generate_inter_key(rand_num_in_64b, rotors)
	return str(rand_num_in_64b)  # todo usuń rotors
	# # 64b transformed to DEC
	# rand_num_in_DEC_from_64b = 0
	# exponent = 0
	# for i in rand_num_in_64b:
	# 	rand_num_in_DEC_from_64b += (dic_64b_1[i] * (64 ** exponent))
	# 	exponent += 1
	# if show:
	# 	print("Random number in DEC from 64b: ")
	# 	for i in range(0, len(str(rand_num_in_DEC_from_64b)) + 60, 60):
	# 		if str(rand_num_in_DEC_from_64b)[i: 60 + i]:
	# 			print(str(rand_num_in_DEC_from_64b)[i: 60 + i])
	# 		else:
	# 			# print("")
	# 			break
	# 		# print(str(rand_num_in_DEC_from_64b)[i: 60 + i])
	# rand_num_in_DEC_from_64b_save = rand_num_in_DEC_from_64b
	#
	# # Generate internal key from DEC
	# i = 0
	# inter_key = [0, ]
	# while rand_num_in_DEC_from_64b:
	# 	inter_key[i] = rand_num_in_DEC_from_64b % (len(rotors[0]))
	# 	rand_num_in_DEC_from_64b //= (len(rotors[0]))
	# 	i += 1
	# 	if rand_num_in_DEC_from_64b < (len(rotors[0])):
	# 		inter_key += [rand_num_in_DEC_from_64b, ]
	# 		break
	# 	inter_key += [0]
	# # inter_key = inter_key[::-1]   # the number in the correct order, without this number, is invert
	# if len(inter_key) % len(rotors) != 0:
	# 	add_zeros = abs((len(inter_key) % len(rotors)) - len(rotors))
	# 	for _ in range(0, add_zeros):
	# 		inter_key.insert(0,0)
	#
	# if show:
	# 	print("\nInternal key: ")
	# 	for i in range(0, len(str(inter_key)) + 60, 60):
	# 		if str(inter_key)[i: 60 + i]:
	# 			print(str(inter_key)[i: 60 + i])
	# 		else:
	# 			# print("")
	# 			break
	# 		# print(str(inter_key)[i: 60 + i])
	# 	if (rand_num_in_DEC_save != rand_num_in_DEC_from_64b_save) or (len(inter_key) % len(rotors) != 0):
	# 		print("\nFail\n")
	# 		return False
	# 	else:
	# 		print("\nPass\n")
	# return inter_key, rand_num_in_64b
	
def calc_number_comb(rotors, key):
	if isinstance(key, str):
		for i in range(len(rotors), 0, -1):
			if len(generate_from_64b_inter_key(key, rotors)) % i == 0:
				cal_pattern_length = (len(rotors[0]) ** i) ** (len(generate_from_64b_inter_key(key, rotors)) // i)
				return cal_pattern_length
	else:
		for i in range(len(rotors), 0, -1):
				cal_pattern_length = (len(rotors[0]) ** i) ** (len(key) // i)
				return 	cal_pattern_length
		# return key
		# cal_pattern_length = (len(rotors[0]) ** len(rotors))
		# return cal_pattern_length
		
def print_long(name, objects, min, max, show_all = False):
	order_number = 1
	space = min - len(name)
	if not(len(objects) > 1 and (isinstance(objects[1], dict) or isinstance(objects[1], list))):
		objects = str(objects)
	if not isinstance(objects, str):
		for obj in objects:
			name_int = str(name + " " + str(order_number) + ":" + (" " * (space - len(str(order_number)))))
			if (len(name_int + str(obj)) > max) and not show_all:
				name_int2 = name_int + str(obj)[0:((max - len(name_int)) // 2) - 6] + "  +...+  "
				print(name_int2 + str(obj)[-(max - len(name_int2)):])
			else:
				if (len(name_int + str(obj)) > max) and show_all:
					obj_str = str(obj)
					print(name_int + obj_str[0:max - len(name_int)])
					for i in range(max - len(name_int), len(obj_str), max - len(name_int) ):
						print(" " * len(name_int) + obj_str[i: i + max - len(name_int)])
				else:
					print(name_int + str(obj))
			order_number += 1
	else:
		if isinstance(objects, str):
			obj = objects
			name_int = str(name + ":" + (" " * (space + len(str(order_number)))))
			if (len(name_int + str(obj)) > max) and not show_all:
				# a = 0
				# print(max, space, len(name_int))
				# if (max - space) % 2 == 0:
				# 	a = 1
				# # else:
				# # 	a = 9
				name_int2 = name_int + str(obj)[0:((max - len(name_int)) // 2) - 6] + "  +...+  "
				print(name_int2 + str(obj)[-(max - len(name_int2)):])
			else:
				if (len(name_int + str(obj)) > max) and show_all:
					obj_str = str(obj)
					print(name_int + obj_str[0:max - len(name_int)])
					for i in range(max - len(name_int), len(obj_str), max - len(name_int)):
						print(" " * len(name_int) + obj_str[i: i + max - len(name_int)])
				else:
					print(name_int + obj)
					
def convert_str_to_list(text_before):
	text_in_list = []
	for c in text_before:
		text_in_list.append(ord(c))
	return text_in_list

def convert_list_to_str(text_before):
	text_in_str = ''
	for c in text_before:
		text_in_str += chr(c)
	return text_in_str


def show_help(place):
	print(place)
	print("""
Simple programme for encrypts and decrypts files.
Usage:      enigma5 -c [file of files, you can use reg.]
                Encryption the file (default key will be used the last created in the keys directory,
                the drums will be loaded with all the last ones created in the rotors directory)
            enigma5 -d [file of files, you can use reg.]
                Decryption the file (default are the same as with encryption)
            enigma5 -c [file] -k [file or key name in dictionary keys]
                Encryption with the indicated key
            enigma5 -d [file] -k [file or key name in dictionary keys]
                Decryption with the indicated key
            enigma5 -c [file] -k [file] -r [first rotor file, or name in dictionary rotors]
                Encryption with the indicated key and indicated rotors and their number
            enigma5 -d [file] -k [file] -r [first rotor file, or name in dictionary rotors]
                Decryption with the indicated key and indicated rotors and their number
            
            enigma5 -R [name], [number]     Create rotors, name only common part, number of created rotors
            enigma5 -K [name], [size]       Create key, size in bits
            
            enigma5 -v --verbose            Show all progress
            # todo enigma5 -t --tests              Run tests encrypt and decrypt
            enigma5 -h --help               Display this help and exit
            enigma5 -V --version            Output version information and exit
   
Examples:   enigma5.py -K your_key_name 2048
                First you need to create a random key, 2048 it is size in bit
            enigma5.py -R your_rotors_name 20
                Then you have to create a random 8-bit rotors, 8bit is the default setting for files,
                20 is the number of rotors
            enigma5.py -c some_file.txt [-k your_key_name] [-r your_rotors_name]
                Now you can encrypt any file or files if you use reg. [for example *], encrypted files
                will be updated .enc. You can also use a different key or rotors if you insert the -k or -r option.
                By default, the most recently created keys and rotors are loaded from the keys and rotors
                catalogs from the enigma5.py directory.
            enigma5.py -d some_file.txt.enc [-k your_key_name] [-r your_rotors_name]
                And last you can decrypt file or files, remember that you must use the same rotors and keys as
                 you use to encrypt, what is logically
	""")
	exit()