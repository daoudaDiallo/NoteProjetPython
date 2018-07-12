import MySQLdb

import time

db = MySQLdb.connect("localhost", "root", "123456", "bd_notes")

cursor = db.cursor()
global resultsExportEtudiants
resultsExportEtudiants = []
global resultsExportMatieres
resultsExportMatieres = []
global resultsExportNotes
resultsExportNotes = []
global resultsExportNotesEtu
resultsExportNotesEtu = []


def getmatieres():
    del resultsExportMatieres[:]
    sql = "SELECT * FROM t_matiere"
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            item = {
                "id": row[0],
                "libelle": row[1],
                "coefficient": row[2]
            }
            resultsExportMatieres.append(item)
    except MySQLdb.Error as e:
        try:
            print ("MySQL Error [%d]: %s" % (e.args[0], e.args[1]))
            return None
        except IndexError:
            print ("MySQL Error: %s" % str(e))
            return None
        finally:
            cursor.close()
            db.close()


def getetudiants():
    del resultsExportEtudiants[:]
    sql = "SELECT * FROM t_etudiant"
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            item = {
                "id_etudiant": row[0],
                "matricule": row[1],
                "prenom": row[2],
                "nom": row[3]
            }
            resultsExportEtudiants.append(item)
    except MySQLdb.Error as e:
        try:
            print ("MySQL Error [%d]: %s" % (e.args[0], e.args[1]))
            return None
        except IndexError:
            print ("MySQL Error: %s" % str(e))
            return None
        finally:
            cursor.close()
            db.close()


def getnotes():
    del resultsExportNotes[:]
    sql = "SELECT t_note.valeur as note, t_matiere.libelle as lib, t_matiere.coefficient as coef, t_etudiant.nom as nom, t_etudiant.prenom as pren, t_etudiant.matricule as mat  FROM t_note, t_matiere, t_etudiant WHERE t_note.id_etudiant = t_etudiant.id_etudiant AND t_note.id_matiere = t_matiere.id_matire"
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            item = {
                "note": row[0],
                "lib": row[1],
                "coef": row[2],
                "nom": row[3],
                "pren": row[4],
                "mat": row[5],
            }
            resultsExportNotes.append(item)
    except MySQLdb.Error as e:
        try:
            print ("MySQL Error [%d]: %s" % (e.args[0], e.args[1]))
            return None
        except IndexError:
            print ("MySQL Error: %s" % str(e))
            return None
        finally:
            cursor.close()
            db.close()


def getnotesetu(id_etu):
    del resultsExportNotesEtu[:]
    sql = "SELECT t_note.valeur as note, t_matiere.libelle as lib, t_matiere.coefficient as coef, t_etudiant.nom as nom, t_etudiant.prenom as pren, t_etudiant.matricule as mat  FROM t_note, t_matiere, t_etudiant " \
          "WHERE t_note.id_etudiant = t_etudiant.id_etudiant AND t_note.id_matiere = t_matiere.id_matire AND t_etudiant.id_etudiant = '%d'" \
          % id_etu
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            item = {
                "note": row[0],
                "lib": row[1],
                "coef": row[2],
                "nom": row[3],
                "pren": row[4],
                "mat": row[5],
            }
            resultsExportNotesEtu.append(item)
    except MySQLdb.Error as e:
        try:
            print ("MySQL Error [%d]: %s" % (e.args[0], e.args[1]))
            return None
        except IndexError:
            print ("MySQL Error: %s" % str(e))
            return None
        finally:
            cursor.close()
            db.close()


def creatematiere(matiere):
    sql = "Insert into t_matiere(libelle, coefficient) values('%s', '%d')" % (matiere['libelle'], matiere['coefficient'])
    try:
        cursor.execute(sql)
        db.commit()
    except MySQLdb.Error as e:
        try:
            print ("MySQL Error [%d]: %s" % (e.args[0], e.args[1]))
            return None
        except IndexError:
            db.rollback()
            print ("MySQL Error: %s" % str(e))
            return None
        finally:
            cursor.close()
            db.close()


def createetudiant(etudiant):
    sql = "Insert into t_etudiant(matricule, nom, prenom) values('%s', '%s', '%s')" % (etudiant['matricule'], etudiant['nom'], etudiant['prenom'])
    try:
        cursor.execute(sql)
        db.commit()
    except MySQLdb.Error as e:
        try:
            print ("MySQL Error [%d]: %s" % (e.args[0], e.args[1]))
            return None
        except IndexError:
            db.rollback()
            print ("MySQL Error: %s" % str(e))
            return None
        finally:
            cursor.close()
            db.close()


def createnote(note):
    now = time.strftime('%Y-%m-%d %H:%M:%S')
    sql = "Insert into t_note(valeur, date_creation, id_matiere, id_etudiant) values('%d', '%s', '%d', '%d')" % (note['valeur'], now, note['id_matiere'], note['id_etudiant'])
    try:
        cursor.execute(sql)
        db.commit()
    except MySQLdb.Error as e:
        try:
            print ("MySQL Error [%d]: %s" % (e.args[0], e.args[1]))
            return None
        except IndexError:
            db.rollback()
            print ("MySQL Error: %s" % str(e))
            return None
        finally:
            cursor.close()
            db.close()
