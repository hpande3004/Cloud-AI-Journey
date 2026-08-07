'''EXCEPTION HANDLING'''
#try - except

try:
    print(x)                                    #X not defined, so prog will show error. Try was just to test that
except:
    print("Exception occured")                  #Instead of showing error, it will show the message in except block

try:
    print(x)
except NameError:                               #Runs if the referred var is undefined
    print("Var not defined")
except:
    print("Smth else is wrong")

try:
    print("Hey")
except:
    print("Wrong")
else:
    print("Everything Good")                    #If there's not error in the code, else block gets executed

try:
    print(x)
except:
    print("Wrong in code")
finally:
    print("Try Except is finished")            #Finally block gets printed regardless the code is wrong or right

