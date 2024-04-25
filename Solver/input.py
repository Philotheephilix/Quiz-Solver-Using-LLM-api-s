from .connect import chat
def sent_prompt(json):
    option_string=""
    j=0
    print(json)
    print(json['options'])
    for i in json['options']:
        option_string=option_string+str(j)+". "+i+", "
    prompt="Solve this DBMS oracle question "+json['question']+'the options are '+option_string+"Give result with only the correct option number dont give the value just one charecter"
    response=chat(prompt)
    print(response)