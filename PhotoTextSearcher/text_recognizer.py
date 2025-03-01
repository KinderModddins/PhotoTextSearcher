from PIL import Image, ImageEnhance, ImageFilter
import pytesseract
from langdetect import detect, DetectorFactory

# Фиксируем случайность для стабильности langdetect
DetectorFactory.seed = 0

class TextRecognizer:
    def __init__(self, tesseract_cmd=None):
        if tesseract_cmd:
            pytesseract.pytesseract.tesseract_cmd = tesseract_cmd

    def preprocess_image(self, image_path):
        """ Загружает и подготавливает изображение для распознавания """
        image = Image.open(image_path)
        image = image.convert("L")  # Преобразование в ЧБ
        image = image.filter(ImageFilter.SHARPEN)  # Повышение резкости
        enhancer = ImageEnhance.Contrast(image)
        image = enhancer.enhance(2)  # Усиление контраста
        return image

    def detect_language(self, text):
        """ Определяет язык текста """
        try:
            lang_code = detect(text)
        except:
            lang_code = "eng"  # Если язык не определён, используем английский
        return lang_code

    def recognize_text(self, image_path):
        """ Распознаёт текст и автоматически определяет язык """
        image = self.preprocess_image(image_path)
        raw_text = pytesseract.image_to_string(image)  # Распознавание текста
        lang = self.detect_language(raw_text)  # Определение языка
        final_text = pytesseract.image_to_string(image, lang=lang)  # Повторное распознавание с правильным языком
        return final_text

# Пример использования
if __name__ == "__main__":
    recognizer = TextRecognizer()
    text = recognizer.recognize_text("example.jpg")
    print("Распознанный текст:", text)
