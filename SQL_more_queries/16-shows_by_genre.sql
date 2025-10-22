-- Affiche deux colonnes :
   -- title : nom de la série
   -- name  : nom du genre (NULL si pas de genre)
-- Inclut toutes les séries même si elles n’ont aucun genre
-- Résultats triés par ordre alphabétique du titre puis du nom du genre
-- Utilise un seul SELECT
-- La requête utilise LEFT JOIN pour inclure les séries sans genre

SELECT tv_shows.title AS title, tv_genres.name AS name
FROM tv_shows LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
ORDER BY tv_shows.title, tv_genres.name;