import random as rd

class Matrix():
	"A matrix to make music"

	#building an instance of a Matrix...
	def __init__(self, module, string_matrix):
		self.mod = module #defining the cardinality of notes set to work (commonly 12)...
		self.h = None #height of the matrix...
		self.w = None #width of the matrix...
		self.max_in_cell = 0 #the maximum number of elements on any cell...
		self.data = [] #this is the matrix...
		self.r_status = [] #order of rows...
		self.c_status = [] #order of columns...
		self.build_cells(string_matrix)
		self.build_status()

	#function to move the matrix in pitch space...
	def translation(self, t):
		for r in range(self.h):
			for c in range(self.w):
				for v in range(len(self.data[r][c])):
					self.data[r][c][v] = (self.data[r][c][v] + t) % self.mod

	#function to move the matrix in pitch space...
	def invert(self):
		for r in range(self.h):
			for c in range(self.w):
				for v in range(len(self.data[r][c])):
					self.data[r][c][v] = -(self.data[r][c][v]) % self.mod

	#functions to change matrix status (order of rows and columns)
	def shuffle_status(self):
		self.shuffle_rows()
		self.shuffle_columns()

	def shuffle_rows(self):
		rd.shuffle(self.r_status)

	def shuffle_columns(self):
		rd.shuffle(self.c_status)

	#function to build the status (order of rows and columns)
	def build_status(self):
		self.r_status = []
		self.c_status = []
		for r in range(self.h):
			self.r_status.append(r)
		for c in range(self.w):
			self.c_status.append(c)

	#function to build the cells of the matrix from a complete string...
	def build_cells(self, string_matrix):
		string_rows = string_matrix.split("/")
		for r in string_rows:
			row = []
			string_cell = r.split("-")
			for c in string_cell:
				notes = self.get_notes(c)
				row.append(notes)
				if self.max_in_cell < len(notes):
					self.max_in_cell = len(notes)
			self.data.append(row)
		self.h = len(self.data)
		self.w = len(self.data[0])
	
	#function to create a cell notes list...
	def get_notes(self, string_notes):
		notes = []
		for n in string_notes.split(" "):
			try:
				notes.append(int(n))
			except:
				pass
		return notes
	
	#getting a trasposition of a cell...
	def translate_notes(self, notes, t):
		new_notes = []
		for n in notes:
			new_notes.append((n+t)%self.mod)
		return new_notes
	
	#setting up matrix size...
	def set_size(self, w, h):
		self.h = h
		self.w = w

	#function to get information in a cell...
	def get_cell(self, r, c):
		rd.shuffle(self.data[self.r_status[r]][self.c_status[c]])
		return self.data[self.r_status[r]][self.c_status[c]]

	#function to set a matrix cell...
	def set_cell(self, position, string_notes):
		notes = self.get_notes(string_notes)
		self.data[position[0]][position[1]] = notes
		if self.max_in_cell < len(notes):
			self.max_in_cell = len(notes)

	#function to create an empty matrix...
	def empty_matrix(self, width, height):
		self.set_size(width, height)
		self.max_in_cell = 0
		self.data = []
		for r in range(self.h):
			row = []
			for c in range(self.w):
				row.append([])
			self.data.append(row)
		self.build_status()

	#function to create a type 1 matrix...
	def build_type_one(self, notes):
		self.build_type_two(notes, notes)

	#function to create a type 2 matrix...
	def build_type_two(self, notes, other_notes):
		self.set_size(len(notes), len(other_notes))
		self.max_in_cell = 1
		self.data = []
		for o in other_notes:
			row = []
			for n in notes:
				row.append([(n+o)%self.mod])
			self.data.append(row)
		self.build_status()
	
	#function to build a matrix by trasposition...
	def trasposition_cycle(self, string_row, t):
		size = self.trasposition_cycle_size(t)
		first_row = self.get_first_cycle_row(string_row, size)
		self.set_size(size, size)
		self.max_in_cell = 1
		self.data = [first_row]
		for h in range(1, size):
			row = []
			for c in range(len(self.data[h-1])):
				row.append(self.translate_notes(self.data[h-1][(c-1)%size], t))
				if len(row[c]) > self.max_in_cell:
					self.max_in_cell = len(row[c])
			self.data.append(row)
		self.build_status()

	#function to get the first row of a matrix by trasposition...
	def get_first_cycle_row(self, string_row, size):
		cells = string_row.split("-")
		if not len(cells) == size:
			self.repair_first_cycle_row(cells, size)
		return [self.get_notes(c) for c in cells]
		
	#function to repair a bad first row for a matrix by trasposition...
	def repair_first_cycle_row(self, cells_candidate, size):
		if len(cells_candidate) > size:
			return cells_candidate[0:size]
		else:
			difference = size - len(cells_candidate)
			for i in range(difference):
				cells_candidate.append([])
		return cells_candidate

	#function to know a matrix by trasposition size...
	def trasposition_cycle_size(self, t):
		return int(self.lowest_multiple(self.mod, t)/t)

	#function to know the lowest multiple of two numbers...
	def lowest_multiple(self, a, b):
		n = 1
		for i in range(1, b + 1, 1):
			n = a * i #Checking a multiples...
			if (n%b == 0):
				break #We save the minumun which is b multiple too...
		return n

	#printing matrix information...
	def __str__(self):
		return "-- Hi, I am a matrix to make music" + "\n" \
				+ "-- I have " + str(self.w) + " columns" + "\n" \
				+ "-- And " + str(self.h) + " rows" + "\n" \
				+ "-- I think I could sound perfectly." + "\n" \
				+ "-- My current status is: " + str(self.r_status) + ", " + str(self.c_status)

	#function to print the matrix...
	def print_matrix(self):
		print(self.matrix_to_string())
	
	#formatting the matrix...
	def matrix_to_string(self):
		m = ""
		for r in range(self.h):
			row = "| "
			for c in range(self.w):
				row += self.cell_text(self.data[self.r_status[r]][self.c_status[c]])
				row += " | "
			m += row + "\n"
			if r < self.h - 1:
				m += self.line_string(len(row)-3)
		return m
	
	#drawing a line...
	def line_string(self, row_length):
		m = " "
		for r in range(row_length):
			m += "-"
		return m + "\n"

	#trying to print cells content...
	def cell_text(self, cell):
		c_size = len(cell)
		c_text = ""
		if c_size == 0:
			for l in range(self.max_in_cell * 3):
				c_text += " "
		else:
			for l in range(self.max_in_cell):
				if l < c_size:
					n = cell[l]
					if n < 10:
						c_text += " "
					c_text += str(n)
					c_text += " "
				else:
					c_text += "   "
		return c_text