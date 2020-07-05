import PySimpleGUI as sg
import os as os

def save_mechanic(class_respect, teachers, grades, situation, year, slot):
	with open(slot, 'w') as file:
		print('class_respect =', class_respect, file = file)
		print('teachers =', teachers, file = file)
		print('grades =', grades, file = file)
		print('year =', year, file = file)
		print(situation, file = file)

	sg.theme('Purple')
	window = sg.Window('SAVED!', layout = [[sg.Text('SAVED!')],[sg.Button('ok')]], size = (100, 100))
	while True:
		event, values = window.read()
		if event == sg.WIN_CLOSED or event == 'ok':
	window.close()

def save(class_respect, teachers, grades, situation, year):
	sg.theme('Purple')
	save_layout = []

	for i in range(1,7):
		path = 'saves/slot' + str(i) + '.dat'
		if os.path.isfile(path):
			save_layout.append([sg.Button('Slot ' + str(i), size = (20, 1)), sg.Text('(Taken)', size = (20, 1))])
		else:
			save_layout.append([sg.Button('Slot ' + str(i), size = (20, 1)), sg.Text('(Empty)', size = (20, 1))])

	save_layout.append([sg.Button('Back', size = (40, 1))])

	save_window = sg.Window('Saves', layout = save_layout, size = (600, 355))

	while True:
		event, values = save_window.read()
		#выход
		if event == sg.WIN_CLOSED or event == 'Back':
			break
		if event == 'Slot 1':
			save_mechanic(class_respect, teachers, grades, situation, year, 'saves/slot1.dat')
		if event == 'Slot 2':
			save_mechanic(class_respect, teachers, grades, situation, year, 'saves/slot2.dat')
		if event == 'Slot 3':
			save_mechanic(class_respect, teachers, grades, situation, year, 'saves/slot3.dat')
		if event == 'Slot 4':
			save_mechanic(class_respect, teachers, grades, situation, year, 'saves/slot4.dat')
		if event == 'Slot 5':
			save_mechanic(class_respect, teachers, grades, situation, year, 'saves/slot5.dat')
		if event == 'Slot 6':
			save_mechanic(class_respect, teachers, grades, situation, year, 'saves/slot6.dat')							

	save_window.close()		

def getSaveInfo(slot):
	with open(slot, 'r') as file:
		class_respect = file.readline().split()[2]
		teachers = file.readline().split()[2]
		grades = file.readline().split()[2]
		year = file.readline().split()[2]
		situation = file.readline()
	return (class_respect, teachers, grades, year, situation)


def load():
	sg.theme('Purple')
	load_layout = []

	for i in range(1,7):
		path = 'saves/slot' + str(i) + '.dat'
		if os.path.isfile(path):
			load_layout.append([sg.Button('Slot ' + str(i), size = (20, 1)), sg.Text('(Taken)', size = (20, 1))])
		else:
			load_layout.append([sg.Button('Slot ' + str(i), size = (20, 1)), sg.Text('(Empty)', size = (20, 1))])

	load_layout.append([sg.Button('Back', size = (40, 1))])

	load_window = sg.Window('Load menu', load_layout, size = (600, 355))

	while True:
		event, values = load_window.read()
		if event == sg.WIN_CLOSED or event =='Back':
			load_window.close()
			return False
		if event == 'Slot 1':
			load_window.close()
			return getSaveInfo('saves/slot1.dat')
		if event == 'Slot 2':
			load_window.close()
			return getSaveInfo('saves/slot2.dat')
		if event == 'Slot 3':
			load_window.close()
			return getSaveInfo('saves/slot3.dat')
		if event == 'Slot 4':
			load_window.close()
			return getSaveInfo('saves/slot4.dat')
		if event == 'Slot 5':
			load_window.close()
			return getSaveInfo('saves/slot5.dat')
		if event == 'Slot 6':
			load_window.close()
			return getSaveInfo('saves/slot6.dat')
