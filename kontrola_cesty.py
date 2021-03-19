from pprint import pprint as pp

paths = {'/bin/mkdir' : None,

             '/lib/init/vars/vars.sh' : None,

             '/lib/init/vars.sh' : None,

             '/home/documents/reports/report1.xls' : None,

             '/home/music/album3/song2.mp3' : None,

             '/home/music/album1/song2.mp3' : None,

             '/lib/systemd/system/sudo.service' : None

             }

def main():
    # Otevreni txt souboru

    with open('FILESYSTEM.txt') as file:
        # cteni souboru a prevod na slovnik

        filesystem = eval(file.read())

    # Kontrola existenci cesty pomoci funkce file_exist

    for path in paths:
        paths[path] = file_exists(path, filesystem)

    # Tisk slovniku paths

    pp(paths)


def file_exists(path, filesystem):
    # Jednotlive uzly/složky

    nodes = split_path(path)

    # Cil

    target = nodes[-1]

    # Aktualni pracovni adresar

    cwd = filesystem['/']

    # Dokud mame uzly v nodes

    while nodes:

        # Dej mi prvni clen nodes

        node = nodes.pop(0)

        # Zmena aktualniho adresare

        cwd = search_folder(cwd, node)

        # Pokud se cwd rovna nasemu cili a nodes je prazny,

        if cwd == target and not nodes:

            # vrat True

            return True



        # Pokud jsem nenasli dalsi adresar,

        elif not cwd:

            # rozbij loop

            break

    # a vrat False

    return False


def search_folder(folder, target):
    # Projdi slovnik folder

    for item in folder:

        # Pokud je prvek slovnik a jedna se o hledane jmeno

        if isinstance(item, dict) and target in item:

            # vrat danou slozku

            return item[target]



        # Jinak pokud nejde o slovnik (je to tedy soubor, ne slozka)

        elif item == target:

            # Vrati nazev souboru

            return item


def split_path(path):
    # Pokud neni cesta absolutni

    if not is_absolute(path):

        # Rozdeleni znakem '/'

        return path.split('/')



    # Pokud je absolutni

    else:

        # Odstran znak '/' a rozdel znakem '/'

        return path[1:].split('/')


def is_absolute(path):
    # Zacina znakem '/'?

    return path.startswith('/')

main()