from sqlalchemy import Column, Boolean, ForeignKey, Integer, String, \
    create_engine
from sqlalchemy.orm import backref, relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
engine = create_engine('sqlite:///3cup.db')


class Player(Base):
    __tablename__ = 'players'

    id = Column(Integer, primary_key=True)
    name = Column(String(32))

    def __repr__(self):
        return '<Player id={} name="{}">'.format(self.id, self.name)


class Game(Base):
    __tablename__ = 'games'

    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return '<Game id={}>'.format(self.id)


class Shot(Base):
    __tablename__ = 'shots'

    id = Column(Integer, primary_key=True)
    player_id = Column(Integer, ForeignKey('players.id'))
    game_id = Column(Integer, ForeignKey('games.id'))
    shot_number = Column(Integer)
    points = Column(Integer)
    is_moneyball = Column(Boolean, default=False)

    player = relationship('Player', backref=backref('Player', lazy='dynamic'))

    def __repr__(self):
        return '<Shot id={} name="{}" game_id={} shot_number={} points={} is_moneyball={}>'.format(
            self.id,
            self.player.name,
            self.game_id,
            self.shot_number,
            self.points,
            self.is_moneyball)


Session = sessionmaker()
session = Session(bind=engine)


def create_db():
    print('Creating tables...')
    Base.metadata.create_all(engine)
    print('Done!')


if __name__ == '__main__':
    create_db()
