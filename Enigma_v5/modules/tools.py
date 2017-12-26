# only functions to generate, load, save, check itp..
from random import randint

from Enigma_all.Enigma_v5.modules.__tools_single \
	import (__cre_rotor, __save_rotor, __load_rotor, __check_rand_rotor)
from Enigma_all.Enigma_v5.modules.core import EncryptNextRotor, EncryptSet, DecryptNextRotor, DecryptSet


def create_rotors(size_in_bit, mix, number_of_rotors):
	size = 2 ** size_in_bit
	return ([__cre_rotor(size, mix) for _ in range(0, number_of_rotors)])
	
	
def save_rotors(rotors, name):
	i = 1
	for rotor in rotors:
		__save_rotor(rotor, name + str(i))
		i += 1
		
		
def load_rotors(name, number):
	return ([__load_rotor(x) for x in (name + str(x) for x in range(1, number + 1))])
	
	
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
	internal_key_enc = create_key(key_enc, rotors)
	encrypt_rotors = [EncryptNextRotor(rotor) for rotor in rotors]
	encrypt_first = EncryptSet(internal_key_enc[:], text_before[:], rotors[0])
	
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
	internal_key_dec = create_key(key_dec, rotors)
	decrypt_rotors = [DecryptNextRotor(rotor) for rotor in rotors]
	decrypt_first = DecryptSet(internal_key_dec[:], text_encrypt[:], rotors[0])
	
	dec = [True]
	while True:
		dec = decrypt_first.set_dec_chain(dec)
		for decrypt_rotor in reversed(decrypt_rotors):
			dec = decrypt_rotor.decrypt(dec)
		if not dec[-1]:
			break
	text_decrypt = decrypt_first.get_decrypt_list()
	return text_decrypt


def check_all_patterns(min_pattern, max_pattern, max_num_patterns, text_encrypt, del_patterns = [], mark = -1):  #todo make optimizations
	t_i = text_encrypt[:]   # text internal
	m_p = min_pattern       # min length pattern
	p_l = []                # pattern list
	max = max_pattern       #300 #len(t_i) // 2
	min = 0
	pf = 0
	ps = 0
	i_m = mark              # internal mark

	if del_patterns:
		for i in del_patterns:
			p_len = i[0]
			i.pop(0)
			i.pop(0)
			for ii in i:
				t_i[ii: p_len + ii] = [i_m for _ in range(ii, p_len + ii)]

	while True:
		if len(p_l) >= max_num_patterns:
			return p_l
		# -1 in Stały ?
		if i_m not in t_i[min + pf: max + pf]:
			# -1 in Ruchomy ?
			if i_m not in t_i[max + pf + ps: 2*max + pf + ps]:
				# Stały == Ruchomy ?
				if t_i[min + pf: max + pf] == t_i[max + pf + ps: 2*max + pf + ps]:
					# Save and zamień na -1
					p_l.append([len(t_i[min + pf: max + pf]), min + pf, max + pf + ps])
					t_i[max + pf + ps: 2*max + pf + ps] = [i_m for _ in range(max + pf + ps, 2*max + pf + ps)]
			# Ruchomy END ?
			if t_i[max + pf + ps: 2*max + pf + ps] == t_i[-len(t_i[max + pf + ps: 2*max + pf + ps]):]:
				# Stały END ?
				if t_i[min + pf: max + pf] + t_i[max + pf + ps: 2*max + pf + ps] == t_i[-2*len(t_i[max + pf + ps: 2*max + pf + ps]):]:
					# Len min ?
					if len(t_i[min + pf: max + pf]) == m_p:
						# STOP
						return p_l
					# Stały -1, Ruchomy - 1, Stały << p, Ruchomy << p
					else:
						max -= 1
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
			if t_i[min + pf: max + pf] + t_i[max + pf + ps: 2 * max + pf + ps] == t_i[-2 * len(
					t_i[max + pf + ps: 2 * max + pf + ps]):]:
				# Len min ?
				if len(t_i[min + pf: max + pf]) == m_p:
					# STOP
					return p_l
				# Stały -1, Ruchomy - 1, Stały << p, Ruchomy << p
				else:
					max -= 1
					pf = 0
					ps = 0
			# stały >> 1, Ruch << p
			else:
				pf += 1
				ps = 0


def check_patterns(text_to_check, min_len = 4): #todo https://www.tutorialspoint.com/python/string_find.htm
	list_of_patterns = []
	m = min_len
	nr_del = 0
	text_to_check_inter = text_to_check[:]
	while True:
		for i in range(0, len(text_to_check_inter)):
			# print(a, nr_del, i, list_of_patterns)
			if (m + i) * 3 > len(text_to_check_inter):
				break
			if text_to_check_inter[0: m + i] == text_to_check_inter[m + i: (m + i) * 2] == \
					text_to_check_inter[(m + i) * 2: (m + i) * 3]:
				list_of_patterns.append([len(text_to_check_inter[0: m + i]), nr_del, nr_del + (m + i), nr_del + (m + i) * 2])
		if len(text_to_check_inter) >= 1:
			text_to_check_inter.pop(0)
		else:
			break
		nr_del += 1
		if list_of_patterns:
			return list_of_patterns
	return False


def create_key(key_my, rotors):
	dic_32b = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "a": 10,
	          "b": 11, "c": 12, "d": 13, "e": 14, "f": 15, "g": 16, "h": 17, "i": 18, "j": 19, "k": 20,
	          "l": 21, "m": 22, "n": 23, "o": 24, "p": 25, "r": 26, "s": 27, "t": 28, "u": 29, "v": 30, "w": 31}
	
	
	if isinstance(key_my, str):
		key_my = key_my.lower()
		number_in_32b = 0
		i = 0
		while key_my:
			number_in_32b += dic_32b[key_my[-(1 + i)]] * (32 ** i)
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


def key_in_dec(key_my):
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