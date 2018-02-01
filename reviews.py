
"""
Created on Wed Jan 31 14:04:52 2018

@author: Wey Hwang
"""
import scrapy

class ReviewsSpider(scrapy.Spider):
    name = "reviews_spider"
    start_urls =['https://www.tripadvisor.com/Hotel_Review-g298314-d6514509-Reviews-Tune_Hotel_KLIA_2-Sepang_Sepang_District_Selangor.html',
    'https://www.tripadvisor.com/Hotel_Review-g298570-d663497-Reviews-Tune_Hotel_Kuala_Lumpur-Kuala_Lumpur_Wilayah_Persekutuan.html',
    'https://www.tripadvisor.com/Hotel_Review-g298314-d10758776-Reviews-Tune_Hotel_KLIA_Aeropolis-Sepang_Sepang_District_Selangor.html', 
    'https://www.tripadvisor.com/Hotel_Review-g298312-d6387320-Reviews-Tune_Hotel_DPulze_Cyberjaya-Cyberjaya_Sepang_District_Selangor.html',
    'https://www.tripadvisor.com/Hotel_Review-g298278-d1770042-Reviews-Tune_Hotel_Danga_Bay-Johor_Bahru_Johor_Bahru_District_Johor.html',
    'https://www.tripadvisor.com/Hotel_Review-g298303-d1231105-Reviews-Tune_Hotel_Georgetown_Penang-George_Town_Penang_Island_Penang.html',
    'https://www.tripadvisor.com/Hotel_Review-g298307-d1072974-Reviews-Tune_Hotel_1Borneo_Kota_Kinabalu-Kota_Kinabalu_Kota_Kinabalu_District_West_Coast_Divis.html'
    ]
    
    def parse(self,response):
        for review in response.css('div.review-container'):
            yield {
            'hotel_name': response.css('h1.heading::text').extract_first(),
            'review_title': review.css('span.noQuotes::text').extract_first(),
            'review_body': review.css('p.partial_entry::text').extract_first(),
            'review_date': review.css('span.relativeDate').xpath("@title").extract_first(),
            'reviewer_name': review.css('span.scrname::text').extract_first(),
            'bubble_rating': review.css('span.ui_bubble_rating').xpath("@class").extract_first()[24]

        }
    
            
