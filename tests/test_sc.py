import requests

base_url = "http://127.0.0.1"
final_url = base_url + ":8080/api/user/1/deck/2"
# final_url=base_url+":8080/api/user/<u_id>/deck/<d_id>"
# final_url="/{0}/friendly/{1}/url".format(base_url,any_value_here)

# payload = {'number': 2, 'value': 1}
"""
payload = {
  "first_name": "Narendra",,k
  "last_name": "Mishra",
  "roll_number": "MA19M010"
}
"""

payload = {"easy": 10, "moderate": 10, "hard": 10}

response = requests.post(
    final_url,
    headers={
        "Authentication-Token": "WyJkYzJjMWQwZGQwMDc0ZWJhYjE5ODRjYTM5ODYzNmVhMCJd.YhkCag.vehrlD2rWxmeSIBrEkdXmcDsQr0"
    },
    data=payload,
)

print(response.text)  # TEXT/HTML
print(response.status_code, response.reason)  # HTTP
