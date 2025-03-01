from PhotoTextSearcher import TextRecognizer

recognizer = TextRecognizer()
text = recognizer.recognize_text("photo.jpg")
print("📜 Распознанный текст:\n", text)
