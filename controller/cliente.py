import services.database as db

def incluir (nome, discricao, link, programa, animador):
    db.cur.execute("""
            INSERT into Personagens (nome, discricao, link, programa, animador) 
            values('%s', '%s', '%s', '%s',, '%s')
    """ % (nome, discricao, link, programa, animador))
    db.con.commit()

def excluir (id):
    db.cur.execute("""
            DELETE FROM Personagens WHERE id = '%s'
    """ % (id))
    db.con.commit()

def alterar (nome, discricao, link, programa, animador, id):
    db.cur.execute("""
            UPDATE Personagens SET (nome, discricao, link, programa, animador) = ('%s', '%s', '%s', '%s',, '%s')  WHERE id = '%s'
    """ % (nome, discricao, link, programa, animador))
    db.con.commit()

def selecionar ():
    db.cur.execute("""SELECT * FROM Personagens""")
    recset = db.cur.fetchall()
    rows = []
    for rec in recset:
        rows.append(rec)
    return rows

def selecionar_id (id):
    db.cur.execute("""
            SELECT * FROM Personagens WHERE id = '%s'
    """ % (id))
    recset = db.cur.fetchall()
    rows = []
    for rec in recset:
        rows.append(rec)
    return rows