import os
import sys
import secrets

from tqdm import tqdm, trange
from time import sleep


tokens = {
        '0': (secrets.token_bytes()),
        '1': (secrets.token_bytes(20)),
        '2': (secrets.token_hex()),
        '3': (secrets.token_hex(20)),
        '4': (secrets.token_urlsafe()),
        '5': (secrets.token_urlsafe(16)),
        '6': (secrets.token_urlsafe(20))
            }
          
token = input(
    
    '####################################\n'
    '##   Choose Secure Token Type:    ##\n'
    '## 0 => Secure Byte Token         ##\n'
    '## 1 => Secure Byte Token (20)    ##\n'
    '## 2 => Secure Hex Token          ##\n'
    '## 3 => Secure Hex Token (20)     ##\n'
    '## 4 => Secure urlsafe Token      ##\n'
    '## 5 => Secure urlsafe Token (16) ##\n'
    '## 6 => Secure urlsafe Token (16) ##\n'
    '####################################\n'
        )
sys.stdout.write("\033[F")        
sys.stdout.write("\033[F")

progressbar = tqdm([2,4,6,8,10,12,14,16])

for item in progressbar:
	sleep(0.5)
	progressbar.set_description('Processing element: {}'.format(item))

print('\n\n'
      '\n Secure Token Generated => ', tokens.get(token, -1),'\n'
      '\n\n')
