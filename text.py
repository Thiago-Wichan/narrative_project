from string import Template
from pathlib import Path

FILE_PATH = Path(__file__).parent / 'text_files'

singular_interdition_path = FILE_PATH / 'singular_text_interdition.txt'

plural_interdition_path = FILE_PATH / 'plural_text_interdition.txt'

singular_path = FILE_PATH / 'singular_text.txt'

plural_path = FILE_PATH / 'plural_text.txt'


def open_text(path, variables):
    with open(path, 'r', encoding='utf8') as file:
        text_ = file.read()
        template = Template(text_)
        return (template.substitute(variables))


def situation_singular(scene_situation, interdition_situation):
    variables = dict(scene=scene_situation,
                     interdition=interdition_situation)

    if interdition_situation:
        return open_text(singular_interdition_path, variables)

    else:
        return open_text(singular_path, variables)


def situation_plural(scene_situation, interdition_situation):
    variables = dict(scene=scene_situation,
                     interdition=interdition_situation)

    if interdition_situation:
        return open_text(plural_interdition_path, variables)

    else:
        return open_text(plural_path, variables)
