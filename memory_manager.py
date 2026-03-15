import json
import os

MEMORY_FILE = "memory.json"

def load_memory():
    if not os.path.exists(MEMORY_FILE):
        return {}
    with open(MEMORY_FILE , "r") as file:
        return json.load(file)
    
def save_memory(memory):
    with open(MEMORY_FILE , "w") as f:
        json.dump(memory , f , indent = 2)
        
def update_memory(facts):
    memory = load_memory()
    for key ,value in facts.items():
        if isinstance(value , list):
            if key not in memory:
                memory[key] = []
                
            for item in value:
                if item not in memory[key]:
                    memory[key].append(item)
        else:
            memory[key] = value
            
    save_memory(memory)
    
def get_memory():
    return load_memory()           
                    



