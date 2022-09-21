import calendar

print('Welcome to the My Calendar\n')

year = int(input('Please enter year: '))
month = int(input('Enter the number of any month: '))

print(calendar.month(year, month))

print('Good luck!')
