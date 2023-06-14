import PyPDF2
import os
from dotenv import load_dotenv
load_dotenv()
ARTICLE_TXT_PATH = os.getenv("ARTICLE_TXT_PATH")

SYSTEM = "You are an expert in reading research papers. Now I will paste the full text of a paper and ask questions. Please answer my questions based on the content of the paper. There is no need to provide additional summaries unless necessary. Please provide concise and clear answers to my questions."

def GetSystemPrompt():
    return SYSTEM

def GetBaseArticlePrompt(path):
    def combine_text(file_path):
        with open(file_path, 'r', encoding="utf-8") as file:
            lines = file.readlines()
            combined_text = ' '.join(lines)
        return combined_text
    # Call the function to combine the text
    combined_string = combine_text(path)
    return f"\"Article\":{combined_string}"

def write_string_to_txt(string, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(string)

def GetBaseArticlePromptByPDF(path):
    def extract_text_from_pdf(file_path):
        with open(file_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            num_pages = len(reader.pages) -2

            text = ""
            for page_number in range(num_pages):
                page = reader.pages[page_number]
                text += page.extract_text()

            return text
    combined_string = extract_text_from_pdf(path)
    write_string_to_txt(combined_string, ARTICLE_TXT_PATH)
    return f"\"Article\":{combined_string}"

def GetQuestionPrompt(question):
    return f"\"Question\":{question}"
