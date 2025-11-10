from abc import ABC, abstractmethod


class Downloader(ABC):

    @abstractmethod
    def download(self, url: str) -> bytes:
        pass


class SimpleDownloader(Downloader):

    def download(self, url: str) -> bytes:
        print(f"Downloading: {url}")
        return f"data from {url}".encode("utf-8")


class CachedDownloaderProxy(Downloader):

    def __init__(self, downloader: Downloader):
        self._downloader = downloader
        self._cache = {}

    def download(self, url: str) -> bytes:
        if url in self._cache:
            print(f"Got from cache: {url}")
            return self._cache[url]

        data = self._downloader.download(url)
        self._cache[url] = data
        return data


class Page(ABC):
    @abstractmethod
    def render(self, downloader: Downloader):
        pass


class SimplePage(Page):
    def render(self, downloader: Downloader):
        downloader.download("http://site.com/simple.png")
        print("simple page")


class ProductPage(Page):
    def render(self, downloader: Downloader):
        downloader.download("http://site.com/product.png")
        print("product page")


if __name__ == "__main__":

    downloader = CachedDownloaderProxy(SimpleDownloader())
    pages = [SimplePage(), ProductPage(), SimplePage()]

    for p in pages:
        print("page rende")
        p.render(downloader)
