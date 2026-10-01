## [Datum] – [Kort titel på problemet]

**Vad gick fel:**
När jag beyggde textaventry var det svårt att keep track of all the different choices and endings. I also had to make sure that the player's name was used with f-strings and that the choices led to different parts of the story. 
**Varför:**
[Din analys av grundorsaken]
The story has several choices after each other. For example, the player firts chooses whether to enter the temple, then chooses whether to go deeper, and later chooses whteher to enter the portal. Because there are several (if,elif) and (else) statements inside each other, it was easy to put a choice in the wrong place or make an ending unreachable. 

**Hur jag löste det:**
[Vad du faktiskt gjorde]
i organised the story into smaller sections and used an if/ekif/else structure for each choice. I used f-string to iclude player's name in several messages and created different endings depending on the player's choices. 

**Vad jag skulle göra annorlunda:**
[Din reflektion – det viktigaste fältet]
i would plan the differnt paths on paper before writing the code. i would write down each choice and where it should lead, including all the possible endings. this would make the nested id/else statements easier to organize amd would make it less likely that I accidently create a path that does not work. 

**AI-granskning (om tillämpligt):**
[Vad AI föreslog / vad du ändrade / vad AI missade]
I didnt really use AI, I asked it what it thought about my story outline, here is the response i got "The only thing I'd improve is making the (get lost- alternative universe) transition a little more connected. For example, After getting lost inside the temple, you find a strange room with an ancient portal. When you activate it, you are transported to an alternative universe where history developed differently. That makes the story flow more naturally instead of the alternative universe appearing suddenly.

It made sense to change it but since the code is working and am not interested in doing anything that would alter that, decided not to. If the code is working and the story still made sense, whom am I to change things even if the ai said so. 