import requests

url = "https://seeking-alpha.p.rapidapi.com/analysis/v2/list"

querystring = {"id":"tsla","until":"0","since":"0","size":"20","number":"1"}

headers = {
	"X-RapidAPI-Key": "422ecd716emshed42af11c5f61fcp1686c5jsn2e622a110ff0",
	"X-RapidAPI-Host": "seeking-alpha.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)