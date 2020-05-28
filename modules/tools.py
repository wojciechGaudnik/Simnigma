# only functions to generate, load, save, check itp..

from random import randint
from math import log

import inspect
import os
import sys
import pickle

from .__tools_single import __cre_rotor, __save_rotor, __load_rotor, __check_rand_rotor, generate_from_64b_inter_key, \
	bcolors
from .core import EncryptNextRotor, EncryptSet, DecryptNextRotor, DecryptSet


def create_rotors(size_in_bit, mix, number_of_rotors):  # todo daj mix Tru i na koncu
	size = 2 ** size_in_bit
	return ([__cre_rotor(size, mix) for _ in range(0, number_of_rotors)])


def check_rand_rotors(rotors):
	__key_min = min(rotors[0])
	__key_max = max(rotors[0])
	__value_min = min(rotors[0].values())
	__value_max = max(rotors[0].values())
	__len = len(rotors[0])
	__random = __check_rand_rotor(rotors[0])
	
	for rotor in rotors:
		if __key_min != min(rotor) or __key_max != max(rotor) or __len != len(rotor) or __random != __check_rand_rotor(
				rotor) \
				or __value_min != min(rotor.values()) or __value_max != max(rotor.values()):
			return False, __random
	return True, __random

number_of_printd = 0

def print_format_table():
	"""
    prints table of formatted text format options
    """
	for style in range(10):
		for fg in range(20, 40):
			s1 = ''
			for bg in range(35, 60):
				format = ';'.join([str(style), str(fg), str(bg)])
				s1 += '\x1b[%sm %s \x1b[0m' % (format, format)
			print(s1)
		print('\n')

# def gen_text(char_max, ran, size_triple, rotor_for_gen, *char_size):
# 	print("Dorób proces postępu gen_text ")
# 	x = []
# 	if len(char_size) == 1:
# 		char = char_size[0]
# 		size = 1
# 	else:
# 		if len(char_size) == 2:
# 			char = char_size[0]
# 			size = char_size[1]
# 		else:
# 			char = 0
# 			size = 1
#
# 	rotor_for_gen = dict(rotor_for_gen)
# 	[[[x.append(randint(0, len(rotor_for_gen) - 1) if ran else char) for _ in range(3 * len(rotor_for_gen))]
# 	if not char_max else [x.append(len(rotor_for_gen) - 1) for _ in range(3 * len(rotor_for_gen))]]
# 	if size_triple else [[x.append(randint(0, len(rotor_for_gen) - 1) if ran else char) for _ in range(size)]
# 	if not char_max else [x.append(len(rotor_for_gen) - 1) for _ in range(size)]]]
# 	return x


def check_text_const(text_before):
	for i in range(1, len(text_before)):
		if text_before[0] != text_before[i]:
			return False
	return True


def encrypt(rotors, key_enc, text_before, show=False):
	encrypt_rotors = [EncryptNextRotor(rotor) for rotor in rotors]
	encrypt_first = EncryptSet(key_enc[:], text_before[:], rotors, show=show)
	enc = [True]
	while True:
		enc = encrypt_first.set_enc_chain(enc)
		for encrypt_rotor in encrypt_rotors:
			enc = encrypt_rotor.encrypt(enc)
		if not enc[-1]:
			break
	text_encrypt = encrypt_first.get_encrypt_list()
	return text_encrypt


def decrypt(rotors, key_dec, text_encrypt, show=False):
	decrypt_rotors = [DecryptNextRotor(rotor) for rotor in rotors]
	decrypt_first = DecryptSet(key_dec[:], text_encrypt[:], rotors, show=show)
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
		del_patterns=None, show=False,
		mark=-1):
	if del_patterns is None:
		del_patterns = []
	t_i = text_encrypt[:]
	min_p = min_pattern
	max_p = max_pattern
	stop_if = max_pattern
	p_l = []
	min = 0
	pf = 0
	ps = 0
	i_m = mark
	
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
		sys.stdout.write(("\rPatterns shorter, only {} first in progress ...".format(max_num_patterns) + " " * 7)[:49] +
		                 str(p_l)[1:-1] + str([', ' if p_l else ""])[2:-2] + str(
			list([len(t_i[min + pf: max_p + pf]), min + pf, max_p + pf + ps]))) \
			if show else None
		if len(p_l) >= max_num_patterns:
			print(("\rPatterns shorter, only {} first:".format(max_num_patterns) + " " * 20)[:49] + str(
				[p_l if p_l else "[None]"])[1:-1]) if show else None
			sys.stdout.write("\r")
			return p_l
		if i_m not in t_i[min + pf: max_p + pf]:
			if i_m not in t_i[max_p + pf + ps: 2 * max_p + pf + ps]:
				if t_i[min + pf: max_p + pf] == t_i[max_p + pf + ps: 2 * max_p + pf + ps]:
					p_l.append([len(t_i[min + pf: max_p + pf]), min + pf, max_p + pf + ps])
					t_i[max_p + pf + ps: 2 * max_p + pf + ps] = [i_m for _ in
						range(max_p + pf + ps, 2 * max_p + pf + ps)]
			if t_i[max_p + pf + ps: 2 * max_p + pf + ps] == t_i[-len(t_i[max_p + pf + ps: 2 * max_p + pf + ps]):]:
				if t_i[min + pf: max_p + pf] + t_i[max_p + pf + ps: 2 * max_p + pf + ps] == t_i[-2 * len(
						t_i[max_p + pf + ps: 2 * max_p + pf + ps]):]:
					if len(t_i[min + pf: max_p + pf]) < min_p:
						print(
							("\rPatterns shorter, only {} first:".format(max_num_patterns) + " " * 20)[:49] + str(p_l)[
							1:-1]) if show else None
						sys.stdout.write("\r")
						return p_l
					else:
						max_p -= 1
						pf = 0
						ps = 0
				else:
					pf += 1
					ps = 0
			else:
				ps += 1
		else:
			if t_i[min + pf: max_p + pf] + t_i[max_p + pf + ps: 2 * max_p + pf + ps] == t_i[-2 * len(
					t_i[max_p + pf + ps: 2 * max_p + pf + ps]):]:
				if len(t_i[min + pf: max_p + pf]) < min_p:
					print(("\rPatterns shorter, only {} first:".format(max_num_patterns) + " " * 20)[:49] +
					      str(p_l)[1:-1]) if show else None
					sys.stdout.write("\r")
					return p_l
				else:
					max_p -= 1
					pf = 0
					ps = 0
			else:
				pf += 1
				ps = 0


def check_patterns(text_to_check, min_len=4, max_num_patterns=1,
		show=False):
	p_l = []
	m = min_len
	nr_del = 0
	text_to_check_inter = text_to_check[:]
	while True:
		for i in range(0, len(text_to_check_inter)):
			if show:
				sys.stdout.write((("\rPatterns over, only {} first in progress ...".format(max_num_patterns) + " " * 7)[
				                  :49] + str(p_l)[1:-1] + str([', ' if p_l else ""])[2:-2] +
				                  str([len(text_to_check_inter[0: m + i]), nr_del, nr_del + (m + i),
					                  nr_del + (m + i) * 2])))
			if (m + i) * 3 > len(text_to_check_inter):
				break
			if text_to_check_inter[0: m + i] == text_to_check_inter[m + i: (m + i) * 2] == \
					text_to_check_inter[(m + i) * 2: (m + i) * 3]:
				p_l.append([len(text_to_check_inter[0: m + i]), nr_del, nr_del + (m + i), nr_del + (m + i) * 2])
				if len(p_l) == max_num_patterns:
					if show:
						print(
							str("\rPatterns over, first {}:".format(max_num_patterns) + " " * 30)[:49] + str(p_l)[1:-1])
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

def key_from_64b_to_dec(key_my):
	dic_64b_1 = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "a": 10,
		"b": 11, "c": 12, "d": 13, "e": 14, "f": 15, "g": 16, "h": 17, "i": 18, "j": 19, "k": 20,
		"l": 21, "m": 22, "n": 23, "o": 24, "p": 25, "q": 26, "r": 27, "s": 28, "t": 29, "u": 30,
		"v": 31, "w": 32, "x": 33, "y": 34, "z": 35, "A": 36, "B": 37, "C": 38, "D": 39, "E": 40,
		"F": 41, "G": 42, "H": 43, "I": 44, "J": 45, "K": 46, "L": 47, "M": 48, "N": 49, "O": 50,
		"P": 51, "Q": 52, "R": 53, "S": 54, "T": 55, "U": 56, "V": 57, "W": 58, "X": 59, "Y": 60,
		"Z": 61, "+": 62, "/": 63}
	
	number_in_dec = 0
	i = 0
	if isinstance(key_my, str):
		for h in key_my:
			number_in_dec += dic_64b_1[h] * (64 ** i)
			i += 1
	return number_in_dec


def check_64b_key(key_my):
	dic_64b_1 = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "a": 10,
		"b": 11, "c": 12, "d": 13, "e": 14, "f": 15, "g": 16, "h": 17, "i": 18, "j": 19, "k": 20,
		"l": 21, "m": 22, "n": 23, "o": 24, "p": 25, "q": 26, "r": 27, "s": 28, "t": 29, "u": 30,
		"v": 31, "w": 32, "x": 33, "y": 34, "z": 35, "A": 36, "B": 37, "C": 38, "D": 39, "E": 40,
		"F": 41, "G": 42, "H": 43, "I": 44, "J": 45, "K": 46, "L": 47, "M": 48, "N": 49, "O": 50,
		"P": 51, "Q": 52, "R": 53, "S": 54, "T": 55, "U": 56, "V": 57, "W": 58, "X": 59, "Y": 60,
		"Z": 61, "+": 62, "/": 63}
	
	for k in key_my:
		if k in dic_64b_1:
			continue
		else:
			return False
	return True

def create_random_64b_key(size_in_bit=2, max_print_length=110, show=False):
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
		for i in range(0, len(str(rand_num_in_DEC)) + max_print_length, max_print_length):
			if str(rand_num_in_DEC)[i: max_print_length + i]:
				print(str(rand_num_in_DEC)[i: max_print_length + i])
			else:
				print("")
				break
	
	# DEC transformed to 64b
	rand_num_in_64b = ""
	while rand_num_in_DEC:
		mod = rand_num_in_DEC % 64
		one_64b = dic_64b_2[mod]
		rand_num_in_64b += one_64b
		rand_num_in_DEC //= 64
	if show:
		print("Random number in 64b: ")
		for i in range(0, len(str(rand_num_in_64b)) + max_print_length, max_print_length):
			if str(rand_num_in_64b)[i: max_print_length + i]:
				print(str(rand_num_in_64b)[i: max_print_length + i])
			else:
				print("")
				break
	return str(rand_num_in_64b)

def calc_number_comb(rotors, key):
	if isinstance(key, str):
		for i in range(len(rotors), 0, -1):
			if len(generate_from_64b_inter_key(key, rotors)) % i == 0:
				cal_pattern_length = (len(rotors[0]) ** i) ** (len(generate_from_64b_inter_key(key, rotors)) // i)
				return cal_pattern_length
	else:
		for i in range(len(rotors), 0, -1):
			cal_pattern_length = (len(rotors[0]) ** i) ** (len(key) // i)
			return cal_pattern_length

def print_long(name, objects, min, max, show_all=False):
	order_number = 1
	space = min - len(name)
	if not (len(objects) > 1 and (isinstance(objects[1], dict) or isinstance(objects[1], list))):
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
					for i in range(max - len(name_int), len(obj_str), max - len(name_int)):
						print(" " * len(name_int) + obj_str[i: i + max - len(name_int)])
				else:
					print(name_int + str(obj))
			order_number += 1
	else:
		if isinstance(objects, str):
			obj = objects
			name_int = str(name + ":" + (" " * (space + len(str(order_number)))))
			if (len(name_int + str(obj)) > max) and not show_all:
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


def show_help(message='', show=True):
	if show:
		print("""
Simple programme for encrypts and decrypts files.
Usage:      simnigma -c [file of files, you can use reg.]
                Encryption the file (default key will be used the last created in the keys directory,
                the drums will be loaded with all the last ones created in the rotors directory)
            simnigma -d [file of files, you can use reg.]
                Decryption the file (default are the same as with encryption)
            simnigma -c [file] -k [file or key name in dictionary keys]
                Encryption with the indicated key
            simnigma -d [file] -k [file or key name in dictionary keys]
                Decryption with the indicated key
            simnigma -c [file] -k [file] -r [first rotor file, or name in dictionary rotors]
                Encryption with the indicated key and indicated rotors and their number
            simnigma -d [file] -k [file] -r [first rotor file, or name in dictionary rotors]
                Decryption with the indicated key and indicated rotors and their number
            
            simnigma -R [name], [number]     Create rotors, name only common part, number of created rotors
            simnigma -K [name], [size]       Create key, size in bits
            
            simnigma -v --verbose            Show all progress
            # todo simnigma -t --tests              Run tests encrypt and decrypt
            simnigma -h --help               Display this help and exit
            simnigma -V --version            Output version information and exit
            
   
   
Examples:   simnigma.py -K your_key_name 2048
                First you need to create a random key, 2048 it is size in bit
            simnigma.py -R your_rotors_name 20
                Then you have to create a random 8-bit rotors, 8bit is the default setting for files,
                20 is the number of rotors
            simnigma.py -c some_file.txt [-k your_key_name] [-r your_rotors_name]
                Now you can encrypt any file or files if you use reg. [for example *], encrypted files
                will be updated .enc. You can also use a different key or rotors if you insert the -k or -r option.
                By default, the most recently created keys and rotors are loaded from the keys and rotors
                catalogs from the simnigma.py directory.
            simnigma.py -d some_file.txt.enc [-k your_key_name] [-r your_rotors_name]
                And last you can decrypt file or files, remember that you must use the same rotors and keys as
                 you use to encrypt, what is logically
	""")
	os.system('setterm -cursor on')
	if message:
		exit(bcolors.WARNING + 'Error: ' + message + bcolors.ENDC)
	else:
		os.system('setterm -cursor on'); exit()


def printd(*argss, debug=False, max_print_length=100):
	global number_of_printd
	if debug:
		line_no = inspect.stack()[1][2]
		frame = inspect.getouterframes(inspect.currentframe())[1]
		string = inspect.getframeinfo(frame[0]).code_context[0].strip()
		varibal_name = string[string.find('(') + 1:-1].split(',')
		
		for i, arg in enumerate(argss):
			number_of_printd += 1
			if len(str(arg)) > max_print_length - 30:
				print_long((bcolors.INYELLOW + '{} --- Debag line: {} ---{} ---> '.format(number_of_printd, line_no,
					varibal_name[i])), arg, 20, 140)
				print(bcolors.ENDC, end='')
			else:
				print(bcolors.INYELLOW + '{} --- Debag line: {} ---{} ---> '.format(number_of_printd, line_no,
					varibal_name[i]) + str(arg) + bcolors.ENDC)


def load_file_all(name, what_load='', show=False, number=0):
	"""
	
	:param name:
	:param what_load: 'key', 'rotors_from_one_file'
	:param show:
	:param number:
	:return:
	"""
	if what_load == 'key':
		name += ".key" if ".key" not in name[-4:] else ""
		key_list = []
		try:
			f = open(name, 'rb')
			key_list = f.read()
			f.close()
		except:
			show_help("Can't open key file {}".format(name), False)
		key = ""
		key_ret = ""
		for c in key_list:
			key += chr(c)
		key_ret = key_ret.join(key)
		if not key: show_help("File with key is empty", False)
		if show == True: print('Loaded key:   ', name, (int(log(key_from_64b_to_dec(key_ret[:-1]), 2))), 'bit')
		return key_ret[:-1]
	
	if what_load == 'rotors_from_one_file':
		name += ".rotors" if ".rotors" not in name[-7:] else ""
		rotors = {}
		try:
			f = open(name, 'rb')
			rotors = pickle.load(f)
			f.close()
			
			if show == True:  print('Loaded rotors:', name, len(rotors), 'items', str(int(log(len(rotors[0]), 2))),
				'bit')
		except EOFError:
			show_help("File with rotors is empty", False)
		except:
			show_help("Can't open rotors file {}".format(name), False)
		return rotors
	
	if what_load == 'rotors_from_files':
		name += ".rot" if ".rot" not in name[-4:] else ""
		return ([__load_rotor(x) for x in (name + '_' + str(x) for x in range(1, number + 1))])
	
	if what_load == 'file':
		file = []
		try:
			f = open(name, "rb")
			file = f.read()
			f.close()
			if show == True:  print('Loaded file:  ', name)
		except:
			exit(bcolors.WARNING + "Error: Can't open file {}".format(name) + bcolors.ENDC)
		file = list(file)
		return file[:-1]


def save_file_all(name, obj, what_save='', show=False):
	if what_save == 'key':
		name += ".key" if ".key" not in name[-4:] else ""
		f = open(name, "wb")
		try:
			f.write(bytes(obj + "\n", 'ascii'))
			f.close()
			if show == True: print('Saved key:     ', name)
		except:
			exit(bcolors.WARNING + "Error: Can't save key file {}".format(name) + bcolors.ENDC)
	
	if what_save == 'rotors_in_one_file':
		name += ".rotors" if ".rotors" not in name[-7:] else ""
		try:
			f = open(name, 'wb')
			pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)
			f.close()
			if show == True: print('Saved rotors: ', name)
		except:
			exit(bcolors.WARNING + "Error: Can't save rotors file {}".format(name) + bcolors.ENDC)
	
	if what_save == 'rotors_in_files':
		name += ".rot" if ".rot" not in name[-4:] else ""
		for i, rotor in enumerate(obj):
			__save_rotor(rotor, name + '_' + str(i + 1))
	
	if what_save == 'file':
		obj.append(10)
		try:
			f = open(name, "wb")
			f.write(bytes(obj))
			f.close()
			if show == True:  print('Saved file:   ', name)
		except:
			exit(bcolors.WARNING + "Error: Can't save file {}".format(name) + bcolors.ENDC)
