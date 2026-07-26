# PROGETTO 2 - GESTIONE DI UN CENTRO DI ANALISI MEDICHE
#
# Il programma gestisce pazienti, medici e risultati di laboratorio
# utilizzando la programmazione a oggetti (OOP) e la libreria NumPy.
#
# NOTA: gli intervalli usati per valutare le analisi sono semplificati
# e hanno esclusivamente finalità didattiche.


import numpy as np


# ============================================================
# PARTE 1 - VARIABILI E TIPI DI DATI
# ============================================================

# Primo paziente
nome1 = "Mario"
cognome1 = "Rossi"
codice_fiscale1 = "RSSMRA81A01H501Z"
eta1 = 45
peso1 = 78.5
analisi1 = ["emocromo", "glicemia", "colesterolo"]

# Secondo paziente
nome2 = "Lucia"
cognome2 = "Bianchi"
codice_fiscale2 = "BNCLCU91B41H501Y"
eta2 = 35
peso2 = 62.3
analisi2 = ["glicemia", "colesterolo", "trigliceridi"]

# Terzo paziente
nome3 = "Giovanni"
cognome3 = "Verdi"
codice_fiscale3 = "VRDGNN71C15H501X"
eta3 = 55
peso3 = 84.7
analisi3 = ["emocromo", "glicemia", "trigliceridi"]


def stampa_dati_iniziali():
    """Stampa i tre pazienti definiti mediante variabili semplici."""
    print("=== PARTE 1: DATI INIZIALI DEI PAZIENTI ===")

    print(
        f"1. {nome1} {cognome1} | CF: {codice_fiscale1} | "
        f"Età: {eta1} | Peso: {peso1} kg | Analisi: {analisi1}"
    )

    print(
        f"2. {nome2} {cognome2} | CF: {codice_fiscale2} | "
        f"Età: {eta2} | Peso: {peso2} kg | Analisi: {analisi2}"
    )

    print(
        f"3. {nome3} {cognome3} | CF: {codice_fiscale3} | "
        f"Età: {eta3} | Peso: {peso3} kg | Analisi: {analisi3}"
    )


# ============================================================
# PARTE 2 E PARTE 4 - CLASSI, OOP E INTEGRAZIONE CON NUMPY
# ============================================================

class Paziente:
    """Rappresenta un paziente del centro di analisi."""

    def __init__(
        self,
        nome,
        cognome,
        codice_fiscale,
        eta,
        peso,
        analisi_effettuate,
        risultati_analisi
    ):
        self.nome = nome
        self.cognome = cognome
        self.codice_fiscale = codice_fiscale
        self.eta = eta
        self.peso = peso
        self.analisi_effettuate = list(analisi_effettuate)

        # Conversione dei risultati in un array NumPy di numeri decimali
        self.risultati_analisi = np.array(
            risultati_analisi,
            dtype=float
        )

        # Ogni analisi deve avere il proprio risultato numerico
        if len(self.analisi_effettuate) != len(self.risultati_analisi):
            raise ValueError(
                "Il numero delle analisi deve essere uguale "
                "al numero dei risultati."
            )

    def scheda_personale(self):
        """Restituisce una stringa con i dati principali del paziente."""
        elenco_analisi = ", ".join(self.analisi_effettuate)

        return (
            f"Paziente: {self.nome} {self.cognome}\n"
            f"Codice fiscale: {self.codice_fiscale}\n"
            f"Età: {self.eta} anni\n"
            f"Peso: {self.peso:.1f} kg\n"
            f"Analisi effettuate: {elenco_analisi}"
        )

    def statistiche_analisi(self):
        """
        Calcola media, minimo, massimo e deviazione standard
        dei risultati del paziente utilizzando NumPy.
        """
        if self.risultati_analisi.size == 0:
            return None

        return {
            "media": float(np.mean(self.risultati_analisi)),
            "minimo": float(np.min(self.risultati_analisi)),
            "massimo": float(np.max(self.risultati_analisi)),
            "deviazione_standard": float(
                np.std(self.risultati_analisi)
            )
        }

    def stampa_risultati(self):
        """Stampa ogni analisi con il risultato e la valutazione."""
        print("Risultati delle analisi:")

        for tipo, risultato in zip(
            self.analisi_effettuate,
            self.risultati_analisi
        ):
            analisi = Analisi(tipo, risultato)

            print(
                f"- {tipo.capitalize()}: {risultato:.2f} "
                f"({analisi.valuta()})"
            )


class Medico:
    """Rappresenta un medico del centro di analisi."""

    def __init__(self, nome, cognome, specializzazione):
        self.nome = nome
        self.cognome = cognome
        self.specializzazione = specializzazione

    def __str__(self):
        return (
            f"Dott. {self.nome} {self.cognome} - "
            f"{self.specializzazione}"
        )

    def visita_paziente(self, paziente):
        """Stampa quale medico sta visitando quale paziente."""
        print(
            f"Il medico {self.nome} {self.cognome}, "
            f"specialista in {self.specializzazione}, "
            f"sta visitando il paziente "
            f"{paziente.nome} {paziente.cognome}."
        )


class Analisi:
    """Rappresenta una singola analisi con un risultato numerico."""

    # Intervalli semplificati e inventati per l'esercizio
    INTERVALLI_DIDATTICI = {
        "glicemia": (70, 100),
        "colesterolo": (120, 200),
        "trigliceridi": (40, 150),
        "emocromo": (4, 10)
    }

    def __init__(self, tipo, risultato):
        self.tipo = tipo.lower()
        self.risultato = float(risultato)

    def valuta(self):
        """
        Stabilisce se il risultato è nella norma usando
        intervalli didattici semplificati.
        """
        if self.tipo not in self.INTERVALLI_DIDATTICI:
            return "criterio non disponibile"

        minimo, massimo = self.INTERVALLI_DIDATTICI[self.tipo]

        if minimo <= self.risultato <= massimo:
            return "valore nella norma"

        return "valore fuori norma"


# ============================================================
# PARTE 3 - USO DI NUMPY SU 10 PAZIENTI
# ============================================================

def analizza_campione_centro():
    """
    Rappresenta i risultati di glicemia di 10 pazienti
    e calcola le principali statistiche con NumPy.
    """
    risultati_glicemia = np.array(
        [82, 95, 105, 88, 110, 76, 99, 91, 84, 102],
        dtype=float
    )

    print("\n=== PARTE 3: ANALISI NUMPY SU 10 PAZIENTI ===")
    print("Risultati glicemia:", risultati_glicemia)
    print(f"Media: {np.mean(risultati_glicemia):.2f}")
    print(f"Valore massimo: {np.max(risultati_glicemia):.2f}")
    print(f"Valore minimo: {np.min(risultati_glicemia):.2f}")
    print(
        "Deviazione standard: "
        f"{np.std(risultati_glicemia):.2f}"
    )


# ============================================================
# PARTE 5 - PROGRAMMA PRINCIPALE
# ============================================================

def main():
    """Esegue il programma completo."""

    stampa_dati_iniziali()
    analizza_campione_centro()

    # Creazione di almeno tre medici
    medici = [
        Medico("Anna", "Neri", "Medicina generale"),
        Medico("Paolo", "Romano", "Cardiologia"),
        Medico("Elena", "Conti", "Medicina interna")
    ]

    # Creazione di almeno cinque pazienti.
    # Ogni paziente possiede almeno tre risultati di analisi.
    pazienti = [
        Paziente(
            "Mario",
            "Rossi",
            "RSSMRA81A01H501Z",
            45,
            78.5,
            ["emocromo", "glicemia", "colesterolo"],
            [7.2, 95, 185]
        ),
        Paziente(
            "Lucia",
            "Bianchi",
            "BNCLCU91B41H501Y",
            35,
            62.3,
            ["glicemia", "colesterolo", "trigliceridi"],
            [108, 198, 145]
        ),
        Paziente(
            "Giovanni",
            "Verdi",
            "VRDGNN71C15H501X",
            55,
            84.7,
            ["emocromo", "glicemia", "trigliceridi"],
            [6.8, 115, 160]
        ),
        Paziente(
            "Sara",
            "Esposito",
            "SPSSRA96D52H501W",
            30,
            58.9,
            ["glicemia", "colesterolo", "emocromo"],
            [89, 172, 5.9]
        ),
        Paziente(
            "Luca",
            "Ferrari",
            "FRRLCU86E18H501V",
            40,
            91.2,
            ["trigliceridi", "glicemia", "colesterolo"],
            [132, 101, 210]
        )
    ]

    print("\n=== MEDICI DEL CENTRO ===")
    for medico in medici:
        print(medico)

    print("\n=== SCHEDE, VISITE E STATISTICHE DEI PAZIENTI ===")

    # A ogni paziente viene assegnato un medico.
    # L'operatore % permette di riutilizzare i medici a rotazione.
    for indice, paziente in enumerate(pazienti):
        medico_assegnato = medici[indice % len(medici)]

        print("\n" + "=" * 60)
        print(paziente.scheda_personale())
        print()

        medico_assegnato.visita_paziente(paziente)
        print()

        paziente.stampa_risultati()

        statistiche = paziente.statistiche_analisi()

        if statistiche is not None:
            print("\nStatistiche dei risultati:")
            print(f"- Media: {statistiche['media']:.2f}")
            print(f"- Minimo: {statistiche['minimo']:.2f}")
            print(f"- Massimo: {statistiche['massimo']:.2f}")
            print(
                "- Deviazione standard: "
                f"{statistiche['deviazione_standard']:.2f}"
            )

    print("\n" + "=" * 60)
    print("=== FINE PROGRAMMA ===")


# Il programma parte solo quando il file viene eseguito direttamente
if __name__ == "__main__":
    main()