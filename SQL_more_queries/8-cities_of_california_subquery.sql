-- Affiche les colonnes id et name de la table cities
-- Ne pas utiliser JOIN
-- Utilise une sous-requête pour récupérer l'id de California depuis la table states
-- Trie les résultats par id en ordre croissant

SELECT id, name
FROM cities
WHERE state_id = (SELECT id FROM states WHERE name = 'California')
ORDER BY id ASC;