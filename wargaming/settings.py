from wargaming.version import get_version

ALLOWED_GAMES = ('wot', 'wgn', 'wows', 'wotb', 'wotx', 'wowp')

ALLOWED_REGIONS = ('ru', 'asia', 'na', 'eu', 'kr', 'xbox', 'ps4')
REGION_API_ENDPOINTS = {
    'ru': 'ru',
    'asia': 'asia',
    'na': 'com',
    'eu': 'eu',
    'kr': 'kr',
    'xbox': 'com',
    'ps4': 'com'
}
GAME_API_ENDPOINTS = {
    'wot': 'api.worldoftanks',
    'wotb': 'api.wotblitz',
    'wows': 'api.worldofwarships',
    'wotx': 'api-{}-console.worldoftanks',
    'wowp': 'api.worldofwarplanes',
    'wgn': 'api.worldoftanks'
}
DEFAULT_REGION = 'ru'

ALLOWED_LANGUAGES = ('en', 'ru', 'pl', 'de', 'fr', 'es', 'zh-cn', 'tr', 'cs', 'th', 'vi', 'ko')
DEFAULT_LANGUAGE = 'en'

HTTP_USER_AGENT_HEADER = 'python-wargaming/{0} (https://github.com/svartalf/python-wargaming)'.format(get_version())

# How many times retry api call
RETRY_COUNT = 10
