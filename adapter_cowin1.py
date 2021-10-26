from chatterbot.logic import LogicAdapter


class MyLogicAdapter(LogicAdapter):
    def __init__(self, chatbot, **kwargs):
        super().__init__(chatbot, **kwargs)


    def process(self, statement1, additional_response_selection_parameters):
        from chatterbot.conversation import Statement
        import requests
        import datetime
        import json
        import time
        import random
        import nltk 
        import numpy as np
        import random 
        import string 
        import streamlit as st
        from sklearn.metrics.pairwise import cosine_similarity 
        from sklearn.feature_extraction.text import TfidfVectorizer 
        import warnings
        warnings.filterwarnings('ignore')
        
        user_input = statement1.text.lower()
        
        ##### Cosine Similarity ####
        
        filepath='Vaccination.txt'
        corpus=open(filepath,'r',errors = 'ignore')
        raw_data=corpus.read()
        raw_data=raw_data.lower()
        sent_tokens = nltk.sent_tokenize(raw_data)
        lemmer = nltk.stem.WordNetLemmatizer()
        def LemTokens(tokens):
            return [lemmer.lemmatize(token) for token in tokens]
        
        remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)
        def LemNormalize(text):
            return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))
            
        def response(user_response):
            robo_response='' # initialize a variable to contain string
            sent_tokens.append(user_response) #add user response to sent_tokens
            TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english') 
            tfidf = TfidfVec.fit_transform(sent_tokens) #get tfidf value
            vals = cosine_similarity(tfidf[-1], tfidf) #get cosine similarity value
            idx=vals.argsort()[0][-2] 
            flat = vals.flatten() 
            flat.sort() #sort in ascending order
            req_tfidf = flat[-2]
            
            if(req_tfidf==0):
                robo_response=robo_response+"I am sorry! I don't understand you"
                return robo_response
            else:
                robo_response = robo_response+sent_tokens[idx]
                return robo_response
        
        def bot_response(userip):
            c = response(userip)
            sent_tokens.remove(userip)
            return c
            


        #### Greeting ####
        
        GREETING_RESPONSES = ["hi", "hey", "hi there", "hello", "I am glad! You are talking to me", "wanna talk", "great!", ":)", "glad to meet you"]
        
        def greeting(user_response):
            for word in user_response.split(): 
                if word.lower() in greet: 
                    g = random.choice(GREETING_RESPONSES)
            return g


                    
        #### COWIN API ###
        
        print_flag = 'y'
        numdays = 5
        
        def api():
            DIST_ID = st.number_input('Enter the District ID(https://github.com/bhattbhavesh91/cowin-vaccination-slot-availability/blob/main/district_mapping.csv)')
            age = st.number_input('Enter your Age')
            base = datetime.datetime.today()
            date_list = [base + datetime.timedelta(days=x) for x in range(numdays)]
            date_str = [x.strftime("%d-%m-%Y") for x in date_list]
            URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id={}&date={}".format(DIST_ID, date_str[1])
            headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
            response = requests.get(URL, headers=headers)
            if response.ok:
                resp_json = response.json()
                if resp_json["centers"]:
                    if(print_flag=='y' or print_flag=='Y'):
                        for center in resp_json["centers"]:
                            name = center["name"]
                            print(name)
                            b = []
                            for session in center["sessions"]:
                                if session["min_age_limit"] <= age:
                                    if((session["available_capacity_dose1"])>0 or (session["available_capacity_dose2"])>0):
                                        y = True
                                        a = "Dose 1"+str(name)+ " " +str(session["available_capacity_dose1"])
                                        b.append(a)
                                        a = "Dose 2"+str(name)+ " " +str(session["available_capacity_dose2"])
                                        b.append(a)
                                        #print(a)
                                    else:
                                        new = 1
                else:
                    a = "No available slots in your city"
                    b.append(a)
            return b
            
            
        #### Calling functions ####
          
        greet = ["hello", "hi", "greetings", "sup", "what's up","hey", "hey there", "how r u?", "how are you?","how","are","you","kese ho"]
        vaccine_api = ["vaccine","number of dose","how many dose","my city","city","dose 1","dose one","dose1","dose 2","dose two","dose2","doses","number"]
        faqs = ["faqs","FAQs","FAQS","questions"]
        

        if ((any(w in user_input.lower().split(' ') for w in vaccine_api)) or (user_input.lower() in vaccine_api)):
            final = api()

        if ((any(w in user_input.lower().split(' ') for w in greet)) or (user_input.lower() in greet)):
            final = greeting(user_input)
            
        if ((any(w in user_input.lower().split(' ') for w in faqs)) or (user_input.lower() in faqs)):
            title = st.text_input("Enter your questions: ")
            final = bot_response(title)
            
    
        response_statement = Statement(text='Response: {}'.format(final))

        return response_statement
