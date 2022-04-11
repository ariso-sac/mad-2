import requests

base_url = "http://127.0.0.1"
final_url = base_url + ":8080/api/deck"


payload = {"name": "HelloWorld"}

response = requests.post(
    final_url,
    headers={
        "Authentication-Token": "WyJkYzJjMWQwZGQwMDc0ZWJhYjE5ODRjYTM5ODYzNmVhMCJd.YhkCag.vehrlD2rWxmeSIBrEkdXmcDsQr0"
    },
    json=payload,
)

print(response.text)  # TEXT/HTML
print(response.status_code, response.reason)  # HTTP
