# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string 
# import only system from os 
from os import system, name 
  
# import sleep to show output for some time period 


WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()



def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    
    letters_true_guessed=[]
    for i in (letters_guessed):
      for n in (secret_word):
       if i ==n:
         letters_true_guessed.append(i)
    if len(letters_true_guessed)==len(secret_word):
        result = True
    else:
        result = False
    return result



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    letters_true_guessed=[]
    for i in range(len(secret_word)):
     letters_true_guessed.append('_ ')
    position = 0
    for i in (secret_word):
       for n in (letters_guessed):
           if i==n:
              letters_true_guessed[position]=i
       position +=1
    full_str = ' '.join([str(elem) for elem in letters_true_guessed])   
    return full_str


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    A=string.ascii_lowercase
    Letters_available=[]
    position=0
    count=0
    for i in A:
      Letters_available.append(i)
    for i in A:
        for n in letters_guessed:
          if i==n:
           del Letters_available[position-count]
           count += 1
        position += 1
    full_str = ' '.join([str(elem) for elem in Letters_available])
    return (full_str)

def check_if_the_character_vowel(letters_guessed):
      '''
      this function is to check if the inputed letter is a vowel or a consonants 
      '''
      ch = str.lower(letters_guessed)

      if(ch=='a' or ch =='e' or ch=='i' or ch=='o' or ch=='u'):
          result = True
    
      else:
          result = False
     
      return (result)
  
 # define our clear function 
def clear(): 
  
     # for windows 
     if name == 'nt': 
        _ = system('cls') 
  
     # for mac and linux(here, os.name is 'posix') 
     else: 
        _ = system('clear')  

def calculating_score (guesses,secret_word):
    unique_letters=[];
    for i in (secret_word):
        if i not in unique_letters:
            unique_letters.append(i)
    result= guesses*len(unique_letters)
    return (result)

# this function just return true or false depending either the word has letters or not
def match_with_gaps(my_word,other_word):
    z=0
    y=0
    for i in range(len(my_word)):
      if len(my_word) != len(other_word):
            result = False
            break
      if str.isalpha(my_word[i])== True:
            z +=1
      if my_word[i] == other_word[i]:
              y += 1
    if z==y and z != 0:
       result =(True)
    else:
        result =False

    return result
        
def show_possible_match(my_word):
    z=0
    possible_matches=[]
    for i in range(len(my_word)):
       if str.isalpha(my_word[i])== False:
           z +=1
    if z == len(my_word):
       possible_matches=(wordlist)
    for n in wordlist:
        if match_with_gaps(my_word,n) == True:
           possible_matches.append(n)
           
    return(possible_matches)
         
    
            
    
def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    #number_of_guesses=6;
    print('welcome to the game Hangman!');print('I am thinking of a word that is',len(secret_word), 'letters long')
    print('------------------');print('Note :you lose 2 guesses for wrong vowel and 1 guess for wrong consonants');
    print(' IMPORTANT NOTE : you can use a hint by entering the special charachter * but dont use it if you didn`t do any right guesses')
    guesses=6
    warning=3
    
    letter_guessed=[];
    while guesses >0:
        #this part is to give the user the number of warnings and number of guesses remaining
        clear() 
        print('Available letters:' , get_available_letters(letter_guessed))
        print ('you have' , guesses,'guesses left');print('you have', warning ,' warning left')
        letters_guessed=input('please guess a letter')
        if str.isalpha(letters_guessed)== False and warning == 0 and letters_guessed != '*':
              guesses -= 1
              print('oops that is not a valid letter ');
              print('your guessed word letters so far ' , get_guessed_word(secret_word, letter_guessed))             
        if str.isalpha(letters_guessed) == False and warning > 0 and letters_guessed != '*':
            warning -= 1
            print('oops that is not a valid letter ');
            print(get_guessed_word(secret_word, letter_guessed))
        if letters_guessed == '*':
            my_word=get_guessed_word(secret_word, letter_guessed)   # this is to get the letter guessed so far
            my_word=my_word.replace(' ','')       #this is to remove the spaces in the word to compare it 
            print('your possible matches are ',show_possible_match(my_word))
            
        letters_guessed=str.lower(letters_guessed)
        # this part is to check if the guess is valid or not 
        n=0
        for i in (secret_word):
            if i==letters_guessed:
                letter_guessed.append(letters_guessed)
                print ('Good guess: your guessed letters so far  ' , get_guessed_word(secret_word, letter_guessed));
                if  is_word_guessed(secret_word, letter_guessed) ==True:
                    print('congratulation you have guessed the word correctly your final score is ',calculating_score (guesses,secret_word))
                    guesses=0
                break
            n += 1
            if n==len(secret_word) and str.isalpha(letters_guessed)== True:
                letter_guessed.append(letters_guessed)
                if check_if_the_character_vowel(letters_guessed) ==True:
                    guesses -= 2
                else:
                    guesses -= 1
                print ('oops ! that letter is not in my word: your guessed letters so far  ',get_guessed_word(secret_word, letter_guessed));
                if guesses ==0:
                   print ('oops you have lost the unique word was ', secret_word , 'your score is' ,calculating_score (guesses,secret_word))
                    
            
                 
        
          
    
        


# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



#def match_with_gaps(my_word, other_word):
  #  '''
  #  my_word: string with _ characters, current guess of secret word
  #  other_word: string, regular English word
  #  returns: boolean, True if all the actual letters of my_word match the 
#        corresponding letters of other_word, or the letter is the special symbol
   #     _ , and my_word and other_word are of the same length;
   #     False otherwise: 
 #   '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
 #   pass



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    secret_word = choose_word(wordlist)
    #secret_word='aheed'
    hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    #secret_word = choose_word(wordlist)
    #hangman_with_hints(secret_word)
