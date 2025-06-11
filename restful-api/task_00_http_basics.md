# 🌐 Comprendre HTTP et HTTPS

## 🎯 Objectif du projet

Ce projet a pour but de comprendre le fonctionnement du protocole HTTP, de différencier HTTP de HTTPS, d’analyser les structures de requêtes/réponses HTTP, de reconnaître les méthodes courantes et d’interpréter les codes de statut.  
À la fin, l’étudiant(e) saura :

- Faire la différence entre HTTP et HTTPS, notamment sur les aspects de sécurité.
- Lire et comprendre une requête et une réponse HTTP.
- Identifier les méthodes HTTP les plus utilisées.
- Reconnaître les principaux codes de statut HTTP et leur signification.

---

## 🔐 Différences entre HTTP et HTTPS

| Critère              | HTTP                                | HTTPS                                  |
|----------------------|-------------------------------------|----------------------------------------|
| Sécurité             | Non sécurisé (pas de chiffrement)   | Sécurisé grâce au chiffrement SSL/TLS  |
| Port utilisé         | 80                                  | 443                                    |
| Préfixe dans l’URL   | `http://`                           | `https://`                             |
| Confidentialité      | Aucune : données visibles en clair  | Oui : données chiffrées                |
| Certificat SSL       | Non requis                          | Requis (certificat SSL/TLS)            |
| Exemple d’usage      | Blogs simples, sites publics        | Banques, e-commerce, messageries       |

**⚠️ Remarque :**  
Les sites utilisant HTTPS protègent vos données contre les pirates, ce qui est crucial pour tout échange d'informations sensibles (mots de passe, cartes bancaires…).

---

