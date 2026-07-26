# PROGETTO 1 - GESTIONE DI UNA BIBLIOTECA DIGITALE
#
# In una biblioteca digitale si vuole realizzare un piccolo sistema
# software per gestire libri, utenti e prestiti.
# Il programma utilizza variabili, strutture dati, controlli e OOP.


# ============================================================
# PARTE 1 - VARIABILI E TIPI DI DATI
# ============================================================

titolo = "Il nome della rosa"
copie = 5
prezzo_medio = 11.00
disponibile = True

print("=== DATI INIZIALI ===")
print("Titolo:", titolo)
print("Numero di copie:", copie)
print("Prezzo medio:", prezzo_medio)
print("Disponibile:", disponibile)


# ============================================================
# PARTE 2 - STRUTTURE DATI
# ============================================================

# Lista contenente almeno cinque libri
libri = [
    "Il nome della rosa",
    "Il signore degli anelli",
    "I promessi sposi",
    "Harry Potter e la pietra filosofale",
    "La Divina Commedia"
]

# Dizionario che associa ogni titolo al numero di copie disponibili
copie_libri = {
    "Il nome della rosa": 5,
    "Il signore degli anelli": 3,
    "I promessi sposi": 7,
    "Harry Potter e la pietra filosofale": 2,
    "La Divina Commedia": 4
}

# Set contenente gli utenti registrati
utenti_registrati = {"Alberto", "Corinne", "Marco", "Giulia"}

print("\n=== STRUTTURE DATI ===")
print("Lista libri:", libri)
print("Copie disponibili:", copie_libri)
print("Utenti registrati:", utenti_registrati)


# ============================================================
# PARTE 3 - CLASSI E PROGRAMMAZIONE A OGGETTI
# ============================================================

class Libro:
    """Rappresenta un libro presente nella biblioteca."""

    def __init__(self, titolo, autore, anno, copie_disponibili):
        self.titolo = titolo
        self.autore = autore
        self.anno = anno
        self.copie_disponibili = copie_disponibili

    def __str__(self):
        return (
            f"{self.titolo} - {self.autore} ({self.anno}) | "
            f"Copie disponibili: {self.copie_disponibili}"
        )

    def info(self):
        """Stampa tutte le informazioni del libro."""
        print("\n=== SCHEDA LIBRO ===")
        print(f"Titolo: {self.titolo}")
        print(f"Autore: {self.autore}")
        print(f"Anno: {self.anno}")
        print(f"Copie disponibili: {self.copie_disponibili}")


class Utente:
    """Rappresenta un utente registrato alla biblioteca."""

    def __init__(self, nome, eta, id_utente):
        self.nome = nome
        self.eta = eta
        self.id_utente = id_utente

    def __str__(self):
        return (
            f"Utente: {self.nome} | Età: {self.eta} | "
            f"ID: {self.id_utente}"
        )

    def scheda(self):
        """Stampa tutti i dati dell'utente."""
        print("\n=== SCHEDA UTENTE ===")
        print(f"Nome: {self.nome}")
        print(f"Età: {self.eta}")
        print(f"ID utente: {self.id_utente}")


class Prestito:
    """Rappresenta il prestito di un libro a un utente."""

    def __init__(self, utente, libro, giorni):
        self.utente = utente
        self.libro = libro
        self.giorni = giorni

    def __str__(self):
        return (
            f"Prestito | Utente: {self.utente.nome} "
            f"(ID: {self.utente.id_utente}) | "
            f"Libro: {self.libro.titolo} | "
            f"Durata: {self.giorni} giorni"
        )

    def dettagli(self):
        """Stampa tutte le informazioni relative al prestito."""
        print("\n=== DETTAGLI PRESTITO ===")
        print(
            f"Utente: {self.utente.nome} "
            f"(ID: {self.utente.id_utente})"
        )
        print(f"Età utente: {self.utente.eta}")
        print(f"Libro: {self.libro.titolo}")
        print(f"Autore: {self.libro.autore}")
        print(f"Anno: {self.libro.anno}")
        print(f"Giorni di prestito: {self.giorni}")
        print(
            "Copie disponibili dopo il prestito:",
            self.libro.copie_disponibili
        )


# ============================================================
# PARTE 4 - CREAZIONE DEGLI OGGETTI
# ============================================================

# Creazione dei cinque libri del progetto originale
libro1 = Libro(
    "Il nome della rosa",
    "Umberto Eco",
    1980,
    5
)

libro2 = Libro(
    "Il signore degli anelli",
    "J.R.R. Tolkien",
    1954,
    3
)

libro3 = Libro(
    "I promessi sposi",
    "Alessandro Manzoni",
    1827,
    7
)

libro4 = Libro(
    "Harry Potter e la pietra filosofale",
    "J.K. Rowling",
    1997,
    2
)

libro5 = Libro(
    "La Divina Commedia",
    "Dante Alighieri",
    1321,
    4
)

biblioteca = [libro1, libro2, libro3, libro4, libro5]

# Creazione degli utenti
utente1 = Utente("Alberto", 40, 1)
utente2 = Utente("Marco", 25, 2)
utente3 = Utente("Simona", 30, 3)
utente4 = Utente("Corinne", 35, 4)

lista_utenti = [utente1, utente2, utente3, utente4]

print("\n=== LIBRI PRESENTI IN BIBLIOTECA ===")
for libro in biblioteca:
    print(libro)

print("\n=== UTENTI REGISTRATI ===")
for utente in lista_utenti:
    print(utente)


# ============================================================
# PARTE 5 - FUNZIONE PER EFFETTUARE UN PRESTITO
# ============================================================

def presta_libro(utente, libro, giorni):
    """
    Verifica che il libro abbia almeno una copia disponibile.

    Se il libro è disponibile:
    - riduce le copie di una unità;
    - crea e restituisce un oggetto Prestito.

    Se non è disponibile:
    - stampa un messaggio di errore;
    - restituisce None.
    """

    if giorni <= 0:
        print(
            f"\nERRORE: la durata del prestito di "
            f"'{libro.titolo}' deve essere maggiore di zero."
        )
        return None

    if libro.copie_disponibili >= 1:
        libro.copie_disponibili -= 1
        nuovo_prestito = Prestito(utente, libro, giorni)

        print("\nPrestito effettuato con successo.")
        print(f"Utente: {utente.nome}")
        print(f"Libro: {libro.titolo}")
        print(f"Durata: {giorni} giorni")
        print(f"Copie rimaste: {libro.copie_disponibili}")

        return nuovo_prestito

    print(
        f"\nERRORE: nessuna copia disponibile "
        f"per il libro '{libro.titolo}'."
    )
    return None


# ============================================================
# PARTE 6 - SIMULAZIONE DEI PRESTITI
# ============================================================

print("\n=== INIZIO SIMULAZIONE PRESTITI ===")

# La consegna ne richiede almeno tre.
# Qui vengono simulati cinque prestiti, uno per ciascun libro.
prestito1 = presta_libro(utente1, libro1, 14)
prestito2 = presta_libro(utente2, libro2, 10)
prestito3 = presta_libro(utente3, libro3, 7)
prestito4 = presta_libro(utente4, libro4, 12)
prestito5 = presta_libro(utente1, libro5, 20)

# Inserisce nella lista solo i prestiti creati correttamente
prestiti = [
    prestito
    for prestito in [
        prestito1,
        prestito2,
        prestito3,
        prestito4,
        prestito5
    ]
    if prestito is not None
]

# ============================================================
# PARTE 7 - STAMPA FINALE RICHIESTA
# ============================================================

# Stampa i dettagli di ogni prestito effettuato
print("\n=== DETTAGLI DI OGNI PRESTITO EFFETTUATO ===")

if len(prestiti) > 0:
    for numero, prestito in enumerate(prestiti, start=1):
        print(f"\n--- PRESTITO NUMERO {numero} ---")
        prestito.dettagli()
else:
    print("Non è stato effettuato nessun prestito.")


# Stampa l'elenco aggiornato delle copie disponibili
# per ciascun libro
print("\n=== ELENCO AGGIORNATO DELLE COPIE DISPONIBILI ===")

for libro in biblioteca:
    print(
        f"Titolo: {libro.titolo} | "
        f"Copie disponibili: {libro.copie_disponibili}"
    )


print("\n=== FINE PROGRAMMA ===")
