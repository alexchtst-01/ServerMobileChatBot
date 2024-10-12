from dotenv import load_dotenv, dotenv_values
from groq import Groq

load_dotenv()

GROQ_API = dotenv_values('.env')['GROQ_API']

groq_client = Groq(
    api_key=GROQ_API
)

chat_completion = groq_client.chat.completions.create(
    messages=[{
        'role': 'user',
        'content': 'what is the defenition of burn out?',
    }],
    model='gemma2-9b-it'
)

print(chat_completion.choices)
print(chat_completion.choices[0].message)
print(chat_completion.choices[0].message.content)

# coba lu bikin class instance biar lebih bisa fleksible nanti kalo dipake