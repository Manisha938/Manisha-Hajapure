#Convert the time entered in hh,min and sec into seconds.
#take input from the user
seconds=int(input('enter seconds:'))

hours=seconds//3600
remaining_seconds=seconds%3600

minutes=remaining_seconds//60
remaining_seconds=remaining_seconds%60

print(f'{seconds} seconds is equal to {hours} hours, {minutes} minutes and {remaining_seconds} seconds.')