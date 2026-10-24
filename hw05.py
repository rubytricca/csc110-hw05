"""
Name: Ruby Tricca
Peers: none
References: my notes
"""

def get_letter():
    #Add your own Docstring
    while True:
        letter = str(input("Give an single uppercase letter: "))
        if len(letter) > 1:
            print("Error: it needs to be a single character.")
            continue
        if letter not in "ABC":
            print("Error: You provided the wrong character.")
            continue
        else:
            return letter

def get_digit():
    #Add your own Docstring 
    # remove the default return and add your code 
        while True:
            digit= str(input("Give a single number character: "))
            if not digit.isdigit():
                print("Error: your input should be only digits.")
                continue
            if digit not in "123":
                print("Error: a single digit needs to be in [1,3].")
                continue
            else:
                return digit
                break

def check_pattern(letter, digit):
    # Add your own Docstring
    st_list = ["@C@2", "@2B", "A3", "C2C2", "AA@1", "@B@33",
    "B@2@", "@@C1", "1B@", "A@@2", "@A3@", "@1@A", "2AA@",
    "1B1B", "333B", "1@CC", "3@@C", "333C"]
    print("Strings with the pattern:")
    for idx in st_list:
            if idx[1::2] == letter+digit:
                word1 = idx
                print(word1, end=" ")
                continue 
            if f"{letter}{digit}" in idx:
                word2 = idx
                print(word2, end=" ")
                continue

def main ():
    """ gets a letter-num pair and searches inside a list for matches"""
    while True:
        letter = get_letter()
        digit = get_digit()
    #The list inside of which we will search the user pair (DO NOT MODIFY)
        check_pattern(letter, digit)
        st_list = ["@C@2", "@2B", "A3", "C2C2", "AA@1", "@B@33",
        "B@2@", "@@C1", "1B@", "A@@2", "@A3@", "@1@A", "2AA@",
        "1B1B", "333B", "1@CC", "3@@C", "333C"]
        print("\n")
        cont=str(input("Try Again? (y/n): "))
        if cont=="y":
            continue
        else:
            exit
              
    # No need to modify anything Below this line
    print("The End")
    

# Do not modify these two lines
if __name__ == "__main__":
    main()