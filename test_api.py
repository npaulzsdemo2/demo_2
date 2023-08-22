import requests

response = requests.get(
f'https://eng4237-api-internal.stage1.sightd.io/canonic/v1/saas?app_id={31}&mod_id={10}', headers={'X-Token': 'bwfyiuMziJ1nUnKilM3PBpewQiThYKqQ'})
print(response.content)