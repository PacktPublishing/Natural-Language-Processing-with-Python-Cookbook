import nltk
import threading
import queue
import feedparser
import uuid

threads = []
queues = [queue.Queue(), queue.Queue()]

def extractWords():
    url = 'https://timesofindia.indiatimes.com/rssfeeds/1081479906.cms'
    feed = feedparser.parse(url)
    for entry in feed['entries'][:5]:
        text = entry['title']
        if 'ex' in text:
            continue
        words = nltk.word_tokenize(text)
        data = {'uuid': uuid.uuid4(), 'input': words}
        queues[0].put(data, True)
        print(">> {} : {}".format(data['uuid'], text))

def extractPOS():
    while True:
        if queues[0].empty():
            break
        else:
            data = queues[0].get()
            words = data['input']
            postags = nltk.pos_tag(words)
            queues[0].task_done()
            queues[1].put({'uuid': data['uuid'], 'input': postags}, True)

def extractNE():
    while True:
        if queues[1].empty():
            break
        else:
            data = queues[1].get()
            postags = data['input']
            queues[1].task_done()
            chunks = nltk.ne_chunk(postags, binary=False)
            print("  << {} : ".format(data['uuid']), end = '')
            for path in chunks:
                try:
                    label = path.label()
                    print(path, end=', ')
                except:
                    pass
            print()

def runProgram():
    e = threading.Thread(target=extractWords())
    e.start()
    threads.append(e)

    p = threading.Thread(target=extractPOS())
    p.start()
    threads.append(p)

    n = threading.Thread(target=extractNE())
    n.start()
    threads.append(n)

    queues[0].join()
    queues[1].join()

    for t in threads:
        t.join()

if __name__ == '__main__':
    runProgram()
