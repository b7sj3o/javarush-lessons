# import http.client
#
# # Створюємо з'єднання з HTTPS-сервером
# conn = http.client.HTTPSConnection("jsonplaceholder.typicode.com")
#
# # Відправляємо GET-запит
# conn.request("GET", "/posts/1")
# # Отримуємо відповідь
# response = conn.getresponse()
# print(response.status, response.reason)
# # Читаємо дані відповіді і декодуємо їх
# data = response.read().decode('utf-8')
# print(data)
# # Закриваємо з'єднання
# conn.close()
#


import http.client

# Налаштування проксі-сервера
proxy_host = '10.10.1.10'
proxy_port = 3128
# Цільовий URL
dest_url = 'jsonplaceholder.typicode.com'
dest_path = '/ip'
# Створюємо з'єднання з проксі-сервером
conn = http.client.HTTPConnection(proxy_host, proxy_port)
# Встановлюємо тунель до цільового сервера
conn.set_tunnel(dest_url)
# Відправляємо GET-запит
conn.request('GET', dest_path)
# Отримуємо відповідь
response = conn.getresponse()
print(response.status, response.reason)
print(response.read().decode('utf-8'))
# Закриваємо з'єднання
conn.close()