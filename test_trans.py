from deep_translator import GoogleTranslator
try:
    translated = GoogleTranslator(source='en', target='ar').translate("Hello World")
    print(f"Translation success: {translated}")
except Exception as e:
    print(f"Error: {e}")
