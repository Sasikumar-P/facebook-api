



import facebook
graph = facebook.GraphAPI("EAACEdEose0cBAFQCfNdrYVku4Rm7GZCfdP0K4BxeDxZATGi1cP508ZABtQz41uw0PUOWz1iGyED9dIJiql5MsUBaHWjEioSiKC9wnyC3ZBZCiHJ9pdIiFWfIqpq0tKu7OUbJ01f3CQlg4MKvZBZAvKd3nHB9Y7OjSLVe2Rh9fJFPbFKUFzAvfUz5uk8fvMZCrRUZD")
friends = graph.get_object("me/friends")
for friend in friends['data']:
    print "{0} has id {1}".format(friend['name'].encode('utf-8'), friend['id'])
