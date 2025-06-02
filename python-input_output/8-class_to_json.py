#!/usr/bin/python3

def class_to_json(obj):
    """
    Retourne le dictionnaire des attributs simples de l'objet `obj`
    """
    # récupérer les attributs de l'objet sous forme de dictionnaire
    # attention à inclure aussi les attributs de classe si besoin

    # exemple : utiliser obj.__dict__ pour obtenir les attributs d'instance
    obj_dict = obj.__dict__

    # si tu veux inclure les attributs de classe, pense à utiliser vars(type(obj)) ou dir(obj)

    # retourner un dictionnaire filtré avec uniquement les types simples (list, dict, str, int, bool)
    # ici tu peux juste retourner obj_dict pour commencer

    return obj_dict
