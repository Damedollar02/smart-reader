import sys
from openai import OpenAI
from PyPDF2 import PdfReader

API_KEY = open("API_KEY", "r").read().strip()

client = OpenAI(api_key=API_KEY)

#Case where we're extracting a PDF
filename = sys.argv[1]
if filename.endswith(".pdf"):
    reader = PdfReader(filename)
    page = reader.pages[0]
    raw = page.extract_text()

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

