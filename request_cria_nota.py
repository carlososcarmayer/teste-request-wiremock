import requests
from constants import CERTIFICADO

url = 'https://celero-wiremock-qa-tzhjf7clga-ue.a.run.app/v2/nfse/'
headers = {
    "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6ImM2MjYzZDA5NzQ1YjUwMzJlNTdmYTZlMWQwNDFiNzdhNTQwNjZkYmQiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL2FjY291bnRzLmdvb2dsZS5jb20iLCJhenAiOiIzMjU1NTk0MDU1OS5hcHBzLmdvb2dsZXVzZXJjb250ZW50LmNvbSIsImF1ZCI6IjMyNTU1OTQwNTU5LmFwcHMuZ29vZ2xldXNlcmNvbnRlbnQuY29tIiwic3ViIjoiMTA5NzQ1ODAwOTY1MDE2MDcwOTQ0IiwiaGQiOiJjZWxlcm8uY29tLmJyIiwiZW1haWwiOiJjYXJsb3MubWF5ZXJAY2VsZXJvLmNvbS5iciIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJhdF9oYXNoIjoiVUJOYk1pZ1ItUjE3ZnluNEVDOWxEdyIsImlhdCI6MTY5Njk0ODUwMSwiZXhwIjoxNjk2OTUyMTAxfQ.EHTu1eG6y5bI1qmErHwHakRc-uYAOKyz7QPYlnbI1lX__yRp0v-GiRc6wXbi6L_gsOwy3CfgMhwgaFjlb1pJfZortTF0oTqc3MzniumfyUVYVg149OTfAiZyAoxJN8iEWUcHwgvXzgA1ZC_iE4uTgnex5UWIhPjeCFJKMra9Ien4NWAu5B5pgxDESjxo_8kfiuKE3Hq41WNo-yfYHsquJrRBI20KsBsyHoc-FfcSXjyn3-P9b6xnCuKA5-zM12OgIiDWXiBj_nKFCm8-KDME8HyduNE_uTfY5Zn-Ap_w8RAAcg3sp6Pb50P6bhgTRqWVomTnCH1S91JktkWknm_3bg",
    "Content-Type": "application/json"
}
params = {
    'token': 'tN2w5RzXvBp9A8QcYsD4F6HjM0Kg7L1',
    'ref': 'afdfkshdshhsdhg'
}
payload = {
   "data_emissao":"2023-04-23",
   "prestador":{
      "cnpj":"000000000",
      "inscricao_municipal":"${json-unit.any-string}",
      "codigo_municipio":"${json-unit.any-string}"
   },
   "tomador":{
      "cnpj":"testefdsfds",
      "razao_social":"${json-unit.any-string}",
      "email":"${json-unit.any-string}",
      "endereco":{
         "logradouro":"${json-unit.any-string}",
         "numero":"${json-unit.any-string}",
         "complemento":"${json-unit.any-string}",
         "bairro":"${json-unit.any-string}",
         "codigo_municipio":"${json-unit.any-string}",
         "uf":"${json-unit.any-string}",
         "cep":"${json-unit.any-string}"
      }
   },
   "servico":{
      "aliquota":1,
      "discriminacao":"${json-unit.any-string}",
      "iss_retido":"${json-unit.any-string}",
      "item_lista_servico":"${json-unit.any-string}",
      "codigo_tributario_municipio": "${json-unit.any-string}",
      "valor_servicos":11
   }
}

response = requests.post(url=url, headers=headers, params=params, json=payload)
print(response)
print(response.text)
