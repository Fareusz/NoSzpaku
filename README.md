# Dependencies 

> pip install python-dotenv os requests spotipy json time 


# WARNING ⚠️ How to make it work?

To make script work you have to get your own client id and client secret from spotify, it's ultra simple. To get that please go to https://developer.spotify.com/dashboard/applications

Then proceed with instructions:

0. Clony the repository to a new folder. You will get an noszpaku.py file and .env file
1. Create an app using "Create an App" green button on the top right.
2. Enter anything you want. It doesn't matter at all.
3. Copy client ID and client secret. 
https://i.imgur.com/2sDk4CG.png <- it looks like on this screenshot
4. Paste both of those tokens into .env file. (redirect uri can be anything you want)
5. Run the script by command line `python noszpaku.py`. Keep the window in the background. If you want to stop the script close window.


# NoSzpaku

Everyone likes to discover new songs on spotify. For example, you like white 2115 (two thousand one hundred fifteen) and you decide to play a radio of this artist to find new exciting beats. But suddenly then spotify plays you something that... that can kill your ears. Yeah. I talk about "Szpaku". If you don't want to risk your life please run this script in background when you are listening to new songs. 

# How it works? It can't be real.

Well. It's simple, script uses "spotipy" python library to get your username and song that you are currently playing. If it detects "Szpaku" in artists list it skips the song. Nothing special right? Remember it has a 5 seconds delay, otherwise spotify could block requests.
