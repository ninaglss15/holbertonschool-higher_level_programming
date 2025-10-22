-- Affiche une seule colonne :
    --name : nom du genre
-- Résultats triés par ordre alphabétique du nom
-- Utilise un seul SELECT
-- La requête relie tv_shows et tv_show_genres pour récupérer l'id de la série, puis récupère les genres associés

SELECT tv_genres.name
FROM tv_genres INNER JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
INNER JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
WHERE tv_shows.title = 'Dexter'
ORDER BY tv_genres.name;