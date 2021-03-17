# -vytvorte funkci, ktera ma jako argumenty: jmeno, prijmeni, rok_narozeni, *dobrovolne_informace, **dodatkove_informace
# -Funkce nic nevrací jen vypisuje.
# ve funkci se nachází oddelovac nastavte ho tak aby kopíroval délku dynamického text: Jméno: Jakub, příjmení: Valenta, rok narození: 1994

def informace_o_klientovi(jmeno, prijmeni, rok_narozeni, *args, **kwargs):
    first_line = f"Jméno: {jmeno}, příjmení: {prijmeni}, rok narození: {rok_narozeni}"
    separator = "=" * len(first_line)

    print(first_line + "\n" + separator)
    print("Jaké jsou vaše koníčky?\n" + separator)

    for item in args:
        print(item)
    print(separator)

    print("Přejete si něco vzkázat?\n" + separator)
    for key, value in kwargs.items():
        print(f"klic: {key}, Napsal jsi: {value}")


informace_o_klientovi("Jakub", "Valenta", 1994, "Posledni dobou se věnuji programování", "Taky se zajímám o kryptoměny", podekovani = "Děkuji za možnost učit.", prani="Vsem přeji hezký den")