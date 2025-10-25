#!/usr/bin/env python3
import scrapy


class ExampleSpider(scrapy.Spider):
    name = "example"
    allowed_domains = ["mohiafrica.org"]
    start_urls = ["https://mohiafrica.org"]
    visited = set()  # keep track of visited URLs to prevent loops

    def parse(self, response):
        # Extract all links from the current page
        for link in response.css('a::attr(href)').getall():
            absolute = response.urljoin(link)

            # Follow only internal pages within mohiafrica.org
            if "mohiafrica.org" in absolute and absolute not in self.visited:
                self.visited.add(absolute)
                yield {"link": absolute}
                yield response.follow(absolute, callback=self.parse)
#!/usr/bin/env python3
import scrapy


class ExampleSpider(scrapy.Spider):
    name = "example"
    allowed_domains = ["mohiafrica.org"]
    start_urls = ["https://mohiafrica.org"]

    def parse(self, response):
        # Extract all links from the homepage
        for link in response.css('a::attr(href)').getall():
            yield {"link": response.urljoin(link)}

