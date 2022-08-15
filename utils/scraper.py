
from requests import get
from bs4 import BeautifulSoup

_URL = 'https://www.fundsexplorer.com.br/ranking'
_PARSER = 'html.parser'


def scrap():

    _page = BeautifulSoup(get(_URL).content, _PARSER)
    _trs = _page.find_all('tr')

    # HEADERS
    _headers = [BeautifulSoup(str(_a).replace(
        '<br/>', ' '), _PARSER).get_text() for _a in _trs[0].find_all('th')]

    # DATA
    _bodys = []
    _idx = 1
    while _idx < len(_trs):
        _tmp = []
        for a in _trs[_idx].find_all('td'):
            _tmp.append(a.get_text())
        _bodys.append(_tmp)
        _idx += 1

    return _headers, _bodys
