#BigRed.py
"""
This is a reddit bot created to comment on any of a users
posts and post a particular reply.
"""
#needs download
import praw 

import time
import random
import traceback

error_file_name = 'BigRedErrors.log'
attack_log = 'BigRedAttacks.log' #tracks actions
#name of program reddit sees
r = praw.Reddit('TheSpellingAsshole Replier') 

def last_comment(user):
	"""Get last comment for a particular user."""
	comments = user.get_comments()
	last = comments.next()
	print 'last comment from user was: ' + last.body
	return last

def last_submission(user):
	"""Get last submission for user object."""
	subs = user.get_submitted()
	last = subs.next()
	print last
	return last

def get_new_comments(user, last):
	"""Get new comments submitted by user
	
	user -- user object from praw
	last -- previous most recent comment object from praw
	"""
	comments = user.get_comments()
	new_comments = []
	recent = comments.next()
	while recent != last:
		new_comments.append(recent)
		recent = comments.next()
	#print 'New comments: ', new_comments
	return new_comments

def get_new_subs(user, last):
	"""Get new posts submitted by user

	user -- user object from praw
	last -- previous most recent submission object from praw
	"""
	subs = user.get_submitted()
	new_subs = []
	recent = subs.next()
	while recent != last:
		new_subs.append(recent)
		recent = subs.next()
	#print 'New Subs: ', new_subs
	return new_subs

def post_comment(sub, reply):
	"""Post the input reply as a root comment on sub.

	sub -- submission (link or text post)
	reply -- str of what you want to say
	"""
	sub.reply(reply) # Needs own method?

def post_reply(comment, reply):
	"""Posts the reply comment.

	the comment object must have been generated using a logged-in
	praw session (i.e. call r.login())
	"""
	comment.reply(reply) # Needs own method?

def count_parents(comment_id, count):
	"""Count levels up from comment_id to root comment"""
	child = r.get_info(thing_id=comment_id)
	root = child.is_root
	if (root != true):
		count = count_parents(child.parent_id, count + 1)
	return count

def prune_comments(comm):
	"""Trim comment based on arbitrary criteria"""
	comment_text = comm.body
	reply = ''

	if (comment_text.startswith("It's spelled")):
		#error_end = trimmed.index(',')
		#Strip "It's spelled " from front 
		#error text = comment_text[13:error_end]
		reply = ("I know you're a spelling bot, "
		"but please try to be a little less rude. ")
		should_reply = True
	else: 
		should_reply = False
	return reply, should_reply

def handle(output):
	"""print console exceptions to output

	output -- str location of output file
	"""
	e = traceback.format_exc()
	error_file = open(output, 'a')
	error_file.write('\n****NEW EXCEPTION THROWN****\n')

	print 'Printing error to ' + output
	#Timestamp	
	error_file.write('Program critical error at ' + time.ctime())
	error_file.write('\n\n')
	error_file.write(e)
	error_file.write('****END OF EXCEPTION****\n')

def log_start(error_file_name):
	"""Timestamp and separate this portion in log file."""
	error_file = open(error_file_name, 'a')
	ts = time.ctime()
	error_file.write('\n\n*************************')
	error_file.write('\n*************************\n\n')
	error_file.write('Begin log for program initialized '
					'on ' + ts)

def __main__():
	print 'Starting __main__'
	user = r.get_redditor("TheSpellingAsshole")
	r.login()
	end_comment = last_comment(user)
	should_run = True
	down_count = 0
	reply_count = 0

	while should_run:
		new_comms = get_new_comments(user, end_comment)
		#get most recent comment if any
		if (len(new_comms) > 0):
			end_comment = new_comms[0] 

		for comm in new_comms:
			should_vote = (random.randrange(4) > 0)
			if should_vote:
				comm.downvote()
				down_count = down_count + 1
			reply, should_reply = prune_comments(comm)
			print reply, should_reply
			if should_reply:
				try:
					post_reply(comm, reply) #requires logged in user
					reply_count = reply_count + 1
				except (ClientException, APIException):
					#hoping this doesn't allow password issues to persist
					handle(error_file_name)
				
		print time.ctime()
		print '%d replies, %d downvotes...sleeping for 10 minutes' % (reply_count, down_count)

		time.sleep(600)

		#some stuff for getting going:
		#user_reply = raw_input('Would you like to test again? (Y/N): ')
		#user_reply = user_reply.lower()
		#should_run = user_reply.startswith('y')


try:
	log_start(error_file_name)
	__main__()
except Exception:
	exception = traceback.format_exc()
	handle(error_file_name)
finally:
	print 'test'

