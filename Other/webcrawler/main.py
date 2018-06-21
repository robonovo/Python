import threading
from queue import Queue
from spider import Spider
from domain import *
from fileops import *


def crawl():
    queued_links = file_to_set(queue_file)
    if len(queued_links) > 0:
        print(str(len(queued_links)) + ' Links in the queue')
        create_jobs(queued_links)


def create_jobs(links):
    for link in links:
        queue.put(link)
        queue.join()
        crawl()


def create_workers():
    for _ in range(number_of_threads):
        t = threading.Thread(target=work)
        t.daemon = True
        t.start()


def work():
    while True:
        url = queue.get()
        Spider.crawl_page(threading.current_thread().name, url)
        queue.task_done()


if __name__ == "__main__":
    project_name = input('Enter the project name: ')
    home_page = input('Enter the site to be crawled (include the http://): ')
    domain_name = get_domain_name(home_page)
    queue_file = project_name + '/queue.txt'
    crawled_file = project_name + '/crawled.txt'
    number_of_threads = 8
    queue = Queue()
    Spider(project_name, home_page, domain_name)
    create_workers()
    crawl()
