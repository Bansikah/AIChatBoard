import random
#from http.client import responses

greetings = ["Hello", "What's up?", "Howdy", "Greetings!"]
goodbyes = ["Bye", "Goodbye!", "See you later!", "See you soon"]

keywords = ["Music","pet","book","game"]
responses = ["Music is so relaxing", "Dogs are main's best friend!", "I know about a lot of books.","I like to play video games"]

print(random.choice(greetings))

user = input("say something (or type bye to quit):")
user = user.lower()

#while (user != "bye"):
#
# while (user != "bye"):
#     for index in range(len(keywords)):
#      if (keywords[index] in user):
#         print("Bot: " + responses[index])
# #
#
#
#     for index in range(len(keywords)):
#      if (keywords[index] in user):
#          print("Bot: " + responses[index])
#          keyword_found = True

while (user != "bye"):
    keyword_found = False
    for index in range(len(keywords)):
        if (keywords[index] in user):
            print("Bot: " + responses[index])
            keyword_found = True

    if(keyword_found == False):
        new_keyword = input("I'm  not sure how to response. What keyword should i respond to?")
        keywords.append(new_keyword)
        new_response = input("How should i respond to " + new_keyword + "?")
        responses.append(new_response)

    user = input("Say something (or type bye to quit):")
    user = user.lower()

    print(random.choice(goodbyes))



