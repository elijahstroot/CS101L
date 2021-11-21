#Elijah Stroot
#CS101 L 
#Assignment 11
#Nov 20, 2021

### Algorithm:
'''
1. Create a Class that basically inserts the hours, minutes, and seconds of a clock
2. Create a method in the class that increases the clock time every second and adjusts the printed time appropriately
3. Create the print method of the class using str
4. Ask the user for their input and then insert that into the class and use the class methods to print a running clock. 
'''

###Code:
import time

class Clock:
  def __init__(self, hours =0, minutes=0, seconds=0, clock_type=0):
    self.hours = hours
    self.minutes = minutes
    self.seconds = seconds
    self.clock_type = type

  def tick(self):
    if self.clock_type == 0:
        self.seconds += 1
        if self.seconds == 60:
          self.minutes +=1
          self.seconds = 0
        if self.minutes == 60:
          self.hours +=1
          self.minutes = 0
          self.seconds = 0
        if self.hours == 13:
          self.hours = 1
          self.minutes = 0
          self.seconds = 0
    if self.clock_type == 1:
        self.seconds += 1
        time.sleep(1)
        if self.seconds == 60:
          self.minutes +=1
          self.seconds = 0
        if self.minutes == 60:
          self.hours +=1
          self.minutes = 0
          self.seconds = 0
        if self.hours == 25:
          self.hours = 0
          self.minutes = 0
          self.seconds = 0


  def __str__(self):
    return "{:02}:{:02}:{:02}".format(self.hours, self.minutes, self.seconds)


print("Welcome to the clock program")
current_hour = int(input("What is the current hour ==> "))
current_minute = int(input("What is the current minute ==> "))
current_second = int(input("What is the current second ==> "))
clock_type = int(input("If your clock type is normal, type 0; if your clock type is military, enter 1"))

clock = Clock(current_hour, current_minute, current_second, clock_type) 
clock.tick()
print(clock)
while True:
  clock.tick()
  time.sleep(1)
  clock.seconds += 1
  print(clock)

    