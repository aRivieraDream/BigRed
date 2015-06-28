#Hitler.py
"""
Sample line change. 

This is a bot created to comment on anything of a users
posts and post a particular reply
"""
import time 
import praw
import random
r = praw.Reddit('TheSpellingAsshole Reply')


def last_comment(user):
#gets the last comment for a particular user 
	comments = user.get_comments()
	last = comments.next()
	print 'last comment from user was: ' + last.body
	return last

def last_submission(user):
#gets the last submission for a particular user
	subs = user.get_submitted()
	last = subs.next()
	print last
	return last

def get_new_comments(user, last):
#gets any new comments submitted by user
	comments = user.get_comments()
	new_comments = []
	recent = comments.next()
	while recent != last:
		new_comments.append(recent)
		recent = comments.next()
	#print 'New comments: ', new_comments
	return new_comments

def get_new_subs(user, last):
#gets any new posts submitted by user
	subs = user.get_submitted()
	new_subs = []
	recent = subs.next()
	while recent != last:
		new_subs.append(recent)
		recent = subs.next()
	#print 'New Subs: ', new_subs
	return new_subs

def post_comment(sub, reply):
#posts the input reply to that user from the given login
	sub.reply(reply)

def post_reply(comment, reply):
#posts the input reply to that comment from the given login
#the comment object must have been generated using a
#logged in session
	comment.reply(reply)

def count_parents(comment_id, count):
#takes a comment id and determine how many levels up to get
#to root, count starts at 0
	child = r.get_info(thing_id=comment_id)
	root = child.is_root
	if (root != true):
		count = count_parents(child.parent_id, count + 1)
	return count

def prune_comments(comm):
#trims comments based on some criteria
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


user = r.get_redditor("TheSpellingAsshole")
r.login()
end_comment = last_comment(user)

should_run = True
down_count = 0
reply_count = 0
while True:
	new_comms = get_new_comments(user, end_comment)
	if (len(new_comms) > 0):
		end_comment = new_comms[0] #this should be most recent comment
		#if it's not, order list with oldest first and take last 
		#element in for loop

	for comm in new_comms:
		should_vote = (random.randrange(4) > 0)
		if should_vote:
			comm.downvote()
			down_count = down_count + 1
		reply, should_reply = prune_comments(comm)
		print reply, should_reply
		if should_reply:
			post_reply(comm, reply) #requires logged in user
			reply_count = reply_count + 1
	print time.ctime()
	print '%d replies, %d downvotes...sleeping for 10 minutes' % (reply_count, down_count)

	time.sleep(600)
	#user_reply = raw_input('Would you like to test again? (Y/N): ')
	#user_reply = user_reply.lower()
	#should_run = user_reply.startswith('y')





