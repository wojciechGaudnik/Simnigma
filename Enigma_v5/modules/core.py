# only classes for encryption and decryption


class EncryptSet:
	
	def __init__(self, key_enc, list_before, any_drum_for_max_i):
		self.__key_enc = key_enc
		self.__list_before = list_before
		self.__list_after = []
		self.__max_i = len(any_drum_for_max_i)
		self.__len_key = len(key_enc)
		self.__cycles = 0
		self.__cycles_finished = 0
		self.__len_key_block = 0
		
		for i in range(EncryptNextDrum.drum_number, 0, -1):
			if len(self.__key_enc) % i == 0:
				# self.__cycles = len(self.__key_enc) // i
				self.__cycles = i
				# self.__len_key_block = i
				self.__len_key_block = len(self.__key_enc) // i
				enc = [0, ]
				enc += self.__key_enc[0:self.__len_key_block]
				enc.append(True)
				self.__init__enc = enc
				break
				
	def set_enc_chain(self, enc):
		if len(enc) == 1:
			enc = self.__init__enc
			EncryptNextDrum.drum_number = 1
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


class EncryptNextDrum:
	drum_number = 1
	
	def __init__(self, drum):
		self.__drum = drum
		self.__max_i = len(drum)
		self.__drum_number = EncryptNextDrum.drum_number
		EncryptNextDrum.drum_number += 1
	
	def encrypt(self, char_in_int_p_key): # todo zamien na enc; char_in_in razem z enc z set_enc_chain i enc z pętli posprzątaj
		inter_char = char_in_int_p_key
		if char_in_int_p_key[-1]:
			if self.__drum_number < (len(char_in_int_p_key) - 1):
				inter_char[0] = self.__drum[char_in_int_p_key[0]] + char_in_int_p_key[self.__drum_number]
				if inter_char[0] >= self.__max_i:
					inter_char[0] -= self.__max_i
		return inter_char


class DecryptSet:
	
	def __init__(self, key_dec, list_before, any_drum_for_max_i):
		self.__key_dec = key_dec
		self.__list_before = list_before
		self.__list_after = []
		self.__max_i = len(any_drum_for_max_i)
		self.__len_key = len(key_dec)
		self.__cycles = 0
		self.__cycles_finished = 0
		self.__len_key_block = 0
		
		for i in range(DecryptNextDrum.drum_number, 0, -1):  # todo zamiast 3 EncryptNextDrum.drum_number
			if len(self.__key_dec) % i == 0:
				# self.__cycles = len(self.__key_dec) // i
				# self.__len_key_block = i
				
				# self.__cycles = len(self.__key_enc) // i
				self.__cycles = i
				# self.__len_key_block = i
				self.__len_key_block = len(self.__key_dec) // i
				
				dec = [0, ]
				dec += self.__key_dec[-self.__len_key_block:]
				dec.append(True)
				self.__init__dec = dec
				break
	
	def set_dec_chain(self, dec):
		if len(dec) == 1:
			dec = self.__init__dec
			DecryptNextDrum.drum_number = 1
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


class DecryptNextDrum():
	drum_number = 1
	
	def __init__(self, drum):
		self.__drum = {}
		for key, value in drum.items():
			self.__drum[value] = key
		self.__max_i = len(drum)
		self.__drum_number = DecryptNextDrum.drum_number
		DecryptNextDrum.drum_number += 1
	
	def decrypt(self, char_in_int_p_key):
		inter_char = char_in_int_p_key
		if char_in_int_p_key[-1]:
			if self.__drum_number < (len(char_in_int_p_key) - 1):
				inter_char[0] -= char_in_int_p_key[self.__drum_number]
				if inter_char[0] < 0:
					inter_char[0] += self.__max_i
				inter_char[0] = self.__drum[inter_char[0]]
		return inter_char
