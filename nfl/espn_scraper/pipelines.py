from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import text
from models import NFL_Team_2015, NFL_Player_2015, NFL_QB_Game_2015, NFL_RB_Game_2015, NFL_WR_Game_2015, NFL_TE_Game_2015, db_connect, create_tables


def upsert_season_total(model, scrapy_item, row, s):
    """Insert or update player's season totals
    Args:
        model: model for position being queried
        scrapy_item: loaded scrapy item scraped from row
        row: unpacked vars from scrapy item applied to model
        s: open session
    """
    print('\n----------\nupserting season total\n----------\n')
    if s.query(model).filter(model.player_name == scrapy_item['player_name'], model.is_season_totals == True).count() > 0:

        # update season totals
        to_be_del = s.query(model).filter(model.player_name == scrapy_item['player_name'], model.is_season_totals == True).one()

        print('\n----------\nto be deleted:\n----------\n')

        print (to_be_del)

        try:
            s.delete(to_be_del)
            s.add(row)
            s.commit()
        except:
            s.rollback()
            print('---------\nerror updating row\n---------')
        finally:
            s.close()
    else:
        print('---------\nsaving new season totals\n---------')
        try:
            s.add(row)
            s.commit()
        except:
            s.rollback()
            print('---------\nerror inserting row\n---------')
        finally:
            s.close()


def insert_new_row(row, s):
    """Add item if it does not exist yet"""
    print('\n----------\ninserting new item\n----------\n')
    try:
        s.add(row)
        s.commit()
    except:
        s.rollback()
        print('error saving item!')
        raise
    finally:
        s.close()

# Pipeline from processing nfl teams from 'nfl_team_info' spider
class NFL_Team_Info_2015_Pipeline(object):
    def __init__(self):
        """
        Initializes database connection and sessionmaker.
        Creates nfl_teams_2015 table.
        """
        engine = db_connect()
        create_tables(engine)
        self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
        """This method is called for every item pipeline component."""
        print('passing through NFL_Team_Info_2015 pipeline')

        # Only process items for the nfl team info spider
        if spider.name == 'nfl_team_info':
            session = self.Session()
            team = NFL_Team_2015(**item)

            # Add team if it does not exist yet
            if session.query(NFL_Team_2015).filter(NFL_Team_2015.name == item['name']).count() == 0:
                insert_new_row(team, session)
            else:
                print('team already exists')

        # pass item to next pipeline
        return item

# Pipeline from processing nfl teams from 'nfl_team_rosters' spider
class NFL_Player_2015_Pipeline(object):
    def __init__(self):
        """
        Initializes database connection and sessionmaker.
        Creates nfl_rosters_2015 table.
        """
        engine = db_connect()
        create_tables(engine)
        self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
        """This method is called for every item pipeline component."""
        print('passing through NFL_Player_2015 pipeline')

        # Only process items for the nfl team info spider
        if spider.name == 'nfl_players':
            print(item)
            session = self.Session()
            player = NFL_Player_2015(**item)

            # Add team if it does not exist yet
            if session.query(NFL_Player_2015).filter(NFL_Player_2015.name == item['name']).count() == 0:
                insert_new_row(player, session)
            else:
                print('player already exists')

        # pass item to next pipeline
        return item

# Pipeline from processing nfl teams from 'nfl_qb_stats' spider
class NFL_QB_Stats_2015_Pipeline(object):
    def __init__(self):
        """
        Initializes database connection and sessionmaker.
        Creates nfl_qb_games_2015 table if it doesn't exist.
        """
        engine = db_connect()
        create_tables(engine)
        self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
        """This method is called for every item pipeline component."""
        print('passing through NFL_QB_Stats_2015 pipeline')

        # Only process items for the nfl team info spider
        if spider.name == 'nfl_qb_stats':
            session = self.Session()
            game = NFL_QB_Game_2015(**item)

            # If season totals, delete old row and insert new row
            if item['is_season_totals'] == True:
                upsert_season_total(NFL_QB_Game_2015, item, game, session)
            # Add game if it hasn't been added yet
            elif session.query(NFL_QB_Game_2015).filter(NFL_QB_Game_2015.date == item['date'], NFL_QB_Game_2015.player_name == item['player_name']).count() == 0:
                insert_new_row(game, session)
            else:
                print('\n----------\nqb season game already exists\n----------\n')

        # pass item to next pipeline
        return item


# Pipeline from processing nfl teams from 'nfl_rb_stats' spider
class NFL_RB_Stats_2015_Pipeline(object):
    def __init__(self):
        """
        Initializes database connection and sessionmaker.
        Creates nfl_rb_games_2015 table if it doesn't exist.
        """
        engine = db_connect()
        create_tables(engine)
        self.Session = sessionmaker(bind=engine)


    def process_item(self, item, spider):
        """This method is called for every item pipeline component."""
        print('passing through NFL_RB_Stats_2015 pipeline')

        # Only process items for the nfl team info spider
        if spider.name == 'nfl_rb_stats':
            # print(item)
            session = self.Session()
            game = NFL_RB_Game_2015(**item)

            # If season totals, delete old row and insert new row
            if item['is_season_totals'] == True:
                upsert_season_total(NFL_RB_Game_2015, item, game, session)
            # Add game if it hasn't been added yet
            elif session.query(NFL_RB_Game_2015).filter(NFL_RB_Game_2015.date == item['date'], NFL_RB_Game_2015.player_name == item['player_name']).count() == 0:
                insert_new_row(game, session)
            else:
                print('\n----------\nrb game already exists\n----------\n')

        # pass item to next pipeline
        return item

# Pipeline from processing nfl teams from 'nfl_wr_stats' spider
class NFL_WR_Stats_2015_Pipeline(object):
    def __init__(self):
        """
        Initializes database connection and sessionmaker.
        Creates nfl_wr_games_2015 table if it doesn't exist.
        """
        engine = db_connect()
        create_tables(engine)
        self.Session = sessionmaker(bind=engine)


    def process_item(self, item, spider):
        """This method is called for every item pipeline component."""
        print('passing through NFL_WR_Stats_2015 pipeline')

        # Only process items for the nfl team info spider
        if spider.name == 'nfl_wr_stats':
            session = self.Session()
            game = NFL_WR_Game_2015(**item)

            # If season totals, delete old row and insert new row
            if item['is_season_totals'] == True:
                upsert_season_total(NFL_WR_Game_2015, item, game, session)

            # Add game if it hasn't been added yet
            elif session.query(NFL_WR_Game_2015).filter(NFL_WR_Game_2015.date == item['date'], NFL_WR_Game_2015.player_name == item['player_name']).count() == 0:
                insert_new_row(game, session)
            else:
                print('\n----------\nwr game already exists\n----------\n')

        return item

# Pipeline from processing nfl teams from 'nfl_wr_stats' spider
class NFL_TE_Stats_2015_Pipeline(object):
    def __init__(self):
        """
        Initializes database connection and sessionmaker.
        Creates nfl_te_games_2015 table if it doesn't exist.
        """
        engine = db_connect()
        create_tables(engine)
        self.Session = sessionmaker(bind=engine)


    def process_item(self, item, spider):
        """This method is called for every item pipeline component."""
        print('passing through NFL_TE_Stats_2015 pipeline')

        # Only process items for the nfl team info spider
        if spider.name == 'nfl_te_stats':
            # print(item)
            session = self.Session()
            game = NFL_TE_Game_2015(**item)

            # If season totals, delete old row and insert new row
            if item['is_season_totals'] == True:
                upsert_season_total(NFL_TE_Game_2015, item, game, session)

            # Add game if it hasn't been added yet
            elif session.query(NFL_TE_Game_2015).filter(NFL_TE_Game_2015.date == item['date'], NFL_TE_Game_2015.player_name == item['player_name']).count() == 0:
                insert_new_row(game, session)
            else:
                print('\n----------\nwr game already exists\n----------\n')

        return item
