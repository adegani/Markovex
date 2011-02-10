#    markovex - Markov chain generative music
#
#    Audio synthesis helper function and utilities
#
#   Copyright (c) 2010-2011 Alessio Degani <alessio.degani@gmail.com>
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

def playNote(note,duration,alsaseq,CH):
	#Play a note for a given duration
	ev=alsamidi.noteonevent(CH, int(note), 127)
	alsaseq.output(ev)
	time.sleep(duration)
	ev=alsamidi.noteoffevent(CH, int(note), 0)
	alsaseq.output(ev)

def computeNextState(table,curr_state,first_state):
	#evolve chain computing next state for given current_state

	pdf=[]
	rand_p=0

	#populating the list of available notes
	stateList=table[first_state].keys()

	if (curr_state==(0,0)):
		#first step of chain... play first note deterministicaly
		next_state=(0,first_state[0])
	elif (curr_state[0]==0 and not(curr_state[1]==0)):
		#second step of chain... play second note deterministicaly
		next_state=first_state
	else:
		#calculate next state

		#pick random probability (~uniform[0,1])
		rand_p=float(random.rand(1)[0])

		pdf=table[curr_state].values()

		pdf_cumulative=0
		next=0
		for p in pdf:
			pdf_cumulative+=p
			if (rand_p<=pdf_cumulative):
				break
			next+=1

		if (next>len(stateList)-1):
			#Trap state!! Fall back to start state
			next_state=first_state

			if (VERBOSE):
				print bcolors.FAIL+"Trap!!!"+bcolors.ENDC

			#recalculate next note
			pdf=table[first_state].values()
			pdf_cumulative=0
			next=0
			for p in pdf:
				pdf_cumulative+=p
				if (rand_p<=pdf_cumulative):
					break
				next+=1
		else:
			next_state=(curr_state[1],stateList[next])

	#evolve...
	return next_state

def playTable(pitchTbl,pitchFirstSt,durationTbl,durationFirstSt,bpm,alsaseq,CH):
	#init markov chain
	#Note: state (0,0) isn't the first state of the chain, but it's needed to init the chain
	pitchCurrState=(0,0)
	durationCurrState=(0,0)

	#Whait time calculated from BPM
	tempo=float(1/(float(bpm)/60))

	#duration in milliseconds of Thirty-second note(1/32)
	biscroma=float(1000/(float(bpm)/60))/8

	if (VERBOSE):
		print "tempo: "+str(tempo)+"\""

	while(1):
		(pitchNextState)=computeNextState(pitchTbl,pitchCurrState,pitchFirstSt)
		(durationNextState)=computeNextState(durationTbl,durationCurrState,durationFirstSt)
		duration=float((durationNextState[1]*biscroma)/1000)

		playNote(pitchNextState[1],duration,alsaseq,CH)

		pitchCurrState=pitchNextState
		durationCurrState=durationNextState
		if (VERBOSE):
			print "pitchCurrState: "+str(pitchCurrState)
			print "durationCurrState: "+str(durationCurrState)

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
					(songName, trackName, bpm, pitchFirstState, durationFirstState, rows, cols)=eval(line)
					pitchTbl={}
					durationTbl={}
					first=False
				else:
					#Read the rest of the table
					if (count<rows):
						#pitch table
						buff=eval(line)
						pitchTbl[(buff[0])]=buff[1]
						count+=1
					else:
						#duration table
						buff=eval(line)
						durationTbl[(buff[0])]=buff[1]
		filename.close()
		print "File successfully read."
	except Exception, msg:
		print "Error reading file "+filename.name
		print '"',msg,'"'
		raise
		sys.exit(1)
	
	if (VERBOSE):
		printTable(pitchTbl,pitchFirstState)
		printTable(durationTbl,durationFirstState)
		
	return (pitchTbl,pitchFirstState,durationTbl,durationFirstState,bpm)
