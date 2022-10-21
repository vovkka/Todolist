import enum
import time

class Operation(enum.Enum):
	addTask = 1
	viewTask = 2
	viewListOfTasks = 3
	deleteTask = 4
	findTask = 5
	exit = 6
	
	def __str__(self):
		title = ""
		match self:
			case Operation.addTask:
				title = "Создать задачу"
			case Operation.viewTask:
				title = "Посмотреть задачу"
			case Operation.viewListOfTasks:
				title = "Посмотреть список задач"
			case Operation.deleteTask:
				title = "Удалить задачу"
			case Operation.findTask:
				title = "Найти задачу"
			case Operation.exit:
				title = "Выйти из программы"
				
		return f"{self.value}.{title}"

class Task:
	def __init__(self, heading, body, date, tags):
		self.heading = heading
		self.body = body
		self.date = date
		self.tags = tags
	
	#Выводит информацию о задаче
	def print_task(self, number_of_task):
		print("\nЗадача №" + str(number_of_task))
		print("Заголовок: " + self.heading)
		print("Задача: " + self.body)
		print("Дата дедлайна: " + self.date)
		print("Теги: " + str(self.tags))


class Menu:
	
	def print_menu():
		options = [Operation.addTask, Operation.viewTask, Operation.viewListOfTasks, Operation.deleteTask, Operation.findTask, Operation.exit]
		print("")
		for option in options:
			print(Operation.__str__(option))



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
		task_heading = input("Введите заголовок задачи: ")
		task_description = input("Введите задачу: ")
		task_date = input("Введите дату: ")
		task_tags = []
		tag = input("Вводите теги, когда закончите - нажмите Enter: ")

		while tag != "":
			task_tags.append(tag)
			tag = input("Введите тег: ")
		
		task = Task(task_heading, task_description, task_date, task_tags)
		self.list_of_tasks.append(task)
	
	def delete_task(self):
		try:
			task_number = int(input("Введите номер задачи: "))
			if task_number > len(self.list_of_tasks) or task_number < 1:
				print("\nЗадача с таким номером не обнаружена")
			else:
				self.list_of_tasks.pop(task_number - 1)
				print("\nЗадача №" + str(task_number) + " удалена")
		except ValueError:
			print("\nЗадача с таким номером не обнаружена")

	def view_task(self):

		try:
			number_of_task = int(input("Введите номер задачи: "))
			
			if number_of_task > 0:
				
				self.list_of_tasks[number_of_task - 1].print_task(number_of_task)
			
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

	def find_task(self):
		if len(self.list_of_tasks) < 1:
			print("\nУ вас нет ни одной задачи")
		else:
			tag_to_find = input("Введите тег: ")


			for i in range(len(self.list_of_tasks)):
			

				if tag_to_find in self.list_of_tasks[i].tags:
					self.list_of_tasks[i].print_task(i + 1)
				
				else:
					print("\nЗадачи с таким тегом не обнаружено")

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
	
	#Удаление задачи
	if operation == Operation.deleteTask:
		to_do_list.delete_task()
	
	#Поиск задачи
	if operation == Operation.findTask:
		to_do_list.find_task()
