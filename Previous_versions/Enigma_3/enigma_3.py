# from Szyfr_enigma.Enigma_3.modules_3 import (bcolors, check_rand_dict, save_dict, cre_mix_dict, load_dict, check_rand_dict,
#                        Drum_first_encrypt, Drum_last_decrypt, Drum_next_encrypt,
#                        Drum_next_decrypt)

from modules_3 import (bcolors, check_rand_dict, save_dict, cre_mix_dict, load_dict, check_rand_dict,
                       Drum_first_encrypt, Drum_last_decrypt, Drum_next_encrypt,
                       Drum_next_decrypt)


from random import randint
import decimal
import time

# start_time = time.time()

# todo timingi dorub
# todo ogranicz wielkosc slownika do tłumaczenia
# todo dorub sprwadzanie max i min słownika czy jest OK i print
# todo printowanie przebiegu procesu
# todo print_all true or false
# todo print only 2 decimals
# todo auto_generate if change bit
# todo generate or load new dict
# todo komentarze
# todo how to division with out decimal
# todo ostatnie wartosci kluczy mogą być wieksze niż max z dic !!!
# todo dlaczego jeśli podaję do metody listę def bleble(self, cos_tam) to nie mogę pracować na coś tam i jej zwrucić ?


# klucz wyciagnij i revers
# Drum_next.encrypt if one_char_in_list plus if self.i zrob 1 warunek
# optymalizacja przeksztalcenia slownika
# usuń niepotrzebne self

# from Szyfr_enigma.Enigma_3.modules_3 import *



bit = 2 #22
size = 3# 2 ** bit

# be1 = cre_mix_dict(size, True)
# print("1")
# be2 = cre_mix_dict(size, True)
# print("2")
# be3 = cre_mix_dict(size, True)
# print("3")
# be4 = cre_mix_dict(size, True)
# print("4")
# be5 = cre_mix_dict(size, True)
# print("5")
# be6 = cre_mix_dict(size, True)
# print("6")
# __save_drum(be1, "be1")
# print("1s")
# __save_drum(be2, "be2")
# print("2s")
# __save_drum(be3, "be3")
# print("3s")
# __save_drum(be4, "be4")
# print("4s")
# __save_drum(be5, "be5")
# print("5s")
# __save_drum(be6, "be6")
# print("6s")

# __check_rand_rotor(be1)
# __check_rand_rotor(be2)
# __check_rand_rotor(be3)
# __check_rand_rotor(be4)
# __check_rand_rotor(be5)
# __check_rand_rotor(be6)



be1 = load_dict("be1")
be2 = load_dict("be2")
be3 = load_dict("be3")
be4 = load_dict("be4")
be5 = load_dict("be5")
be6 = load_dict("be6")

# __check_rand_rotor(be1)
# __check_rand_rotor(be2)
# __check_rand_rotor(be3)
# __check_rand_rotor(be4)
# __check_rand_rotor(be5)
# __check_rand_rotor(be6)


text_before = []
size_of_gen_text = 10
for i in range (0 , 10000):
    for ii in range(0, size):
        text_before.append(0) #randint(0,size - 1))
        # print("Generation text progress: ", (len(text_before)/size_of_gen_text) * 100)
    #     if len(text_before) > size_of_gen_text:
    #         print("Break")
    #         break
    # break
# print("text before :\t\t", text_before)
save_dict(text_before, "max_list")

# text_before = __load_drum("max_list")
# text_before = __load_drum("list")

# __check_rand_rotor(be6)
# text_before = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
# print(len(text_before))

key_encrypt = [0, 2, 0, 0, 0, 0]
key_decrypt = [0, 2, 0, 0, 0, 0]

# key_encrypt = [1, 2, 3, 0, 5000, 5096] #4095
# key_decrypt = [1, 2, 3, 0, 5000, 5096]

# key_decrypt.reverse()
suma_time = 0 #todo do liczenia sredniej czasu

start_time = time.time()
# encrypt_drum1 = Drum_first_encrypt(be1, key_encrypt[0])
# print("Generation object 1: Finished")
# encrypt_drum2 = Drum_next_encrypt(be2, key_encrypt[1])
# print("Generation object 2: Finished")
# encrypt_drum3 = Drum_next_encrypt(be3, key_encrypt[2])
# print("Generation object 3: Finished")
# encrypt_drum4 = Drum_next_encrypt(be4, key_encrypt[3])
# print("Generation object 4: Finished")
# encrypt_drum5 = Drum_next_encrypt(be5, key_encrypt[4])
# print("Generation object 5: Finished")
# encrypt_drum6 = Drum_next_encrypt(be6, key_encrypt[5])
# print("Generation object 6: Finished")

# decrypt_drum1 = Drum_next_decrypt(be6, key_decrypt[5])
# print("Generation object 7: Finished")
# decrypt_drum2 = Drum_next_decrypt(be5, key_decrypt[4])
# print("Generation object 8: Finished")
# decrypt_drum3 = Drum_next_decrypt(be4, key_decrypt[3])
# print("Generation object 9: Finished")
# decrypt_drum4 = Drum_next_decrypt(be3, key_decrypt[2])
# print("Generation object 10: Finished")
# decrypt_drum5 = Drum_next_decrypt(be2, key_decrypt[1])
# print("Generation object 11: Finished")
# decrypt_drum6 = Drum_last_decrypt(be1, key_decrypt[0])
# print("Generation objects: Finished")

a = [0,0]
encrypt = []
print("text before :\t\t", text_before)
# text_roll_decrypt = []
text_roll_encrypt = text_before[:]
for ii in range(0, 2) :
    encrypt_drum1 = Drum_first_encrypt(be1, key_encrypt[0])
    print("Generation object 1: Finished")
    encrypt_drum2 = Drum_next_encrypt(be2, key_encrypt[1])
    print("Generation object 2: Finished")
    encrypt_drum3 = Drum_next_encrypt(be3, key_encrypt[2])
    print("Generation object 3: Finished")
    encrypt_drum4 = Drum_next_encrypt(be4, key_encrypt[3])
    print("Generation object 4: Finished")
    encrypt_drum5 = Drum_next_encrypt(be5, key_encrypt[4])
    print("Generation object 5: Finished")
    encrypt_drum6 = Drum_next_encrypt(be6, key_encrypt[5])
    print("Generation object 6: Finished")
    for i in range (0, len(text_roll_encrypt)):
        a[0] = text_roll_encrypt[i]
        a = encrypt_drum1.encrypt(a)
        a = encrypt_drum2.encrypt(a)
        a = encrypt_drum3.encrypt(a)
        a = encrypt_drum4.encrypt(a)
        a = encrypt_drum5.encrypt(a)
        a = encrypt_drum6.encrypt(a)
        text_roll_encrypt[i] = a[0]
        # encrypt.append(a[0])
        # print("Encrypt progress: ",(i/len(text_before))*100)
encrypt = text_roll_encrypt[:]
print("text encrypt:\t\t", encrypt)


decrypt = []
# text_roll_decrypt = []
text_roll_decrypt = encrypt[:]
for ii in range(0, 2):
    Drum_next_decrypt.drum_number = 1
    decrypt_drum1 = Drum_next_decrypt(be6, key_decrypt[5])
    print("Generation object 7: Finished")
    decrypt_drum2 = Drum_next_decrypt(be5, key_decrypt[4])
    print("Generation object 8: Finished")
    decrypt_drum3 = Drum_next_decrypt(be4, key_decrypt[3])
    print("Generation object 9: Finished")
    decrypt_drum4 = Drum_next_decrypt(be3, key_decrypt[2])
    print("Generation object 10: Finished")
    decrypt_drum5 = Drum_next_decrypt(be2, key_decrypt[1])
    print("Generation object 11: Finished")
    decrypt_drum6 = Drum_last_decrypt(be1, key_decrypt[0])
    print("Generation objects: Finished")
    a = [0,0]
    for i in range (0, len(text_roll_decrypt)):
        a[0] = text_roll_decrypt[i]
        a = decrypt_drum1.decrypt(a)
        a = decrypt_drum2.decrypt(a)
        a = decrypt_drum3.decrypt(a)
        a = decrypt_drum4.decrypt(a)
        a = decrypt_drum5.decrypt(a)
        a = decrypt_drum6.decrypt(a)
        text_roll_decrypt[i] = a[0]
        # decrypt.append(a[0])
        # print("Decrypt progress: ", (i / len(encrypt)) * 100)
decrypt = text_roll_decrypt[:]
print("text decrypt:\t\t", decrypt)
stop_time = time.time()

suma_time += (stop_time - start_time) #todo do liczenia sredniej czasu





print("---------------------------------")
if text_before == decrypt and text_before != encrypt:
    print ("Encrypt and decrypt test " + bcolors.BOLD + "OK" + bcolors.ENDC)
else:
    print("Encrypt and decrypt test " + bcolors.WARNING + bcolors.BOLD + "FAIL" + bcolors.ENDC)


number_of_combinations = len(be1)**Drum_next_decrypt.drum_number
number_of_combinations = decimal.Decimal(number_of_combinations)
print("Number of combinations: ", format(number_of_combinations, '.3E'),"   ", number_of_combinations)
print("Execution time: {}s".format(round(suma_time)))
