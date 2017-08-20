import json, codecs, requests, pickle, datetime
import urllib.request, urllib.parse, urllib.error
from googleapiclient.discovery import build 
from itertools import repeat
from unidecode import unidecode
from bs4 import BeautifulSoup
import html2text

# AVAILABLE_TOKEN_SETS = {
#     'ess': {
#         'api_key': 'AIzaSyB_QXKEohLw7XvtgecsshkzkqUOJ8FzSCc',
#         'cse_id': '009043117829057268965:tgiqlni9v2w'
#     },
#     'ssk': {
#         'api_key': 'AIzaSyAn_YOSbC43zmv2cexCddaIYfJfMb9d08s',
#         'cse_id': '003565523015477317201:lwtcnf2u57i'
#     }
# }

# NAME_OF_TOKEN_SET_TO_USE_FOR_THIS_RUN = 'ess'

# API_KEY_TO_USE_FOR_THIS_RUN = AVAILABLE_TOKEN_SETS[NAME_OF_TOKEN_SET_TO_USE_FOR_THIS_RUN]['api_key']
# CSE_ID_TO_USE_FOR_THIS_RUN = AVAILABLE_TOKEN_SETS[NAME_OF_TOKEN_SET_TO_USE_FOR_THIS_RUN]['cse_id']

CODEFORCASH_BASE_URL = 'https://i.codefor.cash'
CODEFORCASH_API_KEY = '5b26197b391c5dab05c5606d43fba9c6'

# MAXIMUM_NUMBER_OF_SEARCH_RESULTS_PER_GOOGLE_API_QUERY = 10

# def do_google_search(search_term, api_key, cse_id, **kwargs):
#     service = build("customsearch", "v1", developerKey=api_key)
#     res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
#     return res['items']

results_from_GSE_query = [
    {
        "cacheId": "FKYdclr58rAJ",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/clerky/59623abf-f7d6-425a-bacb-53ddeaf5035e",
        "htmlFormattedUrl": "https://jobs.lever.co/clerky/59623abf-f7d6-425a-bacb-53ddeaf5035e",
        "htmlSnippet": "<b>Junior</b> Software Engineer. <b>Remote</b>. Product. Full-time. Apply for this job. Help fix <br>\nthe legal ... As a <b>junior</b> software engineer at Clerky, you will: Maintain and add&nbsp;...",
        "htmlTitle": "Clerky - <b>Junior</b> Software Engineer",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/clerky/59623abf-f7d6-425a-bacb-53ddeaf5035e",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/84963f7c-5208-4789-813f-59b515174479-1451935950706.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "40",
                    "src": "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcTVWJmxfo4IYHwoLO1aPEGSPTMcRZyVWULWTxp8OOJkQmA0T-jws1yhhw",
                    "width": "220"
                }
            ],
            "metatags": [
                {
                    "og:description": "Help fix the legal industry! The way legal transactions are done is filled with inefficiencies, which leads to ridiculously high legal fees. We're fixing this by building software that automates and streamlines the process. We're profitable and growing sustainably. We're the most popular way for high-growth technology startups to incorporate. Y Combinator and other top accelerators use our software to handle their investment paperwork. Our product is used by tons of top tier startups and investors. We're a quiet leader in the legal technology space - if you are interested in changing the legal industry, this is arguably the best place to be.",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/84963f7c-5208-4789-813f-59b515174479-1451935950706.png",
                    "og:image:height": "200",
                    "og:title": "Clerky - Junior Software Engineer",
                    "og:url": "https://jobs.lever.co/clerky/59623abf-f7d6-425a-bacb-53ddeaf5035e",
                    "twitter:description": "Help fix the legal industry! The way legal transactions are done is filled with inefficiencies, which leads to ridiculously high legal fees. We're fixing this by building software that automates and streamlines the process. We're profitable and growing sustainably. We're the most popular way for high-growth technology startups to incorporate. Y Combinator and other top accelerators use our software to handle their investment paperwork. Our product is used by tons of top tier startups and investors. We're a quiet leader in the legal technology space - if you are interested in changing the legal industry, this is arguably the best place to be.",
                    "twitter:title": "Clerky - Junior Software Engineer",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "Junior Software Engineer. Remote. Product. Full-time. Apply for this job. Help fix \nthe legal ... As a junior software engineer at Clerky, you will: Maintain and add\u00a0...",
        "title": "Clerky - Junior Software Engineer"
    },
    {
        "cacheId": "xwvcZPHOGWkJ",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/.../506b79db-9cde-4561-8465-d9d3d938d03e",
        "htmlFormattedUrl": "https://jobs.lever.co/.../506b79db-9cde-4561-8465-d9d3d938d03e",
        "htmlSnippet": "As a <b>Junior</b> Brand Designer, you aspire to embody the design team&#39;s mission, ... <br>\ndynamic work environment and are comfortable being productive in a <b>remote</b> or&nbsp;...",
        "htmlTitle": "Creative Market - <b>Junior</b> Brand Designer",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/polleverywhere/b86a2960-abd7-4995-b533-5eeed3c90546",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/8aa36117-4e98-402f-840a-de3de20f2942-1495061536581.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "116",
                    "src": "https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcRXPwUOeyzXjbDS69phkiz_gbOZ5WjEEgG86yngNrWnie3fk1RK11tA4Q",
                    "width": "300"
                }
            ],
            "metatags": [
                {
                    "og:description": "Overview Creative Market is the platform where independent creators around the world buy and sell digital design assets. Our mission is to help creators around the world turn passion into opportunity. As a Brand Designer, you will help make this mission a reality by creating strategic visual work that embodies Creative Market\u2019s brand system, sets our shop owners up for success, and inspires our community. You will collaborate with marketers, designers, community and support managers, and researchers on the entire project lifecycle. You will produce both small tests and larger projects aimed at increasing our MoM growth rate and increasing user acquisition, activation, and retention. Design Team Member As a Junior Brand Designer, you aspire to embody the design team\u2019s mission, vision, and principles. These should be reflected in all aspects of your work. You live & breathe great brand design thinking and visual execution and are passionate about improving our visual design system. You",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/8aa36117-4e98-402f-840a-de3de20f2942-1495061536581.png",
                    "og:image:height": "200",
                    "og:title": "Creative Market - Junior Brand Designer",
                    "og:url": "https://jobs.lever.co/creativemarket/506b79db-9cde-4561-8465-d9d3d938d03e",
                    "twitter:description": "Overview Creative Market is the platform where independent creators around the world buy and sell digital design assets. Our mission is to help creators around the world turn passion into opportunity. As a Brand Designer, you will help make this mission a reality by creating strategic visual work that embodies Creative Market\u2019s brand system, sets our shop owners up for success, and inspires our community. You will collaborate with marketers, designers, community and support managers, and researchers on the entire project lifecycle. You will produce both small tests and larger projects aimed at increasing our MoM growth rate and increasing user acquisition, activation, and retention. Design Team Member As a Junior Brand Designer, you aspire to embody the design team\u2019s mission, vision, and principles. These should be reflected in all aspects of your work. You live & breathe great brand design thinking and visual execution and are passionate about improving our visual design system. You",
                    "twitter:title": "Creative Market - Junior Brand Designer",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "As a Junior Brand Designer, you aspire to embody the design team's mission, ... \ndynamic work environment and are comfortable being productive in a remote or\u00a0...",
        "title": "Creative Market - Junior Brand Designer"
    }
]

def get_job_listings_from_google():
    data_get_job_listings_from_google = results_from_GSE_query
    return data_get_job_listings_from_google

def save_api_call_results(listings):
    with open('finalResults.txt','a+') as f:
        f.write(json.dumps(get_job_listings_from_google(), sort_keys = True,
                indent = 4))
#
def send_job_listings_to_codeforcash(listings):
    for listing in range(len(listings)):
        data_to_send_in_request_body = {
            "key": CODEFORCASH_API_KEY,
            "title": listings[listing]["title"],
            "website": listings[listing]["link"],
            # "description": listings[listing]["snippet"],
            "description": "",
            "utc_datetime": datetime.datetime.utcnow().isoformat(),
            "lat": "",
            "lng": "",
            "country": "",
            "employment_type": "",
            "remote_ok": "",
            "time_commitment": ""
        }
            # data_to_send_in_request_body[data_key] = data_to_send_in_request_body[data_key].replace(chr(128), '')
        
        data_send_job_lisitings_to_codeforcash = json.dumps(data_to_send_in_request_body)

        data_of_each_listing = json.loads(data_send_job_lisitings_to_codeforcash)
        
        soup = BeautifulSoup(urllib.request.urlopen(data_of_each_listing["website"]).read(), 'html.parser')
        
        # title_tag = soup.title.contents[0]

        description_array = []
        for row in (BeautifulSoup(urllib.request.urlopen(data_of_each_listing["website"]).read(), 'html.parser')).find_all('li'):
            description_array.append(row.text)
        description = "\n".join(description_array)

        data_to_send_in_request_body["description"] =description

        for data_key in data_to_send_in_request_body:
            data_to_send_in_request_body[data_key] = data_to_send_in_request_body[data_key].encode('UTF8')
        # print(data_to_send_in_request_body)
    
        response_per_post = requests.post(
            url=CODEFORCASH_BASE_URL+'/api/metum/create',
            data=data_to_send_in_request_body)
        
        with open('responseFromCodeforcash','ab+') as f:
            pickle.dump(response_per_post, f)

# def remove_non_ascii(listings):
#     # for list in listings:
#     #     list.encode('UTF8')
#     unidecode(unicode(listings, encoding = "utf-8"))

# def save_result_of_sending_job_listings_to_codeforcash(listings):
#     with open('responseFromCodeforcash','ab+') as f:
#         pickle.dump(send_job_listings_to_codeforcash(return_value), f)

if __name__ == '__main__':
    save_api_call_results(send_job_listings_to_codeforcash(get_job_listings_from_google()))

    # save_api_call_results(send_job_listings_to_codeforcash(remove_non_ascii(get_job_listings_from_google())))

    # send_job_listings_to_codeforcash(return_value)
    # save_api_call_results(return_value)

    # save_result_of_sending_job_listings_to_codeforcash(send_job_listings_to_codeforcash(return_value))

    # save_api_call_results(get_job_listings_from_google())

    # save_result_of_sending_job_listings_to_codeforcash(
    #     get_job_listings_from_google())
        
