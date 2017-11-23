from gensim.summarization import summarize
from bs4 import BeautifulSoup
import requests

#
# This recipe uses automatic computer science Paper generation tool from mit.edu
# You can generate your own paper by visiting https://pdos.csail.mit.edu/archive/scigen/
# and click generate.
#
# This example needs large amount of text that needs to be available for summary.
# So, we are using this paper generation tool and extracting the 'Introduction' section
# to do the summary analysis.
#

urls = {
    'Daff: Unproven Unification of Suffix Trees and Redundancy': 'http://scigen.csail.mit.edu/scicache/610/scimakelatex.21945.none.html',
    'CausticIslet: Exploration of Rasterization': 'http://scigen.csail.mit.edu/scicache/790/scimakelatex.1499.none.html'
}

for key in urls.keys():
    url = urls[key]
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    data = soup.get_text()
    pos1 = data.find("1  Introduction") + len("1  Introduction")
    pos2 = data.find("2  Related Work")
    text = data[pos1:pos2].strip()
    print("PAPER URL: {}".format(url))
    print("TITLE: {}".format(key))
    print("GENERATED SUMMARY: {}".format(summarize(text)))
    print()
