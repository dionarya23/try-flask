import json
from flask import request, jsonify, Blueprint, abort
from flask.views import MethodView
from my_app import db, app
from my_app.mahasiswa.models import Mahasiswa

mahasiswa = Blueprint('mahasiswa', __name__)

@mahasiswa.route('/')
@mahasiswa.route('/home')
def home():
    return 'Welcome to Mahasiswa Home'


class MahasiswaView(MethodView):

    def get(self, id=None, page=1):
        if not id:
            mahasiswas = Mahasiswa.query.paginate(page, 10).items
            res={}
            for mahasiswa in mahasiswas:
                res[mahasiswa.id] = {
                    'nama': mahasiswa.nama,
                    'nim': mahasiswa.nim
                }
        else:
            mahasiswa = Mahasiswa.query.filter_by(id=id).first()
            if not mahasiswa:
                abort(404)
            res = {
                'nama': mahasiswa.nama,
                'nim': mahasiswa.nim
            }
        return jsonify(res)

    def post(self):
        nama = request.form.get('nama')
        nim = request.form.get('nim')
        mahasiswa = Mahasiswa(nama, nim)
        db.session.add(mahasiswa)
        db.session.commit()
        return jsonify({mahasiswa.id: {
            'nama': mahasiswa.nama,
            'nim': mahasiswa.nim,
        }})
 
    def put(self, id):
        # Update the record for the provided id
        # with the details provided.
        return
 
    def delete(self, id):
        # Delete the record for the provided id.
        return
 
 
mahasiswa_view =  MahasiswaView.as_view('mahasiswa_view')
app.add_url_rule(
    '/product/', view_func=mahasiswa_view, methods=['GET', 'POST']
)
app.add_url_rule(
    '/mahasiswa/<int:id>', view_func=mahasiswa_view, methods=['GET']
)