"""Skills 5: SQLAlchemy & AJAX

Part 1: Define Model Classes
"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Human(db.Model):
    """Data model for a human."""

    human_id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    fname = db.Column(db.String(25), nullable=False)
    lname = db.Column(db.String(25), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    # animals: a list of Animal objects associated with Human

    def __repr__(self):
        """Display info about Human."""
        return f'<Human id={self.human_id} email={self.email}'

class Animal(db.Model):
    """Data model for an animal."""

    # foreign keys???

    animal_id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    human_id = db.relationship('Human', backref='animals', nullable=False)
    name = db.Column(db.String(50), nullable=False)
    animal_species = db.Column(db.String(25), nullable=False)
    birth_year = db.Column(db.Integer)

    def __repr__(self):
        """Display info about Animal."""
        return f'<Animal id={self.animal_id} animal_species={self.animal_species}'


def connect_to_db(app):
    """Connect the database to our Flask app."""

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres:///animals'
    app.config['SQLALCHEMY_ECHO'] = False
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)


if __name__ == '__main__':
    from server import app

    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.
    connect_to_db(app)
    print('Connected to db!')
