from datetime import datetime

from reusable_functions import getMonthDays, isYearLeap, sumOfDigits

start = datetime.now()

def main():
    endYear = 2000
    year = 1900     #we start from 1900 cause we know that 1 Jan is a Monday, usefull for mod 7 on days passed

    days = 0
    sundaysCounter = 0
    monthSundaysPerYear = {}
    counter = 0
    while year <= endYear:
        month = 1
        if year not in monthSundaysPerYear:
            monthSundaysPerYear[year] = []
        monthSundaysPerYear[year+1] = []
        while month <= 12:
            daysOfMonth = getMonthDays(month, year)
            days += daysOfMonth
            if (days + 1) % 7 == 0:
                monthToPrint = month + 1
                yearToPrint = year
                if month == 12:
                    monthToPrint = 1
                    yearToPrint = year + 1

                monthSundaysPerYear[yearToPrint].append(monthToPrint)
                # print("%s/%s will start on Sunday"%(str(monthToPrint), str(yearToPrint)))
            month += 1
        year += 1

    keys = monthSundaysPerYear.keys()
    for year in keys:
        if(year > 1900): #only from 1901 to 2000
            print(str(year) + ": " + str(monthSundaysPerYear[year]))
            sundaysCounter += len(monthSundaysPerYear[year])

    return sundaysCounter


value = main()
print(value)

end = datetime.now()
print("The time of execution of above program is :",
      str(end-start))