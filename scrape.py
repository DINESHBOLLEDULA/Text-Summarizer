from goose3 import Goose
my_goose = Goose()
def scrape_text(url):
    text=my_goose.extract(url)
    return text.cleaned_text