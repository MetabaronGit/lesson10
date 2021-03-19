TEMPLATE_PATH = '/home/martin/PythonBeginner/Lesson6/Templates'
CONTRACTS_PATH = '/home/martin/PythonBeginner/Lesson6/Contracts'
EMPLOYEE_DB_PATH = '/home/martin/PythonBeginner/Lesson6/employees.txt'

TEMPLATES = ['salary change', 'job change', 'contract prolongation']


def main():
    # Volba sablony
    num = int(input(print_prompt()))

    # Nahrani dat
    employees = load_db(EMPLOYEE_DB_PATH)

    # Ziskani jmena sablony
    template_name = TEMPLATES[num].replace(' ', '_')

    # Nahrani sablony
    template = load_template(template_name)

    # Generovani smlouvy
    for employee_id, employee in employees.items():
        print('Creating contract for %s ....' % (employee_id,))
        write_file(employee, template, template_name)

    # Tisk zaverecne zpravy pro uzivatele
    print('\nContracts have been generated.')


def print_prompt():
    # Vyzva uzivateli
    print('Please select the option number of action you want to perform:\n')

    # Tisk moznosti
    for temp in enumerate(TEMPLATES):
        print('{}. {}'.format(*temp))

    # Vraceni noveho radku
    return '\n'


def load_db(path):
    # Kontextovy manazer
    with open(path) as employees_file:
        # Ziskani obsahu
        content = employees_file.read()

    # Vraceni obsahu jako slovnik
    return eval(content)


def load_db(path):
    # Otevreni
    employees_file = open(path)

    # Cteni obsahu
    content = employees_file.read()

    # Zavreni souboru
    employees_file.close()

    # Vraceni obsahu jako slovnik
    return eval(content)


def load_template(template_name):
    # Ziskani cesty k sablone
    template_path = '{}/{}.txt'.format(TEMPLATE_PATH, template_name)
    # Kontextovy manazer
    with open(template_path) as template_file:
        # Cteni obsahu
        template = template_file.read()
    # Vraceni obsahu
    return template


def write_file(employee, template, template_name):
    # Ziskani jmena souboru
    filename = '{}_{}.txt'.format(template_name, employee['full_name'])
    # Ziskani cesty k souboru
    filepath = '{}/{}'.format(CONTRACTS_PATH, filename)
    # Kontextovy manazer
    with open(filepath, 'w') as new_file:
        # Zapis do noveho souboru
        new_file.write(template.format(**employee))


main()