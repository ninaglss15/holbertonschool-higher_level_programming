-- Crée la table id_not_null si elle n'existe pas déjà
-- Colonnes :
    -- id   : entier (INT), valeur par défaut 1
    -- name : texte (VARCHAR(256)), peut être NULL
-- La base de données sera passée en argument lors de l'exécution
-- Si aucune valeur pour id n'est fournie lors de l'insertion, elle prendra la valeur 1

CREATE TABLE IF NOT EXISTS id_not_null (
    id INT DEFAULT 1,
    name VARCHAR(256)
)