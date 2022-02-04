import Calendar as cd
import datetime as dt

h = cd.Holiday()
r = cd.Reminder()
c = cd.Calendar()
r.add_remind('Shopping', '2022-02-28', '09:00')
r.add_remind('OOP C# exam', '2022-02-26', '11:00')

print(f'Today is {dt.datetime.today().date()}')
h.today()
r.today()
classes = ('add holiday', 'delete holiday', 'change holiday', 'show holidays',
           'add remind', 'delete remind', 'change remind', 'show reminds', 'exit')
while True:
    print('I can do:', *classes, sep='\n')
    print('What do You want?')
    if c.do(str(input()).lower()):
        print('Something else? (yes/no)')
    else:
        print("Excuse me. I haven't understood. Try again? (yes/no)")
    if str(input()).lower() in ('no', 'nope'):
        print('Take care!')
        break

