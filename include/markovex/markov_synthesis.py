#    markovex - Markov chain generative music
#
#    Audio synthesis helper function and utilities
#
#   Copyright (c) 2010 Alessio Degani <alessio.degani@gmail.com>
#
#   This program is free software; you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation; either version 2 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>

import sys
import alsaseq
import alsamidi
import time
from utils import *

global VERBOSE


def playTable(table,first_state,bpm,alsaseq,CH):
	#init markov chain
	start_state=first_state
	curr_state=start_state

	#populating the list of available notes
	noteList=table[first_state].keys()
	
	#Whait time calculated from BPM
	tempo=float(1/(float(bpm)/60))
	
	if (VERBOSE):
		print "tempo: "+str(tempo)+"\""
		print "notelist"+str(noteList)
	
	#Firts 2 note are the first_state note
	ev=alsamidi.noteonevent(CH, int(first_state[0]), 127)
	alsaseq.output(ev)
	time.sleep(tempo)
	ev=alsamidi.noteoffevent(CH, int(first_state[0]), 0)
	alsaseq.output(ev)
	ev=alsamidi.noteonevent(CH, int(first_state[1]), 127)
	alsaseq.output(ev)
	time.sleep(tempo)
	ev=alsamidi.noteoffevent(CH, int(first_state[1]), 0)
	alsaseq.output(ev)
	while 1:
		#pick random probability (~uniform[0,1])
		rand_p=float(random.rand(1)[0])

		pdf=table[curr_state].values()
		
		pdf_cumulative=0
		count=0
		for p in pdf:
			pdf_cumulative+=p
			if (rand_p<=pdf_cumulative):
				break
			count+=1
		
		if (count>len(noteList)-1):
			#Trap state!! Fall back to start state
			next_state=first_state
			
			if (VERBOSE):
				print bcolors.FAIL+"Trap!!!"+bcolors.ENDC
			
			#recalculate next note
			pdf=table[first_state].values()
			pdf_cumulative=0
			count=0
			for p in pdf:
				pdf_cumulative+=p
				if (rand_p<=pdf_cumulative):
					break
				count+=1
		else:
			next_state=(curr_state[1],noteList[count])
		
		#evolve...
		curr_state=next_state

		if (VERBOSE):
			print "rand:", rand_p
			print "pdf: "+str(pdf)
			print "count: "+str(count)
			print "note: "+str(noteList[count])
			print "next state:", next_state

		ev=alsamidi.noteonevent(CH, int(noteList[count]), 127)
		alsaseq.output(ev)
		time.sleep(tempo)
		ev=alsamidi.noteoffevent(CH, int(noteList[count]), 0)
		alsaseq.output(ev)

def readTable(filename):
	#Read transitions probability matrix from file
	first=True
	count=0
	try:
		for line in filename:
			#skip comments, and newline
			if not (line[0] == "#" or line == "" or line=="\n"):
				if (first):
					#First line -> the Header contains some general infos
					(songName, trackName, bpm, first_state, rows, cols)=eval(line)
					table={}
					first=False
				else:
					#Read the rest of the table
					buff=eval(line)
					table[(buff[0])]=buff[1]
					count+=1
		filename.close()
		print "File successfully read."
	except Exception:
		print "Error reading file "+filename.name
		sys.exit(1)
	if (VERBOSE):
		printTable(table,first_state)
	return (table,first_state,bpm)
