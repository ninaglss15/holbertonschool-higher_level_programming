#!/usr/bin/python3
"""
Module rectangle
Ce module définit une classe Rectangle avec largeur et hauteur,
en utilisant des propriétés pour l'encapsulation et la validation.
"""


class Rectangle:
    """
    Classe Rectangle qui définit un rectangle par sa largeur et sa hauteur.

    Attributs privés :
        __width (int) : largeur du rectangle (>= 0)
        __height (int) : hauteur du rectangle (>= 0)

    Propriétés :
        width : récupère ou définit la largeur avec validation
        height : récupère ou définit la hauteur avec validation
    """

    def __init__(self, width=0, height=0):
        """
        Initialise un nouveau rectangle avec une largeur et une hauteur.

        Args:
            width (int): largeur du rectangle (défaut 0)
            height (int): hauteur du rectangle (défaut 0)

        Raises:
            TypeError: si width ou height n'est pas un entier
            ValueError: si width ou height est négatif
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Getter de la largeur du rectangle.

        Returns:
            int: la largeur du rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter de la largeur du rectangle, avec validation.

        Args:
            value (int): nouvelle valeur de la largeur

        Raises:
            TypeError: si value n'est pas un entier
            ValueError: si value est négatif
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter de la hauteur du rectangle.

        Returns:
            int: la hauteur du rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter de la hauteur du rectangle, avec validation.

        Args:
            value (int): nouvelle valeur de la hauteur

        Raises:
            TypeError: si value n'est pas un entier
            ValueError: si value est négatif
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
