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


def point_per_shot(name):
    """Gets the points per shot for a person."""
    print('Points per shot for {}'.format(name))

    total_shots = session.query(func.count(Shot.id)) \
                         .join(Player) \
                         .filter(Player.name == name) \
                         .filter(Shot.shot_number == 1) \
                         .scalar()

    query = session.query(func.sum(Shot.points)) \
                   .join(Player) \
                   .filter(Player.name == name) \
                   .filter(Shot.points > 0)

    for i in range(1, 13):
        shot_sum = query.filter(Shot.shot_number == i).first()
        print('  Shot #{}: {:.2f} points'.format(i, shot_sum[0] / float(total_shots)))


def cup_percentage_per_shot(name):
    """Get the cup make percentages per shot."""
    # If a shot is made, what cup is it percentage.
    print('Cup percentage per make per shot for {}'.format(name))

    query = session.query(Shot).join(Player) \
                               .filter(Player.name == name) \
                               .filter(Shot.points > 0)

    for i in range(1, 13):
        makes = {
            1: 0,
            2: 0,
            3: 0,
        }
        num_makes = 0
        for num_makes, s in enumerate(query.filter(Shot.shot_number == i)):
            shot_points = int(s.points)
            if s.is_moneyball:
                shot_points /= 2

            makes[shot_points] += 1

        num_makes += 1

        print('  Shot #{}'.format(i))
        print('    1 point: {:.2f}% ({}/{})'.format(
            (makes[1] / float(num_makes)) * 100, makes[1], num_makes,))
        print('    2 point: {:.2f}% ({}/{})'.format(
            (makes[2] / float(num_makes)) * 100, makes[2], num_makes,))
        print('    3 point: {:.2f}% ({}/{})'.format(
            (makes[3] / float(num_makes)) * 100, makes[3], num_makes,))


if __name__ == '__main__':
    import sys
    name = sys.argv[1]
    if not name:
        return

    makes_for_name(name)
    non_moneyball_makes_for_name(name)
    moneyball_makes_for_name(name)
    point_per_shot(name)
    cup_percentage_per_shot(name)
