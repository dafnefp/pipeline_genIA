import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

def ask_groq(question, df):

    df_json = df.to_json(orient="records", force_ascii=False, date_format='iso')

    client = Groq(
        api_key=os.environ.get("GROQ_API_KEY"),
    )

    prompt_inicial = "Os dados apresentam informações sobre uma ação da bolsa de valores. \
        Cada registro corresponde a um dia e os respectivos valores de abertura, valores de fechamento, \
        valor minimo e maximo atingido, variação em percentual do fechamento de um dia em comparação com o \
        anterior e o volume de ações negociadas no dia. Com essas informações me responda: "
    prompt_fim = "Apenas me traga a informação pedida, por exemplo se eu perguntar qual foi o maior valor? \
        você responderá: O maior valor foi XX, no dia xx/xx/xxxx, ou então se perguntar qual foi o preço de \
        abertura no dia xx/xx/xx, você responderá: o preço de abertura no dia xx/xx/xx foi de XX"
    
    question_aux = f'{prompt_inicial} {question} {prompt_fim}'

    content = {
        "question": question_aux,
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