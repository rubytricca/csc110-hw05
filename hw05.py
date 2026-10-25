"""
Name: Ruby Tricca
Peers: none
References: my notes
"""

def get_letter():
    #takes a string as input and checks length, case, and letter
    #returns letter as a string if all criteria are met
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
            break

def get_digit():
    #takes a string as input and checks whether it is a digit, length, and number
    #returns digit as a string if all criteria are met
        while True:
            digit= str(input("Give a single number character: "))
            if not digit.isdigit():
                print("Error: your input should be only digits.")
                continue
            if digit not in "123" or len(digit)>1:
                print("Error: a single digit needs to be in [1,3].")
                continue
            else:
                return digit
                break
    #takes 3 arguments and checks given list for strings containing letter and digit in that order
    #prints strings in list that meet the criteria 
def check_pattern(letter, digit, st_list):
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
st_list = ["@C@2", "@2B", "A3", "C2C2", "AA@1", "@B@33",
"B@2@", "@@C1", "1B@", "A@@2", "@A3@", "@1@A", "2AA@",
"1B1B", "333B", "1@CC", "3@@C", "333C"]

#runs all functions
#main function repeats if user enters input y, ends otherwise
def main ():
    while True:
        letter = get_letter()
        digit = get_digit()
        check_pattern(letter, digit, st_list)
        cont=str(input("Try Again? (y/n): "))
        if cont=="y":
            continue
        else:
            break
        
        
        
              
    # No need to modify anything Below this line
    print("The End")
    

# Do not modify these two lines
if __name__ == "__main__":
    main()