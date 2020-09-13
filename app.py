

def emoji_picker(message):
    words = message.split(" ")
    emojis = {
        ":)" : "😊",
        ":(" : "😒",
        ":D":"😁",
        ":/":"🤔",
        ";)": "😉" ,
        ":|":"😐️"

    }
    output = ""
    for word in words:
        output += emojis.get(word,word) + " "
    return output


info = input ("-->")

print(emoji_picker(info))