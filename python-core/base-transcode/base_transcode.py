def convert_base_digits(number: str, source_base: int, target_base: int) -> str:
    # 1. Vérifier que les bases sont valides (2 à 36)
    if source_base < 2 or source_base > 36 or target_base < 2 or target_base > 36:
        return "invalid"

    # 2. Vérifier que la chaîne n'est pas vide et ne commence pas par '-'
    if not number or number[0] == '-':
        return "invalid"

    # 3. Essayer de convertir en entier décimal
    try:
        decimal_value = int(number, source_base)
    except ValueError:
        return "invalid"

    # 4. Vérifier que le résultat est non négatif (au cas où int() accepterait un signe)
    if decimal_value < 0:
        return "invalid"

    # 5. Cas particulier du zéro
    if decimal_value == 0:
        return "0"

    # 6. Conversion vers la base cible (target_base ≤ 36)
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result_chars = []

    while decimal_value > 0:
        remainder = decimal_value % target_base
        result_chars.append(digits[remainder])
        decimal_value //= target_base

    return ''.join(reversed(result_chars))
