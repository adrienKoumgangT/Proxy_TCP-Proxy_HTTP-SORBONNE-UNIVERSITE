# progres - Mini-Projet 1

## Exercice 1 - Proxy TCP

On cherche à programmer en Python un mécanisme de proxy entre un client et un serveur normalement connectés via TCP.
Un proxy est un programme qui agit comme un serveur vis à vis du client, et comme un client vis à vis du serveur.
Il retransmet au serveur toutes les données que le client auraient normalement transmises au serveur,
et il retransmets au client toutes les données que le serveur auraient normalement transmises au client.


1. A partir des exemples de code vus en cours pour le client TCP et le serveur TCP, programmer le mécanisme de
proxy en Python; On considèrera que l'adresse IP et le numéro de port du serveur sont fournies au proxy.
2. Tester le proxy avec des programmes clients et serveurs utilisant TCP, sur la meme machine et sur des machines
différentes; s'assurer que tout fonctionne correctement.
3. Tester le proxy avec plusieurs clients (ou plusieurs instances du meme client) qui effectuent des requetes simultanées
sur le serveur (via le proxy); s'assurer que tout fonctionne correctement.


## Exercice 2 - Proxy HTTP

On cherche à programmer en Python un proxy dédié au protocole HTTP.
On considère donc que tous les échanges entre le client et le serveur (via le proxy) utilisent le protocole HTTP.
Le client est donc typiquement un navigateur web, et le serveur est donc typiquement un serveur web.

1. Modifier le proxy TCP dévéloppé pour l'exercice 1 pour qu'il fasse office de loggeur HTTP :
la première fois qu'une URI est fournie en argument de GET dans une requete HTTP,
le proxy retransmets la requete au serveur, et stocke localement sa réponse dans un fichier;
si la meme URI lui est demandée par la suite par le meme client ou un autre client,
il envoie directement au client le fichier qu'il a stocké localement sans faire de nouvelle requetes au serveur.
2. Modifier le proxy TCP développé pour l'exercice 1 pour qu'il fasse office de loggeur HTTP.
Plus précisément, toutes les requetes GET du client sont archivées dans un fichier de log,
toutes les réponses du serveur aux requetes GET sont archivées dans le fichier de log.
Le fichier de log doit contenir suffisament d'information pour effectuer les audits:
étant donnée une URI (ou une partie d'une URI), on veut pouvoir retrouver les adresses IP 
des clients qui ont obtenu une réponse non vide d'un serveur concernant cette URI.
3. Modifier le proxy TCP pour qu'il fasse office de censeur HTTP.
Le proxy dispose maintenant d'une liste de sites interdits (fournie en entrée au proxy).
Si l'URI demandée dans une requete GET du client contient un lien qui renvoie vers un site interdit,
ce lien est remplacée par un message << Interdit >> dans le corps de la réponse.
4. Tester les proxy HTTP réalisés, d'abord individuellement (un proxy entre un client et un serveur),
puis en les enchainant (par exemple, un client est connecté à un cache HTTP qui est connecté à un loggeur HTTP,
qui lui meme est connecté au serveur).
