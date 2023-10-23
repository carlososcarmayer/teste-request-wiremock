import requests

url = 'https://4w4k0.wiremockapi.cloud/v2/empresas'
payload = {
    "nome": "Teste",
    "nome_fantasia": "Teste",
    "bairro": "Vila Isabel",
    "cep": 80210000,
    "cnpj": "10964044000164",
    "complemento": "Loja 1",
    "discrimina_impostos": True,
    "email": "test@example.com",
    "inscricao_estadual": 1234,
    "inscricao_municipal": 46532,
    "logradouro": "Rua João da Silva",
    "numero": 153,
    "regime_tributario": 1,
    "telefone": "4130333333",
    "municipio": "Curitiba",
    "uf": "PR",
    "habilita_nfse": True,
    "arquivo_certificado_base64": "teste_vencido",
    "senha_certificado": "123456",
}
response = requests.post(url=url, json=payload)
print(response)
print(response.text)
