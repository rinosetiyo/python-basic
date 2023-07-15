import random as rd
class PythonBasic():
    def BandName():
        print("Band name generator")
        city = input("where is your grew up ?")
        pet = input('what is your pet name ?')
        print(f"Your band name is {city} {pet}")

    def TipCalculator():
        print("Welcome to tip calculator")
        total_bill = input("what is your total bill ? ")
        percentage = input("how much do you want to give tip 10, 12, 15 ? ")
        split_bill = input("how many people do you want to split ? ")
        calculate = (int(total_bill) - ( int(total_bill) * (int(percentage) / 100))) / int(split_bill)
        print(f"Every person can pay ${round(calculate)}")

    def TreasureIsland():
        print("Treasure Island")
        choose1 = input("In front of there is 2 doors in Rigth and Left, what do you choose ? ")

        if choose1.lower() == "left":
            choose2 = input("in front of you there is river, what do you do swim or waiting boat ? ")
            if choose2.lower() == "waiting":
                choose3 = input("in front of there is 3 doors blue, yellow, red. what do you choose ? ")
                if choose3.lower() == "yellow":
                    print("You win !!!")
                else:
                    print("Game over")
            else:
                print("Game over")
        else:
            print("Game over")

    def RCPaper():
        print("Welcome to rock = 0, scissors = 1, paper = 2")
        import random as rd
        user = int(input("what your choose ? "))
        computer = rd.randint(0, 2)

        print(f"Your choice is {user}")
        print(f"Computer choose {computer}")

        if user == 0 and computer == 1:
            print("You win !")
        elif user == 0 and computer == 2:
            print("You lose, computer win !")
        elif user == 1 and computer == 0:
            print("You lose")
        elif user == 1 and computer == 2:
            print("You win !")
        elif user == 2 and computer == 0:
            print("You win !")
        elif user == 2 and computer == 1:
            print("You lose")
        elif user == computer:
            print("Draw !")
        else:
            print("Invalid input")

    def PyPassword():
        print("Welcome to pypassword generator")
        import random as rd
        latters = ['q','w','e','r','t','y','Q','W','E','R','T','Y']
        numbers = ['1','2','3','4','5']
        symbols = ['!','@','#','$','%','^','&','*','(',')']

        number_latter = int(input("How many latters do you want ? "))
        nr_number = int(input("How many numbers do you want ? "))
        number_symbol = int(input("How many symbols do you want ? "))

        password = []
        for char in range(1, number_latter + 1):
            password += rd.choice(latters)
        for char in range(1, nr_number + 1):
            password += rd.choice(numbers)
        for char in range(1, number_symbol + 1):
            password += rd.choice(symbols)
        rd.shuffle(password)
        convert_str = ""
        for char in password:
            convert_str += char
        print(convert_str)
    
    def GuestWord():
        sosmed_words = ['twitter','instagram','facebook']
        random_word = rd.choice(sosmed_words)

        word_length = len(random_word)

        display = []
        for _ in range(word_length):
            display += "_"
        print(display)
        lives = 4
        end_game = False

        while not end_game:
            guess = input("Guest a letter ? ")
            for position in range(word_length):
                letter = random_word[position]
                if letter == guess:
                    display[position] = letter
            if guess not in random_word:
                lives -= 1
                if lives == 0:
                    end_game = True
                    print("You lose")
                    print(f"The word is {random_word}")
            print(display)
            if "_" not in display:
                end_game = True
                print("You win")

    def Auction():
        print("----- bidding game -----")
        def play():
            name = input("what is your name ? ")
            bid = int(input("how much did you bid ? "))
            bid_dic = {}
            bid_dic[name] = bid
            print(f"the higher is {bid_dic[name]}")
            next_bid = input("did anyone bid more higher ? press y/n ")
            if next_bid == "y":
                name2 = input("what is your name ? ")
                bid2 = int(input("how much did you bid ? "))
                bid_dic[name2] = bid2
                while bid_dic[name2] > bid_dic[name]:
                    bid_dic[name2]
                    print(f"the higher is {bid_dic[name2]}")
                    next_bid = input("did anyone bid more higher ? press y/n ")
                    if next_bid == "y":
                        return play()
                    else:
                        print(f"the higher is {bid_dic[name2]}")
            else:
                print(f"the higher is {bid_dic[name]}")
        play()

def calculator():
    print("----- welcome to calculator -----")
    num1 = int(input("first number : "))
    operator = input("operator + , - , * , /, : ")
    num2 = int(input("second number : "))
    add = num1 + num2
    subtr = num1 - num2
    mutiply = num1 * num2
    devide = num1 / num2
    operations = {
        "+": add,
        "-": subtr,
        "*": mutiply,
        "/": devide,
        }
    if operator == "+":
        print(operations["+"])
    elif operator == "-":
        print(operations["-"])
    elif operator == "*":
        print(operations["*"])
    elif operator == "/":
        print(operations["/"])


calculator()


class codewars():
    def find_needle(haystack):
        find = "needle"
        if find in haystack:
            position = haystack.index(find)
            print(f"find needle at position {position}")

    #find_needle(["baso",1,'ayam geprek',"needle"])

    def friend(x):
        list = []
        for a in x:
            if len(a) == 4:
                list += [a]
        print(list)

    #friend(["rino","setiyo","hadi","mustofa"])