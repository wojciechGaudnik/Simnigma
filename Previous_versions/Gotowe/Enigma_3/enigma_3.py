from Enigma_all.Enigma_3.modules_3 import (check_rand_dict, save_dict, cre_mix_dict, load_dict, check_rand_dict,
                       Drum_first_encrypt, Drum_last_decrypt, Drum_next_encrypt,
                       Drum_next_decrypt)
# todo optymalizacja przeksztalcenia slownika
# todo usuń niepotrzebne self
# todo Drum_next.encrypt if one_char_in_list plus if self.i zrob 1 warunek
# todo klucz wyciagnij i revers
# todo ogranicz wielkosc slownika do tłumaczenia
# todo dorub sprwadzanie max i min słownika czy jest OK i print
# todo printowanie przebiegu procesu
# todo print_all true or false
# todo print only 2 decimals
# todo auto_generate if change bit
# todo generate or load new dict
# todo komentarze
# todo how to division with out decimal

# from Szyfr_enigma.Enigma_3.modules_3 import *
from random import randint
import decimal


bit = 8
size = 2 ** bit

be1 = cre_mix_dict(size, True)
be2 = cre_mix_dict(size, True)
be3 = cre_mix_dict(size, True)
be4 = cre_mix_dict(size, True)
be5 = cre_mix_dict(size, True)
# check_rand_dict(be1)
# check_rand_dict(be2)
# check_rand_dict(be3)
# check_rand_dict(be4)
# check_rand_dict(be5)
# save_dict(be1, "be1")
# save_dict(be2, "be2")
# save_dict(be3, "be3")
# save_dict(be4, "be4")
# save_dict(be5, "be5")


# be1 = load_dict("be1")
# be2 = load_dict("be2")
# be3 = load_dict("be3")
# be4 = load_dict("be4")
# be5 = load_dict("be5")
# check_rand_dict(be1)
# check_rand_dict(be2)
# check_rand_dict(be3)
# check_rand_dict(be4)
# check_rand_dict(be5)



text_before = []
for i in range (0 , 10):
    for ii in range(0, size):
        text_before.append(randint(0,size - 1))
    print("Generation text progress: ", (i / 10) * 100)
print("text before :\t\t", text_before)

# # text_before = [0, 1, 2, 3, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
# print("text before :\t\t", text_before)

encrypt_drum1 = Drum_first_encrypt(be1, 3)
encrypt_drum2 = Drum_next_encrypt(be2, 2)
encrypt_drum3 = Drum_next_encrypt(be3, 1)
encrypt_drum4 = Drum_next_encrypt(be4, 1)
encrypt_drum5 = Drum_next_encrypt(be5, 1)

decrypt_drum1 = Drum_next_decrypt(be5, 1)
decrypt_drum2 = Drum_next_decrypt(be4, 1)
decrypt_drum3 = Drum_next_decrypt(be3, 1)
decrypt_drum4 = Drum_next_decrypt(be2, 2)
decrypt_drum5 = Drum_last_decrypt(be1, 3)
print("Generation objects: Finished")


a = [0,0]
encrypt = []
for i in range (0, len(text_before)):
    a[0] = text_before[i]
    a = encrypt_drum1.encrypt(a)
    a = encrypt_drum2.encrypt(a)
    a = encrypt_drum3.encrypt(a)
    a = encrypt_drum4.encrypt(a)
    a = encrypt_drum5.encrypt(a)
    encrypt.append(a[0])
    print("Encrypt progress: ",(i/len(text_before))*100)
print("text encrypt:\t\t", encrypt)

a = [0,0]
decrypt = []
for i in range (0, len(encrypt)):
    a[0] = encrypt[i]
    a = decrypt_drum1.decrypt(a)
    a = decrypt_drum2.decrypt(a)
    a = decrypt_drum3.decrypt(a)
    a = decrypt_drum4.decrypt(a)
    a = decrypt_drum5.decrypt(a)
    decrypt.append(a[0])
    print("Decrypt progress: ", (i / len(encrypt)) * 100)
print("text decrypt:\t\t", decrypt)


print("---------------------------------")
if text_before == decrypt:
    print("Encrypt and decrypt test OK")
else:
    print("Encrypt and decrypt test FAIL")


number_of_combinations = len(be1)**Drum_next_decrypt.nb
number_of_combinations = decimal.Decimal(number_of_combinations)
print("Number of combinations: ", format(number_of_combinations, '.3E'),"   ", number_of_combinations)

