from my_app import db

class Mahasiswa(db.model):
    id: db.Column(db.Integer, primary_key=True)
    nama: db.Column(db.String(255))
    nim: db.Column(db.String(255))

    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim

    def __repr__(self)
    return '<Mahasiswa %d>' % self.id