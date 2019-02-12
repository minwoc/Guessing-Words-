parts_of_speech1  = ["___1___", "___2___", "___3___", "___4___"]
test_string1 = "A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary, tuple, and ___4___ or can be more complicated such as objects and lambda functions."
test_string2 = "YOOOOOO"
correct_answers1 = ["function", "parameters", "none", "list"]
statement = "That isn't the correct answer!  Let's try again; you have "

def current_paragraph():
    print "The current paragraph reads as such: \n"
    print test_string1

def callgame(user_input, testing_string):
    print "\nYou've chosen " + str(user_input)+"! \n\nYou will get 5 guesses per problem \n\n"
    current_paragraph()

def chose():
    user_input = raw_input("Please chose level of difficulties: Easy Medium Hard:" + " ")
    if(user_input=="Easy"):
        return callgame(user_input, test_string1)
    elif(user_input=="Medium"):
        return callgame(user_input, test_string2)
    elif(user_input=="Hard"):
        return callgame(user_input, test_string3)

def word_in_pos(word, parts_of_speech1):
    #Procedure that return a word(__#__) if it contains part of speech
    for pos in parts_of_speech1:
        if pos in word:
            return pos
    return None

# Plays a full game of mad_libs. A player is prompted to replace words in ml_string,
# which appear in parts_of_speech with their own words.
def play_game(ml_string, parts_of_speech1):
    chose()
    replaced = []
    ml_string = ml_string.split()
    for word in ml_string: #reading string in list you created
        #i=0
        #parts_of_speech1 = parts_of_speech1[i]
        replacement = word_in_pos(word, parts_of_speech1) #same word in variable
        count = 0
        index = 0
        replaced.append(word)
        print replaced
        while replacement != None: #loop until word in not part of speech
            user_input = raw_input("What should be substitued in for " + replacement + "? as  ")
            if (user_input != correct_answers1[index]): #wrong answer, expecting next answer for 2nd and 3rd..
                if (count<4): #four chances
                    count +=1
                    print "This isn't the correct answer! Let's try again; you have " + str((count*-1)+5) + " tries left! \n"#statement + str((i*-1)+5) + "tries left!"
                    current_paragraph()
                else:
                    return "You've failed too many straight guesses!  Game over!"

            else: #correct answer, #need an if statement
                #i+=1
                word = word.replace(replacement, user_input) #this word is __#__ that needs to be replaced in ml string
                replaced.append(word)
                index+=1
                break
    replaced = " ".join(replaced)
    return replaced            #print replaced

    #Need a way to store strings list
    #python fill_in_the_b.py
"""for word in strings_lb:
    if word.isalpha():
    continue
    else:
        empty_list.append(word)
    print empty_list"""

print play_game(test_string1, parts_of_speech1)
