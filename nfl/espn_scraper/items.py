from scrapy.item import Item, Field

class NFL_Team_2015(Item):
    """2015 NFL team container for scraped data"""
    name = Field()
    division = Field()

class NFL_Player_2015(Item):
    """2015 NFL player container for scraped data"""
    name = Field()
    number = Field()
    team = Field()
    position = Field()

class NFL_QB_Game_2015(Item):
    """2015 NFL QB game container for scraped data"""
    player_name = Field()
    date = Field()
    opponent = Field()
    result = Field()
    pass_completions = Field()
    pass_attempts = Field()
    pass_yards = Field()
    comp_percentage = Field()
    avg_yards_per_pass = Field()
    longest_pass = Field()
    pass_tds = Field()
    interceptions = Field()
    qb_rating = Field()
    passer_rating = Field()
    rush_attempts = Field()
    rush_yards = Field()
    avg_yards_per_rush = Field()
    longest_rush = Field()
    rush_tds = Field()
    is_season_totals = Field()

class NFL_RB_Game_2015(Item):
    """2015 NFL RB game container for scraped data"""
    player_name = Field()
    date = Field()
    opponent = Field()
    result = Field()
    rush_attempts = Field()
    rush_yards = Field()
    avg_yards_per_rush = Field()
    longest_rush = Field()
    rush_tds = Field()
    receptions = Field()
    rec_yards = Field()
    avg_yards_per_rec = Field()
    longest_rec = Field()
    rec_tds = Field()
    fumbles = Field()
    fumbles_lost = Field()
    is_season_totals = Field()

class NFL_WR_Game_2015(Item):
    """2015 NFL WR game container for scraped data"""
    player_name = Field()
    date = Field()
    opponent = Field()
    result = Field()
    receptions = Field()
    targets = Field()
    rec_yards = Field()
    avg_yards_per_rec = Field()
    longest_rec = Field()
    rec_tds = Field()
    rush_attempts = Field()
    rush_yards = Field()
    avg_yards_per_rush = Field()
    longest_rush = Field()
    rush_tds = Field()
    fumbles = Field()
    fumbles_lost = Field()
    is_season_totals = Field()

class NFL_TE_Game_2015(Item):
    """2015 NFL TE game container for scraped data"""
    player_name = Field()
    date = Field()
    opponent = Field()
    result = Field()
    receptions = Field()
    targets = Field()
    rec_yards = Field()
    avg_yards_per_rec = Field()
    longest_rec = Field()
    rec_tds = Field()
    rush_attempts = Field()
    rush_yards = Field()
    avg_yards_per_rush = Field()
    longest_rush = Field()
    rush_tds = Field()
    fumbles = Field()
    fumbles_lost = Field()
    is_season_totals = Field()

