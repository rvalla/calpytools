import random as rd

class Chain():
	"A tool to create a constant pitch class set note sequence"

	def __init__(self, pcs, string_notes, link_min, link_max, max_degrading):
		self.pcs = pcs #sometimes we need to analyze pitch class sets...
		self.degrading = 0 #to know how many times we add links trivially...
		self.max_degrading = max_degrading - 1 #to stop after a number of fallbacks...
		self.base_data = self.get_base_data(string_notes)
		self.base = self.base_data["ordered"]
		self.i_base = self.pcs.invert_set(len(self.base), self.base)
		self.candidates, self.i_candidates, self.iter_path, self.candidates_size = self.build_candidates_matrices(self.base, self.i_base)
		self.last_start = None
		self.link_sizes = self.get_link_sizes(len(self.base))
		self.link_min = link_min
		self.link_max = link_max
		self.building = True
		self.is_closed = False
		self.is_closable = False
		self.sequence_size = 2 #asuming at least the two links from de base pitch set...
		self.sequence = None
		self.all_sequences = []
		self.run()
	
	def run(self):
		self.last_start = rd.randint(0,self.candidates_size-1)
		rd.shuffle(self.link_sizes)
		self.sequence = self.start_new_sequence()
		while self.building:
			rd.shuffle(self.iter_path)
			new_link = self.look_for_link(self.sequence[len(self.sequence)-2], self.sequence[len(self.sequence)-1])
			self.sequence.append(new_link)
			self.sequence_size += 1
			if self.check_if_closed() and self.sequence_size >= self.link_min:
				self.building = False
			elif self.degrading > self.max_degrading or self.sequence_size >= self.link_max:
				self.building = False
		self.check_sequence_status()
	
	def start_new_sequence(self):
		notes = self.candidates[self.last_start]
		return [notes[0:self.link_sizes[0]], notes[self.link_sizes[0]:len(self.base)]]

	def look_for_link(self, link_a, link_b):
		link = self.new_link(link_a, link_b)
		if link == None:
			self.degrading += 1
			return link_a
		else:
			return link
	
	def new_link(self, link_a, link_b):
		link = None
		for p in self.iter_path:
			row_p = (self.last_start+p)%self.candidates_size
			if self.is_link_in(link_b, self.candidates[row_p]):
				link = self.substract_link(link_b, self.candidates[row_p])
				self.last_start = row_p
				break
		return link

	def check_sequence_status(self):
		if self.are_equal(self.sequence[0], self.sequence[self.sequence_size-1]):
			self.is_closed = True
			self.is_closable = True
		else:
			ordered_a = self.pcs.ordered_form(self.sequence[0])
			ordered_b = self.pcs.ordered_form(self.sequence[self.sequence_size-1])
			if self.are_the_same_set(ordered_a, ordered_b):
				self.is_closable = True
	
	def check_if_closed(self):
		return self.are_equal(self.sequence[0], self.sequence[self.sequence_size-1])

	def are_equal(self, a, b):
		are_equal = True
		if len(a) == len(b):
			for n in a:
				if not self.is_note_in(n, b):
					are_equal = False
					break
		else:
			are_equal = False
		return are_equal 

	def are_the_same_set(self, a, b):
		are_the_same = False
		if len(a) == len(b):
			ordinal_a = self.pcs.get_set_ordinal(a)
			ordinal_b = self.pcs.get_set_ordinal(b)
			if ordinal_a == ordinal_b:
				are_the_same = True
		return are_the_same
	
	def link_permutation(self, link):
		cardinality = len(link)
		new_link = []
		for i in range(cardinality):
			new_link.append(link[(i+1)%cardinality])
		return new_link
	
	def is_note_in(self, note, notes):
		is_in = False
		for n in notes:
			if note == n:
				is_in = True
				break
		return is_in

	def is_link_in(self, link, notes):
		is_in = True
		for n in link:
			if not self.is_note_in(n, notes):
				is_in = False
				break
		return is_in
	
	def substract_link(self, link, notes):
		complement = []
		for n in notes:
			if not self.is_note_in(n, link):
				complement.append(n)
		return complement

	def get_link_sizes(self, base_cardinality):
		link_sizes = [] #ready to return each link size...
		link_sizes.append(base_cardinality//2)
		link_sizes.append(base_cardinality-link_sizes[0])
		return link_sizes
	
	def sequence_to_string(self, sequence):
		m = ""
		for link in sequence:
			m += self.notes_to_string(link)
			m += "-"
		return m[:len(m)-1]

	def notes_to_string(self, notes):
		m = "" #formating ordered and prime forms...
		for n in notes:
			m += str(n)
			m += " "
		return m[:len(m)-1]
	
	def check_sequence(self, base, sequence):
		good_sequence = True
		cardinality = len(base)
		ordinal = self.pcs.get_set_ordinal(base)
		for i in range(len(sequence) - 1):
			the_set = sequence[i] + sequence[i+1]
			c = len(the_set)
			o = self.pcs.get_set_ordinal(the_set)
			if not (c == cardinality and o == ordinal):
				good_sequence = False
				break
		return good_sequence
	
	def build_candidates_matrices(self, base, i_base):
		candidates = []
		i_candidates = None
		for r in range(self.base_data["candidates_size"]):
			row = []
			for n in base:
				row.append((n+r)%12)
			candidates.append(row)
		if self.base_data["invert_candidates"]:
			i_candidates = []
			for r in range(self.base_data["candidates_size"]):
				row = []
				for n in i_base:
					row.append((n+r)%12)
				i_candidates.append(row)
		iter_path = [i for i in range(1,self.base_data["candidates_size"])]
		return candidates, i_candidates, iter_path, self.base_data["candidates_size"]

	def get_base_data(self, string_notes):
		cardinality, ordinal, interval, is_inverted, z_pair, states, ordered_form, prime_form = self.pcs.get_set_info(string_notes)
		data = {}
		data["cardinality"] = cardinality
		data["ordinal"] = ordinal
		data["is_inverted"] = is_inverted
		data["states"] = states
		data["ordered"] = ordered_form
		data["prime"] = prime_form
		data["candidates_size"], data["invert_candidates"] = self.get_candidates_matrix_size(states)
		return data

	def get_candidates_matrix_size(self, states):
		invert_candidates = True
		size = 12
		if states == 12:
			invert_candidates = False
		elif states == 6:
			invert_candidates = False
			size = 6
		elif states == 4:
			invert_candidates = False
			size = 4
		elif states == 3:
			invert_candidates = False
			size = 3
		elif states == 2:
			invert_candidates = False
			size = 2
		elif states == 1:
			invert_candidates = False
			size = 2
		return size, invert_candidates
	
	def __str__(self):
		return "-- Hi, I am a notes chain with constant pitch class set." + "\n" + \
				"-- My notes are: " + self.sequence_to_string(self.sequence) + "\n"