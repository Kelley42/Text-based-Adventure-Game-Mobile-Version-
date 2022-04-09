# Adventure Game (Mobile Version)

This is a game I wrote for Udemy's 100 Days of Code. It's a command-line program written in Python. It takes you on an adventure through a cursed island to find a treasure.

I had so much fun creating it! I've always wanted to write something like this. The original storyline structure we were invited to model ours after only had 3 steps, so I decided to add a lot more to make it feel like an actual story.

It was important to me to make it feel as old-school as possible, so I didn't want users to input a letter or number as their choice but to actually type their response as a word or phrase. While it was more difficult this way and involved more lines of code to cover all likely responses they might give, I'm happy with the result.

While the original 3-step model had each GAME OVER branch completely ending the game, I wanted to make it less frustrating so users wouldn't have to start all the way at the beginning each time they died in the game. (Though this could be removed to make the game more difficult.) Instead, after each life lost, they would be offered a choice to either start over from the beginning or just to revert to the last step before their death so they can choose a new action. However, after their third death it's game over, and they must start from the beginning.

While creating this game, organization within each section was the most difficult and something I rewrote many times. It was a good learning experience tracking all the branches within the story, using breakpoints to link functions to each other, and figuring out how to error-check all possible responses. I also learned how to wrap the text so it would be easier to read. (Although it is still wrapping too early on the first lines of paragraphs - hopefully I can fix that on subsequent revisions!)

To make it easier to view on mobile devices, I adjusted the textwrap width and added textwrap to the remaining sentences, which hadn't been necessary in the desktop version.

