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

from numpy import *
import string

#Some costants for friednly note printing
OCTAVE_MAX_VALUE = 12
NOTE_NAMES = ['C','C#','D','D#','E','F','F#','G','G#','A','A#','B']
NOTE_PER_OCTAVE = len( NOTE_NAMES )

def noteNameFromNum(value):
	noteidx = value % NOTE_PER_OCTAVE
	octidx = value / OCTAVE_MAX_VALUE
	name = NOTE_NAMES[int(noteidx)]
	return name

def printTable(table):
	'Print a Markov Chain Probabilty Matrix in a readable way'
	(numRows,numCols)=shape(table)
	hr=''.join(repeat("--------",numCols))+"-"
	print hr
	head= "| state\t| "
	for i in range(numRows):
		head=head+noteNameFromNum(table[i,0])+"\t| "
	print head
	print hr
	for r in range(numRows):
		buff="| "+noteNameFromNum(table[r,0])+"\t| "
		for c in range(1,numCols):
			buff=buff + str(table[r,c]) + "\t| "
		print buff
	print hr
