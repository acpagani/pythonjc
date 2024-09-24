dados = [
    {
        "dia": 12,
        "mes": 2,
        "ano": 2019,
        "temp": 30.5
    },
    {
        "dia": 18,
        "mes": 3,
        "ano": 2019,
        "temp": 29.1
    },
    {
        "dia": 22,
        "mes": 4,
        "ano": 2019,
        "temp": 28.5
    },
    {
        "dia": 17,
        "mes": 5,
        "ano": 2019,
        "temp": 26.4
    }
]

for data in dados:
    print(f"{data['dia']}/{data['mes']}/{data['ano']}: Temperatura: {data['temp']}ºC")
