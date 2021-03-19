import requests
s = requests.Session()
url = 'https://formsdss-v3.uk.barclays/dss/service/co.uk/mortgages/costcalculator/productservic'
s.headers.update({
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36",
    "referer": "https://www.barclays.co.uk/"
})
s.get("https://www.barclays.co.uk/mortgages/mortgage-calculator/")
print(s.cookies)

s.headers.update({"referer": "https://www.barclays.co.uk/mortgages/mortgage-calculator/",
    "origin": "https://www.barclays.co.uk",
    "action": "default",
    "currentstate": "default_current_state",
    'contentType': 'application/json'})

borrowAmount = 10000
estimatedPropertyValue = 20000
repaymentAmount = 10000
month = 80
ltv = round(repaymentAmount/estimatedPropertyValue*100)
data = {"header": {"flowId": 0},
        "body": {
            "borrowAmount": borrowAmount,
            "estimatedPropertyValue": estimatedPropertyValue,
            "interestOnlyAmount": 0,
            "ltv": ltv,
            "purchaseType": "Repayment",
            "repaymentAmount": repaymentAmount,
            "totalTerm": month,
            "wantTo": "FTBP"
                }
        }

res = s.post(url, json=data)
print(res.cookies)
print(res.json())
