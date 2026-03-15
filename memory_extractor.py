import re

def extract_user_facts(message):
    if not message:
        return {}
    
    message = message.lower()
    facts = {}
    
    name_match = re.search(r"my name is (\w+)" , message)
    if name_match:
        facts["name"] = name_match.group(1).capitalize()
        
    goal_match = re.search(r"i want to become (.+)" , message)
    if goal_match:
        facts.setdefault("goals" , []).append(goal_match.group(1))
        
    language_match = re.search(r"i (?:love|like) (\w+)",message)
    if language_match:
        facts.setdefault("perferences" , {}).setdefault(
            "programming_languages",[]
        ).append(language_match.group(1))
        
    return facts





