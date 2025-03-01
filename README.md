
# PhotoTextSearcher

Библиотека для распознавания текста на изображениях с помощью Tesseract OCR.

## Установка

Для установки библиотеки требуется Python версии 3.9 или выше.

Установите библиотеку с помощью pip:

```bash
pip install PhotoTextSearcher
```

И всё готово!

## Пример использования

Вот пример того, как можно использовать библиотеку для распознавания текста на изображении:

```python
from PhotoTextSearcher import TextRecognizer  # Импорт вашей библиотеки

# Создаем экземпляр класса TextRecognizer
recognizer = TextRecognizer()

# Указываем путь к изображению, которое нужно распознать
image_path = "example.jpg"

# Получаем распознанный текст
recognized_text = recognizer.recognize_text(image_path)

# Выводим распознанный текст
print("Распознанный текст:", recognized_text)
```

## Зависимости

- `pytesseract`
- `Pillow`
- `langdetect`

Эти библиотеки автоматически установятся при установке `PhotoTextSearcher`.

## Лицензия

Этот проект лицензирован под лицензией MIT. См. файл LICENSE для подробностей.
