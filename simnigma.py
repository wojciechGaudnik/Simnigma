#!/usr/bin/python3


# check -f force mode in case of file over 1M
# todo key from screen and save ?
# todo change rotors order and save ?
# todo print and check rotors and key, rotors all or one
# todo szerokosci zcreeinu dobiera szerokosc printu albo error
# todo --config rotors order, max i min length
# todo przenieś z generatorów kluczy funkcje zmieniaja ce 64b na DEC itp do __Tools_single
# todo komentarze


# todo niesymetryczna kolejnosc przejsc przez rotorsy
# todo szyfrowanie plikow txt tylko na rotorsach do txt
# todo zamykaj kluczem RSA
# todo dorób rekurenje do wychodzenia w katalogu ponad ../
# todo zrób mozliwość szyfrowania ponad 8b rotors https://docs.python.org/2/library/struct.html
# todo zrób to na https://stormpath.com/blog/building-simple-cli-interfaces-in-python
# todo przerywanie szukania paternów klawiszem ew. po czasie
# todo popraw gen_text
# todo timingi do optymalizacji dorub
# todo timingi zrób dekoratorami ?
# todo dlaczego jeśli podaję do metody listę def bleble(self, cos_tam)
# todo      to nie mogę pracować na coś tam i jej zwrucić ?
# a zmien klucz 1 liczkbe
# generate or load new dict
# ogranicz wielkosc slownika do tłumaczenia
# generate drum wyeliminuj dic losowe w kolejności przypadkiem zrobione
# czas pozostały do zaszyfrowania odszyfrowania
# simnigma
# obsługę wyjątków
# rotors rozzezenie na rot zroó” !!
# rotors w 1 pliku
# print_all true or false
# printowanie przebiegu procesu
# przeszukiwanie wzorców max i min albo podział łancucha albo dzielenie przez więcej niż 2
# cycles w kluczu zrób tak żeby 1 znaczyło 1 cykl 2 dwa itd chyba juz jest ?!
# ostatnie wartosci kluczy mogą być wieksze niż max z dic !!!
# key przenieś do metody -1i zamien z hex na liste
# generator klucza do ilosci przejść i bębnów zrub
# karetkę bardziej widoczną zrób
# dorub sprwadzanie max i min słownika czy jest OK i print
# print only 2 decimals
# how to division with out decimal
# drums ---> rotors drum ---> drum

import sys
import os
import glob
import time

from modules.__tools_single import bcolors
from modules.test_print import test_print
from modules.tools import (encrypt, decrypt, load_file_all, save_file_all, convert_str_to_list, convert_list_to_str,
                           create_random_64b_key, key_from_64b_to_dec, check_64b_key,
                           create_rotors, check_rand_rotors,
                           print_long, show_help, printd)



# print(sys.argv)
# exit()


version = '5.0.0'
options = sys.argv + [' ',]
options[0] = options[0][1:]
options_all = ('-c', '-d', '-k', '-r', '-K', '-R', '-v', '-f', '--verbose', '-t', '--tests', '-h', '--help', '-V' ,'--version',
               '-s', '--silent')
max_print_length = int(os.popen('stty size', 'r').read().split()[1]) - 10
min_print_length = 15

space = 45
debug = False
os.system('setterm -cursor off')

files_to_encrypt = []
files_to_decrypt = []
key_name_load = ''
rotors_name_load = ''
key_name_save = ''
key_size = 0
rotors_name_save = ''
rotors_number = 0
show = False
only_screen = False
force = False
key = ''
rotors = []

# extracting options from the command line
printd( options, debug=debug)
if '-c' in options:
	for file_my in options[options.index('-c') + 1:]:
		if file_my[0] != '-' and file_my[0] != ' ':
			files_to_encrypt.append(file_my)
		else:
			break
	del options[options.index('-c') + 1: options.index('-c') + len(files_to_encrypt) + 1]
	options.remove('-c')
if '-d' in options:
	for file_my in options[options.index('-d') + 1:]:
		if file_my[0] != '-' and file_my[0] != ' ':
			files_to_decrypt.append(file_my)
		else:
			break
	del options[options.index('-d') + 1: options.index('-d') + len(files_to_decrypt) + 1]
	options.remove('-d')
if '-k' in options:
	if options[options.index('-k') + 1][0] != '-':
		key_name_load += options[options.index('-k') + 1]
	del options[options.index('-k') + 1]
	options.remove('-k')
if '-r' in options:
	if options[options.index('-r') + 1][0] != '-':
		rotors_name_load += options[options.index('-r') + 1]
	del options[options.index('-r') + 1]
	options.remove('-r')
if '-v' in options or '--verbose' in options:
	show = True
	try: options.remove('-v')
	except: options.remove('--verbose')
if '-s' in options or '--silent' in options:
	only_screen = True
	try: options.remove('-s')
	except: options.remove('--silent')
if '-K' in options:
	if options[options.index('-K') + 1][0] != '-':
		key_name_save += options[options.index('-K') + 1]
	try:
		key_size = options[options.index('-K') + 2]
		key_size = int(key_size)
	except:
		show_help('Invalid name or size of key')
	del options[options.index('-K') + 2]
	del options[options.index('-K') + 1]
	options.remove('-K')
if '-R' in options:
	if options[options.index('-R') + 1][0] != '-':
		rotors_name_save += options[options.index('-R') + 1]
	try:
		rotors_number = options[options.index('-R') + 2]
		rotors_number = int(rotors_number)
	except:
		show_help('Invalid number of rotors')
	del options[options.index('-R') + 2]
	del options[options.index('-R') + 1]
	options.remove('-R')
if '-h' in options  or '--help' in options:
	show_help('')
if '-V' in options or '--version' in options:
	printd(options, show)
	if len(sys.argv) != 2:
		show_help("Invalid options")
	else:
		printd(version)
		print("Simnigma version", version)
		exit()
if '-f' in options:
	force = True
	options.remove('-f')


# check options from cmd
printd( options, files_to_encrypt, files_to_decrypt, key_name_load, key_name_save, key_size)
printd( rotors_name_load, rotors_name_save, rotors_number, only_screen, show, debug=debug)
if len(sys.argv) == 1:
	show_help("No options")
if len(options) > 2:
	show_help("Invalid options")
if '-c' in sys.argv and files_to_encrypt == []:
	show_help("File to encrypt or to save if -s")
if '-d' in sys.argv and files_to_decrypt == []:
	show_help("File to decrypt or to load if -s")
if '-k' in sys.argv and key_name_load == ' ':
	show_help("Name of key to load")
if '-r' in sys.argv and rotors_name_load == ' ':
	show_help("Name of rotors to load")
if '-c' in sys.argv and len(files_to_encrypt) != 1 and only_screen:
	show_help("Too many files to save if -s")
if '-d' in sys.argv and len(files_to_decrypt) != 1 and only_screen:
	show_help("Too many files to load if -s")
if ('-c' in sys.argv or '-d' in sys.argv) and ('-K' in sys.argv or '-R' in sys.argv):
	show_help("Too many options, at the same time you can't encrypt/decrypt and create key or rotors")
if ('-K' in sys.argv or '-R' in sys.argv) and ('-s') in sys.argv:
	show_help("Too many options, at the same time you can't create key or rotors in silent mode")
if key_name_save and key_size > 10000 and not force:
	show_help("Too long key [limit 10 000], if you have enough time put -f in options")
if rotors_name_save and rotors_number > 100 and not force:
	show_help("Too many rotors [limit 100], if you have enough time put -f in options")
if show and not [opt for opt in sys.argv if opt in ['-c', '-d', '-k', '-r', '-K', '-R']]:
	show_help("Verbose works only in ['-c', '-d', '-k', '-r', '-K', '-R']")


# loading the key
if key_name_load:
	printd(key_name_load, debug=debug)
	if key_name_load[0] == '/':
		key = load_file_all(key_name_load, 'key', True)
	elif key_name_load[0:2] == '..':
		key = load_file_all(os.getcwd()[:os.getcwd().rfind('/')] + key_name_load[2:], 'key', True)
	elif key_name_load[0:2] == './':
		key = load_file_all(os.getcwd() + key_name_load[1:], 'key', True)
	elif key_name_load[-4:] == '.key':
		key = load_file_all(os.getcwd() + '/' + key_name_load, 'key', True)
	elif key_name_load:
		key = load_file_all(options[0][:options[0].rfind('/')] + '/keys/' + key_name_load, 'key', True)
elif ('-c' in sys.argv) or ('-d' in sys.argv):
	if sys.platform == 'linux':
		if glob.glob("/media/**/*.key", recursive=True):
			key_name_load = max(glob.glob("/media/**/*.key", recursive=True), key=os.path.getatime)
			key = load_file_all(key_name_load, 'key', True)
	if (glob.glob(options[0][:options[0].rfind('/') + 1] + 'keys/*'))  and not key:
		key_name_load = max(glob.glob(options[0][:options[0].rfind('/') + 1] + 'keys/*'), key=os.path.getatime)
		key = load_file_all(key_name_load, 'key', True)
printd(key, debug=debug)
if not rotors_name_save and not key_name_save and key:
	if check_64b_key(key):
		if show==False: print("Key test:" + " " * (space - 6) + "[" + bcolors.BOLD + "PASS" + bcolors.ENDC + "]")
	else:
		show_help("Key {} are broken, make new or del broken".format(key_name_load))
elif not rotors_name_save and not key_name_save :
	show_help("You don't have any keys, make or connect USB with key")


# loading of rotors
if rotors_name_load:
	printd(rotors_name_load, debug=debug)
	if rotors_name_load[0] == '/':
		rotors = load_file_all(rotors_name_load, 'rotors_from_one_file', True)
	elif rotors_name_load[0:2] == '..':
		rotors = load_file_all(os.getcwd()[:os.getcwd().rfind('/')] + rotors_name_load[2:], 'rotors_from_one_file', True)
	elif rotors_name_load[0:2] == './':
		rotors = load_file_all(os.getcwd() + rotors_name_load[1:], 'rotors_from_one_file', True)
	elif rotors_name_load[-4:] == '.rotor':
		rotors = load_file_all(os.getcwd() + '/' + rotors_name_load, 'rotors_from_one_file', True)
	elif rotors_name_load:
		rotors = load_file_all(options[0][:options[0].rfind('/')] + '/rotors/' + rotors_name_load, 'rotors_from_one_file', True)
elif ('-c' in sys.argv) or ('-d' in sys.argv):
	if sys.platform == 'linux':
		if glob.glob("/media/**/*.rotors", recursive=True):
			rotors_name_load = max(glob.glob("/media/**/*.rotors", recursive=True), key=os.path.getatime)
			rotors = load_file_all(rotors_name_load, 'rotors_from_one_file', True)
	if (glob.glob(options[0][:options[0].rfind('/') + 1] + 'rotors/*.rotors')) and not rotors:
		rotors_name_load = max(glob.glob(options[0][:options[0].rfind('/') + 1] + 'rotors/*.rotors'), key=os.path.getatime)
		rotors = load_file_all(rotors_name_load, 'rotors_from_one_file', True)
printd(rotors, debug=debug)
if  not rotors_name_save and not key_name_save and rotors:
	if check_rand_rotors(rotors):
		if min(rotors[0]) == 0 and max(rotors[0]) == 255 and min(rotors[0].values()) == 0 and max(rotors[0].values()) == 255:
			if show==False: print("Randomness and integrity rotor test:" + " " * (space - 33) + "[" + bcolors.BOLD + "PASS" + bcolors.ENDC + "]")
		else:
			show_help("Rotors {} are broken, make new or del broken".format(rotors_name_load))
elif not rotors_name_save and not key_name_save:
	show_help("You don't have any rotors, make or connect USB with rotors")


# encrypt file
if files_to_encrypt and not only_screen:
	printd(files_to_encrypt, debug=debug)
	for file_my in files_to_encrypt[:]:
		if not os.path.isfile(file_my):
			print(bcolors.IMPORTANT + 'Warning: "{}" this isn\'t a file'.format(file_my) + bcolors.ENDC)
			files_to_encrypt.remove(file_my)
	for file_my in files_to_encrypt[:]:
		if os.stat(str(os.path.abspath('') + '/' + file_my)).st_size > 0:
			files_to_encrypt[files_to_encrypt.index(file_my)] = str(os.path.abspath('') + '/' + file_my)
		else:
			print(bcolors.IMPORTANT + "Warning: Empty file {}".format(file_my) + bcolors.ENDC)
			files_to_encrypt.remove(file_my)
	for file_my in files_to_encrypt:
		text_before = load_file_all(file_my, 'file', True)
		text_encrypt = encrypt(rotors, key, text_before, show=True)
		save_file_all(file_my + '.enc', text_encrypt, 'file', True)
		if show: test_print(rotors=rotors, key_enc=key, text_before=text_before, text_encrypt=text_encrypt,
		                    show_all=True, show_uni=True, max_print_length=max_print_length, min_print_length=min_print_length,
		                    space=space)
if files_to_encrypt and only_screen:
	printd(files_to_encrypt, debug=debug)
	print("Enter/Paste your content. Ctrl-D or Ctrl-C to save it.")
	os.system('setterm -cursor on')
	text_before = ''
	while True:
		try:
			if text_before: text_before += '\n'
			text_before += input('<--- ')
		except KeyboardInterrupt:
			break
		except EOFError:
			break
	if len(text_before) == 0: show_help('Text is empty')
	os.system('setterm -cursor off')
	text_before = convert_str_to_list(text_before)
	text_encrypt = encrypt(rotors, key, text_before, show=True)
	save_file_all(files_to_encrypt[0] + '.enc', text_encrypt, 'file', True)
	if show: test_print(rotors=rotors, key_enc=key, text_before=text_before, text_encrypt=text_encrypt,
	                    show_all=True, show_uni=True)
	

# decrypt file
if files_to_decrypt and not only_screen:
	printd(files_to_decrypt, debug=debug)
	for file_my in files_to_decrypt[:]:
		if (not os.path.isfile(file_my) or (file_my[-4:] != '.enc')):
			print(bcolors.IMPORTANT + 'Warning: "{}" this isn\'t a .enc file'.format(file_my) + bcolors.ENDC)
			files_to_decrypt.remove(file_my)
	for file_my in files_to_decrypt[:]:
		if os.stat(str(os.path.abspath('') + '/' + file_my)).st_size > 0:
			files_to_decrypt[files_to_decrypt.index(file_my)] = str(os.path.abspath('') + '/' + file_my)
		else:
			print(bcolors.IMPORTANT + "Warning: Empty file {}".format(file_my) + bcolors.ENDC)
			files_to_decrypt.remove(file_my)
	for file_my in files_to_decrypt:
		text_encrypt = load_file_all(file_my, 'file', True)
		text_decrypt = decrypt(rotors, key, text_encrypt, show=True)
		save_file_all(file_my + '.dec', text_decrypt, 'file', True)
		if show: test_print(rotors=rotors, key_enc=key, text_encrypt=text_encrypt, text_decrypt=text_decrypt,
		                    show_all=True, show_uni=True, max_print_length=max_print_length, min_print_length=min_print_length,
		                    space=space)
if files_to_decrypt and only_screen :
	printd(files_to_decrypt, debug=debug)
	for file_my in files_to_decrypt[:]:
		if os.stat(str(os.path.abspath('') + '/' + file_my)).st_size > 0:
			files_to_decrypt[files_to_decrypt.index(file_my)] = str(os.path.abspath('') + '/' + file_my)
		else:
			exit(bcolors.IMPORTANT + "Warning: Empty file {}".format(file_my) + bcolors.ENDC)
	for file_my in files_to_decrypt[:]:
		if (not os.path.isfile(file_my) or (file_my[-4:] != '.enc')):
			exit(bcolors.WARNING + '"{}" this isn\'t a .enc file'.format(file_my) + bcolors.ENDC)
	for file_my in files_to_decrypt:
		text_encrypt = load_file_all(file_my, 'file', True)
		text_decrypt = decrypt(rotors, key, text_encrypt, show=True)
		if show: test_print(rotors=rotors, key_enc=key, text_encrypt=text_encrypt, text_decrypt=text_decrypt,
		                    show_all=True, show_uni=True)
		text_decrypt = convert_list_to_str(text_decrypt[:-1])
		text_decrypt = text_decrypt.split('\n')
		for line in text_decrypt:
			print('---> ', line)
		time.sleep(1)
		for _ in range(1000): print('\n')
		os.system('clear -h')
		

# creating and saving key and rotors
if key_name_save:
	printd(key_name_save, key_size, debug=debug)
	if key_name_save[0] == '/':
		pass
	elif key_name_save[0:2] == '..':
		key_name_save = os.getcwd()[:os.getcwd().rfind('/')] + key_name_save[2:]
	elif key_name_save[0:2] == './':
		key_name_save = os.getcwd() + key_name_save[1:]
	elif key_name_save[-4:] == '.key':
		key_name_save = os.getcwd() + '/' + key_name_save
	elif key_name_save:
		key_name_save = options[0][:options[0].rfind('/')] + '/keys/' + key_name_save
	key = create_random_64b_key(key_size, max_print_length=max_print_length, show=show)
	print('Key created:   ', key_name_save[key_name_save.rfind('/') + 1:], str(key_size) + " bit")
	save_file_all(key_name_save, key, 'key', show=True)
	printd(key, debug=debug)
if rotors_name_save:
	printd(rotors_name_save, rotors_number, debug=debug)
	if rotors_name_save[0] == '/':
		pass
	elif rotors_name_save[0:2] == '..':
		rotors_name_save = os.getcwd()[:os.getcwd().rfind('/')] + rotors_name_save[2:]
	elif rotors_name_save[0:2] == './':
		rotors_name_save = os.getcwd() + rotors_name_save[1:]
	elif rotors_name_save[-7:] == '.rotors':
		rotors_name_save = os.getcwd() + '/' + rotors_name_save
	elif rotors_name_save:
		rotors_name_save = options[0][:options[0].rfind('/')] + '/rotors/' + rotors_name_save
	rotors = create_rotors(8, True, rotors_number)
	if show: print_long('Rotor', rotors, min=min_print_length, max=max_print_length)
	print('Rotors created:', rotors_name_save[rotors_name_save.rfind('/') + 1:], str(rotors_number) + " items")
	save_file_all(rotors_name_save, rotors, 'rotors_in_one_file', show=True)
	printd(rotors, debug=debug)
	
	
os.system('setterm -cursor on')
exit()
	

# todo ---------- this part will be our playground :)----------

