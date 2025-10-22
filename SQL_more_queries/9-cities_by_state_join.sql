-- Affiche les colonnes suivantes :
    --cities.id   : identifiant unique de la ville
    --cities.name : nom de la ville
    --states.name : nom de l'état auquel la ville appartient
-- Relie la table cities à la table states via une jointure (cities.state_id = states.id)
-- Résultats triés par cities.id en ordre croissant
-- Utilise un seul SELECT
-- La requête est idempotente et fonctionnera quelle que soit la base hbtn_0d_usa

SELECT id, name
FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;