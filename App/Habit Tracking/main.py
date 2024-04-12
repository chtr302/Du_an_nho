import requests

USERNAME = "chtrr"
TOKEN = "thisistranconghaunhehihi"

pixel_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token" : USERNAME,
    "username" : TOKEN,
    "agreeTermsOfService" : "yes",
    "notMinor" : "yes",
}

# response = requests.post(url=pixel_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixel_endpoint}/{USERNAME}/graphs"

response = requests.post
