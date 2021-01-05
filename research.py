import tweepy
import json
import secret
import time, calendar
import os
import sys

def TwitterApiLogin( conf ):
    CONSUMER_KEY = conf["consumer_key"]
    CONSUMER_SECRET = conf["consumer_secret"]
    ACCESS_TOKEN = conf["access_token"]
    ACCESS_TOKEN_SECRET = conf["access_token_secret"]

    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    return tweepy.API(auth ,wait_on_rate_limit = True)


if __name__ == "__main__":

    args = sys.argv
    
    if(len(args) == 2):
        keyword = args[1]
    elif(len(args) == 1):
        keyword = input(u"input: ")
    else:
        sys.exit()

    api = TwitterApiLogin(secret.auth_data)
    get_count = 100
    user_list = []

    tweets = api.search(q=keyword, lang='ja', result_type='recent', count=get_count)

    total_tweet_count = 0
    for tweet in tweets:
        user_list.append(tweet.user.screen_name)

        print('twid : ', tweet.id)               # tweetのID
        print('user : ', tweet.user.screen_name)  # ユーザー名
        print('date : ', tweet.created_at)      # 呟いた日時
        print(tweet.text)                  # ツイート内容
        print('favo : ', tweet.favorite_count)  # ツイートのいいね数
        print('retw : ', tweet.retweet_count)  # ツイートのリツイート数
        print("--" * 40)


    total_tweet_count += len(tweets) -1
    current_tweet_id = tweets[-1].id

    print("#" * 15 + " tweet count ")
    print("-> "  + str(total_tweet_count) )
    print("#" * 15 + " current tweet id ")
    print("-> " + str(current_tweet_id))

    if input(u"このまま続けますか？ (y or else): ") != 'y':
        exit()


    last_date = tweets[0].created_at

    while True:
        print("@" * 15 + "Next!!! 3s..." + "@" * 15)
        time.sleep(3)

        try:
            tweets = api.search(q=keyword, lang='ja', result_type='recent', count=get_count, max_id=current_tweet_id, include_entities=False)
            for tweet in tweets:
                user_list.append(tweet.user.screen_name)

                print('twid : ', tweet.id)               # tweetのID
                # print('user : ', tweet.user.screen_name)  # ユーザー名
                print('date : ', tweet.created_at)      # 呟いた日時
                # print(tweet.text)                  # ツイート内容
                # print('favo : ', tweet.favorite_count)  # ツイートのいいね数
                # print('retw : ', tweet.retweet_count)  # ツイートのリツイート数
                print("--" * 40)
            
            total_tweet_count += len(tweets) -1

            if current_tweet_id == tweets[-1].id:
                first_date = tweets[-1].created_at
                break
            current_tweet_id = tweets[-1].id
        except:
            print("@" * 15 + "Error!!! " + "@" * 15)
            break

        print("#" * 15 + " sesarch keyword")
        print("-> "  + keyword )
        print("#" * 15 + " tweet count ")
        print("-> "  + str(total_tweet_count) )
        print("#" * 15 + " current tweet id ")
        print("-> " + str(current_tweet_id))



    print("@" * 15 + "Finish!!! " + "@" * 15)
    print("#" * 15 + " sesarch keyword")
    print("-> "  + keyword )
    
    print("#" * 15 + " term ")
    print(str(first_date) + " -> " + str(last_date))

    print("#" * 15 + " tweet count ")
    print("-> "  + str(total_tweet_count) )

    print("#" * 15 + " user count ")
    print("-> " + str(len(set(user_list))))