# WAP to Convert time into minute, hour and second
#take one input from the user
import datetime
#the above line is to import timedelta from datatime liberary 
sec = int(input("enter the time in Seconds"))
print('Time in Seconds:', sec)
x = datetime.timedelta(seconds=sec)
print('Time in days,hh:mm:ss:', x)
print(str(datetime.timedelta(seconds=sec)))