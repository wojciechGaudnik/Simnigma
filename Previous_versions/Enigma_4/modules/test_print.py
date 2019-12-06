import decimal
from math import log

from Simnigma_all.Enigma_4.modules.__tools_single import bcolors
from Simnigma_all.Enigma_4.modules.tools import check_text_const, check_rand_drums


# todo uporadkuj nazwy

def test_print(drums, key_enc, key_dec, text_before, text_encrypt, text_decrypt, show_all=True):
	print("----------------------------------------------------------------------------------------------------")
	
	if show_all:
		# Print drums
		drum_number = 1
		for drum in drums:
			name_drum = str("Drum " + str(drum_number) + ":")
			name_drum = name_drum + (17 - len(name_drum)) * " "
			if len(name_drum + str(drum)) > 82:
				print(name_drum + str(drum)[:82 - len("... = items  " + format(decimal.Decimal(len(drum)), '.2E') + "]")],
				      ("... = items  " + format(decimal.Decimal(len(drum)), '.2E') + "]"))
			else:
				print(name_drum + str(drum))
			drum_number += 1
		
		# Print texts before, encrypt and decrypt
		if len(str(text_before)) > 82:
			print("Text before: \t",
			      str(text_before)[:82 - len("... = items  " + format(decimal.Decimal(len(text_before)), '.2E') + "]")],
			      ("... = items  " + format(decimal.Decimal(len(text_before)), '.2E') + "]"))
		else:
			print("Text before: \t", text_before)
		if len(str(text_encrypt)) > 82:
			print("Text encrypt: \t", str(text_encrypt)[:82 - len("... = items  " + format(decimal.Decimal(len(text_encrypt)), '.2E') + "]")],
			      ("... = items  " + format(decimal.Decimal(len(text_encrypt)), '.2E') + "]"))
		else:
			print("Text encrypt: \t", text_encrypt)
		if len(str(text_decrypt)) > 82:
			print("Text decrypt: \t", str(text_decrypt)[:82 - len("... = items  " + format(decimal.Decimal(len(text_decrypt)), '.2E') + "]")],
			      ("... = items  " + format(decimal.Decimal(len(text_decrypt)), '.2E') + "]"))
		else:
			print("Text decrypt: \t", text_decrypt)
		
		
		print("Text length:" + " " * 35, "[" + format(decimal.Decimal(len(text_before)), '.2E') + "]")
		print("Encrypt key:" + " " * 35, key_enc)
		print("Decrypt key:" + " " * 35, key_dec)
		print("Size of drums in bit" + " " * 27, "[" + str(int(log(len(drums[0])) / log(2))) + " bit]")
		print("Number of existing drums:" + " " * 22, "[" + str(len(drums)) + " drums]")  # number of exists drums
		print("Number of used drums:" + " " * 26, "[" + str(len(key_enc) - 1) + " drums]")
		if check_rand_drums(drums)[0]:
			print("Equality test of drums:\t\t\t\t\t\t\t" + bcolors.BOLD + "[PASS]" + bcolors.ENDC)
			print("Maximum value in the drum:\t\t\t\t\t\t" + "[" + str(max(drums[0])) + " max]")
			print("Minimum value in the drum:\t\t\t\t\t\t" + "[" + str(min(drums[0])) + " min]")
			if check_rand_drums(drums)[1]:
				print("Randomness and integrity drum test:\t\t\t\t" + bcolors.BOLD + "[PASS]" + bcolors.ENDC)
			else:
				print("Randomness and integrity drum test:\t\t\t\t" + bcolors.WARNING + bcolors.BOLD + "[FAIL]" + bcolors.ENDC)
		else:
			print("Equality test of drums:\t\t\t\t\t\t\t" + bcolors.BOLD + bcolors.WARNING + "[FAIL]" + bcolors.ENDC)
			print("Maximum value in the drum:\t\t\t\t\t\t" + "[" + str(max(drums[0])) + " max]")
			print("Minimum value in the drum:\t\t\t\t\t\t" + "[" + str(min(drums[0])) + " min]")
		print("Number of passes:" + " " * 30, "[" + str(key_enc[0]) + " passes]")
	
	# Calculated variations with repetitions
	cal_name_length = "Calculated variations with repetitions:\t\t\t"
	cal_length = len(drums[0]) ** ((len(key_enc) - 1) * key_enc[0])
	if show_all:
		print(cal_name_length + "[" + format(decimal.Decimal(cal_length), '.2E') + "]")
	
	
	# Pattern only if it starts at the beginning and is duplicated three times without a break
	ii = 2
	test = True
	check_name_length = "Checked length of the pattern:\t\t\t\t\t"
	pattern_name = ""
	pattern_size = 0  # todo uporadkuj nazwy
	while test:
		for i in range(0, len(text_encrypt)):
			if ((2 * i + 1) + (2 * ii)) > len(text_encrypt):
				pattern_name += "[No pattern]"
				test = False
				break
			if (text_encrypt[i] == text_encrypt[i + ii]) and text_encrypt[i] == text_encrypt[(2 * i) + (2 * ii)]:
				for x in range(0, i + ii):
					if (text_encrypt[x] == text_encrypt[x + ii]) and text_encrypt[x] == text_encrypt[
						(x) + (2 * ii)]:
						if x == (i + ii - 1):
							pattern_name += ("[" + format(decimal.Decimal(str(i + ii)), '.2E') + "]")
							pattern_size = i + ii
							test = False
					else:
						break
			ii += 1
			break
	
	name = "Calculated and checked pattern test:\t\t\t"
	if len(text_encrypt) > cal_length * 3:
		if pattern_name == "[No pattern]":
			if check_text_const(text_before):
				print(check_name_length + bcolors.WARNING + bcolors.BOLD +
				      "[" + "No pattern" + "]" + bcolors.ENDC)
				print(name + bcolors.BOLD + "[PASS]" + bcolors.ENDC)
			else:
				print(check_name_length + "[No pattern]")
				print(name + bcolors.BOLD + "[PASS]" + bcolors.ENDC)
		else:
			if show_all:
				print(check_name_length + pattern_name)
			if pattern_size == cal_length:
				print(name + bcolors.BOLD + "[PASS]" + bcolors.ENDC)
			else:
				print(name + bcolors.WARNING + bcolors.BOLD + "[FAIL]" + bcolors.ENDC)
	else:
		print(name + "[too short]")
	
	
	# Encrypt and decrypt tests
	if ((text_before != text_encrypt) and (text_before == text_decrypt) and (key_enc == key_dec)) or \
			((text_before != text_encrypt) and (text_before != text_decrypt) and (key_enc != key_dec)):
		print("Encrypt, decrypt and keys test:\t\t\t\t\t" + bcolors.BOLD + "[PASS]" + bcolors.ENDC)
	else:
		if ((text_before != text_encrypt) and (text_before != text_decrypt) and (key_enc == key_dec)):
			print("Decrypt test:\t\t\t\t\t\t\t\t\t" + bcolors.WARNING + bcolors.BOLD + "[FAIL]" + bcolors.ENDC)
		else:
			if ((text_before != text_encrypt) and (text_before == text_decrypt) and (key_enc != key_dec)):
				print("Keys test:\t\t\t\t\t\t\t\t\t\t" + bcolors.WARNING + bcolors.BOLD + "[FAIL]" + bcolors.ENDC)
			else:
				if (text_before == text_encrypt):
					print(
						"Encrypt test:\t\t\t\t\t\t\t\t\t" + bcolors.WARNING + bcolors.BOLD + "[FAIL]" + bcolors.ENDC)

