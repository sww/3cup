from sqlalchemy import func

from models import Player, Shot, session


def makes_for_name(name):
    """Gets the make percentage per shot number for a person."""
    print('Make percentage for {}'.format(name))

    query = session.query(func.count(Shot.id)) \
                   .join(Player) \
                   .filter(Player.name == name)

    for i in range(1, 13):
        attempts = query.filter(Shot.shot_number == i) \
                        .scalar()

        makes = query.filter(Shot.shot_number == i) \
                     .filter(Shot.points > 0) \
                     .scalar()

        make_percentage = (makes / float(attempts or 1)) * 100
        print('  Shot #{}: {:.2f}% ({}/{})'.format(i, make_percentage, makes, attempts))


def non_moneyball_makes_for_name(name):
    """Gets the non moneyball make percentage per shot number for a person."""
    print('Non moneyball make percentage for {}'.format(name))

    query = session.query(func.count(Shot.id)) \
                   .join(Player) \
                   .filter(Player.name == name) \
                   .filter(Shot.is_moneyball.is_(False))

    for i in range(1, 13):
        attempts = query.filter(Shot.shot_number == i) \
                        .scalar()

        makes = query.filter(Shot.shot_number == i) \
                     .filter(Shot.points > 0) \
                     .scalar()
        make_percentage = (makes / float(attempts or 1)) * 100
        print('  Shot #{}: {:.2f}% ({}/{})'.format(i, make_percentage, makes, attempts))


def moneyball_makes_for_name(name):
    """Gets the moneyball make percentage per shot number for a person."""
    print('Moneyball make percentage for {}'.format(name))

    query = session.query(func.count(Shot.id)) \
                   .join(Player) \
                   .filter(Player.name == name) \
                   .filter(Shot.is_moneyball.is_(True))

    for i in range(1, 13):
        moneyball_attempts = query.filter(Shot.shot_number == i) \
                                  .scalar()

        moneyball_makes = query.filter(Shot.shot_number == i) \
                               .filter(Shot.points > 0) \
                               .scalar()
        moneyball_make_percentage = (moneyball_makes / float(moneyball_attempts or 1)) * 100
        print('  Shot #{}: {:.2f}% ({}/{})'.format(i, moneyball_make_percentage, moneyball_makes, moneyball_attempts))


if __name__ == '__main__':
    import sys
    name = sys.argv[1]
    if not name:
        return

    makes_for_name(name)
    non_moneyball_makes_for_name(name)
    moneyball_makes_for_name(name)
