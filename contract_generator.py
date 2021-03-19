def main():
    print("""
Please select the option number of action you want to perform: 
0. salary change
1. job change
2. contract prolongation""")
    template = input()
    if template == "0":
        template = "salary_change.txt"
    elif template == "1":
        template = "job_change.txt"
    elif template == "2":
        template = "contract_prolongation.txt"
    else:
        print("Unknown template number.")
        exit()

def fill_template(template):
    pass
    # načíst šablonu
    # načte údaje zaměstnance
    # doplní ve stringu údaje podle klíčů
    # nový string uloží do souboru


# Creating contract for X12345 ....
# Creating contract for X54321 ....
# Contracts have been generated.

main()