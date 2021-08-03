# -*- coding: utf-8 -*-
import scrapy
from douban.items import DoubanItem

class DoubanSpiderSpider(scrapy.Spider):
    #这里是爬虫名
    name = 'douban_spider'
    #允许的域名
    allowed_domains = ['movie.douban.com']
    #入口URL,扔到调度器里,这里需要配置具体需要抓取的URL
    start_urls = ['https://movie.douban.com/top250']

    def parse(self, response):
        movie_list = response.xpath("//div[@class = 'article']//ol[@class = 'grid_view']/li")
        for i_item in movie_list:
            #item文件导入
            douban_item = DoubanItem()
            #写详细的xpath,进行数据的解析(“extract_first()”方法表示获取第一个内容，而“extract”会把所有结果都找出来)
            douban_item['serial_number'] = i_item.xpath(".//div[@class = 'item']//em/text()").extract_first()
            douban_item['movie_name'] = i_item.xpath(".//div[@class = 'info']/div[@class = 'hd']/a/span[1]/text()").extract_first()
            content = i_item.xpath(".//div[@class = 'info']//div[@class = 'bd']/p[1]/text()").extract()
            #进行多行数据处理
            for i_content in content:
                content_s = "".join(i_content.split())
                douban_item['introduce'] = content_s
            douban_item['star'] = i_item.xpath(".//span[@class = 'rating_num']/text()").extract_first()
            douban_item['evaluate'] = i_item.xpath(".//div[@class = 'star']//span[4]/text()").extract_first()
            douban_item['describe'] = i_item.xpath(".//div[@class = 'bd']/p[@class = 'quote']/span/text()").extract_first()
            #你需要将数据yield到pipelines里面去,这里的yield当成一个返回就行,只不过这里是一个生成器的返回.这块查过资料.
            yield douban_item
        #解析下一页规则,取的后页的xpath
        next_link = response.xpath("//span[@class = 'next']/link/@href").extract()
        if next_link:
            #如果连接有就取,如果没有就不取
            next_link = next_link[0]
            yield scrapy.Request("https://movie.douban.com/top250" + next_link,callback=self.parse)