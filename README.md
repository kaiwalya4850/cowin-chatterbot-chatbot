## COWIN Bot using Chatterbot
Recently while working on Chatterbot framework, I realized there are very few tutorials/repositories for making a bot that performs tasks according to your necessities. So, this repository is created to give a code structure that can be used to create your own logical adapters and integrate it with the framework.
### Features of Bot
- Greetings
- Provide district wise vaccination count across India (provides insights on how to integrate custom APIs with your bot)
- Answer FAQs on Vaccine (provides insights on how to use any existing model/algorithm in order to process the data)

### Execution and code
First things first, Chatterbot doesn.t work with Python >3.8.0, so make sure your environment matches the criteria. 

Examples of Custom Logical Adapters:

```bash
adapter_first.py
adapter_second.py
```
There are 3 functions this file, which are features of the bot:
```bash
adapter_cowin1.py
```
There are conditions, based on user's input, at the end of the class, which help the Bot select appropriate function. (Idea: You may try applying concept of N-grams to the list for better results and selection.)

Main file, with everything integrated:

```bash
bot_ui.py
```

To run everything, issue this command:

```bash
streamlit run bot_ui.py
```

That would be it, hope this repository saves A LOT of time of anyone who is working with the framework, especially with the Logical Adapter aspect!
