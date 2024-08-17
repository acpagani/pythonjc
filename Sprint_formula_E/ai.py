import google.generativeai as genai

genai.configure(api_key="AIzaSyAlcB1egvD3BYmTzmpCjBbVtOybZNl1bDk")

generation_config = {
  "temperature": 1,
  "top_p": 1,
  "top_k": 0,
  "max_output_tokens": 2048,
  "response_mime_type": "text/plain",
}
safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_LOW_AND_ABOVE",
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_LOW_AND_ABOVE",
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_LOW_AND_ABOVE",
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_LOW_AND_ABOVE",
  },
]

model = genai.GenerativeModel(
  model_name="gemini-1.0-pro",
  safety_settings=safety_settings,
  generation_config=generation_config,
)

chat_session = model.start_chat(
  history=[
    {
      "role": "user",
      "parts": [
        """Você é Volt, uma assistente amigável que trabalha para a plataforma E-WAY. E-WAY é um website que busca a 
        maior visibilidade da Fórmula E (uma modalidade de automobilismo organizada pela FIA com carros monopostos 
        exclusivamente elétricos), e para isso, a plataforma busca reunir notícias, curiosidades, histórias, 
        estatísticas e calendários, todos relacionados à modalidade, a fim de despertar a curiosidade e engajamento pelo 
        esporte no usuário. O seu papel é prestar suporte ao usuário quanto às informações do esporte. Quando 
        solicitado, responda a dúvidas, mostre calendários futuros de acordo com a data solicitada, conte curiosidades, 
        sempre relacionados à Fórmula E. Utilize uma linguagem simples. As solicitações sempre tenderão a ter algum tipo 
        de relação à Fórmula E. Caso o usuário solicite informações desconexas à Fórmula E, gentilmente alerte-o que 
        esse tipo de informação não se enquadra no escopo da plataforma e não responda o que foi solicitado. 
        Para fins de utilização de datas, peça ao usuário a data atual, que será utilizada como parâmetro para a 
        resposta.""",
      ],
    },
  ]
)

response = chat_session.send_message("Quem é você?")

print(response.text)

response = chat_session.send_message(input("Você: "))

print(response.text)
