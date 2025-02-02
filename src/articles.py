from app import db

def add_new_article(title, author, doi, url, owner, tag=[]):
    sql = "INSERT INTO article (title, author, doi, url, tag, created_at, owner) VALUES (:title, :author, :doi, :url, :tag, NOW(), :owner)"
    db.session.execute(sql, {"title":title, "author":author, "doi":doi, "url":url, "tag":tag, "owner":owner})
    db.session.commit()
    return True

def get_all():
    sql = "SELECT * FROM article WHERE visible=1"
    result = db.session.execute(sql)
    articles = result.fetchall()
    return articles
    
def get_by_user(owner):
    sql = "SELECT * FROM article WHERE visible=1 AND owner = :owner"
    result = db.session.execute(sql, {"owner":owner})
    articles = result.fetchall()
    return articles

def get_one(id):
    sql = "SELECT * FROM article WHERE id=:id"
    result = db.session.execute(sql, {"id":id})
    article = result.fetchone()
    return article

def hide(item_id):
    sql = "UPDATE article SET visible = 0 WHERE id=:item_id"
    db.session.execute(sql, {"item_id":item_id})
    db.session.commit()
    return True
