-- Crée la table unique_id si elle n'existe pas déjà
-- Colonnes :
   -- id   : entier (INT), valeur par défaut 1, doit être unique
    -- name : texte (VARCHAR(256)), peut être NULL
-- La base de données sera passée en argument lors de l'exécution
-- Si on tente d'insérer un id déjà présent, MySQL renverra une erreur

CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
)