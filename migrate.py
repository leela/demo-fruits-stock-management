from fsm import db

schema = open("fsm/schema.sql").read()
db.query(schema)