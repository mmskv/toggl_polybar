import time, requests, json

api_token = "" # Paste your API token here
current = json.loads(
    requests.get("https://www.toggl.com/api/v8/time_entries/current", auth=(api_token, "api_token")).content)
if current['data'] is not None and ("pid" in current["data"] or "description" in current["data"]):
    seconds = time.time() - abs(current['data']['duration'])
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    if "pid" in current["data"]:
        link = 'https://www.toggl.com/api/v8/projects/' + str(current['data']['pid'])
        name = json.loads(requests.get(link, auth=(api_token, "api_token")).content)["data"]["name"]
    else:
        name = current['data']['description']
    m = int(m)
    h = int(h)
    if m < 10: m = '0' + str(m)
    m = str(m)
    h = str(h)
    out = name + " " + '(' + h + ':' + m + ')'
    print(out)
else:
    print("No project is running")
