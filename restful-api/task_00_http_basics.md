# HTTP & HTTPS

## 1 : Différences entre HTTP et HTTPS

La différence principale entre HTTP et HTTPS réside dans la sécurité.

### HTTP (Hypertext Transfer Protocol)  
HTTP est un ensemble de règles régissant le transfert de fichiers (texte, images, son, vidéo, etc.) sur le Web. Lorsqu'un utilisateur ouvre un navigateur et se connecte au Web, il utilise indirectement le protocole HTTP. C'est un protocole d'application qui s'exécute au-dessus de la suite de protocoles TCP/IP.

### HTTPS (Hyper Text Transfer Protocol Secure)  
HTTPS est une extension sécurisée de HTTP. Le « S » signifie « Secure » (sécurisé), ce qui indique que les données échangées entre le navigateur et le site web sont chiffrées et protégées contre l'espionnage ou la modification.  
Pour activer HTTPS, il faut acquérir et installer un certificat SSL/TLS auprès d’une Autorité de Certification reconnue.  

#### Niveaux d’authentification des certificats HTTPS :  
- **Domain Validation (DV)** : Authentification faible  
- **Organization Validation (OV)** : Authentification forte  
- **Extended Validation (EV)** : Authentification renforcée  

---

## 2 : Structure d'une demande et d'une réponse HTTP

### Exemple de requête HTTP GET  
```plaintext
GET /index.html HTTP/1.1  
Host: www.exemple.com  
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36  
Accept: text/html,application/xhtml+xml,application/xml  
Accept-Language: en-US  
Connection: keep-alive

Explications des éléments clés :

-   **GET** : Méthode HTTP utilisée (ici, GET pour récupérer des données).
-   **/index.html** : Chemin de la ressource demandée.
-   **HTTP/1.1** : Version du protocole HTTP utilisée.
-   **Host** : Nom de domaine du serveur cible.
-   **User-Agent** : Informations sur le navigateur ou l'application utilisée.
-   **Accept** : Types de contenus acceptés par le client.
-   **Connection** : Indique si la connexion doit être maintenue ouverte.
```

### Exemple de réponse HTTP:
```plaintext
-HTTP/1.1 200 OK  
-Date: Mon, 18 Feb 2025 12:34:56 GMT  
-Server: Apache/2.4.41 (Ubuntu)  
-Content-Type: text/html; charset=UTF-8  
-Content-Length: 1234  

-<!DOCTYPE html>
-<html lang="en">
-<head>
-    <title>Exemple</title>
-</head>
-<body>
 -   <h1>Bienvenue sur notre site web</h1>
-</body>
-</html>

Explications des éléments clés :

-   **HTTP/1.1 200 OK** : Code de statut et message indiquant que la requête a été traitée avec succès.
-   **Date** : Date et heure de la réponse.
-   **Server** : Informations sur le serveur web utilisé.
-   **Content-Type** : Type de contenu renvoyé (ici, HTML avec encodage UTF-8).
-   **Content-Length** : Longueur du contenu renvoyé en octets.
-   **Corps de la réponse** : Contient la ressource demandée (ici, une page HTML).
```
## 3 : Liste des méthodes HTTP courantes
-   **GET**
    
    -   **Description** : Récupère des données sans modifier l'état du serveur.
    -   **Cas d'utilisation** : Récupération d'une page Web ou de données depuis une API.
-   **POST**
    
    -   **Description** : Envoie des données au serveur pour traitement.
    -   **Cas d'utilisation** : Soumission d'un formulaire ou enregistrement de nouvelles données.
-   **PUT**
    
    -   **Description** : Remplace une ressource existante ou la crée si elle n'existe pas.
    -   **Cas d'utilisation** : Mise à jour d'un profil utilisateur.
-   **PATCH**
    
    -   **Description** : Apporte des modifications partielles à une ressource.
    -   **Cas d'utilisation** : Modification d'un champ spécifique, comme l'adresse.
-   **DELETE**
    
    -   **Description** : Supprime une ressource sur le serveur.
    -   **Cas d'utilisation** : Suppression d'un compte.
-   **HEAD**
    
    -   **Description** : Identique à GET, mais sans le corps de la réponse.
    -   **Cas d'utilisation** : Vérification de l'existence d'une ressource.
-   **OPTIONS**
    
    -   **Description** : Récupère les méthodes HTTP autorisées pour une ressource.
    -   **Cas d'utilisation** : Vérification des méthodes disponibles
