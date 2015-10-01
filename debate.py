# -*- coding: utf-8 -*-
#!/usr/bin/env python

#make the other person respond to previous sentence.
#if sentence is None, pull a random sentence from that speaker's file.
#generate up to n sentences until you get a word from the previous thing said (do this client side)

import markovify
import re

print(r"KELLY: It is nine p.m. on the East Coast, and the moment of truth has arrived. \
KELLY: Welcome to the first debate night of the 2016 presidential campaign, live from Quicken Loans Arena in Cleveland, Ohio. I'm Megyn Kelly… (APPLAUSE) … along with my co-moderators, Brett Baier and Chris Wallace. Tonight… (APPLAUSE) Nice. Tonight, thousands of people here in the Q, along with millions of voters at home will get their very first chance to see the candidates face off in a debate, answering the questions you want answered.")

def display(speaker, sentence):
	if sentence is None:
		print(speaker)
	else:
		print(speaker+': '+sentence)

order_text = open('speaker_order.txt', 'r')
order = order_text.readlines()

speakers = {}

for speaker in order:
	if speaker not in speakers:
		with open("speakers/" + speaker.strip() + ".txt") as f:
			text = f.read()
			speakers[speaker] = markovify.Text(text)
	# if speaker.strip() == 'KELLY':
	# 	seed_words = ('Tonight,', 'thousands')
	# 	print(seed_words[0] + " " + seed_words[1] + " ")
	# 	display(speaker.strip(), speakers[speaker].make_sentence(seed_words))
	# else:
	display(speaker.strip(), speakers[speaker].make_sentence())
	# print(speaker)


# Print three randomly-generated sentences of no more than 140 characters
# for i in range(3):
#     print(text_model.make_short_sentence(140))
