import PySimpleGUI as sg
import saveload as svld

def gameplay():
	sg.theme('Purple')

	fin = open('script/' + str(year) + 'grade.dat', 'r')
	n_of_situations = int(fin.readline())

	n_of_situations = n_of_situations - int(loaded_situation) + 1
	for _ in range(int(loaded_situation) - 1):
		fin.readline() #situation
		fin.readline() #option1
		fin.readline() #consequences
		fin.readline() # reply1
		fin.readline() #option2
		fin.readline() #consequences
		fin.readline() # reply2
		fin.readline() #option3
		fin.readline() #consequences
		fin.readline() # reply3
		fin.readline() #option4
		fin.readline() #consequences
		fin.readline() # reply4
		fin.readline() #void

	for _ in range(n_of_situations):
		situation = fin.readline()

		option1 = fin.readline()
		numeric_cons1 = list(map(lambda x: int(x), fin.readline().split()))
		reply1 = fin.readline()

		option2 = fin.readline()
		numeric_cons2 = list(map(lambda x: int(x), fin.readline().split()))
		reply2 = fin.readline()

		option3 = fin.readline()
		numeric_cons3 = list(map(lambda x: int(x), fin.readline().split()))
		reply3 = fin.readline()

		option4 = fin.readline()
		numeric_cons4 = list(map(lambda x: int(x), fin.readline().split()))
		reply4 = fin.readline()

		this_is_void = fin.readline()


		opt_1_3_col = [ [sg.Button(option1, size = (35, 3.5))],
						[sg.Button(option3, size = (35, 3.5))]]
		opt_2_4_col = [ [sg.Button(option2, size = (35, 3.5))],
						[sg.Button(option4, size = (35, 3.5))]]

		layout = [	[sg.Text('Респект однокл: ' + str(class_respect) + ' Отношения с учителями: ' + str(teachers) + ' Успеваемость: ' + str(grades))],
					[sg.Multiline(situation, size = (590, 15))],
					[sg.Column(opt_1_3_col), sg.Column(opt_2_4_col)],
					[sg.Button('Save', size = (100, 1))],
					[sg.Button('Quit', size = (100, 1))] ]

		gameplay_window = sg.Window('THE GAME', layout, size = (600, 440))

		while True:
			event, values = gameplay_window.read()
			if event == sg.WIN_CLOSED or event =='Quit':
				gameplay_window.close()
				fin.close()
				return
			if event == 'Save':
				svld.save(class_respect, teachers, grades, year, situation)
			if event == option1:
				class_respect += numeric_cons1[0]
				teachers += numeric_cons1[1]
				grades += numeric_cons1[2]
				gameplay_window.close()
				replyWindow(reply1)
				break
			if event == option2:
				class_respect += numeric_cons2[0]
				teachers += numeric_cons2[1]
				grades += numeric_cons2[2]
				gameplay_window.close()
				replyWindow(reply2)
				break
			if event == option3:
				class_respect += numeric_cons3[0]
				teachers += numeric_cons3[1]
				grades += numeric_cons3[2]
				gameplay_window.close()
				replyWindow(reply3)
				break
			if event == option4:
				class_respect += numeric_cons4[0]
				teachers += numeric_cons4[1]
				grades += numeric_cons4[2]
				gameplay_window.close()
				replyWindow(reply4)
				break

	fin.close()
	info = finishWindow(class_respect, teachers, grades, year)
	if info != None:
		return info
		
	gameplay_window.close()

def finishWindow(class_respect, teachers, grades):
	sg.theme('Purple')

	if class_respect < -10 and grades < -5 and teachers < -5:
		result_name = 'Жмыра! Работаешь в кфс, хуле'
	elif class_respect < -5 and grades > 10 and teachers > 10:
		result_name = 'Жыд! Пошёл нахуй'
	elif class_respect > 10 and grades > 10 and teachers > 10:
		result_name = 'Соня Б! Респект, хуле'
	else:
		result_name = 'та хуй знает кто пока что'

	if year == 11:
		finish_layout = [	[sg.Text('Игра закончена!!')],
							[sg.Text('Ваш результат:')],
							[sg.Text('Респект однокл - ' + str(class_respect))],
							[sg.Text('Отношения с учителями - ' + str(teachers))],
							[sg.Text('Успеваемость - ' + str(grades))],
							[sg.Text('Ты' + result_name)],
							[sg.Button('Back')] ]
	else:
		finish_layout = [	[sg.Text('Год ' + str(year) + ' завершён!!')],
							[sg.Text('Ваш результат:')],
							[sg.Text('Респект однокл - ' + str(class_respect))],
							[sg.Text('Отношения с учителями - ' + str(teachers))],
							[sg.Text('Успеваемость - ' + str(grades))],
							[sg.Text('Покачто ты' + result_name)],
							[sg.Button('Save')],
							[sg.Button('Continue')],
							[sg.Button('Back')] ]		


	finish_window = sg.Window('Finish window', finish_layout, size = (600, 400))

	while True:
		event, values = finish_window.read()
		if event == sg.WIN_CLOSED or event =='Back':
			break
		if event == 'Save':
			svld.save(class_respect, teachers, grades,year + 1, situation = '1)')
		if event == 'Continue':
			finish_window.close()
			return (class_respect, teachers, grades, year + 1, 1) # laast is situation
			
	reply_window.close()	

def replyWindow(reply):
	sg.theme('Purple')

	layout = [	[sg.Multiline(reply, size = (390, 14))],
				[sg.Button('ok', size = (60, 1))] ]

	reply_window = sg.Window('Reply window', layout, size = (600, 400))

	while True:
		event, values = reply_window.read()
		if event == sg.WIN_CLOSED or event =='ok':
			break
			
	finish_window.close()	

def startMenu():
	sg.theme('Purple')

	layout = [	[sg.Button('Start new game', size = (40, 7))],
				[sg.Button('Load save', size = (40, 7))],
				[sg.Button('Back', size = (40, 7))] ]

	start_window = sg.Window('Start menu', layout, size = (600, 355))

	while True:
		event, values = start_window.read()
		if event == sg.WIN_CLOSED or event =='Back':
			break
		if event == 'Load save':
			#info = (class_respect, teachers, grades, year, situation) or False
			info = svld.load()
			if info == False:
				break
			info = gameplay(class_respect = info[0], teachers = info[1], grades = info[2], year = info[3], loaded_situation = info[4])
			if info != None:
				gameplay(class_respect = info[0], teachers = info[1], grades = info[2], year = info[3], loaded_situation = info[4])
			break
		if event == 'Start new game':
			info = gameplay(class_respect = 0, teachers = 0, grades = 0, year = 8, loaded_situation = 1)
			if info != None:
				gameplay(class_respect = info[0], teachers = info[1], grades = info[2], year = info[3], loaded_situation = info[4])
			break

	start_window.close()

def preferencesMenu():
	sg.theme('Purple')

	layout = [	[sg.Button('fuck you', size = (40, 7))],
				[sg.Button('Back', size = (40, 7))] ]

	preferences_window = sg.Window('Preferences', layout, size = (600, 355))

	while True:
		event, values = preferences_window.read()
		#выход
		if event == sg.WIN_CLOSED or event == 'Back':
			break
		if event =='fuck you':
			pass

	preferences_window.close()

def mainMenu():
	sg.theme('Purple')
	menu_img = 'img/menu.png'

	buttons_column = [	[sg.Button('Start', size = (40, 7))],
						[sg.Button('Preferences', size = (40, 7))],
						[sg.Button('Exit', size = (40, 7))] ]
	img_column = [[sg.Image(filename = menu_img, size = (300, 350))]]

	main_layout = [[sg.Column(buttons_column), sg.Column(img_column)]]

	main_window = sg.Window('D-klass game', layout = main_layout, size = (600, 355))

	while True:
		event, values = main_window.read()
		#выход
		if event == sg.WIN_CLOSED or event == 'Exit':
			break
		if event == 'Start':
			startMenu()
		if event == 'Preferences':
			preferencesMenu()

	main_window.close()

if __name__=='__main__':
	mainMenu()




