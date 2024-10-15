from groq import Groq

class ChatBot:
    def __init__(self, api_key, modelName='gemma2-9b-it', autosavehistory=False):
        self.__qroqClient__ = Groq(api_key=api_key)
        self.__model__ = modelName
        self.__history__ = []
    
    def generateText(self, query):
        answer = self.__qroqClient__.chat.completions.create(
            messages=[{
                'role': 'user',
                'content': query
            }],
            model=self.__model__
        )
        return answer.choices
    
    def getAnswer(self, query):
        answers = self.generateText(query)
        return answers[0].message.content
