# How to run
1. Inject Js Script to the webpage of the comment page (pop-out mode):
  - must have atleast have 1 message
2. run python file (websocket.py)

3. enjoy???


# Explaination
## Getting the comments fromt the livestream
  - The best way I went through this was just injecting a Js Script that detects changes in an html element and sending the data to the python script through websockets
### why not use Meta's Live Video API?
  - My account was "suspended" because I had to provide an ID to make a bussines profile to make an App that can be reviewed to request an API key. It took too long and made me want to KMS (Keep Myself Safe).
#### Other ways I tried and why it failed
  1. I used Selenium to look at the livestream and scan it.
     - The problem was it required me to login to my facebook account everytime, it was probably because the stream was on "only me" view mode.
     - and it was probably slow
  2. Used a flask server and send a post request to the serer
     - the problem was that facebook blocked POST request, it was CORS error
     - probably to block bad actors. and bad programmers
  3. Edit the OnCommentAdded() function on the REACT component.
     - Since they were using react(CRINGE) I tried to override the OnCommentAdded() property
     - but It was much more of a hassle trying to read obfuscated code (f = a.CommentData (200 'a' found))
    
