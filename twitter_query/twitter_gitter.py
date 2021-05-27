#created for python v.3.9.5
#the requests library is imported to handle makign GET requests to twitter
#The json library is used to turn the resposne into json formatted data
import requests
import json


"""
This script queries Twitter and filters for the most popular posts from SpaceX
The query result count was limited to 1 for readability but the count querystring
can be altered to include more if desired
The json response results are stored in a .json file names spacex_popular_tweet
"""


#bearer read only token wrapped for PEP8 character count
bearer = "AAAAAAAAAAAAAAAAAAAAAKEYQAEAAAAAEtEmcTDhFT8xp9p%2FJL49TEWh4tI%3Dg\
4fpx7HFDhLQYSBcFNvPSycagzqxTWMavvx3yafuOKsZ7TsHlf"

#This definition construct the urls for our query
#I added the variables who , type, and return_count for readability
def create_url():
    who = "spacex"
    type = "result_type=popular"
    return_count = "count=1"
    url = "https://api.twitter.com/1.1/search/tweets.json?q={}&{}&{}".format(who, type, return_count)
    return url

#constructs the api header using our bearer auth token
def api_headers(bearer):
    header = {"Authorization":"Bearer {}".format(bearer)}
    return header

#issues the GET request using the requests library and expects a response of OK 200
#if response is not 200 it raises an exception otherwise the response is returned
def api_GET_request(url, headers):
    response = requests.request("GET", url, headers=headers)
    # print(response.status_code)
    if response.status_code != 200:
        raise Exception(
            response.status_code, response.text
        )
    return response.json()

#our main function
#utilizes our url creation and api headers functions to set them to variables
#url and headers respectively
#it then passes in the actual variables to the api_GET_request in which the
#json response is saved to its own json_response variable
#finally the standard python open function is used to write the json response to
#a file named spacex_popular_tweet.json in the current working directory
def main():
    url = create_url()
    headers = api_headers(bearer)
    json_response = api_GET_request(url, headers)
    print('The most popular SpaceX Twitter headline is:')
    print(json.dumps(json_response['statuses'][0]['text'], indent=4, sort_keys=True))
    with open('spacex_popular_tweet.json', 'w', encoding='utf-8') as f:
        json.dump(json_response, f, ensure_ascii=False, indent=4)


#of course here is our standard if __name__ == '__main__' so main() will
#be called when the script is run directly
if __name__ == "__main__":
    main()
