days_of_the_week = ['sunday', 'monday', 'tuesday']
def my_day(day):
  if(day in days_of_the_week):
    return day
  else:
    return "day entered does not exist"


day_entered = my_day(input("enter day of the week-->"))
# day_entered = my_day("monday")
print (day_entered)