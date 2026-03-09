def title2(text):
    """Returns a superior title case from default title()"""
    return ' '.join(word.capitalize() for word in text.split(' '))
