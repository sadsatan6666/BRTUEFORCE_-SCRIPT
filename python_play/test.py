import requests

url = "https://portfolio.wealthmaker.in/wmapi_live/WealthMakerAPIKit.svc/PunchLead"
headers = {
    "Accept": "application/json",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-US,en;q=0.5",
    "Connection": "keep-alive",
    "Content-Length": "798",
    "Content-Type": "application/json",
    "Host": "portfolio.wealthmaker.in",
    "OriginL": "https",
    "Referer": "https",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "cross-site",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv",
    "token": "20F614C4C6FB2E83E063AB000084B64C"
}

# Read names and mobile numbers from files
with open('names.txt', 'r') as names_file, open('mobile_numbers.txt', 'r') as mobiles_file:
    names = names_file.readlines()
    mobile_numbers = mobiles_file.readlines()

# Ensure both files have the same number of lines
if len(names) != len(mobile_numbers):
    print("The number of names and mobile numbers do not match.")
else:
    for name, mobile in zip(names, mobile_numbers):
        name = name.strip()
        mobile = mobile.strip()
        
        data = {
            "BranchCD": "10071011",
            "FirstName": name,
            "MobileNo": mobile,
            "Alt_mobile": "",
            "Phone": "",
            "LeadSource": "Door to Door MI Test",
            "Married": "Married",
            "First_child": "",
            "SECOND_child": "",
            "Third_child": "",
            "Occupation": "Business",
            "OCCRemark": "sm",
            "CollDate": "31/08/2024",
            "DataCollName": "163973",
            "FinancialPlan": "NO",
            "PersonalLoan": "NO",
            "TaxSaving": "",
            "HealthInsurance": "NO",
            "LifeInsurance": "NO",
            "UserName": "163973",
            "DOB": "09/09/1990",
            "BaseMobile": "8128039839",
            "SubLeadSource": "DD",
            "Email": "",
            "NoOfChildren": "",
            "Income": "0",
            "City": "-",
            "Vehicle": "Four wheeler",
            "RequireInformation": "NA",
            "BankWith": "Bank with public sector",
            "MonthlyIncome": "30000 - 39999",
            "ContactAT": "Morning",
            "Distance": "0",
            "FamilyAdmitted": "NO",
            "EnoughHealthInsurance": "NO",
            "ChildEducation": "NO",
            "LeadAuditFlag": "",
            "ClientAddress": ""
        }

        response = requests.post(url, headers=headers, json=data)
        
        print(f"Status Code for {name}: {response.status_code}")
        print(f"Response for {name}: {response.json()}")
