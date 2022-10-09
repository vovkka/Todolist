import enum

class Operation(enum.Enum):
	addTask = 1
	viewTask = 2
	viewListOfTasks = 3
	deleteTask = 4
	exit = 5

class Task:
	def __init__(self, heading, body, date, tags):
		self.heading = heading
		self.body = body
		self.date = date
		self.tags = tags

class Menu:
		def print_menu():
			print("\n1.Создать задачу")
			print("2.Посмотреть задачу")
			print("3.Посмотреть список задач")
			print("5.Выйти из программы")



class ToDoList:
	def __init__(self, list_of_tasks):
		self.list_of_tasks = list_of_tasks


	def get_operation(self):
		try:
				
			operation = Operation(int(input("\nДействие: ")))
			return operation
				
		except ValueError:
			print("Такого пункта меню не существует")
			


	
	def add_task(self):
		task = Task(input("Введите заголовок задачи: "), input("Введите задачу: "), input("Введите дату дедлайна: "), [])

		tag = input("Вводите теги, когда закончите - нажмите Enter: ")
		while tag != "":
			task.tags.append(tag)
			tag = input("Введите тег: ")


		self.list_of_tasks.append(task)
		
		


	def view_task(self):

		try:

			number_of_task = int(input("Введите номер задачи: "))
			if number_of_task > 0:
				
				print("\nЗадача №" + str(number_of_task))
				number_of_task -= 1
				print("Заголовок: " + self.list_of_tasks[number_of_task].heading)
				print("Задача: " + self.list_of_tasks[number_of_task].body)
				print("Дата дедлайна: " + self.list_of_tasks[number_of_task].date)
				print("Теги: " + str(self.list_of_tasks[number_of_task].tags))
			
			else:
				print("\nЗадача с таким номером не обнаружена.")	
		except (IndexError, ValueError):
			print("\nЗадача с таким номером не обнаружена.")
	
	def view_list_of_task(self):
		
		if len(self.list_of_tasks) == 0:
			print("Задач нет.")
		
		else:
			
			for i in range(len(self.list_of_tasks)):
				print("\nЗадача №" + str(i+1))
				print("Заголовок: " + self.list_of_tasks[i].heading)





operation = None
to_do_list = ToDoList([])


while operation != Operation.exit:
	Menu.print_menu()
	operation = to_do_list.get_operation()
	
	#Создание задачи
	if operation == Operation.addTask:
		to_do_list.add_task()

	#Просмотр задачи
	if operation == Operation.viewTask:
		to_do_list.view_task()

	#Просмотр списка задач
	if operation == Operation.viewListOfTasks:
		to_do_list.view_list_of_task()
		