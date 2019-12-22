# ev_compare

Website for hosting and comparison of information on electric vehicles so potential buyers can find their dream vehicle.

# How to get things running

* run `export REACT_APP_EVS_SERVICE_URL=http://localhost`
* run `docker-compose up -d`
* navigate to `http://localhost:3007` in your browser of choice

# Testing

## Setup database

* run `docker-compose exec evs python manage.py recreate_db`
* run `docker-compose exec evs python manage.py seed_db`

This will add a few test cars to your SQL database.
