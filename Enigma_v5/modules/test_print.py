from Enigma_all.Enigma_v5.modules.__tools_single import bcolors
from Enigma_all.Enigma_v5.modules.tools import check_text_const, check_rand_drums, create_key, check_patterns

import decimal
from math import log

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
				print(name_drum + str(drum)[:40] + "  +...+  " + str(drum)[-34:])
			else:
				print(name_drum + str(drum))
			drum_number += 1
		
		# Print keys
		if len("Encrypt key:" + " " * 5 + "[" + str(" ".join(map(str ,key_enc))) + "]") > 82:
			print("Encrypt key:" + " " * 5 + "[" + str(" ".join(map(str ,key_enc)))[:38].upper(),
			      ("  +...+  " + str(" ".join(map(str ,key_enc)).upper())[-33:] + "]"))
		else:
			print("Encrypt key:" + " " * 4, "[" + str(" ".join(map(str ,key_enc)).upper()) + "]")
		
		if len("Decrypt key:" + " " * 5 + "[" + str(" ".join(map(str ,key_dec))) + "]") > 82:
			print("Decrypt key:" + " " * 5 + "[" + str(" ".join(map(str ,key_dec)))[:38].upper(),
			      ("  +...+  " + str(" ".join(map(str ,key_dec)).upper())[-33:] + "]"))
		else:
			print("Decrypt key:" + " " * 4, "[" + str(" ".join(map(str ,key_dec)).upper()) + "]")
		
		if len("Int. enc. key:" + " " * 3 + str(create_key(key_enc, drums))) > 82:
			print("Int. enc. key:" + " " * 3 +  str(create_key(key_enc, drums))[:39],
			       ("  +...+  " + str(create_key(key_enc, drums))[-34:]))
		else:
			print("Int. enc. key:" + " " * 3 + str(create_key(key_enc, drums)))
		
		if len("Int. dec. key:" + " " * 3 + str(create_key(key_dec, drums))) > 82:
			print("Int. dec. key:" + " " * 3 +  str(create_key(key_dec, drums))[:39],
			       ("  +...+  " + str(create_key(key_dec, drums))[-34:]))
		else:
			print("Int. enc. key:" + " " * 3 + str(create_key(key_dec, drums)))
		
		
		# Print texts before, encrypt and decrypt
		if len(str(text_before)) > 82:
			print("Text before: \t", str(text_before)[:39],("  +...+  " + str(text_before)[-34:]))
		else:
			print("Text before: \t", text_before)
		if len(str(text_encrypt)) > 82:
			print("Text encrypt: \t", str(text_encrypt)[:39],("  +...+  " + str(text_encrypt)[-34:]))
		else:
			print("Text encrypt: \t", text_encrypt)
		if len(str(text_decrypt)) > 82:
			print("Text decrypt: \t", str(text_decrypt)[:39],("  +...+  " + str(text_decrypt)[-34:]))
		else:
			print("Text decrypt: \t", text_decrypt)
		
		# Print short drums info
		print("Drums length:" + " " * 34, "[" + format(decimal.Decimal(len(drums[0])), '.2E') + "]")
		print("Drums size in bit:" + " " * 29, "[" + str(int(log(len(drums[0])) / log(2))) + " bit]")
		print("Drums, number existing:" + " " * 24, "[" + str(len(drums)) + " drums]")  # number of exists drums
		for i in range(len(drums), 0, -1):
			if len(key_dec) % i == 0:
				print("Drums, number used:" + " " * 28, "[" + str(i) + " drums]")
				print("Number of passes:" + " " * 30, "[" + str(len(key_dec) // i) + " passes]")
				break
		if check_rand_drums(drums)[0]:
			print("Minimum value in the drum:\t\t\t\t\t\t" + "[" + str(min(drums[0])) + " min]")
			print("Maximum value in the drum:\t\t\t\t\t\t" + "[" + str(max(drums[0])) + " max]")
			print("Equality test of drums:\t\t\t\t\t\t\t" + bcolors.BOLD + "[PASS]" + bcolors.ENDC)
			if check_rand_drums(drums)[1]:
				print("Randomness and integrity drum test:\t\t\t\t" + bcolors.BOLD + "[PASS]" + bcolors.ENDC)
			else:
				print("Randomness and integrity drum test:\t\t\t\t" + bcolors.WARNING + bcolors.BOLD + "[FAIL]" + bcolors.ENDC)
		else:
			print("Minimum value in the drum:\t\t\t\t\t\t" + "[" + str(min(drums[0])) + " min]")
			print("Maximum value in the drum:\t\t\t\t\t\t" + "[" + str(max(drums[0])) + " max]")
			print("Equality test of drums:\t\t\t\t\t\t\t" + bcolors.BOLD + bcolors.WARNING + "[FAIL]" + bcolors.ENDC)
		

		# Print short keys info
		
		
		
		
		
		print("Text length:" + " " * 35, "[" + format(decimal.Decimal(len(text_before)), '.2E') + "]")
		
		
	
	# Calculated variations with repetitions
	for i in range(len(drums), 0, -1):
		if len(key_dec) % i == 0:
			cal_name_length = "Calculated variations with repetitions:\t\t\t"
			cal_length = (len(drums[0]) ** i) ** (len(key_dec) // i)
			if show_all:
				print(cal_length)
				print(cal_name_length + "[" + format(decimal.Decimal(cal_length), '.2E') + "]")
			break
	
	
	
	# cal_name_length = "Calculated variations with repetitions:\t\t\t"
	# cal_length = len(drums[0]) ** ((len(key_enc) - 1) * key_enc[0])
	# if show_all:
	# 	print(cal_name_length + "[" + format(decimal.Decimal(cal_length), '.2E') + "]")
	
	
	# Pattern only if it starts at the beginning and is duplicated three times without a break
	ii = 2
	test = True
	check_name_length = "Checked length of the pattern:\t\t\t\t\t"
	pattern_name = ""
	pattern_size = 0 #check_patterns(text_encrypt)  # todo uporadkuj nazwy
	# while test:
	# 	for i in range(0, len(text_encrypt)):
	# 		if ((2 * i + 1) + (2 * ii)) > len(text_encrypt):
	# 			pattern_name += "[No pattern]"
	# 			test = False
	# 			break
	# 		if (text_encrypt[i] == text_encrypt[i + ii]) and text_encrypt[i] == text_encrypt[(2 * i) + (2 * ii)]:
	# 			for x in range(0, i + ii):
	# 				if (text_encrypt[x] == text_encrypt[x + ii]) and text_encrypt[x] == text_encrypt[
	# 					(x) + (2 * ii)]:
	# 					if x == (i + ii - 1):
	# 						pattern_name += ("[" + format(decimal.Decimal(str(i + ii)), '.2E') + "]")
	# 						pattern_size = i + ii
	# 						test = False
	# 				else:
	# 					break
	# 		ii += 1
	# 		break
	
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

