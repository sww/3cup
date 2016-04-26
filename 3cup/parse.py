from bs4 import BeautifulSoup

from models import Game, Player, Shot, session


def parse(filename):
    with open(filename) as f:
        soup = BeautifulSoup(f.read(), 'html.parser')

    if not soup:
        raise

    game = Game()
    session.add(game)
    for tr in soup.find_all('tr'):
        if not tr:
            continue

        tds = tr.find_all('td')
        if not tds:
            session.add(game)
            game = Game()
            continue

        player_name = tds[0].text
        if not player_name:
            game = Game()
            session.add(game)
            continue

        if player_name.startswith('x') \
           or player_name == 'Player':
            continue

        player = session.query(Player).filter(Player.name == player_name).first()
        if player is None:
            player = Player(name=player_name)
            session.add(player)

        for shot_number, td in enumerate(tds[1:13]):
            shot = Shot()
            shot.player_id = player.id
            shot.game_id = game.id
            shot.shot_number = shot_number + 1
            shot.points = int(td.text)
            shot.is_moneyball = 's12' in td.get('class', []) if td.has_attr('class') else False

            session.add(shot)

    session.commit()


if __name__ == '__main__':
    import sys
    parse(sys.argv[1])
