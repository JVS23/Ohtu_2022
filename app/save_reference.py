from flask import session
from app.app import db


def save_book_fields(author, book_name, year, publisher, id):

    fields = {"author": author, "book_name": book_name, "year": year, "publisher": publisher}

    try:
        for key in fields.keys():
                sql = """INSERT INTO fields (name, content, reference_entry)
                VALUES (:name, :content, :id)"""
                db.session.execute(sql, {"name": key, "content": fields[key], "id": id})
    except:
        return False

    return True


def save(type, author=None, book_name=None, year=None, publisher=None):

    try:

        name = f"{author}, {year}"

        sql = """INSERT INTO reference_entries (name, type, created_at)
             VALUES (:name, :type, NOW()) RETURNING id"""
        id = db.session.execute(sql, {"name": name, "type": type}).fetchone()[0]

        if type == "book":
            if not save_book_fields(author, book_name, year, publisher, id):
                raise

        db.session.commit()

    except:
        return False

    return True