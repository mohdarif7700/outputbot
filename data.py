import discord

def  init():
    global bot_token
    global self_bot_token
    global message
    global embed
    global output_channel
    global input_channels
    global command_channel

    global game_in_session
    global counter_public_1
    global counter_public_2
    global counter_public_3
    global counter_private_1
    global counter_private_2
    global counter_private_3
    global counter1
    global counter2
    global counter3
    global weight
    global weight_time
    global seconds_elapsed

bot_token = 'NTU3OTEzMzkwNjY4ODQwOTYz.XN59kA.D4AnPAwhZhnJPzEfhwVVNQKESvc'
self_bot_token = 'NDcxNzUzNjA2Nzk0NTc1ODky.D3DLjw.r9t-wvWsJq-IJ9Y7PvLU2DJ6_ZE'

message = None
embed = None
embed_best = None

#trivia-answers
output_channel = discord.Object(id= '557983875209625630')

input_hq_private  = [
    "557983875209625630",
    "516780082619088905",
    "523360037067030530",
	"514915043796713482",
	"496855838703616032",
	"532833017706577930",
	"544381529829146645",
    "558136902885048329",
    "566979656083963918", # answers1
    "555059371294588930", #answers2
    '559357612068700183' #trivia-answers
]
input_hq_public = ['557983875209625630']
command_channel = '557983875209625630' #trivia-answers
admin_chat = '557983875209625630' # answers2

game_in_session = True
counter_public_1 = 0
counter_public_2 = 0
counter_public_3 = 0
counter_private_1 = 0
counter_private_2 = 0
counter_private_3 = 0
counter1 = 0
counter2 = 0
counter3 = 0
weight = 5
weight_time = 1
wronggone1 = 0
wronggone2 = 0
wronggone3 = 0

seconds_elapsed = 0
