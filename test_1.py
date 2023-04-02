def capitalize_first_letters(str):
    """Capitalizes the first letter of each word in the input string."""
    return str.title()

def capitalize_first_letters(str):
    """Capitalizes the first letter of each word in the input string."""
    words = str.split()  # main branch change
    return " ".join(word.capitalize() for word in words)