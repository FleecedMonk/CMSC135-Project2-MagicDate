### Purpose - To figure out if, in numerical format,
### the day's date of month times the day would equal the year
### (the final two digits of the year)
### example: 01/06/06 would be 1*6=6 and that would be true
### example: 12/30/19 would be 12*30=360 and thus would be not true

### get the month and assign it to the variable
_month = integer(input(Enter the Month in numerical format : ))

### get the day and assign it to the variable
_day =  interget(input(Enter the Day is numberical format : ))

### get the year, in two digit format, and assign it to the
### variable

_year = integer(input(Enter the year in two digit numerical format : ))

### Do the multiplication
magic = _day*_month

### display the whole date
print("The date is ",_month, "/",_day, "/",_year,".")
