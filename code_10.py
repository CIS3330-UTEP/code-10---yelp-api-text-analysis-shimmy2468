import pandas as pd
from yelpapi import YelpAPI 



api_key="I1IOqaJO_GmgvsxusTF7udhYmBMKPTkGYRvTfCymqfp_epg-CJOkrd9HzSk7Ga4HYQdTNdAiM8O-h6fNpx5dnQksa7lCCmNuVl5_Jc-w1rYxmIYUbjbS7i-LVz1IZXYx" 
yelp_api = YelpAPI(api_key)
search_term = "ramen"
location_term = "Pittsburgh, PA"
search_results = yelp_api.search_query(term=search_term, location=location_term, sort_by='rating', limit=20, offset=20)
# List of results in search_results['businesses']
print(search_results)

result_df = pd.DataFrame.from_dict(search_results['businesses'])
result_df.to_csv("yelpapi_businesses_results.csv")

#Business 1

id_for_reviews = "ramen-king-canonsburg-3" #use alias from data 
review_response = yelp_api.reviews_query(id=id_for_reviews) # List of reviews in review_response['reviews']
print(review_response)
#Text is in element (review) text
for review in review_response['reviews']:
    print(review['text'])
#Converting list of json objects to Pandas Data Frame
result_df = pd.DataFrame.from_dict (review_response['reviews']) 
print(result_df)
result_df.to_csv(f"{id_for_reviews}_yelpapi_businesses_results.csv")

#business 2

id_for_reviews = "little-tokyo-pittsburgh" #use alias from data 
review_response = yelp_api.reviews_query(id=id_for_reviews) # List of reviews in review_response['reviews']
print(review_response)
#Text is in element (review) text
for review in review_response['reviews']:
    print(review['text'])
#Converting list of json objects to Pandas Data Frame
result_df = pd.DataFrame.from_dict (review_response['reviews']) 
print(result_df)
result_df.to_csv(f"{id_for_reviews}_yelpapi_businesses_results.csv")

#business 3

id_for_reviews = "fujiya-ramen-pittsburgh-2" #use alias from data 
review_response = yelp_api.reviews_query(id=id_for_reviews) # List of reviews in review_response['reviews']
print(review_response)
#Text is in element (review) text
for review in review_response['reviews']:
    print(review['text'])
#Converting list of json objects to Pandas Data Frame
result_df = pd.DataFrame.from_dict (review_response['reviews']) 
print(result_df)
result_df.to_csv(f"{id_for_reviews}_yelpapi_businesses_results.csv")


#business 4

id_for_reviews = "eiwa-japanese-ramen-and-bar-pittsburgh" #use alias from data 
review_response = yelp_api.reviews_query(id=id_for_reviews) # List of reviews in review_response['reviews']
print(review_response)
#Text is in element (review) text
for review in review_response['reviews']:
    print(review['text'])
#Converting list of json objects to Pandas Data Frame
result_df = pd.DataFrame.from_dict (review_response['reviews']) 
print(result_df)
result_df.to_csv(f"{id_for_reviews}_yelpapi_businesses_results.csv")


#business 5

id_for_reviews = "love-ramen-pittsburgh-7" #use alias from data 
review_response = yelp_api.reviews_query(id=id_for_reviews) # List of reviews in review_response['reviews']
print(review_response)
#Text is in element (review) text
for review in review_response['reviews']:
    print(review['text'])
#Converting list of json objects to Pandas Data Frame
result_df = pd.DataFrame.from_dict (review_response['reviews']) 
print(result_df)
result_df.to_csv(f"{id_for_reviews}_yelpapi_businesses_results.csv")


from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()
review_response = pd.read_csv('ramen-king-canonsburg-3_yelpapi_businesses_results.csv')

for review in review_response['text']:
    sentiment_score = analyzer.polarity_scores(review)
    print(review)
    print(sentiment_score)
    print('\n')


analyzer = SentimentIntensityAnalyzer()
review_response = pd.read_csv('love-ramen-pittsburgh-7_yelpapi_businesses_results.csv')

for review in review_response['text']:
    sentiment_score = analyzer.polarity_scores(review)
    print(review)
    print(sentiment_score)
    print('\n')


analyzer = SentimentIntensityAnalyzer()
review_response = pd.read_csv('little-tokyo-pittsburgh_yelpapi_businesses_results.csv')

for review in review_response['text']:
    sentiment_score = analyzer.polarity_scores(review)
    print(review)
    print(sentiment_score)
    print('\n')


analyzer = SentimentIntensityAnalyzer()
review_response = pd.read_csv('fujiya-ramen-pittsburgh-2_yelpapi_businesses_results.csv')

for review in review_response['text']:
    sentiment_score = analyzer.polarity_scores(review)
    print(review)
    print(sentiment_score)
    print('\n')



analyzer = SentimentIntensityAnalyzer()
review_response = pd.read_csv('eiwa-japanese-ramen-and-bar-pittsburgh_yelpapi_businesses_results.csv')

for review in review_response['text']:
    sentiment_score = analyzer.polarity_scores(review)
    print(review)
    print(sentiment_score)
    print('\n')






