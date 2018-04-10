class Tape():
	
	def __init__(self):
		self.__tape = []
		self.__head = 0

	@property
	def tape(self):
		return self.__tape

	@property
	def head(self):
		return self.__head

	def add_word(self, word):
		self.__tape = list(word)
	
	def __str__(self):
		return "".join(self.tape).strip("_").replace("_", " ").strip()

	def move_head(self, direction):
		if direction == "l":
			self.__head -= 1
			if self.head == -1:
				self.__head = 0
				self.__tape.insert(0, "_")
		elif direction == "r":
			self.__head += 1
			if self.head == len(self.tape):
				self.__tape.append("_")

	def edit(self, commands):
		if commands[0] != "*":
			if 0 <= self.head < len(self.tape):
				self.__tape[self.head] = commands[0]
			elif len(self.tape) == 0:
				self.__tape.insert(0, commands[0])
			elif self.head >= len(self.tape):
				self.__tape.append(commands[0])

		self.move_head(commands[1])

	def get_symbol(self):
		return self.tape[self.head]

