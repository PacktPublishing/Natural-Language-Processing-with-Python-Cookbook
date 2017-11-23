import nltk

def builtinEngines(whichOne):
    if whichOne == 'eliza':
        nltk.chat.eliza.demo()
    elif whichOne == 'iesha':
        nltk.chat.iesha.demo()
    elif whichOne == 'rude':
        nltk.chat.rude.demo()
    elif whichOne == 'suntsu':
        nltk.chat.suntsu.demo()
    elif whichOne == 'zen':
        nltk.chat.zen.demo()
    else:
        print("unknown built-in chat engine {}".format(whichOne))

def myEngine():
    chatpairs = (
        (r"(.*?)Stock price(.*)",
            ("Today stock price is 100",
            "I am unable to find out the stock price.")),
        (r"(.*?)not well(.*)",
            ("Oh, take care. May be you should visit a doctor",
            "Did you take some medicine ?")),
        (r"(.*?)raining(.*)",
            ("Its monsoon season, what more do you expect ?",
            "Yes, its good for farmers")),
        (r"How(.*?)health(.*)",
            ("I am always healthy.",
            "I am a program, super healthy!")),
        (r".*",
            ("I am good. How are you today ?",
            "What brings you here ?"))
    )
    def chat():
        print("!"*80)
        print(" >> my Engine << ")
        print("Talk to the program using normal english")
        print("="*80)
        print("Enter 'quit' when done")
        chatbot = nltk.chat.util.Chat(chatpairs, nltk.chat.util.reflections)
        chatbot.converse()

    chat()

if __name__ == '__main__':
    for engine in ['eliza', 'iesha', 'rude', 'suntsu', 'zen']:
        print("=== demo of {} ===".format(engine))
        builtinEngines(engine)
        print()
    myEngine()
