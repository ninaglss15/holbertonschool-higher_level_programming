-- Affiche deux colonnes :
    --genre             : nom du genre
    --number_of_shows   : nombre de séries liées à ce genre
-- N’affiche que les genres qui ont au moins une série associée
-- Résultats triés par nombre de séries décroissant
-- Utilise un seul SELECT
-- La requête relie genres et tv_show_genres, puis compte le nombre de séries

SELECT tv_genres.name AS genre, COUNT(*) AS number_of_shows
FROM tv_genres INNER JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
GROUP BY tv_show_genres.genre_id
ORDER BY COUNT(tv_show_genres.genre_id) DESC;