# only classes for encryption and decryption
from .__tools_single import generate_from_64b_inter_key, __test
import sys

# from Enigma_all.Enigma_v5.modules.__tools_single import __generate_inter_key, __generate_inter_key

# print("Hello From core:      ", __name__)
# __test()

# from Enigma_all.Enigma_v5.modules.tools import __generate_inter_key
# from Enigma_all.Previous_versions.Enigma_4.enigma_v4 import key_dec



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


class EncryptSet:
	
	def __init__(self, key_enc, list_before, rotors):
		if isinstance(key_enc, str):
			self.__key_enc = generate_from_64b_inter_key(key_enc, rotors)
		else:
			self.__key_enc = key_enc
		# self.__key_enc = key_enc
		self.__list_before = list_before
		self.__list_after = []
		self.__max_i = len(rotors[0])
		self.__len_key = len(self.__key_enc)
		self.__cycles = 0
		self.__cycles_finished = 0
		self.__len_key_block = 0
		self.__list_before_max = len(list_before)
		self.__print_test = 0
		
		for i in range(EncryptNextRotor.rotor_number - 1, 0, -1): # todo dodałęm - 1!!!
			if len(self.__key_enc) % i == 0:
				self.__cycles = len(self.__key_enc) // i
				# self.__cycles = i
				self.__len_key_block = i
				# self.__len_key_block = len(self.__key_enc) // i
				enc = [0, ]
				enc += self.__key_enc[0:self.__len_key_block]
				enc.append(True)
				self.__init__enc = enc
				break
				
	def set_enc_chain(self, enc):
		progress = (len(self.__list_after) * 100) / self.__list_before_max
		if progress == 100:
			if self.__print_test == 0:
				# sys.stdout.flush()
				# sys.stdout.write('\r\b')
				print("\rProgress encrypt:" + " " * 31 + "[100 %]" + " " * 10)
				self.__print_test = -1
		else:
			sys.stdout.write("\rProgress encrypt ... " + " " * 27 + "[%.4f %%]    " % (progress))
		
		if len(enc) == 1:
			enc = self.__init__enc
			EncryptNextRotor.rotor_number = 1
		if self.__cycles_finished == 0:
			# Empty chain
			if len(self.__list_before) == 0:
				self.__list_after.append(enc[0])
				enc[-1] = False
				return enc
			# Next char
			self.__list_after.append(enc[0])
			enc[0] = self.__list_before[0]
			self.__list_before.pop(0)
			# Key plus 1
			self.__key_enc[0] += 1
			for i in range(0, self.__len_key):
				if self.__key_enc[i] == self.__max_i:
					self.__key_enc[i] = 0
					self.__key_enc[i + 1] += 1
					if self.__key_enc[-1] == self.__max_i:
						self.__key_enc[-1] = 0
				else:
					break
		# Key Shift
		enc[1:self.__len_key_block + 1] = self.__key_enc[self.__len_key_block * self.__cycles_finished: (self.__len_key_block * self.__cycles_finished) + self.__len_key_block]
		# One cycle plus
		self.__cycles_finished += 1
		# If the end key, the cycle also ends
		if self.__cycles_finished == self.__cycles:
			self.__cycles_finished = 0
		return enc

	def get_encrypt_list(self):
		return self.__list_after[1:]
	
	def get_number_passes(self):
		return


class EncryptNextRotor:
	rotor_number = 1
	
	def __init__(self, rotor):
		self.__rotor = rotor
		self.__max_i = len(rotor)
		self.__rotor_number = EncryptNextRotor.rotor_number
		EncryptNextRotor.rotor_number += 1
	
	def encrypt(self, char_in_int_p_key): # todo zamien na enc; char_in_in razem z enc z set_enc_chain i enc z pętli posprzątaj
		inter_char = char_in_int_p_key
		if char_in_int_p_key[-1]:
			if self.__rotor_number < (len(char_in_int_p_key) - 1):
				inter_char[0] = self.__rotor[char_in_int_p_key[0]] + char_in_int_p_key[self.__rotor_number]
				if inter_char[0] >= self.__max_i:
					inter_char[0] -= self.__max_i
		return inter_char


class DecryptSet:
	
	def __init__(self, key_dec, list_before, rotors):
		if isinstance(key_dec, str):
			self.__key_dec = generate_from_64b_inter_key(key_dec, rotors)
		else:
			self.__key_dec = key_dec
		self.__list_before = list_before
		self.__list_after = []
		self.__max_i = len(rotors[0])
		self.__len_key = len(self.__key_dec)
		self.__cycles = 0
		self.__cycles_finished = 0
		self.__len_key_block = 0
		self.__list_before_max = len(list_before)
		self.__print_test = 0
		
		for i in range(DecryptNextRotor.rotor_number - 1, 0, -1): # todo dodałęm - 1!!!
			if len(self.__key_dec) % i == 0:
				self.__cycles = len(self.__key_dec) // i
				# self.__len_key_block = i
				
				# self.__cycles = len(self.__key_enc) // i
				# self.__cycles = i
				self.__len_key_block = i
				# self.__len_key_block = len(self.__key_dec) // i
				
				dec = [0, ]
				dec += self.__key_dec[-self.__len_key_block:]
				dec.append(True)
				self.__init__dec = dec
				break
	
	def set_dec_chain(self, dec):
		progress = (len(self.__list_after) * 100) / self.__list_before_max
		if progress == 100:
			if self.__print_test == 0:
				print("\rProgress decrypt:" + " " * 31 + "[100 %]" + " " * 10)
				self.__print_test = -1
		else:
			sys.stdout.write("\rProgress decrypt ... " + " " * 27 + "[%.4f %%]    " % (progress))
		
		if len(dec) == 1:
			dec = self.__init__dec
			DecryptNextRotor.rotor_number = 1
		if self.__cycles_finished == 0:
			# Empty chain
			if len(self.__list_before) == 0:
				self.__list_after.append(dec[0])
				dec[-1] = False
				return dec
			# Next char
			self.__list_after.append(dec[0])
			dec[0] = self.__list_before[0]
			self.__list_before.pop(0)
			# Key plus 1
			self.__key_dec[0] += 1
			for i in range(0, self.__len_key):
				if self.__key_dec[i] == self.__max_i:
					self.__key_dec[i] = 0
					self.__key_dec[i + 1] += 1
					if self.__key_dec[-1] == self.__max_i:
						self.__key_dec[-1] = 0
				else:
					break
		# Key Shift
		if self.__cycles_finished == 0:
			dec[1:self.__len_key_block + 1] = self.__key_dec[-self.__len_key_block:]
		else:
			dec[1:self.__len_key_block + 1] = self.__key_dec[-(self.__len_key_block * (self.__cycles_finished + 1)): -(self.__len_key_block * self.__cycles_finished )]
		# One cycle plus
		self.__cycles_finished += 1
		# If the end key, the cycle also ends
		if self.__cycles_finished == self.__cycles:
			self.__cycles_finished = 0
		return dec
	
	def get_decrypt_list(self):
		return self.__list_after[1:]


class DecryptNextRotor():
	rotor_number = 1
	
	def __init__(self, rotor):
		self.__rotor = {}
		for key, value in rotor.items():
			self.__rotor[value] = key
		self.__max_i = len(rotor)
		self.__rotor_number = DecryptNextRotor.rotor_number
		DecryptNextRotor.rotor_number += 1
	
	def decrypt(self, char_in_int_p_key):
		inter_char = char_in_int_p_key
		if char_in_int_p_key[-1]:
			if self.__rotor_number < (len(char_in_int_p_key) - 1):
				inter_char[0] -= char_in_int_p_key[self.__rotor_number]
				if inter_char[0] < 0:
					inter_char[0] += self.__max_i
				inter_char[0] = self.__rotor[inter_char[0]]
		return inter_char
