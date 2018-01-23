#!/usr/bin/python3

import time
import sys
import os
from modules.tools import save_key, create_rotors, load_key, load_file, save_file

from Simnigma_all.Simnigma.modules.__tools_single import generate_from_64b_inter_key
from Simnigma_all.Simnigma.modules.tests_def import test_5r_8b_file_txt_encrypt, test_5r_8b_file_txt_decrypt, test_3r_2b

# test_5r_8b_file_txt_encrypt()
# test_5r_8b_file_txt_decrypt()
from Simnigma_all.Simnigma.modules.tools import create_key, key_from_64b_to_dec, create_random_64b_key

# rotors = {0: 2, 1: 0, 2: 3, 3: 1}, {0: 3, 1: 2, 2: 0, 3: 1}, {0: 3, 1: 0, 2: 1, 3: 2}
# print("---generate_from_64b_inter_key---", generate_from_64b_inter_key("adsf", rotors, True))
# print("---create_key---", create_key("ad", rotors))
# print('---key_from_64b_to_dec---', key_from_64b_to_dec("aa23rcwevvwvgsdasd"))
# print('---create_random_64b_key---', create_random_64b_key(8, [], True))

test_3r_2b(True, True, True, True)

# a = os.listdir('.')
# print(max(a, key = os.path.getatime))
# print(type(a[-1]))
# [print(x) for x in a]
# print(a)

# from Enigma_all.Enigma_v5.modules.tools import load_key
# from Enigma_all.Enigma_v5.modules.tools import load_file
# from Enigma_all.Enigma_v5.modules.tools import save_file

# rotors = create_rotors(8, True, 1)
# key = create_random_64b_key(2048, rotors)
# print(key)
# # print(help(bytes))
# save_key("pierwszy", key)
#
#
# key_l = load_key("pierwszy")
#
# a = load_file("ls")
# print(a[0])
# print(max(a))
# print(min(a))
# print(len(a))
# b = list(a)
# print(b)
# b[-1:] = [ord("b"), ord("q"), ord("6"), ord("6"), ord("6")]
# print(b)
# c = bytes(b)
# print(c)
# save_file("lsss", c)
# print(chr(99))




# print(type(a))


# print(str(key))

# a = ["a", "b"]
# b = ""
# b = b.join(key)

# zmienna = 999
# string = "testowanie stringa"
# lista = [9, 9, 9, 9, 9, 9]
# slownik = {1: 2, 2: 2, 3: 3, 4: 4}

# __save_rotor(zmienna, "zmienna")
# __save_rotor(string, "string")
# __save_rotor(lista, "lista")
# __save_rotor(slownik, "slownik")


# zmienna_load = __load_rotor("text.txt")
# print(zmienna_load)
#
# f = open("text.txt", "rb")
# try:
#     uptime = f.read()
# finally:
#     f.close()
#
# # print(uptime[0])
# uptime_int = list(uptime)
# text = []
# for c in uptime_int:
#     text.append(c)
# # print(chr(uptime_int[0]))
#
#
#
#
# print(ord("ą"), ord("ć"), ord("ę"), ord("ł"), ord("ń"), ord("ó"), ord("ś"), ord("ź"), ord("ż"))
# print(text)

# uptime_int[0] = 127
# print(uptime_int)
# uptime_int = bytes(uptime_int)

# f = open("uptime", "wb")
# try:
#     f.write(uptime_int)
# finally:
#     f.close()


# uptime[0] = bytes(126)

# # print(byte[1])
# # print(type(byte))
# f = open("binarnie", "wb")
# try:
#     f.write(0)
# finally:
#     f.close()
#
#
#
# cos = 127
# print(hex(cos))
# cos.to_bytes(8, byteorder="big")
# print(type(cos))
# # cos.to_bytes()




# try:
#     f.write(cos)
# finally:
#     f.close()



# print(type(byte))
# print((byte[0]))
# a = byte[0]
# print(a)
#
# text = "test to.byte"
# print(text)
#
# byte_1 = "test to byte"
#
# f = open("text.txt.pkl", "rb")
# try:
#     f.write(bytes(byte_1))
# finally:
#     f.close()



# print(zmienna.__dir__())
# print(zmienna.__str__())

# print(ord("%"))

# from __future__ import print_function
# from time import sleep
#
# for i in range(101):
#   str1="Downloading File FooFile.txt [{}%]".format(i)
#   back="\b"*len(str1)
#   print(str1, end="")
#   sleep(0.1)
#   print(back, end="")


# test_3r_2b()
# # test_5r_8b(True)
#
# key_enc = [0, 1, 2]
# rotors = create_rotors(4, True, 2)
# a = generate_from_64b_inter_key("AA", rotors, True)
# text_before = gen_text(0, False, False, rotors[0], 0, 13000)
# text_encrypt = encrypt(rotors, key_enc, text_before)  # todo zmień kolejność txt pierwzy rotors i key


# a = create_random_64b_key(4048, rotors, True)
# print("----")
# __generate_inter_key(a[1], rotors, True)
# print(str(a[1])[:-1], sep="")

# key = [1]
# key = create_random_64b_key(100, rotors)[1]
# # key[1] = create_random_64b_key(3000, rotors)[1]
# # print("-" * 110)
# # print(rotors)
# test = "Dupa jaś salataaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa12bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb34"
# print_long("Rotor", rotors, 10, 80, False)
# # print(key)
# print_long("Key_enc", key, 10, 80, True)
# print_long("Text", test, 10, 80, True)
# print(create_random_64b_key(2000,rotors, True))
# sys.stdout.softspace=False
# while True:
#     rot = randint(1, 18)
#     num_rot = randint(1, 60)
#     rotors = create_rotors(rot, True, num_rot)
#     bit_key = randint(1, 2500)
#     print(rot, num_rot, bit_key)
#     # print(rotors[0])
#     # create_random_64b_key(2048, rotors, True)
#     if not create_random_64b_key(bit_key, rotors, True):
#         print("KURWA MAC")
#         break

# create_random_64b_key(32, rotors)

# test_list = []
#
# for i in range(1000000):
#     test_list += [0, 1, 2, 3]
# print(test_list)



# test_list = [0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3]
# print(test_list)
# print("start")
# fdsa = check_patterns(test_list, 30, 3, True)
# # print("over:", fdsa)
# asdf = check_all_patterns(test_list, 32, 32, 3, [], True )
# # print("all")
# # print(asdf)
# print(len(asdf))
# except KeyboardInterrupt:
#     print("testtesttesttesttesttesttesttesttest")
    # pass
# print(check_patterns(test_list, 400, 6))
# print(check_patterns(test_list, 4, 6))



# for i in range(1000):
# 	sys.stdout.write("\rPrograss completet {} %".format(format(i/len(range(1000-1))*100, '.4f')))
# 	# sys.stdout.flush()
# 	# time.sleep(0.1)
#
# 	# format(decimal.Decimal(len(rotors[0])), '.2E')
#
# 	# print('\r%s' % (str(i/len(range(10000))*100)), end='\r')
#
# 	# print ("percent complete:", i/len(range(10000))*100, end = "\r")
# 	# sys.stdout.flush()
#
# 	time.sleep(0.01)
#
# for i in range(100):
#     time.sleep(1)
#     sys.stdout.write("\r%d%%" % i)
#     sys.stdout.flush()

# sys.stdout.write(str(i/len(range(10000))*100))
	# sys.stdout.flush()

# def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█'):
#     """
#     Call in a loop to create terminal progress bar
#     @params:
#         iteration   - Required  : current iteration (Int)
#         total       - Required  : total iterations (Int)
#         prefix      - Optional  : prefix string (Str)
#         suffix      - Optional  : suffix string (Str)
#         decimals    - Optional  : positive number of decimals in percent complete (Int)
#         length      - Optional  : character length of bar (Int)
#         fill        - Optional  : bar fill character (Str)
#     """
#     percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
#     filledLength = int(length * iteration // total)
#     bar = fill * filledLength + '-' * (length - filledLength)
#     print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end = '\r')
#     # Print New Line on Complete
#     if iteration == total:
#         print()
#


def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.25)

# delay_print("hello world")