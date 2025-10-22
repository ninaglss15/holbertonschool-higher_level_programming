-- Affiche : tv_shows.title, tv_show_genres.genre_id
-- Inclut uniquement les séries qui n’ont aucun genre associé (genre_id = NULL)
-- Résultats triés par tv_shows.title puis tv_show_genres.genre_id
-- Utilise un seul SELECT
-- La requête utilise LEFT JOIN pour inclure toutes les séries et un filtre WHERE pour sélectionner celles sans genre

SELECT 
    tv_shows.title,
    tv_show_genres.genre_id
FROM 
    tv_shows
LEFT JOIN 
    tv_show_genres
ON 
    tv_shows.id = tv_show_genres.show_id
WHERE
    tv_show_genres.genre_id IS NULL
ORDER BY 
    tv_shows.title ASC,
    tv_show_genres.genre_id ASC;