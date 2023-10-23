import base64
import os

# Nome do arquivo PFX (certificado digital)
pfx_file = '33030506000100_000001011131322.pfx'

# Lê o conteúdo do arquivo PFX
with open(pfx_file, 'rb') as file:
    pfx_data = file.read()

# Codifica o conteúdo em base64
pfx_base64 = base64.b64encode(pfx_data).decode('utf-8')
CERTIFICADO = pfx_base64
