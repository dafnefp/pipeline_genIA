import os
from groq import Groq
from dotenv import load_dotenv
from webscraping import buscar_dados

load_dotenv()

def ask_groq(question, df):

    df_json = df.to_json(orient="records", force_ascii=False, date_format='iso')

    client = Groq(
        api_key=os.environ.get("GROQ_API_KEY"),
    )

    content = {
        "question": question,
        "sales_data": df_json
    }
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": str(content),
            }
        ],
        model="llama3-8b-8192",
    )

    return chat_completion.choices[0].message.content