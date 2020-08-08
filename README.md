# WaniKani2Anki
A set of utility scripts for getting data out of WaniKani and into your Anki database for custom usage. WaniKani is awesome, and I want the chance to do things besides kanji/radicals/vocabulary -> English with their excellent study materials, like focus on reading the example sentences. I hope this growing collection of scripts helps others to do the same.

## Usage Notes

### Colophon
- This project is written in [Python3](https://www.python.org/downloads/)
- Python dependencies are managed with [Pipenv](https://pipenv.pypa.io/en/latest/)
- Configuration (including secrets like the WaniKani API key) is provided to the application as environment variables, as per the [Twelve-Factor App](https://12factor.net) approach

### Privileges
When [creating your WaniKani API key](https://www.wanikani.com/settings/personal_access_tokens) for use with these scripts, a read-only token is perfectly sufficient, so you may leave all extra privilege boxes unchecked to created your key.

### Credentials
However you decide to run these scripts, you will need to provide your own `.env` file:
`cp example.env .env`
`vim .env  # open in your preferred text editor and paste in your own WaniKani API key as the value of API_KEY`
Note that the `MAX_LEVEL` may also be customized. You will likely prefer to enter your current level. 3 is the highest WaniKani level that is available without a paid subscription.

### Docker build and run

```
# e.g., supply the tag as appropriate: 
docker build ./ -t wanikani-get-sentences:v0.0.1
docker run --env-file .env wanikani-get-sentences:v0.0.1 ./get-sentences.py # supply your .env file and which script to run
```

### Local Python run

```
# within directory WaniKani2Anki/
pipenv shell  # pipenv will export the contents of your .env file for you
pipenv sync
python3 get-vocab-sentences/get-sentences.py
```




