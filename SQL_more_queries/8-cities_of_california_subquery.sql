-- Affiche les colonnes id et name de la table cities
-- Ne pas utiliser JOIN
-- Utilise une sous-requête pour récupérer l'id de California depuis la table states
-- Trie les résultats par id en ordre croissant

SELECT cities.id, cities.name
FROM states, cities
WHERE states.id = cities.state_id AND states.name = 'California'
ORDER BY cities.id;