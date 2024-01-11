print("Hello welcome to elite 101 chat bot.")
name =input("What is your name: ")
age =int(input(f'Hello {name}, how old are you? '))

if (age >18):
  print(f'welcome {name}, O to be young again')

else:
  if age >18 and age<20 :
    print(f'welcome {name}, O to be at the turning point of life ')
  
  else:
    if age>20 and age<50:
      print(f'welcome {name}, O to be a the prime of your life')
    else:
      if age>50:
        print(f'welcome {name}, O to be at the golden years')
print("\nHow can i be of assistace ")
while True:
  print("please chose from the following options: ")
  print("placeholder option 1")
  print("placeholder option 2")
  print("placeholder option 3")
  print("exit from program 4")
  x= int(input("please enter your choice: "))
  if x==4:
    break

print(f'goodbye {name}, have a good day.')