# only classes for encryption and decryption


class EncryptFirstDrum():
	def __init__(self, key, any_drum_for_max_i):
		self.__list_after = []
		self.__cycles = key[0]
		self.__num_of_cycles = 0
		self.__cycle_i = -1
		self.__inter_chain = []
		self.__max_i = len(any_drum_for_max_i)
		self.len_key = len(key)
		for i in range(0, (len(key) + 1)):
			self.__inter_chain.append(0)
		self.__inter_chain[-1] = True
		for i in range(1, self.len_key):
			self.__inter_chain[i] = key[i]
		
	def set_encyc_and_i(self, char_in_int_p_key, list_before):
		if self.__cycle_i == -1:
			self.__list_before = list_before
			self.__inter_chain[0] = self.__list_before[0]
			self.__list_before.pop(0)
			self.__cycle_i = 0
			self.__inter_chain[1] -= 1
		
		if self.__cycle_i == self.__cycles:
			if len(self.__list_before) == 0:
				self.__inter_chain[-1] = False
				self.__list_after.append(char_in_int_p_key[0])
				return self.__inter_chain
			self.__list_after.append(char_in_int_p_key[0])
			self.__inter_chain[0] = self.__list_before[0]
			self.__list_before.pop(0)
			self.__cycle_i = 0 #todo daj do góty
		self.__cycle_i += 1
		
		self.__inter_chain[1] += 1
		for i in range(1, self.len_key):  #todo było 1 !!!!!
			if self.__inter_chain[i] == self.__max_i: # todo break ??
				self.__inter_chain[i] = 0
				self.__inter_chain[i + 1] += 1
				if self.__inter_chain[-2] == self.__max_i:
					self.__inter_chain[-2] = 0
		
		return self.__inter_chain
		
	def get_encrypt_list(self):
		return self.__list_after
		
	
class EncryptNextDrum():
	drum_number = 1
	
	def __init__(self, drum):
		self.__drum = drum
		self.__max_i = len(drum)
		self.__drum_number = EncryptNextDrum.drum_number
		EncryptNextDrum.drum_number += 1
		
	def encrypt(self, char_in_int_p_key):
		inter_char = char_in_int_p_key
		if char_in_int_p_key[-1]:
			if self.__drum_number < (len(char_in_int_p_key) - 1):
				inter_char[0] = self.__drum[char_in_int_p_key[0]] + char_in_int_p_key[self.__drum_number]
				if inter_char[0] >= self.__max_i:
					inter_char[0] -= self.__max_i
		return inter_char


class DecryptFirstDrum():
	def __init__(self, key, any_drum_for_max_i):
		self.__list_after = []
		self.__cycles = key[0]
		self.__num_of_cycles = 0
		self.__cycle_i = -1
		self.__inter_chain = []
		self.__max_i = len(any_drum_for_max_i)
		self.len_key = len(key)
		for i in range(0, (len(key) + 1)):
			self.__inter_chain.append(0)
		self.__inter_chain[-1] = True
		for i in range(1, self.len_key):
			self.__inter_chain[i] = key[i]
	
	def set_decyc_and_i(self, char_in_int_p_key, list_before):
		if self.__cycle_i == -1:
			self.__list_before = list_before
			self.__cycle_i = 1
			self.__inter_chain[0] = self.__list_before[0]
			self.__list_before.pop(0)
			for i in range(1, self.__cycles):
				self.__inter_chain[1] += 1
				for ii in range(1, self.__max_i + 1): #todo dodalem +1
					if self.__inter_chain[ii] == self.__max_i: # todo break ?
						self.__inter_chain[ii] = 0
						if ii < (len(self.__inter_chain) - 2):
							self.__inter_chain[ii + 1] += 1   # todo błąd ?!?!?!
		else:
			if self.__cycle_i == self.__cycles:
				if len(self.__list_before) == 0:
					self.__inter_chain[-1] = False
					self.__list_after.append(char_in_int_p_key[0])
					return self.__inter_chain
				self.__list_after.append(char_in_int_p_key[0])
				self.__inter_chain[0] = self.__list_before[0]
				self.__list_before.pop(0)
				self.__cycle_i = 1
				self.__inter_chain[1] -= 1
				for i in range(1, (2 * self.__cycles) + 1):
					self.__inter_chain[1] += 1
					for ii in range(1, self.__max_i + 1): #todo dodalem +1
						if self.__inter_chain[ii] == self.__max_i: # else todo break ??
							self.__inter_chain[ii] = 0
							if ii < (len(self.__inter_chain) - 2): # todo BŁĄD !?!?!?
								self.__inter_chain[ii + 1] += 1
						else:
							break
				
			else:
				self.__cycle_i += 1
				self.__inter_chain[1] -= 1
				for i in range(1, self.__max_i + 1):  #todo dodalem +1
					if self.__inter_chain[i] < 0: # todo else break ??
						self.__inter_chain[i] = self.__max_i - 1
						if i < (len(self.__inter_chain) - 2):
							self.__inter_chain[i + 1] -= 1
		
		
		return self.__inter_chain
	
	def get_encrypt_list(self):
		return self.__list_after
		
		
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
