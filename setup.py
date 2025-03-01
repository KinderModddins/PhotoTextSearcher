from setuptools import setup, find_packages

setup(
    name="PhotoTextSearcher",
    version="0.1.1",
    author="MAKCNMOB",
    author_email="support@modkey.fun",
    description="Библиотека для распознавания текста на изображениях",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/KinderModddins/PhotoTextSearcher",  # Замени на свою ссылку
    packages=find_packages(),
    install_requires=[
        'pytesseract',
        'Pillow',
        'langdetect',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
