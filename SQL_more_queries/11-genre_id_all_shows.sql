-- Affiche : tv_shows.title, tv_show_genres.genre_id
-- Si une série n’a pas de genre, afficher NULL
-- Résultats triés par tv_shows.title puis tv_show_genres.genre_id
-- Utilise un seul SELECT
-- La requête utilise LEFT JOIN pour inclure les séries sans genre

SELECT 
    tv_shows.title,
    tv_show_genres.genre_id
FROM 
    tv_shows
LEFT JOIN 
    tv_show_genres
ON 
    tv_shows.id = tv_show_genres.show_id
ORDER BY 
    tv_shows.title ASC,
    tv_show_genres.genre_id ASC;