import gradio as gr
import os
import openai
from prompt import GetBaseArticlePrompt, GetBaseArticlePromptByPDF, GetQuestionPrompt, GetSystemPrompt
from dotenv import load_dotenv
load_dotenv()
API_KEY = os.getenv("OPENAI_API_KEY")
ARTICLE_PATH = os.getenv("ARTICLE_PATH")
ARTICLE_TXT_PATH = os.getenv("ARTICLE_TXT_PATH")
openai.api_key = API_KEY

def generate_answer(question):

    systemPrompt = GetSystemPrompt()
    baseArticlePrompt = GetBaseArticlePrompt(ARTICLE_TXT_PATH)
    # baseArticlePrompt = GetBaseArticlePromptByPDF(ARTICLE_PATH)
    questionPrompt = GetQuestionPrompt(question)
    userPrompt = f"{baseArticlePrompt}\n{questionPrompt}"

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-16k",
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

iface = gr.Interface(fn=greet, inputs="text", outputs="text")
iface.launch()
