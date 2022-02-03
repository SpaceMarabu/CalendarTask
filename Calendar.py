import datetime


class Holiday:
    def __init__(self):
        self.all_dates = dict()
        self.form = "%Y-%m-%d"
        self.type = 'holidays'
        self.read_holidays()

    def add(self, name, date, flag=False, act='add'):
        if act == 'add':
            action = 'added'
        elif act == 'change':
            action = 'changed'
        else:
            print("Can't do it.")
            return 0
        try:
            self.all_dates[name] = datetime.datetime.strptime(date, self.form)
            if not flag:
                print(f'{name} has been {action} to calendar on {date}.')
        except ValueError:
            if not flag:
                print('Wrong date!')

    def delete(self, name):
        try:
            del self.all_dates[name]
            print(f'{name} has been removed from calendar.')
        except KeyError:
            print(f'No {self.type} with such name.')

    def change(self, name, date):
        if name not in self.all_dates.keys():
            print(f'No {self.type} with such name.')
            return 0
        self.add(name, date, act='change')

    def show(self, time=False):
        if not time:
            use = 10
        else:
            use = 20
        for name, date in self.all_dates.items():
            print(f"{name} {str(date)[:use]}")

    def read_holidays(self):
        with open('holidays.txt' if self.type == 'holidays' else 'reminds.txt', 'r') as file:
            line = file.readline()
            for item in [value for value in line.split('-!end!-') if value]:
                v = item.split('-!space!-')
                if self.type == 'holidays':
                    self.add(v[0], v[1][:10], True)
                else:
                    self.add_remind(v[0], v[1][:-3].split(' ')[0], v[1][:-3].split(' ')[1], True)

    def __del__(self):
        with open('holidays.txt' if self.type == 'holidays' else 'reminds.txt', 'w') as file:
            for key, value in self.all_dates.items():
                file.write(f'{key}-!space!-{value}-!end!-')

    def today(self):
        flag = False
        for key, value in self.all_dates.items():
            if value.date() == datetime.date.today():
                print(key)
                flag = True
        if not flag:
            print(f'There is no {self.type} today.')


class Reminder(Holiday):
    def __init__(self):
        self.all_dates = dict()
        self.form = "%Y-%m-%d %H:%M"
        self.type = 'reminds'
        self.read_reminds()

    def add_remind(self, name, date, time, flag=False):
        super().add(name, f'{date} {time}', flag)

    def change_remind(self, name, date, time):
        super().change(name, f'{date} {time}')

    def show(self):
        super().show(True)

    def read_reminds(self):
        super().read_holidays()

    def __del__(self):
        super().__del__()


class Calendar():
    def __init__(self):
        self.r = Reminder()
        self.h = Holiday()

    def do(self, answer):
        if answer == 'add holiday':
            print('Type name of holiday')
            name = str(input())
            print('Type its date. format: yyyy-mm-dd')
            date = str(input())
            self.h.add(name, date)
            return True
        elif answer == 'change holiday':
            print('Type name of holiday')
            name = str(input())
            print('Type its date. format: yyyy-mm-dd')
            date = str(input())
            self.h.change(name, date)
            return True
        elif answer == 'delete holiday':
            print('Type name of holiday')
            name = str(input())
            self.h.delete(name)
            return True
        elif answer == 'show holidays':
            self.h.show()
            return True
        elif answer == 'add remind':
            print('Type name of remind')
            name = str(input())
            print('Type its date. format: yyyy-mm-dd')
            date = str(input())
            print('Type its time. hh:mm')
            time = str(input())
            self.r.add_remind(name, date, time)
            return True
        elif answer == 'change remind':
            print('Type name of remind')
            name = str(input())
            print('Type its date. format: yyyy-mm-dd')
            date = str(input())
            print('Type its time. hh:mm')
            time = str(input())
            self.r.change_remind(name, date, time)
            return True
        elif answer == 'delete remind':
            print('Type name of remind')
            name = str(input())
            self.r.delete(name)
            return True
        elif answer == 'show reminds':
            self.r.show()
            return True
        elif answer == 'back':
            print('Ok.')
            return True
        else:
            return False
