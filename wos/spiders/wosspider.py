import sys
from scrapy.spider import Spider
from scrapy.selector import Selector
from scrapy.http.request import Request


class wosspider(Spider):
    name = "wos"
    allowed_domains = ["webofknowledge.com"]
    start_urls = [
        "https://apps.webofknowledge.com/UA_GeneralSearch_input.do?product=UA&search_mode=GeneralSearch&SID=S1gYy2Ai9CpWEPRHO34&preferencesSaved=",
        "https://apps.webofknowledge.com/Search.do?product=UA&SID=S1gYy2Ai9CpWEPRHO34&search_mode=GeneralSearch&prID=ac5724a0-4754-4451-a360-0468a37af23e"
    ]
https://apps.webofknowledge.com/summary.do?product=UA&parentProduct=UA&search_mode=GeneralSearch&parentQid=&qid=3&SID=S1gYy2Ai9CpWEPRHO34&&update_back2search_link_param=yes&page=2
    def start_requests(self):
        for url in self.start_urls:
            yield Request(url, cookies={'CUSTOMER': "Northwestern Polytechnical University",
                                        'E_GROUP_NAME': "Northwestern Polytechnical University",
                                        'JSESSIONID': '15B405100C51FF3CBD3B916EE9B05382',
                                        'SID': "S1gYy2Ai9CpWEPRHO34"})

    def parse(self, response):
    	print 
    	print response.xpath('//*[@id="RECORD_1"]/div[3]/div[1]/div/a/value/text()').extract()
    	print response.xpath('//*[@id="RECORD_1"]/div[3]/div[1]/div/a/@href').extract()
        # print response.body
