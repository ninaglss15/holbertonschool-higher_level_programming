#!/usr/bin/env python3
from typing import Any, Iterable

class VerboseList(list):
    """
    Liste qui affiche un message à chaque modification importante :
    ajout (append, extend) ou suppression (remove, pop).
    """


    def append(self, item: Any) -> None:
        """Ajoute un élément et affiche un message."""
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable: Iterable[Any]) -> None:
        """Étend la liste avec plusieurs éléments et affiche un message."""
        count = len(list(iterable))
        super().extend(iterable)
        print(f"Extended the list with [{count}] items.")

    def remove(self, item: Any) -> None:
        """Supprime un élément et affiche un message avant la suppression."""
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index: int = -1) -> Any:
        """
        Supprime et retourne un élément (par défaut le dernier),
        affiche un message avant la suppression.
        """
        item = self[index]
        print(f"Popped [{item}] from the list.")
        return super().pop(index)
