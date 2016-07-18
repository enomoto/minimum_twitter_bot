Minimum Twitter bot
======
This is minimum Twitter bot which works on Heroku.
## Installation
`$ heroku create --stack cedar`   
`$ git push heroku master`    
`$ heroku config:set CONSUMER_KEY=your_cosumer_key CONSUMER_SECRET=your_consumer_secret ACCESS_TOKEN_KEY=your_access_token_key ACCESS_TOKEN_SECRET=your_access_token_secret`    
`$ heroku addons:create scheduler:standard`   
`$ heroku addons:open schedulerk`   
Add scheduler task.
