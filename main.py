from machine import Machine

def init(arquivo, entrada):
	archive = open("files_config/" + arquivo)
	transitions = [i.split() for i in archive if i != "\n" and i[0] != ";"]

	machine = Machine(transitions[0][0])
	machine.add_word(entrada)

	for i in transitions:
	    machine.add_status(i[0], i[1], i[2], i[3], i[4])

	machine.analyze()
	return (machine.steps, machine.get_tape())