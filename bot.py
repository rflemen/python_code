import discord
from discord.ext import commands, tasks
import os
from dotenv import load_dotenv
import asyncio
import aiohttp
from datetime import datetime, timedelta
import json

# Load environment variables
load_dotenv()

# Bot configuration
TOKEN = os.getenv('DISCORD_TOKEN')
YOUTUBE_API_KEY = os.getenv('YOUTUBE_API_KEY')
YOUTUBE_CHANNEL_ID = os.getenv('YOUTUBE_CHANNEL_ID')
DISCORD_CHANNEL_ID = int(os.getenv('DISCORD_CHANNEL_ID', '1429555503100461076'))

# Setup bot
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

# Store last checked video ID
LAST_VIDEO_FILE = 'last_video.json'

def load_last_video():
    """Load the last video ID from file"""
    try:
        with open(LAST_VIDEO_FILE, 'r') as f:
            data = json.load(f)
            return data.get('video_id')
    except FileNotFoundError:
        return None

def save_last_video(video_id):
    """Save the last video ID to file"""
    with open(LAST_VIDEO_FILE, 'w') as f:
        json.dump({'video_id': video_id}, f)

async def get_latest_video():
    """Fetch the latest video from YouTube channel"""
    url = 'https://www.googleapis.com/youtube/v3/search'
    params = {
        'key': YOUTUBE_API_KEY,
        'channelId': YOUTUBE_CHANNEL_ID,
        'part': 'snippet',
        'order': 'date',
        'maxResults': 1,
        'type': 'video'
    }

    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params) as response:
            if response.status == 200:
                data = await response.json()
                if data['items']:
                    return data['items'][0]
    return None

def create_video_embed(video_data):
    """Create a Discord embed for the video"""
    snippet = video_data['snippet']
    video_id = video_data['id']['videoId']
    video_url = f'https://www.youtube.com/watch?v={video_id}'

    embed = discord.Embed(
        title=snippet['title'],
        description=snippet['description'][:500] + '...' if len(snippet['description']) > 500 else snippet['description'],
        url=video_url,
        color=discord.Color.red(),
        timestamp=datetime.fromisoformat(snippet['publishedAt'].replace('Z', '+00:00'))
    )

    embed.set_author(name=snippet['channelTitle'])
    embed.set_thumbnail(url=snippet['thumbnails']['high']['url'])
    embed.add_field(name='Watch Now', value=f'[Click here]({video_url})', inline=False)
    embed.set_footer(text='YouTube', icon_url='https://www.youtube.com/s/desktop/f506bd45/img/favicon_32.png')

    return embed, video_url

@tasks.loop(minutes=20)
async def check_new_videos():
    """Check for new videos every 20 minutes"""
    try:
        latest_video = await get_latest_video()

        if latest_video:
            video_id = latest_video['id']['videoId']
            last_video_id = load_last_video()

            if video_id != last_video_id:
                channel = bot.get_channel(DISCORD_CHANNEL_ID)

                if channel:
                    embed, video_url = create_video_embed(latest_video)
                    await channel.send(
                        content=f"🎥 **New video uploaded!**\n{video_url}",
                        embed=embed
                    )
                    save_last_video(video_id)
                    print(f"Posted new video: {latest_video['snippet']['title']}")
                else:
                    print(f"Error: Could not find channel with ID {DISCORD_CHANNEL_ID}")
    except Exception as e:
        print(f"Error checking for new videos: {e}")

@check_new_videos.before_loop
async def before_check():
    """Wait for the bot to be ready before starting the loop"""
    await bot.wait_until_ready()
    print("Starting video check loop...")

@bot.event
async def on_ready():
    """Event handler for when bot is ready"""
    print(f'{bot.user} has connected to Discord!')
    print(f'Monitoring YouTube channel: {YOUTUBE_CHANNEL_ID}')
    print(f'Posting to Discord channel: {DISCORD_CHANNEL_ID}')

    if not check_new_videos.is_running():
        check_new_videos.start()

@bot.command(name='check')
@commands.has_permissions(administrator=True)
async def manual_check(ctx):
    """Manually check for new videos"""
    await ctx.send("🔍 Checking for new videos...")

    latest_video = await get_latest_video()
    if latest_video:
        embed, video_url = create_video_embed(latest_video)
        await ctx.send(content=f"Latest video:\n{video_url}", embed=embed)
    else:
        await ctx.send("❌ Could not fetch latest video.")

@bot.command(name='status')
async def status(ctx):
    """Check bot status"""
    embed = discord.Embed(
        title="nPmVids Bot Status",
        color=discord.Color.green()
    )
    embed.add_field(name="Status", value="✅ Online", inline=True)
    embed.add_field(name="Monitoring", value=f"Channel ID: {YOUTUBE_CHANNEL_ID}", inline=False)
    embed.add_field(name="Check Interval", value="Every 10 minutes", inline=True)
    await ctx.send(embed=embed)

# Run the bot
if __name__ == '__main__':
    if not TOKEN:
        print("Error: DISCORD_TOKEN not found in .env file")
    elif not YOUTUBE_API_KEY:
        print("Error: YOUTUBE_API_KEY not found in .env file")
    elif not YOUTUBE_CHANNEL_ID:
        print("Error: YOUTUBE_CHANNEL_ID not found in .env file")
    else:
        bot.run(TOKEN)