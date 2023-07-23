import requests

token = 'secret_LjMlQLYBMclgD6Tg13zTkJgihOGMCKvpFngSgZtivnn'
r = requests.request(
    "GET",
    "https://api.notion.com/v1/pages/0e2088a6a95b4daa8344b26f9cde0c99",
    headers={"Authorization": "Bearer " + token, "Notion-Version": "2021-05-13"},
)
print(r.text)