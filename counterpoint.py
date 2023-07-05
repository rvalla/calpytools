import json as js
import random as rd
from markovt import Markovt
from score import m21Score

class Counterpoint(m21Score):
	"A machine to make a different types of couterpoint"

	#building an instance of a Counterpoint()..
	def __init__(self, title, composer, key, t_sig, parts, cycles, mode, markov_path, data, t_unit, t_measure, offs, v_offs):
		m21Score.__init__(self, title, composer, key, t_sig, parts)
		self.cycles = cycles #number of cycles...
		self.mode = mode #texture mode: random, control, markov, conditional, puntual, filled...
		self.t_unit = t_unit
		self.t_measure = t_measure
		self.t_set = int(self.t_measure / self.t_unit)
		self.midi_offset = offs
		self.voice_offset = v_offs
		self.control_list = None
		self.structured_list = None
		self.markov_last = None
		self.markov = None
		self.get_ready(self.mode, data, markov_path) #only loading variables neede for current mode...
		self.build_counterpoint()

	#building initial counterpoint...
	def build_counterpoint(self):
		for i in range(self.cycles):
			self.add_cycle()

	#adding a counterpoint cycle based on configuration...
	def add_cycle(self):
		if self.mode == "random":
			self.add_random_cycle()
		elif self.mode == "control":
			self.add_control_cycle()
		elif self.mode == "conditional":
			self.add_conditional_cycle()
		elif self.mode == "puntual":
			self.add_puntual_cycle()
		elif self.mode == "filled":
			self.add_filled_cycle()
		elif self.mode == "mobile":
			self.add_mobile_cycle()
		elif self.mode == "markov":
			self.add_markov_cycle()

	#functions to create random counterpoint...
	def add_random_cycle(self):
		for r in range(self.parts_count):
			self.parts[r].append(self.random_measure(r))

	#creating a random measure...
	def random_measure(self, part):
		measure = []
		ps = rd.sample(range(1, self.t_set), self.get_measure_cardinality())
		ps.sort()
		ps.insert(0,0)
		ps.append(self.t_set)
		for i in range(len(ps)-1):
			duration = self.t_unit * (ps[i+1] - ps[i])
			pitch = rd.randint(0,11) + self.midi_offset + self.voice_offset * part
			measure.append(self.create_note(pitch, duration))
		return measure

	#Functions to create random counterpoint...
	def add_control_cycle(self):
		for r in range(self.parts_count):
			self.parts[r].append(self.control_measure(r))

	#creating a random measure...
	def control_measure(self, part):
		measure = []
		ps = rd.sample(range(1, self.t_set), self.get_measure_cardinality())
		ps.sort()
		ps.insert(0,0)
		ps.append(self.t_set)
		for i in range(len(ps)-1):
			duration = self.t_unit * (ps[i+1] - ps[i])
			pitch = rd.choice(self.control_list) + self.midi_offset + self.voice_offset * part
			measure.append(self.create_note(pitch, duration))
		return measure

	#functions to create conditional counterpoint...
	def add_conditional_cycle(self):
		for r in range(self.parts_count):
			self.parts[r].append(self.conditional_measure(r))

	#creating a conditional measure...
	def conditional_measure(self, part):
		measure = []
		ps = rd.sample(range(1, self.t_set), self.get_measure_cardinality())
		ps.sort()
		ps.insert(0,0)
		ps.append(self.t_set)
		for i in range(len(ps)-1):
			diff = ps[i+1] - ps[i]
			duration = self.t_unit * diff
			pitch = self.duration_to_pitch(diff) + self.midi_offset + self.voice_offset * part
			measure.append(self.create_note(pitch, duration))
		return measure

	#getting the pitch from note's duration...
	def duration_to_pitch(self, diff):
		return 12 - round(diff * 12 / self.t_set)

	#functions to create puntual melody...
	def add_puntual_cycle(self):
		w = len(self.structured_list)
		for r in range(self.parts_count):
			for c in range(w):
				self.parts[r].append(self.puntual_measure(self.structured_list[c], r))

	#creating a puntual texture measure...
	def puntual_measure(self, cell, part):
		measure = []
		c = len(cell)
		if c > 0:
			ps = rd.sample(range(0, self.t_set), c)
			ps.sort()
			cp = 0
			for i in range(self.t_set):
				if ps[cp] == i:
					pitch = cell[cp] + self.midi_offset + self.voice_offset * part
					measure.append(self.create_note(pitch, self.t_unit))
					if cp < c - 1:
						cp += 1
				else:
					measure.append(self.create_note(-1, self.t_unit))
		else:
			measure.append(self.create_note(-1, self.t_measure))
		return measure

	#functions to create filled texture...
	def add_filled_cycle(self):
		w = len(self.structured_list)
		for r in range(self.parts_count):
			for c in range(w):
				self.parts[r].append(self.filled_measure(self.structured_list[c], r))

	#creating a filled texture measure...
	def filled_measure(self, cell, part):
		measure = []
		c = len(cell)
		if c > 0:
			ps = rd.sample(range(1, self.t_set), c - 1)
			ps.sort()
			ps.insert(0,0)
			ps.append(self.t_set)
			for i in range(c):
				duration = self.t_unit * (ps[i+1] - ps[i])
				pitch = cell[i] + self.midi_offset + self.voice_offset * part
				measure.append(self.create_note(pitch, duration))
		else:
			measure.append(self.create_note(-1, self.t_measure))
		return measure

	#functions to create mobile texture...
	def add_mobile_cycle(self):
		w = len(self.structured_list)
		for r in range(self.parts_count):
			for c in range(w):
				self.parts[r].append(self.mobile_measure(self.structured_list[c], r))

	#creating a mobile texture measure...
	def mobile_measure(self, cell, part):
		measure = []
		c = len(cell)
		if c > 0:
			for i in range(self.t_set):
				pitch = cell[i%c] + self.midi_offset + self.voice_offset * part
				measure.append(self.create_note(pitch, self.t_unit))
		else:
			measure.append(self.create_note(-1, self.t_measure))
		return measure

	#Functions to create a conditional counterpoint based on a markov table...
	def add_markov_cycle(self):
		for r in range(self.parts_count):
			self.parts[r].append(self.markov_measure(r))

	#adding a markov measure...
	def markov_measure(self, part):
		measure = []
		ps = rd.sample(range(1, self.t_set), self.get_measure_cardinality())
		ps.sort()
		ps.insert(0,0)
		ps.append(self.t_set)
		for i in range(len(ps)-1):
			diff = ps[i+1] - ps[i]
			duration = self.t_unit * diff
			pitch_class = self.get_markov_pitch(self.markov_last[part])
			self.markov_last[part] = pitch_class
			pitch = pitch_class + self.midi_offset + self.voice_offset * part
			measure.append(self.create_note(pitch, duration))
		return measure

	#getting a new pitch based on conditional probabilities...
	def get_markov_pitch(self,input):
		r = rd.random()
		p = 0
		while self.markov.data[input][p] < r:
			p += 1
		return p

	#deciding how many notes to put in a measure...
	def get_measure_cardinality(self):
		c = []
		c.append(rd.randint(1,self.t_set-1))
		c.append(rd.randint(1,self.t_set-1))
		return min(c)
	
	#getting the control list from configuration string...
	def get_control_list(self, data):
		l = data.split(" ")
		values = []
		for v in l:
			values.append(int(v))
		return values
	
	#getting structured list from configuration string...
	def get_structured_list(self, data):
		links = data.split("-")
		values = []
		for l in links:
			values.append(self.get_notes(l))
		return values
	
	#function to create a link notes list...
	def get_notes(self, string_notes):
		notes = []
		for n in string_notes.split(" "):
			try:
				notes.append(int(n))
			except:
				pass
		return notes

	#loading needed variables for active mode...
	def get_ready(self, mode, data, markov_path):
		if mode == "control":
			self.control_list = self.get_control_list(data)
		elif mode == "puntual" or mode == "filled":
			self.structured_list = self.get_structured_list(data)
		elif mode == "markov":
			markovc = js.load(open(markov_path))
			self.markov = Markovt(markovc)
			self.markov_last = [self.markov.first_note for p in range(self.parts_count)]

	#printing counterpoint information...
	def __str__(self):
		return "-- Hi, I am a random Counterpoint" + "\n" \
				+ "-- I have " + str(len(self.parts)) + " parts" + "\n" \
				+ "-- And " + self.get_notes_count() + " notes" + "\n" \
				+ "-- I think there is a chance you like me..."

	
