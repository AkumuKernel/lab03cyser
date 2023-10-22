import re

input_file = 'rockyou.txt'
output_file = 'rockyou_mod.dic'

try:
    with open(input_file, 'r', encoding="latin-1") as f:
        passwords = f.read().splitlines()
        modified_passwords = []

        for password in passwords:
            if re.match('^[a-zA-Z].*', password):
                modified_passwords.append(password.capitalize() + '0')

        with open(output_file, 'w') as out:
            out.write('\n'.join(modified_passwords))

        print(f"El diccionario modificado se ha guardado en {output_file}")
except FileNotFoundError:
    print(f"No se pudo encontrar el archivo {input_file}")
