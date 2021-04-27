import asyncio
import datetime
import random
from discord.ext import commands
from pytz import timezone
#Not used but in case you want some commands
BDayBot = commands.Bot(command_prefix="-") 
# Apply the birthdays of people by going (Month, day) : "Name"
bDayOfPeople = {
    (1, 25): "Birthdays in January",
    (2, 13): "Birthdays in February", 
    (3, 23): "Birthdays in March",
    (4, 5): "Birthdays in April", 
    (5, 4): "Birthdays in May", 
    (6, 15): "Birthdays in June",
    (7, 29): "Birthdays in July",
    (8, 19): "Birthdays in August",
    (9, 26): "Birthdays in september",
    (10, 3): "Birthdays in October",
    (11, 21): "Birthdays in November",
    (12, 26): "Birthdays In december"
}

# Holidays dates, includes new year, valentine's day, easter, canada day, holloween and christmas with respective gifs
holidayChecks = {
    (1, 1): "NO JOKE, GIVE YOURSELF A TAP IN THE BACK FOR GETTING THROUGH ANOTHER YEAR! KEEP AT IT AND STAY STRONG, HERE IS TO ANOTHER GOOD YEAR!  \n https://tenor.com/view/happy-new-year-fireworks-motivation-gif-13184540",
    (2, 4): "HAPPY VALENTINE'S DAY YOU  \n https://tenor.com/view/love-hug-happy-valentines-day-heart-cute-gif-5077512",
    (4, 4): "GO CATCH THEM EGGS, HAPPY EASTER! \n https://tenor.com/view/easter-hunt-basket-happy-easter-easter-sunday-gif-13979284",
    (7, 1):  "HAPPY CANADA DAY! \n https://tenor.com/view/happy-canada-day-serious-celebrate-zoom-in-gif-12659947",
    (10, 31): "PUT ON THAT COSTUME AS WE DANCE WITH THE DEATH! HAPPY HOLLOWEEN ALL! \n https://tenor.com/view/dancing-dance-halloween-grooves-moves-gif-16886734",
    (12, 25): "MERRY CHRISTMAS! MY GIFT TO YOU IS GOOD LUCK AND HAVE FUN (AKA SPEND LIKE NO TOMORROW)! \n https://tenor.com/view/buddy-the-elf-excited-christmas-christmas-crazy-oh-gif-13142053"
}

# List of gifs for the birthday reminder
birthdayGifs = ["https://tenor.com/view/monkey-dance-happy-weekend-party-hard-lit-gif-16026466",
                "https://tenor.com/view/happy-birthday-wish-cake-happy-birthday-to-you-my-friend-celebrate-gif-15264814",
                "https://tenor.com/view/happy-birthday-birthday-cake-goat-licking-lick-gif-15968273",
                "https://tenor.com/view/happy-birth-day-dance-dance-80s-gif-10812480",
                "https://tenor.com/view/happy-birthday-donald-trump-wants-to-party-dance-gif-16517276",
                "https://tenor.com/view/happy-birthday-friends-phoebe-its-your-birthday-gif-11931097"]

# On ready event for when you reboot the bot
@BDayBot.event
async def on_ready():
    channel = BDayBot.get_channel("Channel Id as an int")
    await channel.send("Cool I'm Back")

#Main code that does all the checking
async def runCode():
    check = True
    reaction = "🥳"
    await BDayBot.wait_until_ready() # Waits for the bot to get ready
    channel = BDayBot.get_channel("Channel Id as an int") #Channel numbers
    await channel.send("Cool I'm back")
    while not BDayBot.is_closed():
        eastern = timezone('US/Eastern') # Get the timezone
        now = datetime.datetime.now(eastern) # use datetime to get the current date and time which runs on government time (00:00 -> 23:59)
        if now.hour == 00: 
            if check:
                if (now.month, now.day) in bDayOfPeople:
                    msg = await channel.send(f'@everyone, PLEASE WISH ' + bDayOfPeople[(now.month, now.day)].upper() + " A HAPPY GOOD BIRTHDAY WOOT! \n" + random.choice(birthdayGifs))
                    await msg.add_reaction(emoji=reaction)
                if (now.month, now.day) in holidayChecks:
                    await channel.send(f"@everyone, " + holidayChecks[(now.month, now.day)])
                check = False
        else:
            check = True
        await asyncio.sleep(15) # Allow the while loop to stop every loop for 15s to not crash the bot. 

BDayBot.loop.create_task(runCode())

BDayBot.run("Token")
