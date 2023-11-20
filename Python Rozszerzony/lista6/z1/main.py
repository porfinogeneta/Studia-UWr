from bs4 import BeautifulSoup
import re
import requests



def parse_href(current_orig, href):
    # it's an outside link we parse it without concatenation
    if href.startswith("http://") or href.startswith("https://"):
        return href
    else:
        return current_orig + href


def crawl(orig_start_page, full_address, distance, action):
    # orig_start_page - orginal local prefix
    # full_address - address prefix + local href as well as outside websites
    # end of recursion
    if distance < 0:
        yield (), ()
        return
    # retrieve page
    response = requests.get(full_address)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        # main issue - retriving local links without prefix as well as normal links with http/s prefix

        # collect all links
        # we will get links either in form of '/tag/miracles/page/1/' -> need to be extended by orig_start_page or http...
        web_links = soup.select('a') # get links from href tags
        # get all links including ones local for the page, so https:// as well as /index1/hello.html
        # check if parsed version were already checked
        address_links = set(
            filter(lambda link: parse_href(orig_start_page, link) not in checked, [link.get('href', '') for link in web_links]))

        # action
        all_text = soup.get_text()
        pattern = re.compile(r'([A-Z][^.!?]*[.!?])', re.M) # retrieve all sentences
        sentences = pattern.findall(all_text)
        action_res = list(filter(action, sentences))

        # add current link to already checked, so we won't check it again
        # we add link in a full form of https://all_including_local_hrefs
        checked.add(full_address)
        # print(list(address_links))
        # orig_start_page + href => http://quotes.toscrape.com/ + /author/Albert-Einstein
        for href in address_links:
            # an outside website is linked
            if href.startswith("http://") or href.startswith("https://"):
                # we change original link in recursive calls
                yield from crawl(href, href, distance - 1, action)
            else:
                # our address to search is http://quotes.toscrape.com/ + /author/Albert-Einstein = http://quotes.toscrape.com//author/Albert-Einstein
                yield from crawl(orig_start_page, orig_start_page + href, distance - 1, action)

            # crawl(start_page + link, distance - 1, action)

        yield (full_address, action_res)
    else:
        print("Failed to retrieve an address")


if __name__ == '__main__':
    # set of checked websites
    checked = set()
    for url, wynik in crawl('https://docs.python-guide.org/', 'https://docs.python-guide.org/writing/documentation/', 1,
                            lambda text: 'Python' in text):
        # print only non empty
        if (url and wynik):
            print(f"{url}: {wynik}")
