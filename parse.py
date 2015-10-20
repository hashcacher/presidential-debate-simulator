# -*- coding: utf-8 -*-

#Parses a text corpus into speaker files.
import re

def write_line(speaker, line, append):
	# cleaned_line = line.replace(r"’", "'")
	# cleaned_line = line.replace(r"…", ",")
	cleaned_line = re.sub('[^\x00-\x7f]', '', line)

	if append or line[0] == "\xe2":
		speaker.write(' ' + cleaned_line)
	else:
		speaker.write("\n" + cleaned_line)


out_dir = 'speakers/'
speakers = {}
transcript = open("repub-2015-transcript.txt")
speaker_order = open("speaker_order.txt", "w")
last_speaker = None
i = 0
for line in transcript:
	if line.isspace():
		continue
	i+=1
	match = re.match(r'^([A-Z\(\) ]+:)?(.*)', line)
	if match.group(1):
		fixed_name = 'KELLY' if match.group(1) == 'MEGAN:' else match.group(1)[0:-1]
		if fixed_name not in speakers:
			speakers[fixed_name] = open(out_dir + fixed_name + '.txt', 'w')
		
		write_line(speakers[fixed_name], match.group(2).strip(), False)
		
		last_speaker = fixed_name
		speaker_order.write(fixed_name + "\n")
	else:
		write_line(speakers[last_speaker], match.group(2).strip(), True)

for speaker in speakers:
	speakers[speaker].close()
speaker_order.close()