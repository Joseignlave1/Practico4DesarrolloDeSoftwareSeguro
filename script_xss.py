import requests

url = 'http://localhost:8080/AltoroJ/search.jsp'

# Payload con ejecucion de un alert para explotar xss
payload = {'query': '<script>alert("XSS")</script>'}

# Hacemos un get con el payload
response = requests.get(url, params=payload)

# Verificamos si el payload está presente en el HTML de la response
if '<script>alert("XSS")</script>' in response.text:
    # Vulnerabilidad presente
    print("XSS vulnerability found!")
    exit(1)
else:
    # Vulnerabilidad no presente
    print("XSS vulnerability not found!")
    exit(0)
