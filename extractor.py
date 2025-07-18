# extractor.py

import re

colors = [
    "red", "blue", "green", "black", "white", "yellow", "pink", "purple", "floral",
    "striped", "orange", "grey", "navy", "navy blue"
]

materials = [
    "cotton", "denim", "silk", "polyester", "wool", "leather", "lace", "linen", "chiffon"
]

styles = [
    "a-line", "v-neck", "crewneck", "skinny", "slim", "slim fit", "fit", "oversized",
    "halter", "off-shoulder", "wrap"
]

lengths = [
    "mini", "midi", "maxi", "knee-length", "ankle-length", "cropped", "long", "short"
]

sleeves = [
    "short sleeves", "long sleeves", "sleeveless", "cap sleeves", "half sleeves"
]

def extract_attribute(description, keywords):
    for keyword in keywords:
        if re.search(r'\b' + re.escape(keyword) + r'\b', description, re.IGNORECASE):
            return keyword.title()
    return "Not Found"

def extract_attributes(description):
    description = description.lower()

    return {
        "Color": extract_attribute(description, colors),
        "Material": extract_attribute(description, materials),
        "Style": extract_attribute(description, styles),
        "Length": extract_attribute(description, lengths),
        "Sleeves": extract_attribute(description, sleeves)
    }
