import requests

# Chiamata in chiaro
simple_request = requests.get('http://httpbin.org/ip')
response = simple_request.json()
print(f"Questo è il mio indirizzo in chiaro:\n{response['origin']}\n")

# Chiamata usando Tor
session = requests.session()
session.proxies = {'http':  'socks5://127.0.0.1:9150','https': 'socks5://127.0.0.1:9150'}
anonymous_request = session.get('http://httpbin.org/ip')
response = anonymous_request.json()
print(f"Questo è il mio indirizzo mascherato:\n{response['origin']}")
    