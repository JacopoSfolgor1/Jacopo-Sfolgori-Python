'''9. Trova tutti i codici fiscali in un testo

Scrivi una funzione find_fc(text) che trova tutti i codici fiscali all'interno di un testo.

Esempio:

testo = "Mario Rossi CF: RSSMRA85M01H501Z, mentre Maria Bianchi ha il CF BNCMRA85T41H501Y."
codici = find_fc(testo) # ['RSSMRA85M01H501Z', 'BNCMRA85T41H501Y']'''

import re

def find_fc(text: str) -> list[str]:

    return re.findall(r"[A-Z]{6}\d{2}[A-Z]\d{2}[A-L]\d{3}[A-Z0-9]", text)

testo = "Mario Rossi CF: RSSMRA85M01H501Z, mentre Maria Bianchi ha il CF BNCMRA85T41H501Y."
codici = find_fc(testo) # ['RSSMRA85M01H501Z', 'BNCMRA85T41H501Y']'''

print(codici)