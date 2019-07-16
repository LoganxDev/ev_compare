from flask import Blueprint, request, render_template
from flask_restful import Resource, Api
from sqlalchemy import exc

from project import db
from project.api.models import EV

evs_blueprint = Blueprint('evs', __name__, template_folder='./templates')
api = Api(evs_blueprint)


@evs_blueprint.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        make = request.form['make']
        brand = request.form['brand']
        base_price = request.form['base_price']
        storage = request.form['storage']
        db.session.add(EV(make=make, brand=brand, ranges=[],
                          base_price=base_price, storage=storage,
                          option_ids=[]))
        db.session.commit()
    evs = EV.query.all()
    return render_template('index.html', evs=evs)


class EvsPing(Resource):
    def get(self):
        return {
            'status': 'success',
            'message': 'pong!'
        }


class EvsList(Resource):

    def get(self):
        # Gets all users
        response_obj = {
            'status': 'success',
            'data': {
                'evs': [ev.to_json() for ev in EV.query.all()]
            }
        }
        return response_obj, 200

    def post(self):
        post_data = request.get_json()

        response_object = {
            'status': 'fail',
            'message': 'Invalid payload.'
        }

        if not post_data:
            return response_object, 400

        make = post_data.get('make')
        brand = post_data.get('brand')
        ranges = post_data.get('ranges')
        base_price = post_data.get('base_price')
        storage = post_data.get('storage')
        option_ids = post_data.get('option_ids')

        try:
            ev = EV.query.filter_by(make=make).first()
            if not ev:
                db.session.add(EV(make=make, brand=brand, ranges=ranges,
                                  base_price=base_price, storage=storage,
                                  option_ids=option_ids))
                db.session.commit()

                response_object = {
                    'status': 'success',
                    'message': f'{make} was added!'
                }
                return response_object, 201
            else:
                response_object['message'] = 'Sorry, this make already exists'
                return response_object, 400
        except exc.IntegrityError as e:
            print(f'Error is: {e}')
            db.session.rollback()
            return response_object, 400


class Evs(Resource):

    def get(self, ev_id):
        response_object = {
            'status': 'fail',
            'message': 'Vehicle does not exist'
        }
        try:
            ev = EV.query.filter_by(id=int(ev_id)).first()
            if ev:
                response_object = {
                    'status': 'success',
                    'data': {
                        'id': ev.id,
                        'make': ev.make,
                        'brand': ev.brand,
                        'ranges': ev.ranges,
                        'base_price': ev.base_price,
                        'storage': ev.storage,
                        'option_ids': ev.option_ids
                    }
                }
                return response_object, 200
            else:
                return response_object, 404
        except ValueError:
            return response_object, 404


api.add_resource(EvsPing, '/evs/ping')
api.add_resource(EvsList, '/evs')
api.add_resource(Evs, '/evs/<ev_id>')
