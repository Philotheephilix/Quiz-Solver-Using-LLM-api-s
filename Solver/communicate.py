import requests


from .connect import chat
from .config import URL


def sent_prompt(json):
    option_string=""
    j=0
    print(json)
    print(json['options'])
    for i in json['options']:
        option_string=option_string+str(j)+". "+i+", "
    prompt="Solve this DBMS oracle question "+json['question']+'the options are '+option_string+"Give responce with the correct option content as \"Correct Answer:<Correct option here>\""
    response=chat(prompt)
    return json['options'],response

def sendBack(Answer):
    try:
        print(Answer)
        response = requests.post(URL,data=Answer)
        if response.status_code ==200:
            print("Sent Successfully")
        else:
            print(response.status_code)
    except Exception as e:
        print(e)