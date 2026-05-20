# Ishga tushirishdan oldin terminalda: pip install deep-translator
from deep_translator import GoogleTranslator

print("🤖 Kiber Tarjimon (Inglizcha -> O'zbekcha)")
print("To'xtatish uchun 'exit' deb yozing.\n")

while True:
    matn = input("🇬🇧 Inglizcha matn kiriting: ")
    if matn.lower() == 'exit':
        print("👋 Dastur tugatildi.")
        break
        
    if matn.strip() == "":
        continue
        
    try:
        # Google Translate API orqali tarjima qilish
        tarjima = GoogleTranslator(source='en', target='uz').translate(matn)
        print(f"🇺🇿 O'zbekcha tarjimasi: {tarjima}")
        print("-" * 40)
    except Exception as e:
        print(f"❌ Ulanishda xato: {e}")