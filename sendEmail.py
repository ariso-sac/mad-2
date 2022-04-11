import requests
from requests.structures import CaseInsensitiveDict

url = "https://graph.microsoft.com/v1.0/me/sendMail"

headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"
headers["Authorization"] = "Bearer EwCgA8l6BAAUwihrrCrmQ4wuIJX5mbjHYZO8er7D+erJG543pv0Sh409c63i5pwh5JLuxVzwC9BVifz3+GYSdSBbHtXX7L0sMK64CjiMs+B2cSkZEn1RT4sU63RvkaxehkMTefoVi4z4rdmBWJNXekCeMmGfGglz2xluR9vidzDfNHDnqS9sDm+AT9ELg0RRR6XLVwb/sovhXI4rRpFeBvruhFA2rvFqvkIJIE65SekS06ic158nEeEVUYOXUJcyUwxojH2Q5LBoRoBQZQAe9CWyOB0xREBMFSuti8cTDItvkETh5fzcTaYdf2O8Xd7dwjv7pr6dh5CvY2npjr0eUKhvj5PFRTn8DZgAACEvZ5brl5DWzcAKChNPcylT/2n5JBcx66jQdBcjsKPR4H9FOAZoDI605j7USbyX4NYxghUiKbjoJiTrMgj786NsOqSjnTdhU1WsOXO1ZgpR7KghadXjsktlnu2wbNwf801ttkhy3YbbzSBi37rLzSCGZL78xYnaQcJZObjnEJTym/ilHy6pd811/okVs9YTXSNB1p08JD6ZJ3sFdrwUVXiouWGfURO9tRI0YpDNywfK9YhuqGF0AlluN7EPu7/sUTzhEw8joZ47l1exs41Wq4WmjQYM/riw7Kj+FGFk4uEW/FYqpS30sP2mVnJrjbgcWUNtTPFK3t9YPuaEs56aknN5HEs/2+cMXXm8c9uDomAlHk5U644rwJj+YwZqI5T3whsvLY7kSuBmYs65Te7/U/RVmNbmde4l3yF3QW6CBRj98/ttVNz9PDzZTz7nd/7CMwjVk/V0wXh6Vty3hEwH+PyMekQmZkn1EePaRhVDQriFcK2kGg5eILHcm5FHatgOjZHzhJM+q7773zQjnLonY6qWt+dKyJCzWYATJRYZnWOAtpEoeOh+9vG4MyfGhjbEMQL+Rce1ah+1ZTNYJufmI1wIELzUeKgXaz8RtNVucp/SP9dTnvDk/lkW81DD89qWbXvl30LvSvpVpaDYnifTH3rpoY7Ghnk+Q2upte1P/zm8g5rs/3jWXDhJg3AGj3GnvLYpimHGetRUHjG97ZMCvuZR5c+QRHlblcw5uSLVtYB3bQDj0/aglVQ9dDDczILbd8bbBOdyj5xgJ7ZdLZO5cSZBAY3Ov9zbb5b24vav5qiL1rsQBWw/SePpY0e53uAh+GkBL5z5MquYZbamYAg=="
headers["Content-Type"] = "application/json"

data = """
{
    "message": {
        "subject": "Meet for Dinner?",
        "body": {
            "contentType": "Text",
            "content": "The old cafeteria is open."
        },
        "toRecipients": [
            {
                "emailAddress": {
                    "address": "21f1006475@student.onlinedegree.iitm.ac.in"
                }
            }
        ]
    }
}
"""


resp = requests.post(url, headers=headers, data=data)

print(resp.status_code)