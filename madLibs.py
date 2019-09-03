import random
TEMPLATE_LIST = [
    # I found these two on reddit
    ["10 WAYS TO ", "~verb", " YOUR ", "~noun", ". ", "~plural noun", " HATE HIM, FIND OUT WHY!"],
    ["This one time, I was at ", "~place", " when I found a whole pile of ", "~plural noun",
     ", turns out it was pretty toxic. Hope I don't lose my ", "~body part", " to the radiation."],
    # Quote from It's Always Sunny
    ["Whoops! I dropped my ", "~adjective", " ", "~object", " that I use for my ", "~adjective", " ",
     "~body part", "."]
]


# returns random template from template list created above.
def get_random_template():
    return TEMPLATE_LIST[random.randrange(0, len(TEMPLATE_LIST), 1)]


# searches for the needed values in the template array and and returns a Str array with the text for the html form
def get_needed_types(template):
    needed_types = []
    for i in template[1::2]:
        needed_types.append("Name a(n) " + i[1:] + ":")
    return needed_types


# removes extra spaces
def process_responses(responses):
    for i in range(len(responses)):
        while responses[i].endswith(" "):    # removes space at the end, if there is one
            responses[i] = responses[i][:-1]
        while responses[i].startswith(" "):    # removes space at the start, if there is one
            responses[i] = responses[i][1:]
    return responses


class MadLib:
    def __init__(self):
        self.template = get_random_template()
        self.needed_types = get_needed_types(self.template)
        self.final_mad_lib = ""

    def complete_mad_lib(self, user_words):
        for i in range(1, len(self.template), 2):
            self.template[i] = user_words[0]
            user_words.pop(0)
        self.final_mad_lib = "".join(self.template)
        return self.final_mad_lib

playing = True
while playing:
    #main loop

# pickForMe = input("'r' for random words. 'e' to pick your own./n--> ")
# if pickForMe == 'r':
#     random_mad_lib()
# elif pickForMe == 'e':
#     choose_your_own()
