# Custom logic adapter #
# All working #
# Next: add corpus and preprocess and get the answer #

from chatterbot.logic import LogicAdapter


class MyLogicAdapter(LogicAdapter):
    def __init__(self, chatbot, **kwargs):
        super().__init__(chatbot, **kwargs)

    '''
    def can_process(self, statement):

        words = ['what', 'is', 'temperature']
        if all(x in statement.text.split() for x in words)
            return True
        else:
            return False
    '''

    def process(self, statement, additional_response_selection_parameters):
        from chatterbot.conversation import Statement
        import random
        
        user_input = statement.text.lower()

        if 'trial1' in user_input:
            def random_fxn(k):
                process = k + 1
                process = process * process
                return process
                
            a = random.randint(1,100)
            final = random_fxn(a)
            response_statement = Statement(text='The current temperature is {}'.format(final))
            
        if 'trial2' in user_input:
            def random_fxn(k):
                process = k + 1
                return process
                
            a = random.randint(1,100)
            final = random_fxn(a)
            response_statement = Statement(text='The current temperature is {}'.format(final))

        response_statement = Statement(text='The current temperature is {}'.format(final))

        return response_statement