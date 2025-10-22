-- Affiche une seule colonne :
    --name : nom du genre
-- Résultats triés par ordre alphabétique du nom
-- Utilise un seul SELECT
-- La requête relie tv_shows et tv_show_genres pour récupérer l'id de la série, puis récupère les genres associés

SELECT 
    genres.name
FROM 
    tv_shows
JOIN 
    tv_show_genres
ON 
    tv_shows.id = tv_show_genres.show_id
JOIN
    genres
ON
    tv_show_genres.genre_id = genres.id
WHERE 
    tv_shows.title = 'Dexter'
ORDER BY 
    genres.name ASC;