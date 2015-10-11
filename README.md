## AS-Scrapers

A dedicated worker for scraping NFL player, team, and game statistics from ESPN.

## Uses

Sub.py watches a redis queue for tasks. Default listening is blocking. All data is stored in a PostgreSQL database.

## Tasks

```python
'CRAWL ALL SPIDERS'
```  
- Crawls all players, teams, and game spiders:
  * 'nfl_team_info'
  * 'nfl_players'
  * 'nfl_qb_stats'
  * 'nfl_rb_stats'
  * 'nfl_wr_stats'
  * 'nfl_te_stats'
  
```python
'CRAWL ALL GAMES'
```  
- Crawls all game spiders:  
  * 'nfl_qb_stats'
  * 'nfl_rb_stats'
  * 'nfl_wr_stats'
  * 'nfl_te_stats'
  
## Spiders

```python
class TeamSpider(Spider):
    name = 'nfl_team_info'
```
- Crawls all 2015 NFL teams. Pre-existing team data will not be overwritten.  
  
```python
class PlayerSpider(Spider):
    name = 'nfl_players'
```
- Crawls all 2015 NFL quarterbacks, running backs, wide recievers, and tight ends on active rosters. Pre-existing player information will not be overwritten.  
  
```python
class QbSpider(Spider):
    name = 'nfl_qb_stats'
```
- Crawls all 2015 quarterback regular season games and season totals. Season totals will be automatically overwritten, individual games will not be.  
  
```python
class RbSpider(Spider):
    name = 'nfl_rb_stats'
```
  
- Crawls all 2015 running back regular season games and season totals. Season totals will be automatically overwritten, individual games will not be.  
  
```python
class WrSpider(Spider):
    name = 'nfl_wr_stats'
```
- Crawls all 2015 wide receiver regular season games and season totals. Season totals will be automatically overwritten, individual games will not be.  
  
```python
class TeSpider(Spider):
    name = 'nfl_te_stats'
```
- Crawls all 2015 quarterback regular season games and season totals. Season totals will be automatically overwritten, individual games will not be.  
  