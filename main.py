# Funzione di stampa
def stampa_inf(squadre):
    for squadra, statistiche in squadre.items():
        print(f"Squadra: {squadra}")
        print(f"Punti: {statistiche['punti']}")
        print(f"Partite Vinte: {statistiche['partiteVinte']}")
        print(f"Partite Pareggiate: {statistiche['partitePareggiate']}")
        print(f"Partite Perse: {statistiche['partitePerse']}")
        print(f"Gol Segnati: {statistiche['golSegnati']}")
        print(f"Gol Subiti: {statistiche['golSubiti']}")
        print(f"Differenza Reti: {statistiche['df']}")
        print("-" * 30)

#Calcolo automatico del punteggio e della DF
def assegna_punti(squadre):
    for squadra, statistica in squadre.items():
        puntiPartiteVinte = statistica['partiteVinte'] * 3
        statistica['punti'] = puntiPartiteVinte + statistica['partitePareggiate']
        statistica['df'] = statistica['golSegnati'] - statistica['golSubiti']


def stampa_solo_punti(squadre):
    for squadra, statistiche in squadre.items():
        print(f"Squadra: {squadra}")
        print(f"Punti: {statistiche['punti']}")
        print("-" * 30)


# Dizionario delle squadre di Serie A
serie_a = {
    'Napoli': {
        'punti': 0,
        'partiteVinte': 28,
        'partitePareggiate': 6,
        'partitePerse': 4,
        'golSegnati': 77,
        'golSubiti': 28,
        'df': 0
    },
    'Lazio': {
        'punti': 0,
        'partiteVinte': 22,
        'partitePareggiate': 8,
        'partitePerse': 8,
        'golSegnati': 60,
        'golSubiti': 30,
        'df': 0
    },
    'Inter': {
        'punti': 0,
        'partiteVinte': 23,
        'partitePareggiate': 3,
        'partitePerse': 12,
        'golSegnati': 71,
        'golSubiti': 42,
        'df': 0
    },
    'Milan': {
        'punti': 0,
        'partiteVinte': 20,
        'partitePareggiate': 10,
        'partitePerse': 8,
        'golSegnati': 64,
        'golSubiti': 43,
        'df': 0
    },
    'Atalanta': {
        'punti': 0,
        'partiteVinte': 19,
        'partitePareggiate': 7,
        'partitePerse': 12,
        'golSegnati': 66,
        'golSubiti': 64,
        'df': 0
    },
    'Roma': {
        'punti': 0,
        'partiteVinte': 18,
        'partitePareggiate': 9,
        'partitePerse': 11,
        'golSegnati': 50,
        'golSubiti': 38,
        'df': 0
    },
    'Juventus': {
        'punti': 0,
        'partiteVinte': 22,
        'partitePareggiate': 6,
        'partitePerse': 10,
        'golSegnati': 56,
        'golSubiti': 33,
        'df': 0
    },
    'Fiorentina': {
        'punti': 0,
        'partiteVinte': 15,
        'partitePareggiate': 11,
        'partitePerse': 12,
        'golSegnati': 53,
        'golSubiti': 43,
        'df': 0
    },
    'Bologna': {
        'punti': 0,
        'partiteVinte': 14,
        'partitePareggiate': 12,
        'partitePerse': 12,
        'golSegnati': 53,
        'golSubiti': 49,
        'df': 0
    },
    'Torino': {
        'punti': 0,
        'partiteVinte': 14,
        'partitePareggiate': 11,
        'partitePerse': 13,
        'golSegnati': 42,
        'golSubiti': 41,
        'df': 0
    },
    'Monza': {
        'punti': 0,
        'partiteVinte': 14,
        'partitePareggiate': 10,
        'partitePerse': 14,
        'golSegnati': 48,
        'golSubiti': 52,
        'df': 0
    },
    'Udinese': {
        'punti': 0,
        'partiteVinte': 11,
        'partitePareggiate': 13,
        'partitePerse': 14,
        'golSegnati': 47,
        'golSubiti': 48,
        'df': 0
    },
    'Sassuolo': {
        'punti': 0,
        'partiteVinte': 12,
        'partitePareggiate': 9,
        'partitePerse': 17,
        'golSegnati': 47,
        'golSubiti': 61,
        'df': 0
    },
    'Empoli': {
        'punti': 0,
        'partiteVinte': 10,
        'partitePareggiate': 13,
        'partitePerse': 15,
        'golSegnati': 37,
        'golSubiti': 49,
        'df': 0
    },
    'Salernitana': {
        'punti': 0,
        'partiteVinte': 9,
        'partitePareggiate': 15,
        'partitePerse': 14,
        'golSegnati': 48,
        'golSubiti': 62,
        'df': 0
    },
    'Lecce': {
        'punti': 0,
        'partiteVinte': 8,
        'partitePareggiate': 12,
        'partitePerse': 18,
        'golSegnati': 33,
        'golSubiti': 46,
        'df': 0
    },
    'Verona': {
        'punti': 0,
        'partiteVinte': 7,
        'partitePareggiate': 10,
        'partitePerse': 21,
        'golSegnati': 31,
        'golSubiti': 59,
        'df': 0
    },
    'Spezia': {
        'punti': 0,
        'partiteVinte': 6,
        'partitePareggiate': 13,
        'partitePerse': 19,
        'golSegnati': 31,
        'golSubiti': 62,
        'df': 0
    },
    'Cremonese': {
        'punti': 0,
        'partiteVinte': 5,
        'partitePareggiate': 12,
        'partitePerse': 21,
        'golSegnati': 36,
        'golSubiti': 69,
        'df': 0
    },
    'Sampdoria': {
        'punti': 0,
        'partiteVinte': 3,
        'partitePareggiate': 10,
        'partitePerse': 25,
        'golSegnati': 24,
        'golSubiti': 71,
        'df': 0
    },
}
assegna_punti(serie_a)

x = int(input("Cosa vuoi visualizzare:\n[0] - Statistiche Complete\n[1] - Solo Punteggio\n"))

if x == 0:
    stampa_inf(serie_a)
elif x == 1:
    stampa_solo_punti(serie_a)
else:
    print("Errore, devi inserire 1 o 0")




