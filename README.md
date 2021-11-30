#################
Date : 2021-6-22
Projet : Picshare
Groupe : SaLeeMas
#################
INIT FROM SCRATCH
#################
Dossier Git-lab :
git clone https://gitlab.matrice.io/picshare/sbelalo-picshare

Commandes à lancer (>>>) à la première installation, avec le
Résultat attendu (>) :
>>> cd sbelalo-picshare/picshare
>>> mkdir database
>>> python3 init_db.py
>>> cd database
>>> ls
> app.db

############
REQUIREMENTS
############
Prérequis à installer avant la première utilisation :
#####################
Environnement Virtuel
#####################
Dans le répertoire : sbelalo-picshare
(
>>> cd ../..
>>> pwd
> /sbelalo-picshare
)
Installation de virtualenv :
>>> pip3 install virtualenv
Création de l'environnement virtuel env :
>>> virtualenv -p python3 virt-env
Activation de virt-env :
>>> source virt-env/bin/activate
(virt-env) sbelalo-picshare

(désactivation de virt-env :
>>> deactivate
> sbelalo-picshare)

#####
Flask
#####
Dans le répertoire : sbelalo-picshare
(
>>> cd picshare
>>> pwd
> /sbelalo-picshare/picshare
)
>>> pip3 install -r requirements.txt Flask
>>> export FLASK_APP=app.py
>>> export FLASK_ENV=development
################
requirements.txt
################
Dans le répertoire : sbelalo-picshare
>>> pip3 install -r requirements.txt
>>> pip3 freeze > requirements.txt
>>> tail -f requirements.txt
> click==8.0.1
> Flask==2.0.1
> itsdangerous==2.0.1
> Jinja2==3.0.1
> MarkupSafe==2.0.1
> Werkzeug==2.0.1
>>> <CTL+C>
> picshare 

Commande pour lancer l'application :
python3 run.py

URL de test de l'application :
http://127.0.0.1:5000/

#######
Git-Lab
#######
Fichier pour ignorer les fichiers de virt-env à ne pas ajouter dans le Git :
>>> touch sbelalo-picshare/picshare/.gitignore
>>> subl sbelalo-picshare/picshare/.gtiignore
# liste des fichiers à ignorer pour Git
virt-env/
picshare/database


######################
Organisation du projet
######################
Dossier gestion de projet : sbelalo-picshare/trello
Dossier de livrables : sbelalo-picshare/delivery
####################
Architecture du site
####################
Dossier racine : sbelalo-picshare
Fichier README de description de l'architecture du site : sbelalo-picshare/README.md
Dossier du site : sbelalo-picshare/picshare
Dossier static :  sbelalo-picshare/picshare/static
Un dossier CSS : sbelalo-picshare/picshare/static/css
Un dossier IMAGES : sbelalo-picshare/picshare/static/images
(pas celle qu’on rajoute dans le site)
Un dossier JS : sbelalo-picshare/picshare/static/js
Dossier templates : sbelalo-picshare/picshare/templates
Fichiers HTML :
sbelalo-picshare/picshare/templates/layout.html
sbelalo-picshare/picshare/templates/index.html
sbelalo-picshare/picshare/templates/upload.html
sbelalo-picshare/picshare/templates/picture.html
Dossier uploads : sbelalo-picshare/picshare/uploads
Fichiers UPLOADS : (Comprend toutes les images uploadées par les utilisateurs)
/!\ les noms de fichiers, ne doivent pas contenir d'espace /!\
Fichiers Python : 
sbelalo-picshare/picshare/run.py
sbelalo-picshare/picshare/index.py
sbelalo-picshare/picshare/upload.py
sbelalo-picshare/picshare/picture.py
Fichiers Database : 
sbelalo-picshare/picshare/init_db.py
Un fichier de dépendances aux bibliothèques employées dans le projet : 
sbelalo-picshare/picshare/requirements.txt
#####################
Environnement Virtuel
#####################
TeKa:
Installation de virtualenv :
>>> pip3 install virtualenv
Création de l'environnement virtuel env :
>>> virtualenv -p python3 virt-env
Activation de virt-env :
>>> source virt-env/bin/activate
désactivation de virt-env :
>>> deactivate
fichier pour ignorer les fichiers de virt-env à ne pas ajouter dans le Git :
>>> touch sbelalo-picshare/picshare/.gitignore
>>> subl sbelalo-picshare/picshare/.gtiignore
# liste des fichiers à ignorer pour Git
virt-env/
picshare/database
#####
Flask / sbelalo-picshare/picshare/
#####
>>> pip3 install -r requirements.txt Flask
>>> export FLASK_APP=app.py
>>> export FLASK_ENV=development
################
requirements.txt
################
>>> pip3 install -r requirements.txt
>>> pip3 freeze > requirements.txt

