""" Impression Narrative
Module to create a txt file with main's output.
"""
from pathlib import Path
import text

FILE_DESKTOP_PATH = (Path.home() / 'desktop' / 'narrativa.txt')


def write_file(x):
    with open(FILE_DESKTOP_PATH, 'a', encoding='utf8') as file:
        narrative = x
        file.write(narrative)
        return print()


def write_file_singular(x, y):
    with open(FILE_DESKTOP_PATH, 'a', encoding='utf8') as file:
        narrative = text.situation_singular(x, y)
        file.write(narrative)
        return print()


def write_file_plural(x, y):
    with open(FILE_DESKTOP_PATH, 'a', encoding='utf8') as file:
        narrative = text.situation_plural(x, y)
        file.write(narrative)
        return print()


def erase_text_file():
    with open(FILE_DESKTOP_PATH, 'w', encoding='utf8') as file:
        narrative = ''
        return file.write(narrative)


if __name__ == "__main__":
    print(FILE_DESKTOP_PATH)
