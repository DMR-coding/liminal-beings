from bs4 import BeautifulSoup

BEGINNING = '''
<!-- This section is required only once per page, before any videos appear. -->
<link type="text/css" rel="stylesheet" href="https://ozplayer.global.ssl.fastly.net/3.5/ozplayer-core/ozplayer.min.css" media="all" />
<link type="text/css" rel="stylesheet" href="https://ozplayer.global.ssl.fastly.net/3.5/ozplayer-skin/highlights-blue.css" media="all" />
<link type="text/css" rel="stylesheet" href="https://ozplayer.global.ssl.fastly.net/3.5/transcript.css" media="all" />
<script type="text/javascript" src="https://ozplayer.global.ssl.fastly.net/3.5/ozplayer-core/mediaelement.min.js"></script>
<script type="text/javascript" src="https://ozplayer.global.ssl.fastly.net/3.5/ozplayer-core/ozplayer.free.js"></script>
<script type="text/javascript" src="https://ozplayer.global.ssl.fastly.net/3.5/ozplayer-lang/en.js"></script>
'''

END = '''
'''

doc = None
with open("./index.html", "r") as fp:
    soup = BeautifulSoup(fp, features="html.parser")

    soup.head.append(BeautifulSoup(BEGINNING), features="html.parser")
    soup.body.append(BeautifulSoup(END), features="html.parser")

    doc = str(soup)

with open("./index.html", "w") as fp:
    fp.write(doc)
