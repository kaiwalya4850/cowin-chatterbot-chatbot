from chatterbot.logic import LogicAdapter


class MyLogicAdapter1(LogicAdapter):
    def __init__(self, chatbot, **kwargs):
        super().__init__(chatbot, **kwargs)


    def can_process(self, statement):

        user_input = statement.text.lower()
        
        if 'first' in user_input:
            return True
        else:
            final = 0
            return False


    def process(self, statement1, additional_response_selection_parameters):
        from chatterbot.conversation import Statement
        import random
        
        user_input = statement1.text.lower()
        
        #if 'first' not in user_input:
        #    return 0, Statement('')

        
        def random_fxn(k):
            process = k + 1
            process = process * process
            return process
            
        a = random.randint(1,100)
        final = random_fxn(a)

        response_statement = Statement(text='The current temperature is {}'.format(final))

        return response_statement
