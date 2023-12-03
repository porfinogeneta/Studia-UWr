from bs4 import BeautifulSoup
import re
import requests
from urllib.parse import urljoin
import threading, queue



def find_sentences(all_text):
    pattern = re.compile(r'([A-Z][^.!?]*[.!?])', re.M)  # retrieve all sentences
    sentences = pattern.findall(all_text)
    return list(filter(lambda text: 'that' in text, sentences))

def true_crawl(start_page, distance, action):
    # set of checked websites
    checked = set()
    # create a lock for checked
    # https://docs.python.org/3/glossary.html#term-global-interpreter-lock
    # we use lock whenever we try to access/modify checked
    # it's thread-safe, according to docs because it blocks the resource to be accessed only
    # by one thread at a time
    lock = threading.Lock()
    # create results Queue
    # we put all results inside a Queue
    results = queue.Queue()
    def crawl(start_page, distance, action):

        # orig_start_page - orginal local prefix
        # full_address - address prefix + local href as well as outside websites
        # end of recursion
        if distance < 0:
            return
        # retrieve page
        response = requests.get(start_page)

        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')

            # collect all links
            # we will get links either in form of '/tag/miracles/page/1/' -> need to be extended by orig_start_page or http...
            web_links = soup.select('a') # get links from href tags
            # get all links including ones local for the page, so https:// as well as /index1/hello.html
            # check if parsed version were already checked
            address_links = set()
            for link in web_links:
                href = link.get('href', '').strip()
                if href and not href.startswith(('http://', 'https://')):
                    # our base is the base of the start_page
                    base_url = urljoin(start_page, '.')
                    full_url = urljoin(base_url, href)
                    # add link only if not already checked

                    with lock:
                        if full_url not in checked:
                            address_links.add(full_url)
                else:
                    with lock:
                        if href not in checked:
                            # add link only if not already checked
                            address_links.add(href)


            # action
            all_text = soup.get_text()
            action_res = action(all_text)
            # put current result inside a queue
            results.put((start_page, action_res))

            # add current link to already checked, so we won't check it again
            # we add link in a full form of https://all_including_local_hrefs
            # add to checked while also protecting checked resource
            with lock:
                checked.add(start_page)

            threads = []
            for proper_address in address_links:
                # create thread and add to threads list
                thread = threading.Thread(target=crawl, args=(proper_address, distance - 1, action))
                thread.start()
                threads.append(thread)
                # # new start_page are the addresses from the links
                # yield from crawl(proper_address, distance - 1, action)
            # wait for each thread to resolve
            for thread in threads:
                thread.join()

            # yield (start_page, action_res)
        else:
            print("Failed to retrieve an address")

    # run normal crawl
    crawl(start_page, distance, action)

    # yield the prepared results
    while not results.empty():
        yield results.get()


if __name__ == '__main__':
    # pass reference to the function
    for url, wynik in true_crawl('http://quotes.toscrape.com/', 1, find_sentences):
        # print only non empty
        if (url and wynik):
            print(f"{url}: {wynik}")
