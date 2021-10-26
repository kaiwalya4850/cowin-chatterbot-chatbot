from chatterbot import ChatBot
import chatterbot
import spacy 
import warnings
warnings.filterwarnings('ignore')
spacy.load('en_core_web_sm')

'''
# Create a new instance of a ChatBot
bot = ChatBot(
    'Example Bot',
    logic_adapters=[
        {
            'import_path': 'adapter_cowin.MyLogicAdapter',
        },
    ]
)

# Get a response given the specific input
response = bot.get_response('first')
print(response)
'''


bot = ChatBot(
    'Example Bot',
    logic_adapters=[
        {
            'import_path': 'adapter_cowin1.MyLogicAdapter'
        }

    ]
)

# Get a response given the specific input
print("Hey there, my name is Ajey Bot. I'll help you get marks in your assignment")


user_input = str(input("What do you want to ask? "))
try:
    response = bot.get_response(user_input)
    print(response)
except UnboundLocalError:
    print("Please enter correct response, Ajey Bot didn't understand you")
