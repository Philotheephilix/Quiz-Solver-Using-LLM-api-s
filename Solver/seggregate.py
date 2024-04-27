def seggregator(options,answer):
    presence = {}
    for value in options:
        presence[value] = value in answer

    for value, present in presence.items():
        if present :
            return value

def trim_response_claude(main_string):
    return main_string