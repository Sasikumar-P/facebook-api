



import urllib2
import json

def get_page_data(page_id,access_token):
    api_endpoint = "https://graph.facebook.com/v2.4/"
    fb_graph_url = api_endpoint+page_id+"?fields=id,name,likes,link&access_token="+access_token
    try:
        api_request = urllib2.Request(fb_graph_url)
        api_response = urllib2.urlopen(api_request)
        
        try:
            return json.loads(api_response.read())
        except (ValueError, KeyError, TypeError):
            return "JSON error"

    except IOError, e:
        if hasattr(e, 'code'):
            return e.code
        elif hasattr(e, 'reason'):
            return e.reason

page_id = "1713527505598764" # username or id
token = "EAACEdEose0cBAFQCfNdrYVku4Rm7GZCfdP0K4BxeDxZATGi1cP508ZABtQz41uw0PUOWz1iGyED9dIJiql5MsUBaHWjEioSiKC9wnyC3ZBZCiHJ9pdIiFWfIqpq0tKu7OUbJ01f3CQlg4MKvZBZAvKd3nHB9Y7OjSLVe2Rh9fJFPbFKUFzAvfUz5uk8fvMZCrRUZD"  # Access Token
page_data = get_page_data(page_id,token)
print page_data




print "Page Name:"+ page_data['name']
print "Likes:"+ str(page_data['likes'])
print "Link:"+ page_data['link']
