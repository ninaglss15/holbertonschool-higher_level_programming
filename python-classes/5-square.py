#!/usr/bin/python3
"""Module qui définit une classe Square."""


class Square:
    """Classe qui représente un carré."""

    def __init__(self, size=0):
        """Initialise un carré avec une taille optionnelle.
        Args:
            size (int): La taille du côté du carré (doit être un entier >= 0).
        """
        self.size = size  # On passe par le setter, donc on valide déjà ici

    @property
    def size(self):
        """Récupère la taille du carré (getter)."""
        return self.__size

    @size.setter
    def size(self, value):
        """Modifie la taille du carré (setter).
        Args:
            value (int): La nouvelle taille (doit être un entier >= 0).
        Raises:
            TypeError: Si value n'est pas un entier.
            ValueError: Si value est négatif.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calcule et retourne l'aire du carré.
        Returns:
            int: L'aire (size * size).
        """
        return self.__size * self.__size

    def my_print(self):
        """Affiche le carré avec le caractère # dans le terminal.
        Si size vaut 0, affiche une ligne vide.
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
