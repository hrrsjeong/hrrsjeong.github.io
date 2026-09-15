#!/usr/bin/env python3
"""Check the rendered English/Korean pages: python3 bin/check_localization.py _site."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote
import re
import sys

class Page(HTMLParser):
    def __init__(self, path):
        super().__init__()
        self.lang = None
        self.links = []
        self.assets = []
        self.alternates = {}
        self.inputs = []
        self.text = []
        self.styles = []
        self.in_style = False
        self.feed(path.read_text())

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'html': self.lang = attrs.get('lang')
        if tag == 'a': self.links.append(attrs)
        if tag == 'img': self.assets.append(attrs['src'])
        if tag == 'input': self.inputs.append(attrs)
        if tag == 'link' and attrs.get('rel') == 'alternate':
            self.alternates[attrs.get('hreflang')] = urlsplit(attrs['href']).path
        if tag == 'style': self.in_style = True

    def handle_endtag(self, tag):
        if tag == 'style': self.in_style = False

    def handle_data(self, text):
        (self.styles if self.in_style else self.text).append(text)

root = Path(sys.argv[1] if len(sys.argv) > 1 else '_site')
source = Path(__file__).resolve().parents[1]

def output(url):
    path = root / unquote(urlsplit(url).path).lstrip('/')
    return path / 'index.html' if urlsplit(url).path.endswith('/') else path

def main_text(path):
    html = path.read_text().split('role="main">', 1)[1].split('<footer', 1)[0]
    html = re.sub(r'<(?:style|script)\b[^>]*>[\s\S]*?</(?:style|script)>', '', html)
    parser = Page(path)
    parser.text = []
    parser.feed(html)
    return ' '.join(' '.join(parser.text).split())

pairs = {}
for path in (source / '_pages/ko').glob('*.md'):
    front = path.read_text().split('---', 2)[1]
    en = re.search(r'^translation_of: (.+)$', front, re.M).group(1)
    ko = re.search(r'^permalink: (.+)$', front, re.M).group(1)
    assert en not in pairs, f'Duplicate translation: {en}'
    pairs[en] = ko

for en, ko in pairs.items():
    pages = [Page(output(en)), Page(output(ko))]
    for url, language, page in zip([en, ko], ['en', 'ko'], pages):
        assert page.lang == language, (url, page.lang)
        assert page.alternates['en'] == en and page.alternates['ko'] == ko, url
        switches = [a for a in page.links if 'data-language-link' in a]
        assert [a['href'] for a in switches] == [en, ko], (url, switches)
        current = [a for a in switches if a.get('aria-current') == 'true']
        assert len(current) == 1 and current[0]['lang'] == language, url
        for asset in page.assets:
            if asset.startswith('/') and not asset.startswith('//'):
                assert output(asset).is_file(), (url, asset)
    for a in pages[1].links:
        href = a.get('href', '')
        path = urlsplit(href).path
        if path.startswith('/ko/'):
            assert output(path).is_file(), (ko, href)
        if not urlsplit(href).netloc:
            assert path not in pairs or 'data-language-link' in a, (ko, 'English link in Korean page', href)
    # Translations reuse their source page's CSS, preserving responsive layout.
    if pages[0].styles and en != '/404.html':
        assert ''.join(pages[0].styles).strip() == ''.join(pages[1].styles).strip(), (en, 'style mismatch')
    if en.startswith('/people/'):
        assert main_text(output(en)) == main_text(output(ko)), (en, 'Team and profile content must stay in English')
        assert re.search(r'<div class="post"[^>]*\blang="en"', output(ko).read_text()), ko

for lang, prefix in [('en', ''), ('ko', '/ko')]:
    for url in ['/', '/people/', '/research/', '/publications/', '/join/']:
        page = Page(output(prefix + url))
        for target in ['/', '/people/', '/research/', '/publications/', '/join/']:
            assert any(a.get('href') == prefix + target for a in page.links), (prefix + url, target)
    for url in ['/join/graduate-research/', '/join/undergraduate-research/']:
        content = ' '.join(Page(output(prefix + url)).text)
        assert bool(re.search('[가-힣]', content.replace('한국어', ''))) == (lang == 'ko'), (url, lang)

ko_publications = ' '.join(Page(output('/ko/publications/')).text)
assert '초록' in ko_publications
for url in ['/publications/', '/ko/publications/']:
    page = Page(output(url))
    search = [field for field in page.inputs if field.get('id') == 'bibsearch']
    assert len(search) == 1 and search[0].get('type') == 'text', (url, 'Missing search input')
    assert search[0].get('aria-label') and search[0].get('placeholder'), url
    assert '<input' not in ' '.join(page.text), (url, 'Search markup displayed as text')
ko_home = ' '.join(Page(output('/ko/')).text)
assert 'Hyeongwoo Choi 박사가 박사후연구원으로 합류했습니다.' in ko_home
print(f'PASS: {len(pairs)} language pairs, reciprocal switches, localized navigation, assets, metadata, shared styles and translated content')
