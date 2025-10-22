-- Crée la table force_name si elle n'existe pas déjà
-- Colonnes :
    -- id   : entier (INT)
    -- name : texte (VARCHAR(256)), ne peut pas être NULL
-- La base de données sera passée en argument lors de l'exécution

CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL
)