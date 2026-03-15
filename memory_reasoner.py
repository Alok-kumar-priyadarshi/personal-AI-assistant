from memory_manager import get_memory


def should_store_fact(facts):

    memory = get_memory()

    decisions = {}

    for key, value in facts.items():

        if key not in memory:
            decisions[key] = "store"

        elif memory[key] == value:
            decisions[key] = "ignore"

        else:
            decisions[key] = "update"

    return decisions