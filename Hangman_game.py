# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 11:15:34 2020

@author: HP
"""
# import pygame 
import pygame
import sys
import random
import string 
# import only system from os 
from os import system, name 
from pygame import mixer 
WORDLIST_FILENAME = "words.txt"

def show_text(text_n,x,y,color):
    '''
    

    Parameters
    ----------
    text_n : the text that you want to show in the screen N.
    x      : the x position of the text.
    y      : the y position of the text .

    Returns
    -------
    None.

    '''
    text=font.render(text_n ,True ,color)
    screen.blit(text,(x,y))
        
def player(player_image,x,y):
    '''
    

    Parameters
    ----------
    player_image: the image that you want to show on the screen 
    x           : the position of the photo in the screen in x direction.
    y           : the position of the photo in the screen in y direction .

    Returns
    -------
    None.

    '''
    screen.blit(player_image,(x,y))
    
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
      it takes out a letter and return true or false 
      '''
      ch = str.lower(letters_guessed)

      if(ch=='a' or ch =='e' or ch=='i' or ch=='o' or ch=='u'):
          result = True
    
      else:
          result = False
     
      return (result)
  
 # define our clear function 
def clear(): 
    '''
    

    Returns
    -------
    None.

    '''
  
     # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
     # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear')  

def calculating_score (guesses,secret_word):
    '''
    

    Parameters
    ----------
    guesses : the number of guesses remaining (integar).
    secret_word : the word that should be guessed.

    Returns
    -------
    result : score as a number .

    '''
    unique_letters=[];
    for i in (secret_word):
        if i not in unique_letters:
            unique_letters.append(i)
    result= guesses*len(unique_letters)
    return (result)

# this function just return true or false depending either the word has letters or not
def match_with_gaps(my_word,other_word):
    '''
    

    Parameters
    ----------
    my_word : the word that have been guessed so far .
    other_word : the word that should be checked against .

    Returns
    -------
    result : true if they have the same letters in the same position 
    false otherwise .

    '''
    z=0
    y=0
    my_word=my_word.replace(' ','')       #this is to remove the spaces in the word to compare it
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
    '''
    

    Parameters
    ----------
    my_word : it take the word that have been guessed so far and
    it check in a file for a file for a possible matches  .

    Returns
    -------
    all possible matches .

    '''
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
def mesh (position,nx,ny):
    '''
    

    Parameters
    ----------
    position : grid of points .
    nx : number of points in x direction
    ny : number of points in y direction.

    Returns
    -------
    X and Y two list each have a nx*ny points .

    '''
    x=[]; y=[];
    for n in range(nx):
      for k in range(ny):
        x.append(positions[k])
        y.append(positions[n])
    return (x,y)

### Tilte and icon
#initiate pygame 
pygame.init()
#create a screen 
screen=pygame.display.set_mode((1200,800))
## this is to create an image in the screen 
player_image=pygame.image.load('hang_man.jfif')
player_x=300
player_y=350
## create a font variable 
font = pygame .font.Font('freesansbold.ttf',16);

pygame.display.set_caption('Hangman Game')
icon= pygame.image.load('hang_man.jpg')
pygame.display.set_icon((icon))
mixer.music.load('Deep-ambient-music.mp3')
mixer.music.play(-1)
secret_word='ahmedderty'  
#secret_word = choose_word(wordlist)

running = True 
guesses=6

#secret_word = choose_word(wordlist)
text_2='_'
## this loop is for starting the game and then we have the condition for closing it 
#while running:
    
    ##this line here is to add an event 
keyboard_clicks=0
running= True  
while running:
         # to add any color you need to add it RBG (Red , Blue ,Green) and it runs from 0 to 255 
     
    if keyboard_clicks ==0:
        if guesses ==0:
          pygame.time.wait(5000)
          guesses = 6
        elif guesses>0: 
          text_1='welcome to the game Hangman! '
          text_3='------------------' ; text_4='Note :you lose 2 guesses for wrong vowel and 1 guess for wrong consonants'
          text_5=' IMPORTANT NOTE : you can use a hint by entering the special charachter (/) '
          text_6='without brackets but note if it will only show 100 possible option'
          text_2='to start the game please click any button in your keyboard'
          text_position_x_n =[270 ,150,360,100,120,140,375]
          text_position_y_n =[40 ,70,90,110,140,170,275]
          blue=(0,0,100); green=(0,150,0) ; red=(150,0,0) ; black =(0,0,0)
          color=[blue,blue,blue,red,red,red]
          text_n=[text_1 ,text_2,text_3,text_4,text_5,text_6]   
          screen.fill((255,255,255)) 
          guesses=6
          warning=3
          letter_guessed=[];
          secret_word = choose_word(wordlist)
          #secret_word='ahmedderty'  
          #secret_word='ahmedderty' 
    # this player function is to add image to the screen 
          player(player_image,player_x,player_y)
    #then we need to add our text to the screen we will use show_our_text function 
    # the first text is the introduction text     
          for i in range(len(text_n)):
            show_text(text_n[i],text_position_x_n[i],text_position_y_n[i],color[i]) 
      
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit
           # this value is to terminate the print text at the beginning of the game when the game strats     
        if event.type == pygame.KEYDOWN :
             letters_guessed =pygame.key.name(event.key)
             print(letters_guessed)
             keyboard_clicks += 1
             if keyboard_clicks == 1:         
                 print(keyboard_clicks)
                 text_n1            = 'Available letters:' + get_available_letters(letter_guessed)
                 text_n2            = 'you have'+' '+str(guesses)+' '+'guesses left and ' +' ' +str(warning)+' warning left' 
                 text_n3            = 'I am thinking of a word that is ' +' '+str(len(secret_word))+' '+'letters long'
                 text_n4            =('your guessed word letters so far : ' + get_guessed_word(secret_word, letter_guessed))
                 text_nn            =[text_n3,text_n2,text_n1,text_n4]
                 text_position_x_nn =[230 ,230,180,230]
                 text_position_y_nn =[200,230,260,290]
                 color_n            =[green,green,green,green]
                 for i in range(len(text_nn)):
                      show_text(text_nn[i],text_position_x_nn[i],text_position_y_nn[i],color_n[i])
             if len(letters_guessed)==1:
               if str.isalpha(letters_guessed)== False and warning == 0 and letters_guessed != '/':
                   guesses -= 1
                   screen.fill((255,255,255))
                   text1 ='oops that is not a valid letter '
                   text2 ='YOU LOST A guess please enter a letter' 
                   text4=('your guessed word letters so far : ' + get_guessed_word(secret_word, letter_guessed))
                   text_n= 'you have'+' '+str(guesses)+' '+'guesses left and ' +' ' +str(warning)+' warning left' 
                   x     =[280,250,230,180]
                   y     =[150,180,210,270] 
                   color2=[red,red,blue,blue]
                   text  =[text1,text2,text_n,text4]
                   for i in range(len(text)):
                         show_text(text[i],x[i],y[i],color2[i])
                              
               if str.isalpha(letters_guessed) == False and warning > 0 and letters_guessed != '/':
                   warning -= 1
                   screen.fill((255,255,255))
                   text1 ='oops that is not a valid letter '
                   text2 ='YOU LOST A warning please enter a letter' 
                   text4=('your guessed word letters so far : ' + get_guessed_word(secret_word, letter_guessed))
                   text_n= 'you have'+' '+str(guesses)+' '+'guesses left and ' +' ' +str(warning)+' warning left' 
                   x     =[280,250,230,180]
                   y     =[150,180,210,270] 
                   color2=[red,red,blue,blue]
                   text  =[text1,text2,text_n,text4]
                   for i in range(len(text)):
                         show_text(text[i],x[i],y[i],color2[i])
               if str.isalpha(letters_guessed) == True and letters_guessed in letter_guessed:
                   screen.fill((255,255,255))
                   text1 ='oops you entered this letter before  '
                   text2 ='you don`t lose a GUESS please enter a new letter' 
                   text_n= 'you have'+' '+str(guesses)+' '+'guesses left and ' +' ' +str(warning)+' warning left' 
                   print(letter_guessed)
                   text4 =('your guessed word letters so far : ' + get_guessed_word(secret_word, letter_guessed))
                   x     =[220,170,200,180]
                   y     =[150,180,210,240]  
                   color2=[red,red,blue,blue]
                   text  =[text1,text2,text_n,text4]
                   for i in range(len(text)):
                         show_text(text[i],x[i],y[i],color2[i])
               if letters_guessed == '/':
                   my_word=get_guessed_word(secret_word, letter_guessed)   # this is to get the letter guessed so far
                   possible_match= show_possible_match(my_word)
                   if len(possible_match)>25:
                       possible_match=random.sample(possible_match, 25)
                       print(possible_match)
                   positions=[0,150,300,450,600]
                   [x,y]=mesh (positions,len(positions),len(positions))
                   print(x)
                   screen.fill((255,255,255))
                   for i in range(len(possible_match)):
                          color.append(black)
                          show_text(possible_match[i],x[i],y[i],color[i])
                  
                            
                           
                       
                    
                  # show('your possible matches are ',show_possible_match(my_word))
             letters_guessed=str.lower(letters_guessed)
            
             #print(letters_guessed)
             if len(letters_guessed)==1:
              n = 0
              for i in (secret_word):
                   
                   if i==letters_guessed and keyboard_clicks !=1 and i not in letter_guessed:
                      letter_guessed.append(letters_guessed)
                      
                      screen.fill((255,255,255))
                      text1 = 'Good guess: your guessed letters so far:( '+get_guessed_word(secret_word, letter_guessed)+')'
                      text2 ='please guess another letter' 
                      text_n= 'you have'+' '+str(guesses)+' '+'guesses left and ' +' ' +str(warning)+' warning left' 
                      text3 = 'Available letters: (' + get_available_letters(letter_guessed)+')'
                      x     =[140,250,210,150]
                      y     =[150,180,210,240] 
                      color2=[green,green,blue,blue]
                      text  =[text1,text2,text_n,text3]
                      for i in range(len(text)):
                         show_text(text[i],x[i],y[i],color2[i])
                      if  is_word_guessed(secret_word, letter_guessed) ==True:
                          screen.fill((255,255,255))
                          text='congratulation you have guessed the word correctly your final score is ('+str(calculating_score (guesses,secret_word))+')'
                          x=160;  y= 150; color=green;
                          print(x)
                          show_text(text,x,y,color)
                          keyboard_clicks =0
                          guesses=0
                      break
                   n +=1
                   
              if n==len(secret_word) and str.isalpha(letters_guessed)== True and keyboard_clicks != 1 and letters_guessed not in letter_guessed:
                      letter_guessed.append(letters_guessed)
                      if check_if_the_character_vowel(letters_guessed) ==True:
                         guesses -= 2
                      else:
                         guesses -= 1
                      screen.fill((255,255,255))
                      text1 ='oops ! that letter is not in my word: your guessed letters so far ('+ get_guessed_word(secret_word, letter_guessed)+')'
                      text2 ='please guess another letter' 
                      text_n='you have'+' '+str(guesses)+' '+'guesses left and ' +' ' +str(warning)+' warning left' 
                      text3 ='Available letters: (' + get_available_letters(letter_guessed)+')'
                      x     =[80,270,210,150]
                      y     =[150,180,210,240] 
                      color2=[red,red,blue,blue]
                      text  =[text1,text2,text_n,text3]
                      for i in range(len(text)):
                         show_text(text[i],x[i],y[i],color2[i])
                      if guesses <=0:
                          guesses=0
                          screen.fill((255,255,255))
                          text1 ='oops you have lost the unique word was: (' + secret_word+')'
                          text2 =' your score is (' + str(calculating_score (guesses,secret_word))+')'
                          text3 = 'please wait while the game is restarting '
                          x     =[200,220,200]
                          y     =[150,180,210] 
                          color2=[red,red,black]
                          text  =[text1,text2,text3]
                          print(text)
                          for i in range(len(text)):
                             show_text(text[i],x[i],y[i],color2[i])
                          keyboard_clicks =0
    pygame.display.update() 
    
    