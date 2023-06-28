import gradio as gr
import os
import openai
from prompt import GetBaseArticlePrompt, GetQuestionPrompt, GetSystemPrompt
from dotenv import load_dotenv
load_dotenv()
API_KEY = os.getenv("OPENAI_API")
ARTICLE_TXT_PATH = os.getenv("ARTICLE_TXT_PATH")
openai.api_key = API_KEY

def generate_answer(question):
    systemPrompt = GetSystemPrompt()
    baseArticlePrompt = GetBaseArticlePrompt(ARTICLE_TXT_PATH)
    questionPrompt = GetQuestionPrompt(question)
    userPrompt = f"{baseArticlePrompt}\n{questionPrompt}"

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-16k",
        # model="gpt-4",
        messages=[
            {"role": "system", "content": systemPrompt},
            {"role": "user", "content": userPrompt}
        ]
    )
    answer = completion.choices[0].message.content
    return answer

# Create the interface
def greet(question):
    answer = generate_answer(question)
    return answer

# Create the interface
def greet2(question):
    answer = generate_answer(question)
    return answer

iface1 = gr.Interface(fn=greet, inputs="text", outputs="text")

iface1.launch()