import PySimpleGUI as sg
from time import sleep

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

	save_layout = [	[sg.Button('Slot 1', size = (40, 1))],
					[sg.Button('Slot 2', size = (40, 1))],
					[sg.Button('Slot 3', size = (40, 1))],
					[sg.Button('Slot 4', size = (40, 1))],
					[sg.Button('Slot 5', size = (40, 1))],
					[sg.Button('Slot 6', size = (40, 1))],
					[sg.Button('Back', size = (40, 1))]]

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

def load():
	pass
