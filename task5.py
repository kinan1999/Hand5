def vowels(text: str) -> int:
    vowels_count = sum(1 for char in text.lower() if char in 'aeiou')
    return vowels_count