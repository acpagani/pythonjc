import re
import requests


def separar_sentencas(txt):
    pattern = r"""
            (                   
                .*?             
                (?:             
                    [!?]        
                    |           
                    \.(?!\d)    
                )               
            )                   
            (?=\s+|$)           
        """
    regex = re.compile(pattern, re.VERBOSE | re.DOTALL)
    sentences = [m.group(1).strip() for m in regex.finditer(txt)]
    return sentences


texto = """Demais, Arthur, foi ótimo fazer negócio com você! Agora vou passar seus dados para o pessoal de vendas. 
TRANSFERINDO PARA ESPECIALISTA."""

print(separar_sentencas(texto))


chats = [
    {
        "id": "123falkwak",
        "chat": [
            {"role": "system", "content": "AWDHAowh"},
            {"role": "system", "content": "AWDHAowh"},
            {"role": "system", "content": "AWDHAowh"}
        ]
    },
    {
        "id": "123falkwak",
        "chat": [
            {"role": "system", "content": "AWDHAowh"},
            {"role": "system", "content": "AWDHAowh"},
            {"role": "system", "content": "AWDHAowh"}
        ]
    }
]
