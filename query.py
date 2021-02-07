"""Skills 5: SQLAlchemy & AJAX

This file is used in Part 2 and 3 of Skills 5: SQLAlchemy & AJAX. You need to
complete Part 1 first, otherwise this part of the assessment won't work.
"""

from model import db, Human, Animal


def get_human_2():
    """Return the human with the id 2."""
    
    return Human.query.get(2)


def get_first_fish():
    """Return the FIRST animal with the species 'fish'."""

    return Animal.query.filter(Animal.animal_species == 'fish').first()


def get_young_animals():
    """Return all animals that were born after 2015.

    Do NOT include animals without birth years.
    """

    return Animal.query.filter(Animal.birth_year > 2015).all()


def get_j_names():
    """Return the humans with first names that start with 'J'."""

    return Human.query.filter(Human.fname.like('J%')).all()


def get_null_bdays():
    """Return all animals whose birth years are NULL."""

    return Animal.query.filter(Animal.birth_year == None).all()


def get_fish_or_rabbits():
    """Return all animals whose species is 'fish' OR 'rabbit'."""

    return Animal.query.filter((Animal.animal_species == 'fish') | (Animal.animal_species == 'rabbit')).all()


def print_directory():
    """Output a list of humans and their animals.

    For example:

    >>> print_directory()
    Justin Time
    - Peter (rabbit)
    - Peppa (pig)
    Carmen Sandiego
    - Blub (fish)

    You may only use ONE query to retrieve initial data. (Hint: leverage a
    SQLAlchemy relationship to retrieve additional information)
    """

    humans = Human.query.options(db.joinedload('animals')).all()

    for human in humans:
        print(f'{human.fname} {human.lname}') 
        for animal in human.animals:
            print(f'- {animal.name} ({animal.animal_species})')


def find_humans_by_animal_species(species):
    """Return a list of all humans who have animals of the given species.

    Each human should only appear once in the returned list. For example:

    >>> find_humans_by_animal_species('snake')

    Again, you may only use ONE query to retrieve initial data. (Hint: use a
    relationship! Also, you can pursue uniqueness in a Pythonic way --- you
    don't have to do it with pure SQLAlchemy)
    """

    # humans = db.session.query(Human, Animal.animal_species).join(Animal).group_by(Human.human_id, Human.email, Animal.animal_species)
    # # Human.query.options(db.joinedload('animals')).filter(Human.animals.species == species).all()
    # # db.session.query(Human).filter(Human.animals.species == species)
    # # Human.query.filter(Human.animals.species == species).all()
    # # .group_by('email', 'human_id')
    # for human in humans:
    #     print(human.animals.species)

    # cat = find_humans_by_animal_species('cat')


    # directory = db.session.query(Animal, Human).join(Human).all()
    # either/or?
    # directory = Animal.query.options(db.joinedload('human')).all()

    # species = animal_species
    # humans = []

    # if species in human_id:
    #     humans.append(human_id)

    # return humans




if __name__ == '__main__':
    from server import app
    from model import connect_to_db

    connect_to_db(app)
