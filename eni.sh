#!/bin/bash
export PATH=$PATH:~/workspace/Simnigma


simnigma.py -c enigma.py
simnigma.py -d enigma.py
diff enigma.py enigma.py.enc.dec -v
#simnigma.py -c enigma.py -k /home/bq666/workspace/test2/nowy_klucz2.key -v
#simnigma.py -c enigma.py -k do_txt.key -v
#simnigma.py -c enigma.py -r set_drum_8b -v
#simnigma.py -c enigma.py -r for_file -v
#simnigma.py -c enigma.py -r ~/workspace/test2/set_drum_8b_3.pkl -v
#
#simnigma.py -d enigma.py.enc -v
#simnigma.py -d enigma.py.enc -k /home/bq666/workspace/test2/nowy_klucz2.key -v


#simnigma.py -K nowy_testuje 1024 -v
#simnigma.py -R nowy_testuje 3 -v

#simnigma.py -c *
rm *.enc
rm *.dec




#-c sadf
#-d asdf
#-c sdaf -k asdf
#-d asdf -k asdf
#-c asdf -k asdf -r sadf
#-d asdf -k asdf -r asdf
#....... -v
#....... -s
#....... -v -s
#
#-K sadf 1234
#-R asdf 12
#-K asdf 1234 -R asdf 12
#....... -v
#
#-h --help
#-V --version