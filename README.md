# intelligente Ressourcenplanung
Die Räumlichkeiten der FH Technikum Wien sollen für den Semesterbetrieb automatisiert belegt werden, sodass Überschneidungen ausgeschlossen und für Beteiligte besonders ungünstige Zuteilungen bestmöglichst ausgeschlossen werden können. Methoden aus dem Bereich der künstlichen Intelligenz wie die constraint-basierte Programmierung sollen hierfür zum Einsatz kommen.
## Prinzip
Es soll eine Lösung für die Zuordnung beschränkter Ressourcen in einem vorgegebenen System gefunden werden. Das hierfür gewählte Szenario ist ein Hochschulstandort mit mehreren Räumlichkeiten, welchen für den Semesterbetrieb unterschiedliche Lehrveranstaltungen verschiedener Jahrgänge bzw. Studiengänge zugeteilt werden.
## grundlegende Bedingungen
Räume
* haben beschränkte Kapazitäten

Studierende
* haben als Jahrgang einen vorgegebenen Katalog an Lehrveranstaltungen zu besuchen
* können diese Lehrveranstaltungen als Gruppenverband oder Kleingruppe besuchen

Lehrpersonal
* kann nur Lehrveranstaltungen halten, für welche es qualifiziert ist

Lehrveranstaltungen
* werden entsprechend ihrem Typus in Gruppenverbänden oder Kleingruppen abgehalten

Zudem ist eine zeitgleiche Zuteilung von Räumen, Lehrpersonal oder Studierenden zu mehreren Lehrveranstaltungen nicht zulässig.
## erweiterte Bedingungen
Räume
* haben unterschiedliche Ausstattung (EDV-Saal)

Studierende
* wollen "kompakte" Wochenpläne

Lehrpersonal
* darf ein gewisses Lehrkontingent nicht über- oder unterschreiten
