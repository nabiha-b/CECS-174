#create function that contains menu
def menu(): 
    print("-----MENU-----")
    print("1 : Name")
    print("2 : String Reversal")
    print("3 : List Multiplier")
    print("4 : Sentence Capitalizer")
    print("5: To Quit")
    print("")

#create function for Name program
def name():
    print("Enter a name: First Middle Last")
    name = input("") #Get name from user input
    name_list = name.split(" ") #seperate the names and put it in list
    for name in name_list: #iterate over each name in list
        print(name[0], end='. ')#Print first letter of names followed by a period
    print("")

#Create a function for String Reversal program
def string_reversal():
    original_string = input("Enter a string: ") #Get string from user input
    reversed_string = original_string[::-1] #Reverse the string     
    print(reversed_string) #Display reversed string
   
        
#Create function for the List Multiplier program
def list_multiplier():
    print("Enter a list of numbers seperated by single spaces")
    nums = input("") #Get numbers from user input
    num_list = nums.split(" ") #split numbers and put them in list
    print("Number list:", num_list) #Display list of numbers
    product = 1 #initiate a counter
    for x in num_list: #iterate over each number in num_list
        x = int(x) #convert numbers to integers
        product = product*x #calculate product
    print(product) #display product of numbers 

    

#Create function for Sentence Capitalizer program
def sentence_capitalizer():
    string = input("Enter a string: ") #Get string from user input
    def capitalizer(string): #create function which capitalizes first letter
        sentences = string.split(". ") #seperate the sentences
        #capitalize first letter of each sentence
        #and add original remaining sentence for each sentence in string
        sentences_cap = [sentence[0].capitalize() + sentence[1:] for sentence in sentences]
        newstring = ". ".join(sentences_cap) #Join the new capitalized sentences 
        print(newstring) #Display new string
        print("")
    capitalizer(string) #Call function
    
          
#Create main function
def main():
    #Call menu function to display menu
    menu()
    try:
        #Get user input on menu selection
        option = int(input("Menu selection: "))
        #Call the program function which corresponds with user menu selection
        if option == 1:
            name()
            main()
        elif option == 2:
            string_reversal()
            main()
        elif option == 3:
            list_multiplier()
            main()
        elif option == 4:
            sentence_capitalizer()
            main()
        elif option == 5:
            print("You have chosen to quit.")
        else:
            print("Invalid Input, Try Agian.")
            main()
    #Identify and display errors for invalid inputs        
    except:
        print("Invalid input")
        #repeat menu
        main()

#Call main function       
main()

        
