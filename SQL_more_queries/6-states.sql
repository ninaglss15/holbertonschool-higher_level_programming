-- Crée la base hbtn_0d_usa si elle n'existe pas déjà
-- Crée la table states si elle n'existe pas déjà
-- Colonnes de la table states :
    --id   : entier (INT), clé primaire, non nul, auto-incrémenté
    --name : texte (VARCHAR(256)), ne peut pas être NULL
-- La table est conçue pour que l'id s’incrémente automatiquement à chaque nouvelle ligne
-- La base et la table sont idempotentes, donc le script peut être exécuté plusieurs fois sans erreur

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

USE hbtn_0d_usa;

CREATE TABLE IF NOT EXISTS states (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);