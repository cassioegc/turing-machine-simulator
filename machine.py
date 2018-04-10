from status import Status
from tape import Tape

class Machine():
    
    def __init__(self, initial):
        self.__acceptance = ["halt", "halt-accept"]
        self.__rejection = ["halt-reject"]
        self.__current = initial
        self.__tape = Tape()
        self.__status = {}
        self.__steps = 0

    @property
    def acceptance(self):
        return self.__acceptance

    @property
    def current(self):
        return self.__current

    @property
    def rejection(self):
        return self.__rejection

    @property
    def tape(self):
        return self.__tape

    @property
    def status(self):
        return self.__status

    @property
    def steps(self):
        return self.__steps

    def add_status(self, name, read, write, direction, next):
        if name not in self.status.keys():
            self.status[name] = Status()

        self.status[name].add_transition(read, write, direction, next)

    def add_word(self, word):
        self.tape.add_word(word)

    def add_steps(self):
        self.__steps += 1

    def edit_current(self, current):
        self.__current = current

    def analyze(self):
        while self.current not in self.acceptance and self.current not in self.rejection:
            aux = []
            if self.tape.head >= len(self.tape.tape) or self.tape.head < 0:
                aux = self.status[self.current].get_transition("_")
            else:
                aux = self.status[self.current].get_transition(self.tape.get_symbol())

            self.tape.edit(aux[:2])
            self.add_steps()
            self.edit_current(aux[2])

    def get_tape(self):
        return self.tape.__str__()
