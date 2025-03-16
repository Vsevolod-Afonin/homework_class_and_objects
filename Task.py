class Task():
    def __init__(self):
        self.tasks = []
    def add_task(self, deadline, description):
            self.tasks.append({'deadline': deadline,
                               'description': description, "status" : 'не выполнено'})

    def complete_tasks(self, description):
        for task in self.tasks:
            if task['description'] == description:
                task['status'] = 'Выполнено'
                print(f'Задача {description} выполнена')
            else:
                print(f'Задача {description} не найдена')

    def show_tasks(self):
        print('Текущие задачи:')
        for task in self.tasks:
            if task["status"] == 'не выполнено':
                print(f'{task['description']} - {task['deadline']}')

t = Task()

t.add_task('02.03.2025','Захостить бота')
t.add_task('10.05.2025','Пробежать марафон')
t.add_task('17.10.2025','Починить машину')

t.show_tasks()

t.complete_tasks('Пробежать марафон')

t.show_tasks()