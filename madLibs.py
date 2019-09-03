import random
from sys import exit
TEMPLATE_LIST = [
    # I found these two on reddit
    ["10 WAYS TO ", "verb", " YOUR ", "noun", ". ", "plural noun", " HATE HIM, FIND OUT WHY!"],
    ["This one time, I was at ", "place", " when I found a whole pile of ", "plural noun",
     ", turns out it was pretty toxic. Hope I don't lose my ", "body part", " to the radiation."],
    # Quote from It's Always Sunny
    ["Whoops! I dropped my ", "adjective", " ", "object", " that I use for my ", "adjective", " ",
     "body part", "."]
]


# returns random template from template list created above.
def get_random_template():
    return TEMPLATE_LIST[random.randrange(0, len(TEMPLATE_LIST), 1)]


# searches for the needed values in the template array and and returns a Str array with the text for the html form
def get_needed_types(template):
    needed_types = []
    for i in template[1::2]:
        needed_types.append("(?) " + i + ": ")
    return needed_types


# removes extra spaces and that length is at least 2 char
def process_response(response):
    response.strip() # remove spaces and the beggining and end.
    if len(response) < 2:
        return False
    return True


# gets user input for the madlib
def get_responses(needed_words):
    responses = []
    print("    Now fill in the blanks! ")
    for prompt in needed_words:
        input_word = input(prompt)
        while not process_response(input_word): # repeat for edge cases
            input_word = input(prompt)
        responses.append(input_word)
    return responses


def menu():
    print(" ~ * ~ * ~ .: MadLibs Menu :. ~ * ~ * ~ ")
    print("      Z: Select madlib (1 - 3)")
    print("      R: Begin random madlib")
    print("      H: Displays this menu again")
    print("      X: Exit program")

def options(mMadLib, selection):
    selection.lower()
    if selection == "r": #
        responses = get_responses(mMadLib.needed_types)
        mMadLib.complete_mad_lib(responses)
    elif selection == "z": #
        template_num = input("(?) Choose a template (1 - 3): ")
        while not mMadLib.select_template(template_num): # edge cases
            template_num = input("(?) Choose a template (1 - 3): ")

        responses = get_responses(mMadLib.needed_types)
        mMadLib.complete_mad_lib(responses)
    elif selection == "h": # prints the help menu
        menu()
    elif selection == "x": # ends the program
        exit()
    else:
        print("(!) Sorry, I'm not sure what that means. Try again.")


class MadLib:
    def __init__(self):
        self.template = get_random_template()
        self.needed_types = get_needed_types(self.template)
        self.final_mad_lib = ""

    def select_template(self, num):
        if int(num) < len(TEMPLATE_LIST):
            self.template = TEMPLATE_LIST[int(num)-1]
            return True
        else:
            return False

    def complete_mad_lib(self, user_words):
        for i in range(1, len(self.template), 2):
            self.template[i] = user_words[0]
            user_words.pop(0)
        self.final_mad_lib = "".join(self.template)
        self.print_mad_lib()
        menu()

    def print_mad_lib(self):
        print("\n ~ * ~ * ~ .: Your MadLib :. ~ * ~ * ~ ")
        print(self.final_mad_lib)
        print("   ~ * ~ * ~ .: The End :. ~ * ~ * ~ \n")

menu()
while True: # loop ends when the user types in X
    mMadLib = MadLib()
    selection = input("--> ")
    options(mMadLib, selection)
