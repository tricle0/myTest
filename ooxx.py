import urllib.request
import os


def get_page(url):
    req = urllib.request.Request(url)
    req.add_header('User-Agent',
                   'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36')
    response = urllib.request.urlopen(req)
    html = response.read().decode('utf-8')


def find_imgs(url):
    pass


def save_imgs(url):
    filename = 'a'
    with open(filename, 'wb') as f:
        img = 'imgdata'
        f.write(img)


def download_mm(folder='ooxx', pages=10):
    if not os.path.exists(folder):
        os.mkdir(folder)
    os.chdir(folder)

    url = "http://jandan.net/ooxx"
    page_num = int(get_page(url))

    for i in range(pages):
        page_num -= i
        page_url = url + 'page-' + str(page_num) + '#comments'
        img_addrs = find_imgs(page_url)
        save_imgs(folder, img_addrs)


if __name__ == '__main__':
    download_mm()
