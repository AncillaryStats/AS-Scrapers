from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import text
from models import NFL_Team_2015, NFL_Player_2015, NFL_QB_Game_2015, NFL_RB_Game_2015, NFL_WR_Game_2015, NFL_TE_Game_2015, db_connect, create_tables

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
            if not session.query(NFL_Team_2015).filter(NFL_Team_2015.name == item['name']).count():
                print('new team found!')
                try:
                    session.add(team)
                    session.commit()
                except:
                    session.rollback()
                    print('error saving item!')
                    raise
                finally:
                    session.close()
            else:
                print('team already exists')
                session.close()

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
            if not session.query(NFL_Player_2015).filter(NFL_Player_2015.name == item['name']).count():
                print('new player found!')
                try:
                    session.add(player)
                    session.commit()
                except:
                    session.rollback()
                    print('error saving item!')
                    raise
                finally:
                    session.close()
            else:
                print('player already exists')
                session.close()

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
            # print(item)
            session = self.Session()
            game = NFL_QB_Game_2015(**item)

            # Add game if it hasn't been added yet
            # if not session.query(NFL_QB_Game_2015).filter(NFL_QB_Game_2015.date == item['date'], NFL_QB_Game_2015.player_name == item['player_name']).count():
            if True:

                print('new game found!')
                try:
                    session.add(game)
                    session.commit()
                except:
                    session.rollback()
                    print('error saving item!')
                    raise
                finally:
                    session.close()
            else:
                print('game already exists')
                session.close()

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

            # Add game if it hasn't been added yet
            # if not session.query(NFL_RB_Game_2015).filter(NFL_RB_Game_2015.date == item['date'], NFL_RB_Game_2015.player_name == item['player_name']).count():
            if True:
                print('new game found!')
                try:
                    session.add(game)
                    session.commit()
                except:
                    session.rollback()
                    print('error saving item!')
                    raise
                finally:
                    session.close()
            else:
                print('game already exists')
                session.close()

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

            # Add game if it hasn't been added yet
            # if not session.query(NFL_WR_Game_2015).filter(NFL_WR_Game_2015.date == item['date'], NFL_WR_Game_2015.player_name == item['player_name']).count():
            if True:
                print('new game found!')
                try:
                    session.add(game)
                    session.commit()
                except:
                    session.rollback()
                    print('error saving item!')
                    raise
                finally:
                    session.close()
            else:
                print('game already exists')
                session.close()

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

            # Add game if it hasn't been added yet
            # if not session.query(NFL_TE_Game_2015).filter(NFL_TE_Game_2015.date == item['date'], NFL_TE_Game_2015.player_name == item['player_name']).count():
            if True:
                print('new game found!')
                try:
                    session.add(game)
                    session.commit()
                except:
                    session.rollback()
                    print('error saving item!')
                    raise
                finally:
                    session.close()
            else:
                print('game already exists')

        return item
