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

bot_token = 'NTU3OTEzMzkwNjY4ODQwOTYz.XOOOGg.6AQD9Ro2azeQAidTFs6KL0kmJuQ'
self_bot_token = 'NDcxNzUzNjA2Nzk0NTc1ODky.D3DLjw.r9t-wvWsJq-IJ9Y7PvLU2DJ6_ZE'

message = None
embed = None
embed_best = None

#trivia-answers
output_channel = discord.Object(id= '580211268971921409')

input_hq_private  = [
    "513818250652680213","523359669280833536","580198028950896640","580211268971921409" 
]
input_hq_public = ['580211268971921409']
command_channel = '580211268971921409' #trivia-answers
admin_chat = '580211268971921409' # answers2

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
