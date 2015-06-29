# BigRed(dit)

<h1>Overview</h1>
The idea behind BigRed is to provide a programatic interface for Reddit users to have their actions augmented. 
Right now BigRed doesn't do very much. In fact, all he does is follow around /u/TheSpellingAsshole and ask him to be less rude, in addition to giving him the occasional downvote. 


<h1>Setup</h1>
- Clone the project into your local repository or onto an EC2 instance 
- Unless you want to chase down /u/TheSpellingAsshole with me you'll probably want to adjust some of the actions on comments. 
- run 	$python BigRed.py
	- You must be in the same directory as BigRed.py
- you will be prompted for a reddit username and password from the command line


<h2>Potential Features:</h2>
	- Get emails of pms to BigRed
	- Set up BigRed with multiple user accounts
	- Notify user when a topic in their expertise is mentioned


<h2>Known issues with BigRed(dit):</h2>
	- Potential to continuously throw errors if user is logged out.
	- Issue with deleted comments--not quite sure what the issue is. 


<h2>Proposed improvements (in no order):</h2>
	- Needs implementation of OAuth in order to have login info persist beyond August 3. 
	- Needs build out of error handling. 
	- Needs a better interface for operating multiple accounts
	- Needs build out of reply mechanism (perhaps something just a little less basic.)
	- Needs build out of targets. 
	- More dynamic voting/comments threshholds.
	- Error handling: (login issues)
	- Add an actions log