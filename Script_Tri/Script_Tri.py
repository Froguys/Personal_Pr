# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 11:24:06 2024
Objectif: trier les fichiers ici particulièrement download
@author: Froguys
"""

# On importe les librairies

import os
import shutil

# On défini les chemins qui vont être utiliser
Origin_path="Chemin du dossier a modifier"

Image_path="C:\Users\hadri\OneDrive\Bureau\R_Script\Images"
Archives_path="C:\Users\hadri\OneDrive\Bureau\R_Script\Archives"
Documents_path="C:\Users\hadri\OneDrive\Bureau\R_Script\Documents"
Video_path="C:\Users\hadri\OneDrive\Bureau\R_Script\Video"
Other_path="C:\Users\hadri\OneDrive\Bureau\R_Script\Autre"
Presentation_path="C:\Users\hadri\OneDrive\Bureau\R_Script\Presentation"
Dossiers_path="C:\Users\hadri\OneDrive\Bureau\R_Script\Dossiers"

# On définie les mots clé
extensions = {
    "Images": [".jpg", ".jpeg", ".png", ".gif",".apng", ".bmp", ".tif", ".tiff",".webp",".svg",".avif"],
    "Documents": [".pdf", ".docx",".doc", ".txt", ".xlsx",".xls",".csv",".ods",".pub",".rtf",".md",".tex",".epub",".mobi",".json",".xml",".log"],
    "Presentation":[".ppt ",".pptx",".odp"],
    "Vidéos": [".mp4", ".mkv", ".avi", ".mov", ".wmv", ".flv",".webm", ".3gp", ".m4v", ".ts"],
    "Musique": [".mp3", ".wav", ".flac", ".aac", ".ogg",".m4a", ".wma", ".alac", ".aiff"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz", ".bz2",".xz", ".iso", ".tgz", ".tar.gz", ".z", ".cab",".deb", ".rpm"]
}
