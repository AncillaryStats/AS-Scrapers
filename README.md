# Sports-Stats-Scrapers

A dedicated worker for scraping NFL player, team, and game statistics from ESPN.

## Uses

Sub.py makes use of a custom RedisQueue class to listen for work on a specific channel. Default listening is blocking. All data is stored in a PostgreSQL database.

## Env requirements

### Database connection
- DB_DRIVER
- DB_HOST
- DB_PORT
- DB_USER
- DB_PW
- DB_NAME

### Redis connection
- REDISTOGO_URL