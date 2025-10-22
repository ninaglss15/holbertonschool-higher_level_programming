-- Crée l'utilisateur 'user_0d_1'@'localhost' s'il n'existe pas déjà
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- Donne tous les privilèges sur toutes les bases et tables
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';