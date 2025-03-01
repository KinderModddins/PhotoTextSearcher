import easyocr
import numpy as np
from PIL import Image, ImageEnhance, ImageFilter

class TextRecognizer:
    def __init__(self, languages=["en", "ru"]):
        """Инициализация EasyOCR с поддержкой нескольких языков"""
        self.reader = easyocr.Reader(languages)

    def preprocess_image(self, image_path):
        """Предобработка изображения для повышения точности OCR"""
        image = Image.open(image_path).convert("L")  # Ч/б
        image = image.filter(ImageFilter.SHARPEN)  # Улучшение резкости
        image = ImageEnhance.Contrast(image).enhance(2.0)  # Усиление контраста
        return image

    def recognize_text(self, image_path):
        """Распознаёт текст с изображения и фильтрует шум"""
        image = self.preprocess_image(image_path)
        results = self.reader.readtext(np.array(image))

        # Фильтрация мусора: оставляем только длинные слова
        text_lines = [res[1] for res in results if len(res[1]) > 2]
        return "\n".join(text_lines) if text_lines else "Текст не найден"

# 🔹 Пример использования
if __name__ == "__main__":
    recognizer = TextRecognizer()
    text = recognizer.recognize_text("example.jpg")
    print(text)
