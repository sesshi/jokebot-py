# Name:  Debbie Yung
# Student Number:  10417380



#JOKES REFERENCED IN BASE FILE: http://goodriddlesnow.com/jokes/by/clean-jokes



#MODULES
import json
import inpFunc



#GET FILE
FILENAME = 'data.txt'
dataList = inpFunc.getList(FILENAME)



#WELCOME MESSAGE
print('Welcome to the Joke Bot Admin Program.')



#MAIN BODY LOOP
while True:   
    print('Choose [a]dd, [l]ist, [s]earch, [v]iew, [d]elete, [t]op or [q]uit.')
    choice = input('> ').lower() # Prompt for input and convert it to lowercase.



    #ADD    
    if choice == 'a':
        jokeDict = {} #Empty Dictionary
        
        jokeSetup = inpFunc.inputSomething('Write a joke:')
        jokeDict['setup'] = jokeSetup #Stores the setup in empty Dict
        
        jokePunchline = inpFunc.inputSomething('And what is the punchline:')
        jokeDict['punchline'] = jokePunchline #Stores the punchline in empty Dict

        jokeDict['numOfRatings'] = 0 #placeholder
        jokeDict['sumOfRatings'] = 0 #placeholder

        #Append to main file-list and save to JSON 
        dataList.append(jokeDict)         
        inpFunc.saveChanges(dataList)
        print('Joke was added successfully.' + '\n')




    #LIST
    elif choice == 'l':
        
        if not dataList:
            print("No Jokes Saved. Let's add some! Enter (a)")
            
        else:
            for index, item in enumerate(dataList): #Loops through the Dict items in the List
                print("{})".format(index+1),item['setup']) #Displays Dict item joke setups with index number
                



    #SEARCH
    elif choice == 's':

        noJoke = True
        
        if not dataList:
            print("No Jokes Saved. Let's add some! Enter (a)")
            
        else:
            searchItem = inpFunc.inputSomething('Enter a search term: ') #Gets the word user wants to search
            searchItem = searchItem.lower()

            for index, jokeItem in enumerate(dataList):  
                if searchItem in jokeItem['setup'].lower() or searchItem in jokeItem['punchline'].lower():
                    print('Search term found in joke number:',index,'\nSetup:',jokeItem['setup'],'\nPunchline:',jokeItem['punchline'],'\n')
                    noJoke = False

            if noJoke == True:
                print('No match found.')
                
            

    #VIEW
    elif choice == 'v':
        
        if not dataList:
            print("No Jokes Saved. Let's add some! Enter (a)")
            
        else: 
            viewItem = inpFunc.inputInt('Joke number to view: ') - 1 #User inputs number to view

            try:                   
                viewDict = dataList[viewItem]
                print('Setup:',viewDict['setup'],'\nPunchline:',viewDict['punchline'])

                if viewDict['numOfRatings'] == 0:
                    print('Joke has no ratings.')
                else:
                    print('Number of ratings:',viewDict['numOfRatings'])  
                    print('Average ratings:',round(viewDict['sumOfRatings']/viewDict['numOfRatings'],1))
            except IndexError:
                print('Invalid number. Please choose a valid joke number to view.')


                                                            

    #DELETE
    elif choice == 'd':
        
        if not dataList:
            print("No Jokes Saved.")
            
        else:
            
            deleteItem = inpFunc.inputInt('Enter joke number to delete: ') - 1 #User inputs number to delete
            
            try:
                del dataList[deleteItem]
                print('Joke Deleted.')
                inpFunc.saveChanges(dataList)
            except IndexError:
                print('Invalid number. Please choose a valid joke number to delete.')
                



    #TOP        
    elif choice == 't':
        noRate = True
        
        if not dataList:
            print('No Jokes Saved.')
            
        else:
            for index, jItem in enumerate(dataList):  
                if jItem['numOfRatings'] > 0 and (jItem['sumOfRatings']/jItem['numOfRatings'] >= 4):
                    print('Top jokes with ratings over 4.0')
                    print(index, jItem['setup'])
                    noRate = False
            if noRate == True:
                print('No jokes were rated over 4.0')
                    
                  
            

    #QUIT
    elif choice == 'q':
        print('Goodbye!')
        break




    #ANY OTHER INPUT
    else:
        print('Invalid Choice.')

