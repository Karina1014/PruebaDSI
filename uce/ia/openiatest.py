import openai
from pydantic import BaseModel


class Document(BaseModel):
    prompt: str = ''


def inference(prompt: str) -> list:
    openai.organization = 'org-zPsXVbDM9Yfau52v6mAuYsdQ'
    openai.api_key = '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'
    print('[PROCESANDO]'.center(40, '-'))

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": """Eres un profesor de programación para niños, genera una explicación para 
            el tema que se proporciona. E.G: Programación - Es como armar un rompecabezas donde cada pieza forma el 
            sistema completo."""},
            {"role": "user", "content": prompt}
        ]
    )

    content = completion.choices[0].message.content
    total_tokens = completion.usage.total_tokens

    print('[SE TERMINO EL PROCESO Kari]'.center(40, '-'))
    return [content, total_tokens]
