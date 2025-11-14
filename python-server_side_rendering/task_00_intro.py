#!/usr/bin/python3
"""
Task 0: Creating a Simple Templating Program
"""

def generate_invitations(template, attendees):
    # Vérification des types
    if not isinstance(template, str):
        print(f"Invalid input type: template must be a string, got {type(template).__name__}")
        return

    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        invalid_type = type(attendees).__name__
        print(f"Invalid input type: attendees must be a list of dictionaries, got {invalid_type}")
        return

    # Vérification des entrées vides
    if not template.strip():
        print("Template is empty, no output files generated.")
        return

    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    # Liste des placeholders attendus
    placeholders = ["name", "event_title", "event_date", "event_location"]

    # Création des fichiers d'invitation
    for idx, attendee in enumerate(attendees, start=1):
        content = template
        for key in placeholders:
            value = attendee.get(key)
            if value is None:
                value = "N/A"
            content = content.replace(f"{{{key}}}", str(value))
        
        output_file = f"output_{idx}.txt"
        try:
            with open(output_file, 'w') as f:
                f.write(content)
            print(f"Generated invitation for {attendee.get('name', 'N/A')} in {output_file}")
        except Exception as e:
            print(f"Error writing file {output_file}: {e}")
