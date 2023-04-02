def capitalize_all_letters(str):
    """Capitalizes all letters in the input string."""
    return str.upper()

def capitalize_first_letters(str):
    """Capitalizes the first letter of each word in the input string."""
    words = str.split()  # main branch change
    return " ".join(word.capitalize() for word in words)