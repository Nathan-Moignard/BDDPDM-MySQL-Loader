import requests
from os import path, mkdir, rmdir

BASE_URL = 'https://base-donnees-publique.medicaments.gouv.fr/telechargement.php?fichier='

def downloadSource(filename: str):
    if path.exists('sources/') == False:
        mkdir('sources/')

    fileContent = requests.get(BASE_URL + filename, stream=True).content
    open('sources/' + filename, 'wb').write(fileContent)