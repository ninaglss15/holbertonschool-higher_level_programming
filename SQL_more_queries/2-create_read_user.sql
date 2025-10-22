-- Crée la base de données hbtn_0d_2 si elle n'existe pas déjà
-- Crée l'utilisateur user_0d_2 avec le mot de passe user_0d_2_pwd
-- et ne génère pas d'erreur si l'utilisateur existe déjà
-- Donne uniquement le privilège SELECT (lecture) sur toutes les tables
-- de la base hbtn_0d_2

CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';