import asyncio
from googletrans import Translator, constants

async def translate_tagalog_to_english(text):
    translator = Translator()
    try:
        translation = await translator.translate(text, src='tl', dest='en')
        return translation.text
    except constants.LANGUAGES as e:
        return f"Language error: {e}" 
    except Exception as e:
        return f"An error occurred: {e}"  


async def main():
    tagalog_text = input("Enter text: ")
    english_translation = await translate_tagalog_to_english(tagalog_text)
    print(f"Translated text: {english_translation}")

if __name__ == "__main__":
    asyncio.run(main())