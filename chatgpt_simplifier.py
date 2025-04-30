import sys
import os
from openai import OpenAI
from PyPDF2 import PdfReader
from gtts import gTTS

API_KEY = open("API_KEY", "r").read().strip()

client = OpenAI(api_key=API_KEY)

#Case where we're extracting a PDF
#currently only reads 1 page, create a loop to extract all text from pdf
filename = sys.argv[1]
if filename.endswith(".pdf"):
    reader = PdfReader(filename)
    page = reader.pages[0]
    content = page.extract_text()

#Case of txt file
else:
    with open(filename, 'r') as file:
        content = file.read()

response = client.chat.completions.create (
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "Simplify this for a general audience"},
        {"role": "user", "content": content}
    ]
)

simplified_message = response.choices[0].message.content


with open("simplified_out.txt", 'w') as f:
    f.write(simplified_message)

## text-to-speech
language = "en"
speech_input = gTTS(text=simplified_message, lang=language, slow=False)
speech_input.save("simplified.mp3")


#mac specific command to play mp3
os.system("afplay simplified.mp3")

#Window specific command below 
#os.system("afplay simplified.mp3")
