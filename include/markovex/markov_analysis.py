#    markovex - Markov chain generative music
#
#    Markov Analysis helper function and utilities
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

import midi
from utils import *

global VERBOSE

def parseMidi(filename):
	#Reads midi events from file
	stream = midi.read_midifile(filename)

	songName=""
	trackName=""
	tempo=75
	#Get info for track 0 (Song name and master tempo)
	for event in stream.get_track_by_number(0):
		if (event.name=="Track Name"):
			songName=event.data
			tempo=stream.get_tempo().tempo
			print "Song Name: "+songName+", tempo: "+str(tempo)

	#Get info for other tracks
	tracklist=sorted(stream.tracknames.items(), key=lambda trk: trk[1])

	num=0
	if not(len(tracklist)==0):
		#If there are more than one track in the file, you have to choose one
		for track in tracklist:
			if not(track[1]==0): print str(track[1])+") "+track[0]

		#Select a track to analize
		ok=0
		while not(ok):
			select=raw_input("Please insert track number you want to analyze [1.."+str(tracklist[-1][1])+"]: ")
			try:
				num=int(select)
				if (num>=1 and num<=tracklist[-1][1]):
					ok=1
				else:
					print "Number out of range"
			except ValueError:
				print "Invalid input"

	try:
		trackName=tracklist[num][0]
	except IndexError:
		print "Failed to get track name"

	if (songName==""): songName=filename.name.split(".")[0]
	if (trackName==""): trackName=songName

	print "scanning track "+trackName+"..."
	noteList=[]
	for event in stream.get_track_by_number(num):
		if (event.name=="Note On"):
			noteList.append(event)
			if (VERBOSE):
				print event
		if (event.name=="Note Off"):
			#Convert note off event in note on with velocity=0
			event.name="Note On"
			event.velocity=0
			noteList.append(event)
			if (VERBOSE):
				print event

	return (noteList, songName, trackName, tempo)

def writeTableToFile(filename,songname,trackname,bpm,pitchTbl,pitchFirstState,durationTbl,durationFirstState):
	#Write transition probability matrix to file

	#if no out-file name provided
	if not(filename):
		filename=songname+"-"+trackname+".mch"

	out_file = open(filename,"w")
	numRows=len(pitchTbl)
	numCols=len(pitchTbl[pitchTbl.keys()[0]])

	#Header->General parameters
	head=(songname,trackname,bpm,pitchFirstState,durationFirstState,numRows,numCols)

	#Add some comments on the output file to improove readability
	out_file.write("#Markov Chain File generated by markovex for markovex\n")
	out_file.write("#DO NOT modify, or at least be careful :)\n\n")
	out_file.write("#(Song title, Track Name, Bpm, (pitch first state), (duration first state), rows, cols)\n")

	#write header
	out_file.write("('%s', '%s', %s, %s, %s, %s, %s)\n\n" % head)

	out_file.write("#Transition probability table for note pitch\n")

	#write the table in dict format
	for items in pitchTbl.items():
		out_file.write("(%s,%s)\n" % items)

	out_file.write("#Transition probability table for note duration\n")

	#write the table in dict format
	for items in durationTbl.items():
		out_file.write("(%s,%s)\n" % items)

	out_file.close()

def populateTable(walk):
	#General purpose probability transition matrix creation utility
	#-> walk is a general random walk step list

	#Creating a list of any note in the score picked once, and create 2n order states list
	#List of 2nd order states (x,y)
	states={}
	#List of all available state
	stateSpace={}

	for i in range(0,len(walk)):
		stateSpace[walk[i]]=0
		if (i<len(walk)-1):
			state=(walk[i],walk[i+1])
			states[state]=1;
			
	#Declaration of transition probability matrix
	table={}
	for curState in states:
		table[curState]=stateSpace.copy()

	first=1
	#Calculating transition probability matrix
	for i in range(2,len(walk)):
		if (i<len(walk)+1):
			state=(walk[i-2],walk[i-1])
			table[state][walk[i]]+=1
			if (first):
				first_state=state
				first=0

	#Normalization of transition probability matrix to sum(probability)=1 for each row
	for row in table:
		tot=0
		for item in table[row].items():
			tot=tot+item[1]
		for prob in table[row]:
			#tot used to avoid division-by-zero exception in case of trap state (P(escape)=0)
			if not(tot==0):
				table[row][prob]=round(float(table[row][prob])/tot,2)

	if (VERBOSE):
		print ("First state: (%s|%s)" % (noteNameFromNum(first_state[0]),noteNameFromNum(first_state[1])))
		printTable(table,first_state)

	return (first_state, table)

def createTable(notes, songName, bpm, CH):
	#Extimate Markov chain transitions probability matrix sequence from notes array

	#----------------------Markov Chain of note pitch-----------------------
	#Create a list of note-on events only (remove note-off from list notes)
	noteOn=[]
	for i in range(0,len(notes)):
		if not(notes[i].velocity==0):
			noteOn.append(notes[i].pitch)

	#Create transition probability matrix for note pitch
	(pitch_first_state, pitch_table)=populateTable(noteOn)

	#duration in milliseconds of Thirty-second note(1/32)
	biscroma=float(1000/(float(bpm)/60))/8
	noteDuration=[]
	#----------------------Markov Chain of note duration--------------------
	for i in range(0,len(notes)):
		if not(notes[i].velocity==0):
			for j in range(i,len(notes)):
				#Search note-off event of current playing note
				if (notes[j].velocity==0 and notes[j].pitch==notes[i].pitch):
					#Quantize note duration in number-of-Thirty-second notes
					millis=notes[j].msdelay-notes[i].msdelay
					quantized=int(round(millis/biscroma))
					if not(quantized==0 or quantized==1): noteDuration.append(quantized)
					break
	#Create transition probability matrix for note duration

	(duration_first_state, duration_table)=populateTable(noteDuration)

	return (pitch_first_state, pitch_table, duration_first_state, duration_table)
