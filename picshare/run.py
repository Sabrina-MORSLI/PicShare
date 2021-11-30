from flask import Flask, g, render_template, request, send_from_directory, url_for
import sqlite3, os, datetime

from werkzeug.utils import redirect, secure_filename

SITENAME = 'SaLeeMas - PicShare'
# Définir le dossier dans lequel les photos
# vont petre uploadés
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
app = Flask(__name__)
# Attention, à préciser le répertoire local !
DATABASE = 'app.db'
# On définit une variable globale qui rendra
# nos fichiers accesssibles même via les templates
# récupéré de la doc FLASK
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


# Se connecter à la DB (code récupéré de la doc FLASK)
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

# La fonction pour spécifier les types de fichier autorisés
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# La route de la homepage
@app.route("/", methods=["GET", "POST"])
def show_pictures():
    db = get_db()
    print("All categories")
    if request.method == 'GET':
        categories = db.execute("SELECT name from categories order by id")
        pictures = db.execute("SELECT id, title, filename \
                               from pictures order by upload_date desc")
        # print(pictures.fetchall())
        return render_template("index.html",
                all_pictures=pictures, all_categories=categories)


# La route de la homepage avec la categorie name en argument
@app.route("/<category>", methods=["GET", "POST"])
def show_category_pictures(category):
    db = get_db()
    if request.method == 'GET':
        # print("Chosen category", category)
        categories = db.execute("SELECT name from categories order by id")
        if category:
            print("category", category)

            pictures = db.execute("SELECT pictures.id, title, filename \
                                   from pictures left join categories \
                                   on category_id = categories.id \
                                   where categories.name = (?) \
                                   order by upload_date desc", [category])
            # print(pictures.fetchall())
            return render_template("index.html",
                                    all_pictures=pictures,
                                    all_categories=categories,
                                    chosen_category=category)


# La route du chemin d'accès à l'image à renvoyer, avec 
# le nom du répertoire "uploads/", suivi du nom du fichier image
@app.route('/uploads/<filename>')
def download_file(filename):
    print("send_from_directory",
          send_from_directory(app.config["UPLOAD_FOLDER"], filename))
    return send_from_directory(app.config["UPLOAD_FOLDER"], filename)


# La route de la page upload
@app.route("/upload",  methods=["GET", "POST"])

def upload():
    db = get_db()
    categories_cursor = db.execute("select name from categories order by id;")
    categories_name = categories_cursor.fetchall()
    print("I am the result of your query: ", categories_name)
    list_of_categories = []
    for category in categories_name:
        name = category[0]
        list_of_categories.append(name)
    print("i am the list of cat : ", list_of_categories)
    if request.method == 'POST':
        file = request.files['file']
        print("I am the files.filename : ", file.filename)
        if allowed_file(file.filename):                                      
            filename = secure_filename(file.filename) #  c'est le path
            title = request.form.get("title")
            description = request.form.get("description")
            print(description, " - ", request.form.get("description"))
            category = request.form.get("category")            
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            upload_date = datetime.datetime.now()
            # print("datetime.datetime.now()", datetime.datetime.now())
            # sauvegarder le fichier dans la DB
            db = get_db()
            if category:
                cursor1 = db.execute("SELECT id from categories \
                                where name = ?", [category])
                category_id = cursor1.fetchone()
                # print(category_id[0])
            db.execute("INSERT into pictures (title, filename, upload_date, category_id, description) \
                                      values (?    ,     ?   ,       ?    ,      ?     ,      ?     )",
                        [title, filename, upload_date, int(category_id[0]), description])
            # # vérifier si le titre existe déjà
            # cursor_title = db.execute(
            # "SELECT id, title FROM pictures WHERE title = (?)", [title])
            # print("I'am the cursor: ", cursor_title)
            # # On l'enregistre dans une variable et on l'affiche
            # # avec fetchone, si le résultat n'est pas None on retourne 404
            # title_request = cursor_title.fetchone()
            # print("hey I'm the request title ", title_request)
            # if title_request is not None: abort(404)
            db.commit()
            return render_template("picture_uploaded.html")
    return render_template('upload.html', list_of_categories=list_of_categories)                   


#  La route de la page picture
@app.route("/picture/<picture_id>", methods=["GET", "POST"])
def picture_id(picture_id):
    if picture_id and request.method == 'POST':
        comment = request.form.get("comment")
        # print("I am the comment :", comment)
        comment_date = datetime.datetime.now()
        
        # print("datetime.datetime.now()", comment_date)
        # sauvegarder le fichier dans la DB
        db = get_db()
        db.execute("INSERT into comments (comment, comment_date, picture_id) \
                                  values (?      ,        ?    , ?)",
                    [comment, comment_date, picture_id])
        db.commit()
    if picture_id and request.method == 'GET':
        # print("I am the id of the chosen picture :", picture_id)
        db = get_db()
        pictures = db.execute("SELECT title, filename, upload_date, description, categories.name \
                               from pictures inner join categories \
                               on category_id = categories.id \
                               where pictures.id = (?)", [picture_id])
        # print(pictures)
        comments = db.execute("SELECT comment, comment_date \
                               from comments inner join pictures \
                               on picture_id = pictures.id \
                               where pictures.id = (?) \
                               order by comment_date desc", [picture_id])
        # print(comments)
        return render_template("picture.html",
                                all_pictures=pictures,
                                all_comments=comments)
    # print("not picture_id")
    return redirect("/picture/" + picture_id)


if __name__ == "__main__":
    app.run(debug=True)
