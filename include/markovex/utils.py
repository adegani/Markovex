#    markovex - Markov chain generative music
#
#    General utilities and classes
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

from numpy import *

#print color on console output
class bcolors:
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'

#Some costants for friednly note printing
OCTAVE_MAX_VALUE = 12
NOTE_NAMES = ['C','C#','D','D#','E','F','F#','G','G#','A','A#','B']
NOTE_PER_OCTAVE = len( NOTE_NAMES )

def noteNameFromNum(value):
	noteidx = value % NOTE_PER_OCTAVE
	octidx = value / OCTAVE_MAX_VALUE
	name = NOTE_NAMES[int(noteidx)]+"-"+str(octidx)
	return name

def printTable(table,first_state):
	#Print a Markov Chain Probabilty Matrix in a readable way

	print "Transition probabilty Matrix"
	numRows=len(table)
	numCols=len(table[table.keys()[1]])

	hr='----------------'+''.join(repeat("--------",numCols))+"-"
	print hr

	#Table header
	head = ["| Current\Next\t| "]
	for item in table[table.keys()[1]]:
		head.append(noteNameFromNum(item)+"\t| ")
	print ''.join(head)
	print hr

	#print states an transition prob.
	for state in table:
		#Green color to identify the first state
		if (state==first_state):
			buff=["| "+bcolors.OKGREEN, noteNameFromNum(state[0])+"|"+noteNameFromNum(state[1]), bcolors.ENDC+"\t| "]
		else:
			buff=["| ", noteNameFromNum(state[0])+"|"+noteNameFromNum(state[1]), "\t| "]

		notTrap=0
		for item in table[state]:
			buff.append(str(table[state][item]) + "\t| ")
			notTrap+=table[state][item]

		#check if trap state (Prob(escape)=0)
		if (notTrap):
			line=''.join(buff)
		else:
			line=bcolors.FAIL+''.join(buff)+bcolors.ENDC
		print line
	print hr
