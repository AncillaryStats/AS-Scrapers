from sqlalchemy import create_engine, Column, Integer, Float, Boolean, String, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL
from sqlalchemy.orm import relationship, backref

import settings

Base = declarative_base()

def db_connect():
    """
    Performs database connection using database settings from settings.py
    Returns sqlalchemy engine instance
    """
    return create_engine(URL(**settings.DATABASE))

def create_tables(engine):
    Base.metadata.create_all(engine)

class NFL_Team_2015(Base):
    """2015 NFL teams table"""
    __tablename__ = 'nfl_teams_2015'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    division = Column(String)


class NFL_Player_2015(Base):
    """2015 NFL players table"""
    __tablename__ = 'nfl_players_2015'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    number = Column(String)
    team = Column(String)
    position = Column(String)
    # team_id = Column(Integer, ForeignKey('nfl_teams_2015.id'))

    # team = relationship('Team', backref=backref('nfl_players_2015', order_by="position"))


class NFL_QB_Game_2015(Base):
    """2015 NFL qb games table"""
    __tablename__ = 'nfl_qb_games_2015'

    id = Column(Integer, primary_key=True)
    player_name = Column(String)

    date = Column(Date)
    opponent = Column(String)
    result = Column(String)
    pass_completions = Column(Integer)
    pass_attempts = Column(Integer)
    pass_yards = Column(Integer)
    comp_percentage = Column(Float)
    avg_yards_per_pass = Column(Float)
    longest_pass = Column(Integer)
    pass_tds = Column(Integer)
    interceptions = Column(Integer)
    qb_rating = Column(Float)
    passer_rating = Column(Float)
    rush_attempts = Column(Integer)
    rush_yards = Column(Integer)
    avg_yards_per_rush = Column(Float)
    longest_rush = Column(Integer)
    rush_tds = Column(Integer)
    is_season_totals = Column(Boolean)


class NFL_RB_Game_2015(Base):
    """2015 NFL rb games table"""
    __tablename__ = 'nfl_rb_games_2015'

    id = Column(Integer, primary_key=True)
    player_name = Column(String)

    date = Column(Date)
    opponent = Column(String)
    result = Column(String)
    rush_attempts = Column(Integer)
    rush_yards = Column(Integer)
    avg_yards_per_rush = Column(Float)
    longest_rush = Column(Integer)
    rush_tds = Column(Integer)
    receptions = Column(Integer)
    rec_yards = Column(Integer)
    avg_yards_per_rec = Column(Float)
    longest_rec = Column(Integer)
    rec_tds = Column(Integer)
    fumbles = Column(Integer)
    fumbles_lost = Column(Integer)
    is_season_totals = Column(Boolean)

class NFL_WR_Game_2015(Base):
    """2015 NFL wr games table"""
    __tablename__ = 'nfl_wr_games_2015'

    id = Column(Integer, primary_key=True)
    player_name = Column(String)

    date = Column(Date)
    opponent = Column(String)
    result = Column(String)
    receptions = Column(Integer)
    targets = Column(Integer)
    rec_yards = Column(Integer)
    avg_yards_per_rec = Column(Float)
    longest_rec = Column(Integer)
    rec_tds = Column(Integer)
    rush_attempts = Column(Integer)
    rush_yards = Column(Integer)
    avg_yards_per_rush = Column(Float)
    longest_rush = Column(Integer)
    rush_tds = Column(Integer)
    fumbles = Column(Integer)
    fumbles_lost = Column(Integer)
    is_season_totals = Column(Boolean)

class NFL_TE_Game_2015(Base):
    """2015 NFL te games table"""
    __tablename__ = 'nfl_te_games_2015'

    id = Column(Integer, primary_key=True)
    player_name = Column(String)

    date = Column(Date)
    opponent = Column(String)
    result = Column(String)
    receptions = Column(Integer)
    targets = Column(Integer)
    rec_yards = Column(Integer)
    avg_yards_per_rec = Column(Float)
    longest_rec = Column(Integer)
    rec_tds = Column(Integer)
    rush_attempts = Column(Integer)
    rush_yards = Column(Integer)
    avg_yards_per_rush = Column(Float)
    longest_rush = Column(Integer)
    rush_tds = Column(Integer)
    fumbles = Column(Integer)
    fumbles_lost = Column(Integer)
    is_season_totals = Column(Boolean)

