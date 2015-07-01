# BigRed(dit)

<h1>Overview</h1>
The idea behind BigRed is to provide a programatic interface for Reddit users to have their actions augmented. 
Right now BigRed doesn't do very much. In fact, all he does is follow around /u/TheSpellingAsshole and ask him to be less rude, in addition to giving him the occasional downvote. 


<h1>Setup</h1>
- Clone the project into your local repository or onto an EC2 instance 
- Unless you want to chase down /u/TheSpellingAsshole with me you'll probably want to adjust some of the actions on comments. 
- run  
`$ python BigRed.py`
	- You must be in the same directory as BigRed.py
- you will be prompted for a reddit username and password from the command line
- To keep your process running while disconnected from ssh use screen
	- Start session `$ screen`
	- Detach `$ ctrl+a d`
	- When reconnecting be sure to start a new session of screen
	- Reattach `$ screen -r`
	- For multiple screen sessions:
		- List all screens available `$ screen -ls`
		- Reattach particular screen `$ screen -r <first 4 numbers>`
	- More info: http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/install-updates.html
	- Also: http://www.tecmint.com/screen-command-examples-to-manage-linux-terminals/


<h2>Potential Features:</h2>
- Get emails of pms to BigRed
- Set up BigRed with multiple user accounts
- Notify user when a topic in their expertise is mentioned


<h2>Known issues with BigRed(dit):</h2>
- Disown doesn't track comment updates from prior disown
- Deleted comments will likely throw an error
	- Potential infinite loop if handle(output)
- Time isn't actually local time of instance
	- For ref: http://stackoverflow.com/questions/8809765/need-to-convert-utc-aws-ec2-to-pst-in-python


<h2>Proposed improvements (in no order):</h2>
- Needs implementation of OAuth in order to have login info persist beyond August 3. 
- Needs build out of error handling. 
- Needs a better interface for operating multiple accounts
- Needs build out of reply mechanism (perhaps something just a little less basic.)
- Needs build out of targets. 
- More dynamic voting/comments threshholds.
- Error handling: (login issues)
- ~~Add an actions log~~