import re

def normalize_phone(phone_number: str) -> str:
    """
    Normalizing phone number

    Returns:
        clear phone number without symbols
    """
    clean_number = re.sub(r"[^\d+]", "", phone_number)
    if not clean_number.startswith("+"):
        if clean_number.startswith("380"):
            clean_number = "+" + clean_number
        else:
            clean_number = "+38" + clean_number

    return clean_number