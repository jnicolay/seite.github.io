# Importiere benötigte Module für Zeitverzögerung und Zufallsereignisse
import time
import random

# Funktion zum Anzeigen von Nachrichten mit Verzögerung
def verzögertes_drucken(nachricht):
    """
    Funktion, um Nachrichten mit einer kleinen Verzögerung anzuzeigen
    """
    print(nachricht)
    time.sleep(2)

# Startet das Spiel und gibt eine Einführung in die Geschichte
def spiel_starten():
    """
    Funktion, um das Spiel zu starten und eine Einführung zu geben
    """
    verzögertes_drucken("Es ist das Jahr 2150. Die Welt, wie wir sie kannten, ist zerstört.")
    verzögertes_drucken("Mutanten streifen durch das Land, und nur wenige Überlebende haben sich in den Ruinen der Städte versteckt.")
    verzögertes_drucken("Gerüchten zufolge gibt es einen verlassenen Militärbunker, der ein Serum enthält, das dich unbesiegbar macht.")
    verzögertes_drucken("Was möchtest du tun?")
    verzögertes_drucken("1. Begib dich auf die gefährliche Reise, um den Bunker zu finden und das Serum zu bergen.")
    verzögertes_drucken("2. Suche den Rat eines alten Überlebenden, bevor du eine Entscheidung triffst.")

    # Benutzereingabe abfragen
    spieler_wahl = input("Gib 1 oder 2 ein: ")

    if spieler_wahl == "1":
        bunker_finden()
    elif spieler_wahl == "2":
        rat_suchen()
    else:
        verzögertes_drucken("Entschuldigung, ich habe das nicht verstanden. Bitte gib 1 oder 2 ein.")
        spiel_starten()

# Funktion, um den Bunker zu finden
def bunker_finden():
    """
    Funktion, um den Bunker zu finden
    """
    verzögertes_drucken("Du machst dich auf eine gefährliche Reise durch die verstrahlte Einöde.")
    verzögertes_drucken("Nach Tagen des Wanderns erreichst du den verlassenen Bunker.")
    verzögertes_drucken("Im Inneren findest du einen Raum, in dem das Serum aufbewahrt wird. Was möchtest du tun?")
    verzögertes_drucken("1. Nimm das Serum und werde unbesiegbar.")
    verzögertes_drucken("2. Verlasse den Bunker ohne das Serum zu nehmen.")

    spieler_wahl = input("Gib 1 oder 2 ein: ")

    if spieler_wahl == "1":
        serum_nehmen()
    elif spieler_wahl == "2":
        bunker_verlassen()
    else:
        verzögertes_drucken("Entschuldigung, das habe ich nicht verstanden. Bitte gib 1 oder 2 ein.")
        bunker_finden()

# Funktion, um das Serum zu nehmen
def serum_nehmen():
    """
    Funktion, um das Serum im Bunker zu nehmen
    """
    verzögertes_drucken("Du injizierst dir das Serum, und sofort spürst du eine unglaubliche Stärke.")
    verzögertes_drucken("Du bist jetzt unbesiegbar, aber deine Menschlichkeit beginnt zu schwinden.")
    verzögertes_drucken("Mit deiner neuen Kraft stellst du dich den Mutanten, die das Land bedrohen.")
    verzögertes_drucken("In einer epischen Schlacht besiegst du sie alle und wirst der neue Herrscher über die Ruinen.")
    verzögertes_drucken("Herzlichen Glückwunsch, du hast das Spiel gewonnen!")
    verzögertes_drucken("Du HAST GEWONNEN! Spiel beendet!")

    # Möglichkeit, das Spiel erneut zu spielen
    nochmal_spielen()

# Funktion, um den Bunker zu verlassen
def bunker_verlassen():
    """
    Funktion, um den Bunker zu verlassen
    """
    verzögertes_drucken("Du entscheidest dich, das Serum nicht zu nehmen und verlässt den Bunker.")
    verzögertes_drucken("Als du zurückkehrst, hörst du, dass andere Überlebende das Serum gefunden haben und es gegen dich einsetzen.")
    verzögertes_drucken("Leider bedeutet deine Entscheidung, das Serum nicht zu nehmen, dass du den Mutanten und anderen Überlebenden unterlegen bist.")
    verzögertes_drucken("Du HAST VERLOREN! Spiel beendet!")
    
    # Möglichkeit, das Spiel erneut zu spielen
    nochmal_spielen()

# Funktion, um den Rat eines Überlebenden zu suchen
def rat_suchen():
    """
    Funktion, um den Rat eines Überlebenden zu suchen
    """
    verzögertes_drucken("Du suchst den Rat eines alten Überlebenden, der das Ende der Welt miterlebt hat.")
    verzögertes_drucken("Er warnt dich vor dem Serum und erzählt dir von seinen gefährlichen Nebenwirkungen.")
    verzögertes_drucken("Was möchtest du jetzt tun?")
    verzögertes_drucken("1. Folge dem Rat des Überlebenden und gehe nicht zum Bunker.")
    verzögertes_drucken("2. Ignoriere seinen Rat und gehe trotzdem zum Bunker, um das Serum zu holen.")

    spieler_wahl = input("Gib 1 oder 2 ein: ")

    if spieler_wahl == "1":
        rat_befolgen()
    elif spieler_wahl == "2":
        bunker_finden()
    else:
        verzögertes_drucken("Entschuldigung, das habe ich nicht verstanden. Bitte gib 1 oder 2 ein.")
        rat_suchen()

# Funktion, um dem Rat des Überlebenden zu folgen
def rat_befolgen():
    """
    Funktion, um dem Rat des Überlebenden zu folgen
    """
    verzögertes_drucken("Du entscheidest dich, dem Rat des Überlebenden zu folgen und das Serum nicht zu suchen.")
    
    # Zufällige Entscheidung über das Spielergebnis
    if random.choice([True, False]):
        verzögertes_drucken("Du HAST GEWONNEN, weil du den Mutanten entkommen und ein friedliches Leben gefunden hast!")
        verzögertes_drucken("Spiel beendet!")
    else:
        verzögertes_drucken("Leider haben die Mutanten das Gebiet überrannt und alles zerstört!")
        verzögertes_drucken("Du HAST VERLOREN! Spiel beendet!")
    
    # Möglichkeit, das Spiel erneut zu spielen
    nochmal_spielen()

# Funktion, um erneut zu spielen
def nochmal_spielen():
    """
    Funktion, um den Benutzer zu fragen, ob er erneut spielen möchte
    """
    verzögertes_drucken("Möchtest du nochmal spielen? (ja/nein)")

    spieler_wahl = input().lower()

    if spieler_wahl == "ja":
        # Das Spiel wird neu gestartet
        spiel_starten()
    elif spieler_wahl == "nein":
        # Das Spiel endet
        verzögertes_drucken("Okay, danke fürs Spielen!")
    else:
        verzögertes_drucken("Entschuldigung, das habe ich nicht verstanden. Bitte gib 'ja' oder 'nein' ein.")
        nochmal_spielen()

# Das Spiel startet hier
spiel_starten()
