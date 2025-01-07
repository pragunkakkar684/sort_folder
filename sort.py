import os
import re
import shutil
import zipfile
import sys

def normalise(string, orig_case = True):
    translit_mapping = {
        'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'ґ': 'g', 'д': 'd', 'е': 'e',
        'є': 'ie', 'ж': 'zh', 'з': 'z', 'и': 'y', 'і': 'i', 'ї': 'i', 'й': 'i',
        'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r',
        'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'kh', 'ц': 'ts', 'ч': 'ch',
        'ш': 'sh', 'щ': 'shch', 'ь': '', 'ю': 'iu', 'я': 'ia'
    }

    translit_string = ""
    pre_char_is_underscore = False
    for char in string:
        if char.lower() in translit_mapping:
            replacement = translit_mapping[char.lower()]  #changes the char to latin
            if char.isupper() and orig_case:
                replacement = replacement.upper()
            translit_string += replacement
            pre_char_is_underscore = False
        elif re.match(r'[a-zA-Z0-9]',char):
            translit_string += char if orig_case else char.lower()
            pre_char_is_underscore = False
        else:
            if not pre_char_is_underscore:
                translit_string += "_"
                pre_char_is_underscore = True
    return translit_string.strip("_")

def process_archive(file_path,sorting_folder):
    archive_name,file_ext = os.path.basename(file_path).split(".")
    normalised_archive_name = normalise(archive_name)
    archive_folder = os.path.join(sorting_folder,normalised_archive_name)


