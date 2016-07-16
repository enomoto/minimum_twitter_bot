# -*- coding: utf-8 -*-

import os
from datetime import datetime
import twitter


api = twitter.Api(consumer_key=os.environ["CONSUMER_KEY"],
                  consumer_secret=os.environ["CONSUMER_SECRET"],
                  access_token_key=os.environ["ACCESS_TOKEN_KEY"],
                  access_token_secret=os.environ["ACCESS_TOKEN_SECRET"]
                  )
api.PostUpdate("system time is %s" % datetime.now())
