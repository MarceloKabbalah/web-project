from time import sleep
import sys

for i in range(21):
    sys.stdout.write('\r')
    # the exact output you're looking for:
    sys.stdout.write(" Processing element: [%-20s] %d%%" % ('='*i, 5*i))
    sys.stdout.flush()
    sleep(0.25)