#clientID 562444771822403584
#token NTYyNDQ0NzcxODIyNDAzNTg0.XKLByA.fMJs0A2sK_3iD0jKKW58ijQ__UU
#permssions integer 247872

#invite URL https://discordapp.com/oauth2/authorize?client_id=562444771822403584&scope=bot&permissions=247872

import discord
import os
import json
import time
import shutil

# creating a dict to keep track of member details
MemberDict ={
	# name:
	# unique id
	# number of reports
};

timeStr = time.strftime("%H%M%S")

MemberDict['people'] = [];

token = open("token.txt","r").read();

#start the bot client
client = discord.Client();

@client.event
async def on_ready():  # method expected by client. This runs once when connected
    print(f'We have logged in as {client.user}')  # notification of login.
    #initiate guild once in this and then populate list for all the guild members that are not bots
    # RCW_guild = client.get_guild(346399441475076097)
    # for members in RCW_guild.members:
    # 	print(members.name)
    #assign unique member ids to a set variable name



@client.event
async def on_message(message):  # event that happens per any message.

    # each message has a bunch of attributes. Here are a few.
    # check out more by print(dir(message)) for example.
    print(f"{message.channel}: {message.author}: {message.content}")
    RCW_guild = client.get_guild(346399441475076097)
    if "!helpRCWbot" in message.content:
        await message.channel.send("You have accessed the help menu");
    elif "!UpdateMembers" == message.content:
    	for members in RCW_guild.members:
    		if members.bot == 0:
    			MemberDict['people'].append({'name:' : members.name, 'uniqueID:' : members.id, 'reportCount:' : '0'});
    	with open("data.txt", mode = "w") as outfile:
    		outfile.seek(0);
    		json.dump(MemberDict,outfile);
    		outfile.truncate();
    		outfile.close();
    	
    	
    			
        

    elif "!report" in message.content:
    	await message.channel.send("As no RCW member was mentioned ShadowKnight was reported");

    elif "!m" == message.content:
    	# await message.channel.send(f"```{(RCW_guild.members[0].name)}```")	
    	for members in RCW_guild.members:
    		if members.bot == 0:
    			print(f"{members.id} : {members.name}")
    	


client.run(token)  # recall my token was saved!






