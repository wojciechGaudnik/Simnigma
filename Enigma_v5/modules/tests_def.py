# only functions to generate tools for ten drums tests encrypts
from collections import Counter
import decimal

from math import log
from random import randint

from Enigma_all.Enigma_v5.modules.test_print import test_print
from Enigma_all.Enigma_v5.modules.tools import save_rotors, load_rotors, encrypt, decrypt, gen_text, check_patterns, \
    create_key, check_all_patterns, create_rotors, key_in_dec


def test_3d_2b (show_all=True, show_first=False, show_short=False, show_calc=False):
    try:
        rotors = load_rotors("./rotors/set_drum_2b_", 3)
    except:
        rotors = {0: 2, 1: 0, 2: 3, 3: 1}, {0: 3, 1: 2, 2: 0, 3: 1}, {0: 3, 1: 0, 2: 1, 3: 2}
        save_rotors(rotors,"./rotors/set_drum_2b_")
    
    # key_enc = "7V9A"
    key_enc = [0, 2, 2, 0, 1, 2, 3, 3, 3]

    # key_dec = "7V9A"
    key_dec = [0, 2, 2, 0, 1, 2, 3, 3, 3]
   
    
    # def gen_text(char_max, ran, size_triple, drum_for_gen, *char_size):
    text_before = gen_text(0, False, False, rotors[0], 0, 1000)

    text_encrypt = encrypt(rotors, key_enc, text_before)
    text_decrypt = decrypt(rotors, key_dec, text_encrypt)

    # def test_print(rotors, key_enc, key_dec, text_before, text_encrypt, text_decrypt,
    #                show_all=True, show_first=False, show_short=False, show_calc=False):
    test_print(rotors, key_enc, key_dec, text_before, text_encrypt, text_decrypt, show_all,  show_first, show_short, show_calc)



import time
import sys

def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.25)

# delay_print("hello world")
