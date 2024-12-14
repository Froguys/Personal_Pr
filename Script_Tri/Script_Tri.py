# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 11:24:06 2024
Objectif: trier les fichiers ici particulièrement download
@author: Froguys
"""

# On importe les librairies

import os
import shutil
import re

# On défini les chemins qui vont être utiliser
Origin_path=r"C:\Users\hadri\OneDrive\Bureau\Tri_Test"
Image_path=r"C:\Users\hadri\OneDrive\Bureau\R_Script\Images"
Archives_path=r"C:\Users\hadri\OneDrive\Bureau\R_Script\Archives"
Documents_path=r"C:\Users\hadri\OneDrive\Bureau\R_Script\Documents"
Videos_path=r"C:\Users\hadri\OneDrive\Bureau\R_Script\Video"
Presentation_path=r"C:\Users\hadri\OneDrive\Bureau\R_Script\Presentation"
Other_path=r"C:\Users\hadri\OneDrive\Bureau\R_Script\Autre"
Musiques_path=r"C:\Users\hadri\OneDrive\Bureau\R_Script\Musiques"
Dossiers_path=r"C:\Users\hadri\OneDrive\Bureau\R_Script\Dossiers"

def clean_string(filename):
    # Expression régulière pour nom_fichier-n
    pattern1 = r'^(.+)-\d+$' # ^ début de la chaine  (.+) caputre le nom du fichier -\d+  tiret suivit d'un ou plusieurs chiffres.
    # Expression régulière pour nom_fichier(n)
    pattern2 = r'^(.+)\(\d+\)$'# même chose mais\( suivit de (

    # Vérifie si la chaîne correspond à l'un des motifs et extrait le nom de fichier
    match1 = re.match(pattern1, filename)
    match2 = re.match(pattern2, filename)

    if match1:
        # Retourne la partie sans -n
        return match1.group(1)
    elif match2:
        # Retourne la partie sans (n)
        return match2.group(1)

    # Si aucun des motifs ne correspond, retourne le nom tel quel
    return filename


# On définie les mots clé
extensions = {
    "Images": [".jpg", ".jpeg", ".png", ".gif",".apng", ".bmp", ".tif", ".tiff",".webp",".svg",".avif"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz", ".bz2", ".xz", ".iso", ".tgz", ".tar.gz", ".z", ".cab", ".deb",".rpm"],
    "Documents": [".pdf", ".docx",".doc", ".txt", ".xlsx",".xls",".csv",".ods",".pub",".rtf",".md",".tex",".epub",".mobi",".json",".xml",".log"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov", ".wmv", ".flv",".webm", ".3gp", ".m4v", ".ts"],
    "Presentation":[".ppt ",".pptx",".odp"],
    "Musique": [".mp3", ".wav", ".flac", ".aac", ".ogg",".m4a", ".wma", ".alac", ".aiff"],
}

#Corp du script
for file in os.listdir(Origin_path):
    file_path = os.path.join(Origin_path, file)
    filename, extension = os.path.splitext(file_path)
    if not(os.path.isfile(file_path)):
        final_path=Dossiers_path
        shutil.move(file_path, final_path)
    match extension:
        case ext if ext in extensions["Images"]:
            shutil.move(file_path, Image_path)
        case ext if ext in extensions["Documents"]:
            shutil.move(file_path, Documents_path)
        case ext if ext in extensions["Presentation"]:
            shutil.move(file_path, Presentation_path)
        case ext if ext in extensions["Videos"]:
            shutil.move(file_path, Videos_path)
        case ext if ext in extensions["Archives"]:
            shutil.move(file_path, Archives_path)
        case ext if ext in extensions["Musique"]:
            shutil.move(file_path, Musiques_path)
        case _:
            shutil.move(file_path, Other_path)
