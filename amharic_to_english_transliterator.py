
from amharic_mapping import amharic_to_english_mapping

def transliterate(text):
    """Transliterates Amharic text (Fidel) to English (Latin script)."""
    transliteration = ""
    for char in text:
        for mapping in amharic_to_english_mapping:
            if char == mapping["l"]:
                transliteration += mapping["t"]
                break
        else:
            transliteration += char  # Handle non-transliteratable characters
    return transliteration

# Example usage:
print(transliterate("ለምንድን ነው?"))

