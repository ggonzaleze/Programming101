def encode_decodeROT13(message):
    key = {"a":"n","b":"o","c":"p","d":"q","e":"r","f":"s","g":"t","h":"u","i":"v",
    "j":"w","k":"x","l":"y","m":"z","n":"a","o":"b","p":"c","q":"d","r":"e","s":"f",
    "t":"g","u":"h","v":"i","w":"j","x":"k","y":"l","z":"m"}
    message = message.lower()
    new_message = ""
    for letter in message:
        new_message = new_message + key.get(letter,letter)
    return new_message

message = "Pnrfne pvcure? V zhpu cersre Pnrfne fnynq!"
print(encode_decodeROT13(message))
