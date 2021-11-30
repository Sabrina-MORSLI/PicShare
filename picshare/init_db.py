import sqlite3

DATABASE = 'app.db'
db = sqlite3.connect(DATABASE)

cursor = db.cursor()

# Creation of table "categories". If it existed already,
# we delete the table and create a new one
cursor.execute('drop table if exists categories')
cursor.execute("""CREATE table categories (
                id integer primary key AUTOINCREMENT,
                name varchar(200) not null)""")

# We seed the table with initial values.
# Here we insert 6 categories:
# "Animaux", "Citations", "Décorations", "Nature", "Paysages", "Sculptures"
for name in ["Animaux", "Citations", "Decorations",
             "Nature", "Paysages", "Sculptures"]:
    cursor.execute("INSERT INTO categories (name) VALUES (?)", (name,))

# Creation of table "pictures". If it existed already,
# we delete the table and create a new one
cursor.execute("drop table if exists pictures")
cursor.execute("""CREATE table pictures (
                id integer primary key AUTOINCREMENT, \
                title varchar(255) not null, \
                filename varchar(255) not null, \
                upload_date date not null, \
                category_id integer not null, \
                description varchar(255), \
                constraint fk_categories \
                foreign key (category_id) \
                references categories(id))""")

# We seed the table with initial values.
# Here 15 pictures inserted into the table "pictures"
for data in [("Paris Burg'heure Citation d'Henry Ford",
              "2021-520-Paris-idiom-1.jpeg", "2021-05-20 18:02", 2,
              "L'échec est seulement l'opportunité de recommencer de façon plus intelligente."),
             ("Paris Burg'heure Citation d'Albert Einstein",
              "2021-520-Paris-idiom-2.jpeg", "2021-05-20 18:03", 2,
              "La vie c'est comme une bicyclette, il faut avancer pour ne pas perdre l'équilibre."),
             ("Saint-Malo Le Sillon Paysage 21-05-2021",
              "2021-521-St-Malo-landscape.jpeg", "2021-05-21 21:21", 5,
              "Vendredi 21 mai 2021 à 21h21, on était le 21ème jour du mois, dans la 21ème année, du 21ème siècle."),
             ("Saint-Malo Street-art Selor 23-05-2021",
              "2021-523-St-Malo-idiom-1.jpeg", "2021-05-23 18:00", 2,
              "Plus on cherche de réponses, plus il y a de questions."),
             ("Saint-Malo Street-art @LaDactylo 23-05-2021",
              "2021-523-St-Malo-idiom-2.jpeg", "2021-05-23 18:01", 2,
              "Le passé est pansé, le présent est à venir, l'avenir est à penser."),
             ("Sunset", "sunset.jpg",
              "2021-06-21 10:39", 4,
              "Couché de soleil vu à travers un arbre"),
             ("Salon moderne minimaliste",
              "salon_minimaliste.jpg", "2021-06-21 10:40", 3,
              "Photo d'un salon avec une vue sur mer et une décoration moderne et minimaliste"),
             ("Chambre simple et minimaliste",
              "bedroom.jpg", "2021-06-21 10:41", 3,
              "Belle et simple chambre avec une décoration minimaliste et épurée pour un repos garanti"),
             ("Espace bureau",
              "home_office.jpg", "2021-06-21 10:42", 3,
              "Espace bureau épuré avec une Magnifique vue, productivité et créativité au rdv ..."),
             ("Sunrise", "sunrise.jpg",
              "2021-06-21 10:43", 4, "Photo d'un beau levé de soleil"),
             ("Le cousin d'Hamtaro",
              "hamster-fraises.jpeg", "2021-06-21 10:44", 1, "Une fraise pour le goûter"),
             ("Jackie-the-sheep",
              "mouton-en-Irlande.jpeg", "2021-06-21 10:45", 1, "Meet Jackie, the irish sheep !"),
             ("Pluton enlevant Proserpine",
              "pluton-enlevant-proserpine.jpeg", "2021-06-21 10:46", 6,
              "Sculpture en bronze fabriquée/créée par François Girardon entre 1700 et 1800. (Sculpture mythologique)."),
             ("Diane de Versailles",
              "diane-de-versailles.jpeg", "2021-06-21 10:47", 6,
              "Statue en marbre fabriquée/créée par Léocharès, au 2e quart IIe s. ap. J.-C."),
             ("L'Amour et Psyché à demi couchée",
              "lamour-et-psyche-a-demi-couchee.jpeg",
              "2021-06-21 10:48", 6,
              "Statue en marbre fabriquée/créée par Antonio Canova, entre 1787 et 1793 (sculpture mythologique).")
             ]:
    cursor.execute("INSERT into pictures \
            (title, filename, upload_date, category_id, description) \
            values (?, ?, ?, ?, ?)", data)

# Creation of table "comments". If it existed already,
# we delete the table and create a new one
    cursor.execute('drop table if exists comments')
    cursor.execute("""CREATE table comments (
                id integer primary key AUTOINCREMENT,
                comment varchar(255) not null,
                comment_date date not null,
                picture_id integer not null,
                constraint fk_pictures
                foreign key (picture_id)
                references pictures(id))""")


# We save our changes into the database file
db.commit()

# We close the connection to the database
db.close()
