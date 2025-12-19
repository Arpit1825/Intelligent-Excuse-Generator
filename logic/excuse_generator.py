# logic/excuse_generator.py (REPLACE generate_excuse with this version)
import json
import random

with open("data/excuse_templates.json", "r") as f:
    TEMPLATES = json.load(f)

def generate_excuse(scenario, tone, reason, language="en"):
    try:
        options = TEMPLATES[language][scenario][tone]
        template = random.choice(options)
        return template.format(reason=reason)
    except KeyError:
        return "Invalid selection."
