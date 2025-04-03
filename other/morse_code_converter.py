from winsound import Beep
from time import sleep
chars = "abcdefghijklmnopqrstuvwxyz0123456789"
code = ["▄ ▄▄▄","▄▄▄ ▄ ▄ ▄","▄▄▄ ▄ ▄▄▄ ▄","▄▄▄ ▄ ▄","▄","▄ ▄ ▄▄▄ ▄","▄▄▄ ▄▄▄ ▄","▄ ▄ ▄ ▄","▄ ▄","▄ ▄▄▄ ▄▄▄ ▄▄▄","▄▄▄ ▄ ▄▄▄","▄ ▄▄▄ ▄ ▄","▄▄▄ ▄▄▄","▄▄▄ ▄","▄▄▄ ▄▄▄ ▄▄▄","▄ ▄▄▄ ▄▄▄ ▄","▄▄▄ ▄▄▄ ▄ ▄▄▄","▄ ▄▄▄ ▄","▄ ▄ ▄","▄▄▄","▄ ▄ ▄▄▄","▄ ▄ ▄ ▄▄▄","▄ ▄▄▄ ▄▄▄","▄▄▄ ▄ ▄ ▄▄▄","▄▄▄ ▄ ▄▄▄ ▄▄▄","▄▄▄ ▄▄▄ ▄ ▄","▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄","▄ ▄ ▄▄▄ ▄▄▄ ▄▄▄","▄ ▄ ▄ ▄▄▄ ▄▄▄","▄ ▄ ▄ ▄ ▄▄▄","▄ ▄ ▄ ▄ ▄","▄▄▄ ▄ ▄ ▄ ▄","▄▄▄ ▄▄▄ ▄ ▄ ▄","▄▄▄ ▄▄▄ ▄▄▄ ▄ ▄","▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄","▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄"]

def convert_text_to_morse(text:str) -> str:
    ret = ""
    for char in text:
        if char.lower() in chars:
            dit = code[chars.index(char.lower())]
            for b in dit.split(" "):
                 Beep(1000,450) if len(b) == 3 else Beep(500,150)
            sleep(.3)
            ret += dit + '  '
    return ret
def convert_morse_to_text(text:str) -> str:
    return "".join([chars[code.index(b.lower())] for b in text.split("  ") if b in code])

print(convert_text_to_morse("This is a default text"))
print(convert_morse_to_text("▄▄▄  ▄ ▄ ▄ ▄  ▄ ▄  ▄ ▄ ▄  ▄ ▄  ▄ ▄ ▄  ▄ ▄▄▄  ▄▄▄ ▄ ▄  ▄  ▄ ▄ ▄▄▄ ▄  ▄ ▄▄▄  ▄ ▄ ▄▄▄  ▄ ▄▄▄ ▄ ▄  ▄▄▄  ▄▄▄  ▄  ▄▄▄ ▄ ▄ ▄▄▄  ▄▄▄"))