import sys


# https://pt.stackoverflow.com/questions/495999/validar-upload-de-arquivos-csv
def txt_importer(path_file):
    extensions = ['txt']
    lines = list()
    try:
        with open(path_file, mode='r') as file:
            ext = file.name.lower().split('.')[-1]
            if ext not in extensions:
                print("Formato inválido", file=sys.stderr)

            for line in file.readlines():
                lines.append(line.split('\n')[0])

        return lines

    # https://docs.python.org/3/library/exceptions.html
    except OSError:
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
