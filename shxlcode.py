#coding:utf-8

import sys
import argparse
import binascii
import time
from datetime import datetime
import platform


banner_font = '''
  ██████  ██░ ██ ▒██   ██▒ ██▓     ▄████▄  ▒██   ██▒▓█████▄ ▓█████ 
▒██    ▒ ▓██░ ██▒▒▒ █ █ ▒░▓██▒    ▒██▀ ▀█  ▒▒ █ █ ▒░▒██▀ ██▌▓█   ▀ 
░ ▓██▄   ▒██▀▀██░░░  █   ░▒██░    ▒▓█    ▄ ░░  █   ░░██   █▌▒███   
  ▒   ██▒░▓█ ░██  ░ █ █ ▒ ▒██░    ▒▓▓▄ ▄██▒ ░ █ █ ▒ ░▓█▄   ▌▒▓█  ▄ 
▒██████▒▒░▓█▒░██▓▒██▒ ▒██▒░██████▒▒ ▓███▀ ░▒██▒ ▒██▒░▒████▓ ░▒████▒
▒ ▒▓▒ ▒ ░ ▒ ░░▒░▒▒▒ ░ ░▓ ░░ ▒░▓  ░░ ░▒ ▒  ░▒▒ ░ ░▓ ░ ▒▒▓  ▒ ░░ ▒░ ░
░ ░▒  ░ ░ ▒ ░▒░ ░░░   ░▒ ░░ ░ ▒  ░  ░  ▒   ░░   ░▒ ░ ░ ▒  ▒  ░ ░  ░
░  ░  ░   ░  ░░ ░ ░    ░    ░ ░   ░         ░    ░   ░ ░  ░    ░   
      ░   ░  ░  ░ ░    ░      ░  ░░ ░       ░    ░     ░       ░  ░
                                  ░                  ░             
                
                By Davistar\n
'''


def encode(char):
    for encoded in char:
        print('\b\\x'+encoded.encode('hex'))

parser = argparse.ArgumentParser()
parser.add_argument("-e","--encode",help="Encode a string")
parser.add_argument("-d","--decode",help="Decode a string")
parser.add_argument("-s","--stringfile",help="Encode from a file")
parser.add_argument("-f","--filedecode",help="Decode from a file")

args = parser.parse_args()

if args.filedecode:
	fl = args.filedecode
	Banner()
	try:
		f = open(fl,"r")
		for decod in f:
			print "shellcode => ",decod
			cleaninput = decod.replace("\\x","").rstrip('\n')
			print "hex       => ",cleaninput
			print "plaintext => ",
			print "\b"+cleaninput.decode("hex")+"\n"
	except IOError:
			print fl+" isnt found"

if args.stringfile:
	fl = args.stringfile
	print(banner_font)
	f = open(fl,'rw')
	strings = {}
	for line in f:
		strings[line] = line.rstrip('\n')
	try:
		for enc in strings.keys():
			print "plain text => "+strings[enc]
			print "hex        => "+enc.encode("hex")
			print "shellcode  => ",
			encode(strings[enc])
	except IOError:
			print fl+"isnt found"
	f.close()

if args.encode:
	print(banner_font)
	enc = args.encode 
	print "plain text => "+enc+"\n",
	print "hex        => "+enc.encode("hex")
	print "shellcode => ",
	for encoded in enc:
		print("\b\\x"+encoded.encode("hex")),
	print "\n"

if args.decode:
	print(banner_font)
	dec = args.decode
	cleaninput = dec.replace("\\","")
	cleaninput = dec.replace("x","") 
	print "shellcode => ",dec
	print "hex       => ",cleaninput
	print "plaintext => ",
	print "\b"+cleaninput.decode("hex")
