from tkinter import *
from tkinter import ttk
import time

window = Tk()


def salary(dHour, nHour, wHour, dRate, nRate, wRate):
    salary = ((dHour*dRate)+(nHour*nRate)+(wHour*wRate))
    return print(salary)

def get_data():
    dRate = int(DaySalaryEntry.get())
    nRate = int(OvertimeSalaryEntry.get())
    wRate = int(WeekendSalaryEntry.get())
    dHour = int(DayHoursEntry.get())
    nHour = int(OvertimeHoursEntry.get())
    wHour = int(WeekendHoursEntry.get())

    salary(dHour, nHour, wHour, dRate, nRate, wRate)


DaySalaryLabel = Label(window, text="Day hourly rate: ")
DaySalaryLabel.grid(row=0, column=2)

DaySalaryEntry = Entry(window)
DaySalaryEntry.grid(row=0, column=3)

OvertimeSalaryLabel = Label(window, text="Overtime hourly rate: ")
OvertimeSalaryLabel.grid(row=1, column=2)

OvertimeSalaryEntry = Entry(window)
OvertimeSalaryEntry.grid(row=1, column=3)

WeekendSalaryLabel = Label(window, text="Weekend hourly rate: ")
WeekendSalaryLabel.grid(row=2, column=2)

WeekendSalaryEntry = Entry(window)
WeekendSalaryEntry.grid(row=2, column=3)

DayHours = Label(window, text="Day hours: ")
DayHours.grid(row=0, column=0)

DayHoursEntry = Entry(window)
DayHoursEntry.grid(row=0, column=1)

OvertimeHours = Label(window, text="Night hours: ")
OvertimeHours.grid(row=1, column=0)

OvertimeHoursEntry = Entry(window)
OvertimeHoursEntry.grid(row=1, column=1)

WeekendHours = Label(window, text="Weekend hours: ")
WeekendHours.grid(row=2, column=0)

WeekendHoursEntry = Entry(window)
WeekendHoursEntry.grid(row=2, column=1)

submitButton = Button(window, text="submit", command=get_data)
submitButton.grid(row=4, column=0, columnspan=4)

window.mainloop()
