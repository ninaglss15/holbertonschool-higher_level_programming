-- Crée la base hbtn_0d_usa si elle n'existe pas déjà
-- Crée la table cities si elle n'existe pas déjà
-- Colonnes de la table cities :
    --id       : entier (INT), clé primaire, non nul, auto-incrémenté
    --state_id : entier (INT), non nul, clé étrangère référant à states.id
    --name     : texte (VARCHAR(256)), ne peut pas être NULL
-- La clé étrangère garantit que chaque ville appartient à un état existant
-- La table est idempotente, donc le script peut être exécuté plusieurs fois sans erreur

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE if NOT EXISTS hbtn_0d_usa.cities (
	id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	state_id INT NOT NULL,
	FOREIGN KEY (state_id) REFERENCES states(id),
	name VARCHAR(256) NOT NULL
);