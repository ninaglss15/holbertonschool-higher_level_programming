#!/usr/bin/python3

import logging

def generate_invitations(template: str, attendees: list) -> None:
    """
    Génère des fichiers d'invitation personnalisés à partir d'un template et d'une liste de participants.
    Gère les erreurs de type, les entrées vides et les données manquantes.
    """
    # Vérification des types d'entrée
    if not isinstance(template, str):
        logging.error("Erreur: Le template doit être une chaîne de caractères")
        return
    
    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        logging.error("Erreur: Les participants doivent être une liste de dictionnaires")
        return

    # Gestion des entrées vides
    if not template.strip():
        logging.error("Template vide - aucun fichier généré")
        return
    
    if not attendees:
        logging.error("Liste de participants vide - aucun fichier généré")
        return

    # Génération des invitations
    for i, attendee in enumerate(attendees, 1):
        invitation = template
        
        # Remplacement des variables avec gestion des valeurs manquantes
        for key in ['name', 'event_title', 'event_date', 'event_location']:
            value = attendee.get(key, "N/A") or "N/A"  # Gère None et clés absentes
            invitation = invitation.replace(f'{{{key}}}', str(value))
        
        # Écriture sécurisée du fichier
        filename = f'output_{i}.txt'
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(invitation)
        except IOError as e:
            logging.error(f"Erreur d'écriture pour {filename}: {str(e)}")

# Configuration du logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')