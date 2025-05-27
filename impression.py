""" Impression Narrative
Module to create a txt file with main's output.
"""
from pathlib import Path
import text

file_path = (Path.home() / 'desktop' / 'narrativa.txt')


def write_file(x):
    with open(file_path, 'a', encoding='utf8') as file:
        narrative = x
        file.write(narrative)
        return print()


def write_file_singular(x, y):
    with open(file_path, 'a', encoding='utf8') as file:
        narrative = text.situation_singular(x, y)
        file.write(narrative)
        return print()


def write_file_plural(x, y):
    with open(file_path, 'a', encoding='utf8') as file:
        narrative = text.situation_plural(x, y)
        file.write(narrative)
        return print()


def erase_file():
    with open(file_path, 'w', encoding='utf8') as file:
        narrative = ''
        return file.write(narrative)


if __name__ == "__main__":
    print(file_path)
