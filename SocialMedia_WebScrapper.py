import csv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from googlesearch import search
from twitterscraper import query_tweets
from datetime import date
import datetime as dt
import pandas as pd 
import json


global date_today 

class company_news:

	def news(self):
		
		try: 
		    from googlesearch import search 
		except ImportError:  
		    print("No module named 'google' found") 
		  
		# to search 
		query = "QUERY HERE"
		print("for the last 24 Hours")
		query_syntax = search(query, tld="com", tbs="qdr:d", num=5, stop=10, pause=2)	
		date_today = date.today().strftime("%d/%m/%Y")
		with open('Google.csv', mode='a', newline='') as csv_file:
			fieldnames = ['URL/Link of Article - ',  'Date']
			writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
			writer.writeheader()
			for j in query_syntax:
				writer.writerow({'URL/Link of Article - ': j, 'Date': date_today})
				print(j)
		print("------") 
		    		    		    		
mnk_news = company_news()
mnk_news.news()

class social_media_scraping:

	def max(self):
		
		try: 
		    from googlesearch import search 
		except ImportError:  
		    print("No module named 'google' found") 
		  
		# to search 
		inomax_query_1 = "Medical"
		print("Medicine")
		date_today = date.today().strftime("%d/%m/%Y")		
		query_syntax = search(inomax_query_1, tld="com", tbs="qdr:d", num=5, stop=10, pause=2)
		with open('Google.csv', mode='a', newline='') as csv_file:
			fieldnames = ['URL/Link of Article - Inomax', 'Date']
			writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
			writer.writeheader()
			for j in query_syntax:
				writer.writerow({'URL/Link of Article - ': j, 'Date': date_today})
				print(j)
		print("------")     		    		    		
medical = social_media_scraping()
medical.max()



class twitter_scrape_results:

	def scrape_tweets(self):
		print("Twitter Posts")
		begin_date = dt.date(2020,3,23)
		end_date = dt.date(2020,4,6)
		tweet_limit = 1000
		language = 'english'
		tweets = query_tweets('Lawsuit', begindate = begin_date, enddate = end_date, limit = tweet_limit, lang = language)
		df = pd.DataFrame(t.__dict__ for t in tweets)
		print(df.columns.values)
		df1 = df.iloc[:,0:20]
		df1.to_csv('Twitter.csv')
twitter_results = twitter_scrape_results()
twitter_results.scrape_tweets()





