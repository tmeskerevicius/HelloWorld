def lbs_to_kg(weight):
    return weight * 0.45


def kg_to_lbs(weight):
    return weight / 0.45


def emoji_picker(message):
    words = message.split(" ")
    emojis = {
        ":)": "😊",
        ":(": "😒",
        ":D": "😁",
        ":/": "🤔",
        ";)": "😉",
        ":|": "😐️"

    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return output
