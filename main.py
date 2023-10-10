import openai
import langchain
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from time import sleep

RATE = 3 #per minute for free account

with open('.git/key.txt', 'r') as f:
    API = f.read()

gpt = OpenAI(temperature=0.3, openai_api_key=API)
print(gpt.predict('What is the capital of india?'))

sleep(60/RATE)