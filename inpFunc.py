#MODULE
import json


#FUNCTIONS

#CHECK INT VALIDITY
def inputInt(prompt):
    while True:
        userPrompt = input(prompt)        
        try:
            if userPrompt != "0": #Check if minimum of 1
                userPrompt = int(userPrompt) #Check if an integer
            else:
                print('Number is invalid due to not being a minimum of 1.')
                continue
        except:       
            print('Not a valid number.')           
            continue
        break
    return userPrompt


#CHECK STRING INPUT FOR MIN. 1 CHAR AND STRIP ANY WHITE SPACE
def inputSomething(prompt):
        while True:
            userPrompt = input(prompt)
            userPrompt = userPrompt.strip()
            if len(userPrompt) == 0: #Checks if input is at least 1 character
                print('Invalid input. Please re-enter.')
                continue
            else:
                break
        return userPrompt
    

#GET FILE, READ JSON FORMAT AND LOAD INTO A LIST
def getList(filename): 
    try:
        f = open(filename,'r')
        data = json.load(f)
        f.close()
    except: 
        data = [] #New List; if it does not exist
    return data 

    
#SAVE LIST DATA; DUMP TO FILE IN JSON FORMAT
def saveChanges(dataList):
    f = open('data.txt', 'w')
    json.dump(dataList, f, indent = 4)
    f.close()

