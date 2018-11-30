import random

class HangmanBot():
  numGuesses = 1
  numWrong = 0
  maxWrongGuesses = 6
  usedLetters = []
  userSolution = []
  gameInProgress = True
  solution = ""
  selectedCategory = ""

  def __init__(self, dictionary, name="HangmanBot"):
    self.name = name
    self.dictionary = dictionary

  def play_hangman(self):
    """Main function to run our game."""
    
    noOpponent = True

    while noOpponent:
      opponent = input("Play vs HangmanBot or another Player? (b/p) ")

      if opponent == 'b' or opponent == 'p':
        noOpponent = False
      else:
        print(opponent)
        print("\n Invalid choice, please choose again \n")

    self.selectSolution(opponent)

    # username = input("What is your name? ")
    # self.opponent = username

    print('''
    ==============================================================
    =          ******    ******    **    **    ******            =
    =          *         *    *    * *  * *    *                 =
    =          *   **    ******    *   *  *    ******            =
    =          *    *    *    *    *      *    *                 =
    =          ******    *    *    *      *    ******            =
    =                                                            =
    =      ******    *******    ******    ******    *******      =       
    =      *            *       *    *    *    *       *         =
    =      ******       *       ******    *****        *         =
    =           *       *       *    *    *    *       *         =
    =      ******       *       *    *    *    *       *         =
    ==============================================================
    ''')

    print("     TYPE (.quit) or press cntrl + c at any time to stop playing ")

    for char in self.solution:
      if char == " ":
        self.userSolution.append(" ")
      else:
        self.userSolution.append(" _ ")

    self.printUserSolution()
    self.printHangman()
    print('''
    
    ''')

    while self.gameInProgress:
        print("Used letters: ", end="")

        for letter in self.usedLetters:
          print(letter, end="")

        userInput = input("\nPick a letter: ").lower()


        #Check for invalid input
        if len(userInput) < 1 or (len(userInput) > 1 and userInput != ".quit") :
          print("\nEnter characters only!\n")
        elif userInput == '.quit':
          # Check for an end msg 
          self.gameInProgress = False
        else:
          if userInput in self.usedLetters:
            print("\nLetter has been used already, pick another!\n")
            continue
          elif userInput not in self.solution.lower():
            self.numWrong += 1
            print("\nLetter not part of solution!\n")
          else:
            index = 0
            for char in self.solution:
              if char.lower() == userInput:
                self.userSolution[index] = char
              index += 1
          
          self.usedLetters.append(userInput)
          self.numGuesses += 1
          self.printResult()
          self.printUserSolution()
          self.printHangman()
    self.playAgain()



  def playAgain(self):
    userInput = input("\nPlay again? (y/n): ").lower()

    if userInput == 'y':
      self.numGuesses = 1
      self.numWrong = 0
      self.maxWrongGuesses = 6
      self.usedLetters = []
      self.userSolution = []
      self.gameInProgress = True
      self.solution = ""
      self.selectedCategory = ""

      self.play_hangman()
    elif userInput == 'n':
      print('''
 _____ _                 _           __                   _             _             
|_   _| |               | |         / _|                 | |           (_)            
  | | | |__   __ _ _ __ | | _____  | |_ ___  _ __   _ __ | | __ _ _   _ _ _ __   __ _ 
  | | | '_ \ / _` | '_ \| |/ / __| |  _/ _ \| '__| | '_ \| |/ _` | | | | | '_ \ / _` |
  | | | | | | (_| | | | |   <\__ \ | || (_) | |    | |_) | | (_| | |_| | | | | | (_| |
  \_/ |_| |_|\__,_|_| |_|_|\_\___/ |_| \___/|_|    | .__/|_|\__,_|\__, |_|_| |_|\__, |
                                                   | |             __/ |         __/ |
                                                   |_|            |___/         |___/ 
    ''')
    else:
      print("Invalid input, try again.")
      self.playAgain()

  def selectSolution(self, opponent):
    if opponent == 'b':
      maxCategorySelection = len(self.dictionary) - 1

      selectedCategoryIndex = random.randint(0, maxCategorySelection)
      selectedCategory = self.dictionary[selectedCategoryIndex][0]

      maxWordSelection = len(self.dictionary[selectedCategoryIndex][1]) - 1

      selectedWordIndex = random.randint(0, maxWordSelection)
      selectedWord = self.dictionary[selectedCategoryIndex][1][selectedWordIndex]

      self.selectedCategory = selectedCategory
      self.solution = selectedWord
    else:
      player1 = input("\nPlayer1 please enter your name: ")
      player2 = input("\nPlayer2 please enter your name: ")

      userCategory = input("\n(Player1) [" + player1 + "] please enter category/hint for [" + player2 + "]: ")
      userSolution = input("\n(Player1) [" + player1 + "] please enter solution for [" + player2 + "]: ")
      self.selectedCategory = userCategory
      self.solution = userSolution

  def printResult(self):
    testSolution = "".join(self.userSolution)

    if self.numWrong == self.maxWrongGuesses:
      print('''
    ======================================================
                          (`-').->(`-')  _   (`-') ,---. 
        <-.        .->    ( OO)_  ( OO).-/<-.(OO ) |   | 
      ,--. )  (`-')----. (_)--\_)(,------.,------,)|   | 
      |  (`-')( OO).-.  '/    _ / |  .---'|   /`. '|   | 
      |  |OO )( _) | |  |\_..`--.(|  '--. |  |_.' ||  .' 
      (|  '__ | \|  |)|  |.-._)   \|  .--' |  .   .'`--'  
      |     |'  '  '-'  '\       /|  `---.|  |\  \ .--.  
      `-----'    `-----'  `-----' `------'`--' '--'`--'  
    ======================================================
    ''')
      self.gameInProgress = False

    elif testSolution.lower() == self.solution.lower():
      print('''
    ======================================================
  (`\ .-') /`            .-') _      .-') _   ('-.  _  .-')  ,---. 
   `.( OO ),'           ( OO ) )    ( OO ) )_(  OO)( \( -O ) |   | 
,--./  .--.  ,-.-') ,--./ ,--,' ,--./ ,--,'(,------.,------. |   | 
|      |  |  |  |OO)|   \ |  |\ |   \ |  |\ |  .---'|   /`. '|   | 
|  |   |  |, |  |  \|    \|  | )|    \|  | )|  |    |  /  | ||   | 
|  |.'.|  |_)|  |(_/|  .     |/ |  .     |/(|  '--. |  |_.' ||  .' 
|         | ,|  |_.'|  |\    |  |  |\    |  |  .--' |  .  '.'`--'  
|   ,'.   |(_|  |   |  | \   |  |  | \   |  |  `---.|  |\  \ .--.  
'--'   '--'  `--'   `--'  `--'  `--'  `--'  `------'`--' '--''--'  
    ======================================================
    ''')
      self.gameInProgress = False


  def printUserSolution(self):
    print("==================================================================")
    print("\nAttempt " + str(self.numGuesses) + " [Category: " + self.selectedCategory + "]")
    print('''
====================
= CURRENT SOLUTION =
====================
    ''')

    if self.gameInProgress == True:
      for char in self.userSolution:
          print(char, end = "")
      print()
    else:
      print(self.solution)


  def printHangman(self):
    if self.numWrong == 0:
      print('''
      ======================================================

                            *************
                            *           *
                            *           
                            *           
                            *           
                            *          
                            *           
                            *            
                            *           
                            *            
                            *             
                            *              
                            *
                            *
                            *
      ======================================================
      ''')
    elif self.numWrong == 1:
      print('''
      ======================================================

                            *************
                            *           *
                            *          ***
                            *         *   *
                            *          ***
                            *          
                            *           
                            *            
                            *           
                            *            
                            *             
                            *              
                            *
                            *
                            *
      ======================================================
      ''')
    elif self.numWrong == 2:
      print('''
      ======================================================

                            *************
                            *           *
                            *          ***
                            *         *   *
                            *          ***
                            *           * 
                            *           *
                            *           * 
                            *           *
                            *            
                            *             
                            *              
                            *
                            *
                            *
      ======================================================
      ''')
    elif self.numWrong == 3:
      print('''
      ======================================================

                            *************
                            *           *
                            *          ***
                            *         *   *
                            *          ***
                            *           * 
                            *         ***
                            *        *  *  
                            *           *
                            *            
                            *             
                            *              
                            *
                            *
                            *
      ======================================================
      ''')
    elif self.numWrong == 4:
      print('''
      ======================================================

                            *************
                            *           *
                            *          ***
                            *         *   *
                            *          ***
                            *           * 
                            *         *****
                            *        *  *  *
                            *           *
                            *            
                            *             
                            *              
                            *
                            *
                            *
      ======================================================
      ''')
    elif self.numWrong == 5:
      print('''
      ======================================================

                            *************
                            *           *
                            *          ***
                            *         *   *
                            *          ***
                            *           * 
                            *         *****
                            *        *  *  *
                            *           *
                            *          *  
                            *         *    
                            *              
                            *
                            *
                            *
      ======================================================
      ''')
    elif self.numWrong == 6:
      print('''
      ======================================================

                            *************
                            *           *
                            *          ***
                            *         *   *
                            *          ***
                            *           * 
                            *         *****
                            *        *  *  *
                            *           *
                            *          * *
                            *         *   *
                            *              
                            *
                            *
                            *
      ======================================================
      ''')