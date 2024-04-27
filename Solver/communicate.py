import requests


from .connect import chat


def generate_prompt(json):
    option_string=""
    j=0
    print(json)
    print(json['options'])
    for i in json['options']:
        option_string=option_string+str(j)+". "+i+", "
    prompt="Solve this DBMS oracle question "+json['question']+'the options are '+option_string+"Give responce with the correct option content as \"Correct Answer:<Correct option here>\""
    return json['options'],prompt
