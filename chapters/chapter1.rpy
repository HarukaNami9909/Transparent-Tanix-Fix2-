
label chpt_1_intro:
    
    scene CH1 with Dissolve (1.0)
    pause
    
    play music "audio/Transparent_Casual.ogg"
    
    scene classroom with Dissolve (1.0)

    unknown "Settle down, children! Settle down!"
    unknown "Class is not over yet!"
    "Child #1" "But teacher, Lucia is here!"
    "Child #2" "Yeah! She's here to sing with us!"
    "Child #2" "Right, Lucia?!"
    show lufull1
    lu "Oh, uh..."
    "Lucia blushed in embarrassment."
    "She fidgeted her fingers as guilt took over for a moment."
    "She did come in this old classroom unannounced, so many children were eager for class to be over soon."
    "She constantly gave the teacher an apologetic look, hoping that this method would work."
    "Although she expected a frown, a soft smile came across her lips."
    unknown "Well, the sun is setting anyway. I suppose Miss Crimson can take over the lessons for a bit."
    hide lufull1
    show lu1
    #added small details below:
    lu "What, really?!"
    unknown "Yes, since you are so eagerly standing here with your eyes on the children."
    unknown "Perhaps they would listen to you more?"
    lu "Uhh..."
    "All eyes shifted onto Lucia. Many of their eyes were shining as brightly as the sun from each windows from above."
    unknown "You do know what happens next, right, Lucia?" 
    #details ends here.
    lu "I, uhh..."
    lu "(Right... they were talking about how Cunabula was made.)" 
    lu "(Now I just need to talk about how all nests are made around the sky.)"
    lu "(But... can I really do it?)"

    menu:
        "I can do it!":
            "Lucia took a deep breath and stepped forward, hoping no one would notice her feet trembling at each step."
            #deleted an extra dialogue
            "She was already used to having her people watch her sing all the time, but giving lessons to children is a different story!"
            unknown "Well, Lucia? Are you or are you not going to continue the lesson?"
            "Child #1" "Come on, Lucia! You can do this!"
            "Child #2" "Yeah! Don't let the teacher bully you like that!"
            lu "Uhh…"
            lu "(Come on, Lucia! You read it in the history book yesterday!)"
            lu "........................"
            lu "Oh, yeah!"
            lu "Now then... many centuries have passed."  
            lu "The bird who stayed was very weakened, and yet, he used his remaining strength to dance for her one last time." 
            lu "Then his body dispelled, and then he became lost… forever."
            lu "Great grief took over the goddess, and so, she gave half of her soul to the bird."
            #added some small details below:
            lu "Soon, his body changed from wings to arms, claws to nails, and much more happened to become just like his goddess."
            lu "He was reborn... as a different being. As the way we are right now."
            #added details ends here.
            lu "Once he was reborn, the goddess then raised him to become her deputy. She also renamed him, 'Ukylass Emerson.'"
            lu "After searching around the sky, the goddess found out that many of her birds had made their own nests without the use of her powers." 
            lu "Some used sticks, leaves, and even flowers, while others used their own feathers to make a colorful nest."
            lu "Many of them never returned. However, she and her new deputy were able to restore Cunabula as it was." 
            lu "As time passed, rumors of Cunabula's sudden recovery began to spread. Some birds were able to return, but others had doubts."
            lu "The constant debate leads to an upcoming destruction... and you know what she did after that?"
            "Child #1" "Oh my goddess! Just get over with it already!"
            "Child #1" "Everyone here knows what happens next!"
            lu "What?! Just when I thought everything was going good!" 
            
            #achievement! You let Lucia take over the lessons!
            #TODO: Add Archivment

            jump after_class

        "I can't do it!":
            unknown "No?"
            unknown "Are you sure, Miss Crimson?"
            lu "Absolutely!"
            hide lu1
            "The children groaned in disappointment, while the teacher shrugged her shoulders."
            unknown "Perhaps another time? You should try it out sometime!" 
            unknown "Now then, where were we? Ah, yes! Centuries have passed." 
            unknown "The goddess finally returns. However, the nest had turned into a devastated land."
            unknown "The bird who stayed in the nest was weakened without his goddess' powers."
            unknown "The tradition remains in his pain, and so the bird used his remaining strength to dance for her one last time."
            unknown "Soon, he became lost forever, only to be reborn again to become her new deputy, Ukylass Emerson."
            show lu1
            lu "(That's when the first generation of the Emerson family was born.)"
            hide lu1
            unknown "After searching around the sky, our Goddess found out that many of her birds had made their own nests," 
            unknown "even without the use of a goddess' powers."
            unknown "Some used sticks and leaves, while others used their own feathers. They had worked together to regenerate their nest."
            unknown "Even when many of her birds never returned, our goddess never held a grudge against those who no longer believed in her."
            unknown "She and her deputy were able to restore Cunabula!"
            jump Lucia_intro


label after_class:
    
    unknown "Now, now… let's not interrupt our lessons."
    unknown "How about we give her a round of applause for trying anyways?" #added small details here.
    "The children clapped in unison."
    show lu1
    lu "(I don't think I deserve this, though. It was kind of boring, to be honest...)"
    jump Lucia_intro

label Lucia_intro:
    
    unknown "Well, I'm afraid to say that our time is up." 
    unknown "Please remember all this for next week's quiz!"
    e "What?!!!!!!!!!"
    show lu1
    lu "Why, Teacher?!"
    "???" "It's because none of you are patient enough to wait until class is over."
    "???" "That would include yourself, Lucia."
    lu "Are you saying that this is all my fault?!"
    lu "(This teacher! She's doing this on purpose, isn't she?!)"
    unknown "All right! Now that class is over. You know what that means…"
    "As soon as the teacher stepped towards her desk, Lucia took the spotlight of the class." #change a little bit on the end.
    hide lu1
    show lufull1
    lu "Kuliha, everyone!"
    "(Kuliha is an informal way to say 'hello' in Cunablian language. You won't see it often in the story.)" #added sentence to not confuse players
    "Children" "Kuliha, Lucia!!"
    "The children's happy voices echoed in unison, which was music to Lucia’s ears." 
    "She always loved to hear them giggling and being happy about everything."
    "It reminds her of how she acts every day."
    "Young, carefree, and always able to smile through everything."
    "However…"
    hide lufull1
    show lu1
    lu "It’s always good to be reminded of something though!"
    lu "You should know that you are all great Cunablians who will always remember your true home!" #added small details
    lu "If you wish to travel around the sky, then always know that the Cunablian goddesses will always be with you!"
    "Child #1" "We get it, Lucia! You say that every time you come here!"
    lu "I do?" 
    "Child #2" "Yeah! You even said that a week ago!"
    "Lucia cocked her head."
    lu "I did?"
    lu "(How come I don’t remember any of this?)"
    lu "(Or maybe it's my usual bad memory moments.)"
    "Child #1" "Whatever! How about we celebrate our freedom by singing our usual song?" 
    stop music fadeout 1.0
    "Children" "Yeah!"
    lu "Tee-hee! All right, then!" 
    lu "And a one, two, three…"

    pause 0.5

    play music "audio/Transparent_Childs_Song_3.ogg"
    
    hide lu1
    show lufull1
    lu "My name is Lucia Lock Crimson. Sorry about the long wait for my introduction."
    lu "There are times when you have to be patient on what happens next, though."
    lu "Otherwise, you might not know what the settings are!"
    lu "Anyways, you may have noticed that I am adored by these children in such a small and old classroom."
    lu "Well, that's because I’m a very special 'Aria Goddess.'"
    "The bird flies around the sky and sings, Oh glorious nest! I shall call you home!" #000000
    lu "An Aria Goddess has a very important task in Cunabula." #Changed this sentence to make it shorter.
    "They nurture this very nest to give wonderful homes to every phoenix in the sky."
    "Even granting their phoenix protection with her powers."
    "We sing to our goddess~ thank you for protecting our home over and over~"
    lu "Well? Wanna know what happened to the goddess?"
    hide lufull1
    
    menu:
        "Yes":
            show lu1
            lu "Of course you do!" 
            lu "Curious, aren't you?"
            #changed and added details below:
            lu "So, the goddess was able to restore Cunabula. As time passed, her power weakened, like a phoenix who is about to die and be reborn again."
            lu "But the only difference is that the goddess only has one life to spare."
            #details end here. 
            lu "Her life was fading, and so, she left her soul to a loyal female bird who wished to take over for her." 
            lu "Once the bird with the goddess's soul diminished, the next female bird took the soul and nurtured Cunabula again." 
            lu "Evolutionizing the new forms of her people to transform themselves into birds with 'no feathers', as the new forms are called." 
            lu "After she diminished, another female bird took over to replenish Cunabula, and then another, and then another…"
            lu "The Cunablians needed a goddess to keep the nest healthy and alive."
            lu "It has been a tradition for those who are brave enough to protect Cunabula with their lives."
            lu "Including myself!"
            jump after_choice 
            
        "No":
            show lu1
            lu "Oh, I see. Then I will not say anything about it!"
            lu "I just want to say that I'm so happy I get to live like this!" #changed sentences in here.
            lu "Singing with children and such!"
            "La~ la~ la~"
            scene black with Dissolve (1.0)
            jump tome_choice
        
label after_choice:
    lu "Although some nests do not have a goddess."
    lu "There were various reasons why they wouldn't want one."
    lu "But isn't it necessary to keep the nest alive? Cunablians would say to others." 
    #deleted a sentence below
    lu "Some agreed, for  and others didn't."
    lu "
    lu "In Cunabula, Aria Goddesses are known to be great singers and musicians." 
    lu "This occupation was perfect for me because I get to sing and write music for everyone every day!"  
    lu "It’s always fun to sing with the children too!" 
    "La~ la~ la~"
    lu "Music is everything to me. It saved my life and made me become a better person." 
    lu "I’m so glad I get to live like this!"
    stop music fadeout 1.0
    scene black with Dissolve (1.0)
    jump tome_choice

label tome_choice:
    
    hide lufull1
    scene classroom with Dissolve (1.0)
    pause 
    stop music fadeout 1.0
    play music "audio/Transparent_Prologue.ogg"
    show lu1
    lu "All of you! Please be careful on your way home!"
    "Child #2" "Bye, Lucia! I hope you can visit us again!"
    lu "…"
    "Those words tinged a stinging pain inside her chest." 
    "Visit them again? Impossible..." 
    unknown "Goddess Lucia, may I speak with you?"
    lu "Oh, Teacher! I’m not an Aria Goddess yet!"
    unknown "But you will be soon, am I not correct?"
    lu "…"
    lu "Mr. Emerson told you already?"
    unknown "Of course he did! Just before class started, I was so scared when he came in unannounced!" 
    unknown "If the children were here, then they would have spread horrible rumors about me!"
    lu "..."
    lu "I really want to keep doing this…"
    unknown "Do what?"
    lu "Singing with the children, learning more things from you."
    lu "I never would have thought that this would be the last day..."
    unknown "Oh, Lucia. As much as I want to keep tutoring you every day."
    unknown "How about you take this instead?"
    lu "What is this? A tome?"
    lu "(It doesn't seem to be in good condition.)"
    unknown "It’s an old history book I kept for more than five centuries."
    unknown "You can no longer see those on many bookshelves these days..."
    unknown "I want you to keep it for me."
    lu "What?!"
    lu "But teacher, I can't take this! It's yours in the first place!"
    unknown "I know, but you are the youngest Aria Goddess in history." 
    unknown "You still lack the knowledge of our home and our history from many generations ago." 
    unknown "You did hire me to be your tutor for reading and writing."
    unknown "Now you can read everything from this book!" 
    unknown "Please, take it."
    lu "But-"
    unknown "Please, Lucia!"
    lu "..."
    "What should she do? This teacher seems so serious about this..."
    hide lu1

    menu:
        "Take the tome":
            $ tome_taken = True
            show lu1
            lu "I'll take it."
            unknown "Thank you. That means a lot to me. Good luck for the rest of your eternity!"
            lu "Thank you. I shall bless you for an eternity as well!"
            jump Elsa_intro

        "Don't take it":
            $ tome_taken = False
            show lu1
            lu "I'm sorry..."
            lu "I really shouldn't take this."
            unknown "..."
            unknown "I understand, my dear."
            unknown "Thank you for your time then. Good luck for the rest of your eternity."
            lu "Thank you. I shall bless you for an eternity as well."
            jump Elsa_intro

label Elsa_intro:
    scene center with Dissolve (1.0)
    play music "audio/Transparent_Casual.ogg"
    show lu1
    lu "(Goddess, I never would have thought I’d step out of this small building for the last time.)"
    lu "It’s so quiet…" 
    lu "As it usually is…"
    "This nest wasn’t like this before…"
    lu "Back when I was a child, many birds from different nests would frequently visit Cunabula."
    lu "I would often see droplets of colorful feathers on the ground, allowing" 
    lu "children and myself to collect many of them to decorate every room we own."  
    lu "Oh, how I miss those colorful days when our birds would smile every day..." 
    "If only that ‘incident from 200 years ago’ never happened…"
    lu "Oh!"
    lu "(Did someone pat my shoulder just now?)"
    lu "Mrs. Emerson!" 
    lu "Kuliha!"
    e "Kuliha, Lucia."
    e "You know, you really got to stop calling me by my last name."
    e "We're friends!" 
    e "Can't you remember that?!"
    lu "Sorry! It's kind of embarrassing to call you that in public..."
    e "Lucia! How many times do I have to say that no one cares about that?!" 
    e "You're associated with the Emerson family. Why can't you just accept that?"
    lu "Uhh… I don't know."
    e "Oh, you have so much to learn."
    e "Anyways..."
    if tome_taken:
        e "I see you brought something to work on."
        lu "You mean this tome? Oh, no!"
        lu "It was a gift."
    else:
         e "You just left that classroom already?"        
    
    lu "I... had to say goodbye to one of the best tutors in the world." 
    e "Ah… the teacher you hired for yourself." 
    e "You know, you would have enjoyed the finest tutors my son had." 
    e "Instead, you picked the one that teaches the poor."
    lu "Again with your nagging, Elsa."
    "Lucia sighed heavily."
    lu "I wanted to learn how to read and write normally, so why not?!" 
    lu "I never went through those kinds of normal routines during my childhood!"
    lu "Can't I experience something nice for once?"
    "Elsa reflected the sigh back and shook her head." 
    e "Lucia, don't you remember that you are associated with us? The Emerson family?"
    e "We can do anything for you! We CAN transform you into a wonderful goddess!"
    e "Maybe everyone can change their minds about you too!"
    lu "..."
    e "Oh!"
    e "Lucia, I'm sorry! I-"
    lu "Oh, no. It's okay… it's just that…"
    hide lu1
    
    menu:
        "The children wouldn't like that...":
            show lu1
            lu "Silly Elsa! The children wouldn’t care about that! All they want for me is to express myself for who I really am!" 
            lu "I’d be happy to visit them every day to sing for them! Luna said I can do that when I’m an Aria Goddess!"
            jump stage_time

        "I don't care what everyone thinks!":
            show lu1
            lu "Elsa, who cares about THAT?!"
            e "What do you mean about that?"
            lu "Just everyone saying this and that around me?" 
            lu "I hate it!"
            e "Sorry. I didn't mean to mention it."
            e "I won't say it again."
            lu "Yeah, and you said that around twenty years ago?"
            e "Just let it go, will you?"
            jump stage_time
    
        "Hmm... maybe.":
                show lu1
                lu "Hmm... maybe?"
                e "You're considering it for yourself now?"
                e "Including your people?"
                lu "I don't know... maybe."
                lu "Maybe not."
                jump stage_time

    label stage_time:
    e "*Sigh* Sometimes I worry about you, Lucia."
    e "But I look forward to seeing you tonight!"
    lu "What?"
    "Lucia cocked her head."
    e "What do you mean by ‘what?’ Didn’t ‘she’ tell you about that already?"
    lu "‘She?’"
    stop music 
    "Cunablian citizen" "Hey, look! Luna is about to sing!" 
    "A crowd gathered around Cunabula's center, where all Cunablians would gather around for their usual entertainment."
    lu "At this time? I thought Luna was going to sing tonight."
    e "There has been a last minute change."
    e "It was because we have to prepare for your performance tonight."
    lu "My performance?"
    lu "Wait a minute... that's right!"
    hide lu1
    show lufull1
    lu "Today is my last day as an Aria Goddess in training!"
    hide lufull1
    show lu1
    lu "(Goddess... I wish I couldn't have forgotten like I did just now!)"
    lu "(I have to perform inside the castle to 'honor' myself as their secondary Aria Goddess.)"
    lu "(Oh, goddess, it's coming soon!)" 
    b1 "Luna!"
    "As Lucia pondered a bit, a piercing screech made her body jump." 
    b1 "Look over here, Luna!"
    b1 "Luna!"
    b1 "Luna!"
    "She was easily frightened by the slightest sound as she thought to herself." 
    "Lucia is silly that way, but what angers her more is when the music is about to play." 
    "There is unwanted commotion in the middle of nowhere..." 
    b1 "Luna! Praise our goddess!"
    b1 "For she is the one who shall nurture our nest!"
    "Lucia wanted to shout ‘shut up!’ at him right now…" 
    "She wanted to listen to her music peacefully and quietly right now..."
    b1 "Yes! She is our one true goddess who shall serve us for centuries!"
    lu "Grrrr…"
    e "We should move to another spot."
    "Finally, as soon as they did, Lucia was finally able to relax."
    
    stop music fadeout 1.0

    jump Luna_intro

label Luna_intro:
    
    play music "audio/Transparent_Lunas_Song_Ver1_.ogg"
    
    "And soon, the music began to play."
    "Everyone became quiet. All eyes went onto the being who carries an Aria Goddess' soul..."
    hide lu1
    show lunfull1 with Dissolve (2.0)
    "Luna... a name that has never ceased for centuries."
    "Luna... an individual who always sang in this small area for many centuries..."
    "She cupped her hands together to show her prayers for the Cunablian people."
    "Her people joined in her gesture as they showed their prayers toward their beloved figure." 
    "Lucia became lost in the sound of the music."  
    "She then looked at Luna, who happened to be her mentor."
    "Who happened to be the original Aria Goddess that everyone honors..."
    "So beautiful… the way the sun shines around the golden chains around her, even the way her voice echoes around the nest."
    hide lunfull1
    show lu1
    lu "(Although only a full-fledged Aria Goddess can stand on this stage.)" 
    lu "(I’m not even there yet...)"
    lu "I always looked forward to seeing myself up there. I would sing many songs, I would offer lots of prayers and blessings…"
    lu "It’s kind of… exciting when I think about it now."
    "Lucia held Elsa's hand. It was because she felt like it."
    "Elsa squeezed back, sharing their feelings on how music can connect their hearts."
    "Woman" "Hey, isn’t that Lucia Lock Crimson?"
    "Suddenly, a loud voice rang out during the concert."
    "Lucia tightened her grip on Elsa's hand." 
    "Woman #2" "What is she doing here?"
    "Woman" "I bet she's here to ruin the concert!"
    "Woman" "By what? Screaming about someone trying to kill her again?"
    "Woman" "Isn't that what she did when she was a little girl? She does this day and night! I couldn't get my beauty sleep because of her!"
    "Woman" "Not to mention that she has done this ever since she was a little girl!"
    "Woman" "I wouldn’t be surprised if anyone is going to kill her! I would feel a lot safer if she’s not around!"
    "Those voices echoed through her mind, absorbing the information to remind her of her past self."
    "They were right about her... just before she became an Aria Goddess a century ago."
    "She was a child who would often scream out of nowhere."
    "Unable to control her body, unable to control her image..."
    "She can never take back what she did before..."
    hide lu1
    show lufull1
    lu "Maybe I should just... leave."
    "Elsa tightened her grip."
    e "Stay."
    lu "But Elsa!"
    stop music fadeout 0.5
    "Woman" "I feel sorry for our Aria Goddess! Why would she entrust half of her ‘sacred soul’ to that ‘bird’?"
    "Woman" "Maybe it was because of that greedy mind of hers?"
    "Woman" "And what does she do?! Spend time with a bunch of children all day! Is she trying to ruin their minds too?" 
    "Woman" "Oh, is she going to scream again?"
    "Woman #2" "It looks like she's going to cry!" 
    "Woman" "For what? Knowing that SHE'S NOT going to be our goddess soon?!"
    unknown "You two better have a VERY GOOD reason for TALKING during MY concert!" 
    hide lufull1
    show lunfull1 
    stop music fadeout 0.5
    lu "Luna?!"
    "Luna’s loud voice exploded throughout the entire nest, causing the music to cease and all eyes to turn her direction." 
    "Woman" '*Gasp* My goddess!'
    'Woman #2' "We apologize! We didn't mean to interrupt your concert!"
    hide lunfull1
    "The women glared at Lucia, forcing her to hide herself behind Elsa's back." # replaced "quiver" with "hide"
    hide lufull1
    show lu1
    "Just seeing her people stare like that..." 
    "Those disappointed eyes that make her feel like a burden every day..."
    "It was too much for her to handle..."
    hide lu1
    show lunfull1
    lun 'So, do you two have anything else to say?' # replaced "something" with "anything"
    lun "To me? Or to her?"
    lu "(Uh oh, that smile! I know that smile!)"
    lu "(It's not her usual happy one!)"
    lu "(It's the smile that no one would like to see!)"
    lu "It looks like they got the message! Just look at their faces! They look horrified!" 
    lun "Well?"
    'Woman' "We’re-we're very sorry!"
    "Woman #1" "We'll leave!"
    'The two women bowed formally at her, and then they walked away.'
    "One took a dark glance at Lucia."
    "While the other tried not to."
    lu "(Luna… I’m sorry I have to keep making you do this…)"
    hide lunfull1
    jump Luna_talk

label Luna_talk:
    
    play music "audio/Transparent_Lunas_Song_No_Lead_.ogg"
    
    'The same music still plays, but Luna descends from the stage.'
    "Now she is surrounded by her people, having Lucia smile at her from a distance." 
    "Everyone pretended that nothing happened. She couldn’t help but feel really bad about it."
    "Maybe she should have never come here in the first place."
    "Or maybe her existence is-"
    e "Lucia, are you all right?"
    show lu1
    lu "…!"
    lu "I’m okay…"
    lu "(Maybe not...)"
    e "I worry about you, Lucia." 
    e "Why can't our birds just accept you the way you are?"
    e "It's really not fair."
    lu "I know, but... life is not fair."
    lu "But the past is in the past. I can't go back from what I did."
    lu "My people will always remember that."
    lun "That's the spirit! Lucia, I'm proud of you!"
    hide lu1
    show lun1 at right with Dissolve (1.0)
    show lu1 at left
    lu "Luna!"
    e "Kuliha, Luna."
    lun "Kuliha, Mrs. Emerson."
    "Luna formally bowed at her." # replaced the "s" at the end of "bows" with "ed"
    lun "How is your son doing?"
    e "He is doing very well!"
    e "You know, he just made a new friend recently! Now he’s going outside very often with him!"
    lun "That sounds wonderful!"
    lu "Is he around his age?"
    e "Hmm... he is slightly younger than Tyrus, but he’s still in a good range!"
    lun "Oh, speaking of young people."
    "Luna looked at Lucia, making her body jolt from the strike of her innocent smile." # replaced the "s" at the end of "looks" with "ed"
    "It's that same smile she used at the two women earlier. Lucia wanted to back away, but she couldn't." 
    lun "Is there something wrong, Lucia?"
    hide lu1
    show lufull1 at left
    lu "Oh, uhh… It's nothing."
    hide lufull1
    show lu1 at left
    lun "Really? Are you thinking about how you're becoming an Aria Goddess at the age of 316?" # added "how you're" between "about" and "becoming"
    lun "That's the average age of phoenixes who would become new warriors!"
    lun "That makes me very jealous! I became an Aria Goddess at the age of 350!"
    e "Really? I became a deputy when I was at least 500 years old!"
    lun "That's because you had to take extra years of training as a knight, Mrs. Emerson!"
    lun "Sounds pretty hard!"
    e "To you, it is! I was actually okay with that since I needed the extra strength to really protect you and Lucia from harm!"
    e "It's quite interesting for two female birds to become an Aria Goddess!"
    e "It never happened before, but you two make a good pair!"
    lu "R-really?"
    lun "Well, anyways! At least this is what you always wanted to do, Lucia!"
    lun "Are you ready for this?"
    lu "I-I don't know! Am I ready for this?"
    lun "Lucia… that’s exactly how I felt when I first started as an Aria Goddess in training."
    lun "It’s a completely normal feeling!"
    lu "Are you sure? Then why is my heart beating so fast?"
    e "That’s another normal feeling! You’re excited, but nervous at the same time!"
    e "It’s okay to be scared! You’ll do great!" 
    e "Oh, shoot! I should get back to my duty! Look forward to hearing from you soon!"
    lun "Bye~"
    lu "B-bye…"
    lu "(All right, Lucia. Deep breaths, deep breaths…)"
    lun "Are you okay, Lucia?"
    "Luna lifted her right hand, which contains the same golden hand bracelet Lucia wore on her left hand."
    "Then, she felt a tiny warmth on her cheek." # replaced "from" with "on"
    "Her heart skipped a beat when Luna’s warm touch tingled around her hand."
    "It reminded her of how wonderful she looked on stage…"
    "So beautiful… so fair…"
    "Those words did not define Lucia Lock Crimson…"
    lun "Lucia?"
    lu "Huh?"
    lun "I said..."
    lun "Do you like my hand bracelet?"
    lu "Oh, uhh... you gave it to me as soon as we met, right?"
    lu "Of course, I like the design and-"
    lun "Have any thoughts of a song to sing tonight?"
    lu "Oh!"
    lu "Ahaha... I think the one Mr. Emerson wrote for me is good enough…"
    lun "What?"
    lun "You wrote other songs for yourself, so why not use those instead?"
    lu "But.. those songs were written for the children…"
    lun "Don’t you always say that these songs can be used to bring old smiles back?"
    lu "I…"
    lu "I’m not exactly sure if that’ll happen to the others."
    lu "Luna, you’re older than I am. Surely, you must have seen that sudden change after that incident 200 years ago."
    lun "You mean 'The Great Fire?' I will never forget that day! Nobody will!"
    lun "Of course, it really damaged the nest. Mr. Emerson really tried his best to maintain the peace."
    lun "Even making that law to ban all Nosirians from Cunabula."
    lun "It's completely ridiculous of him to think of that law. Do you think so too?"
    lu "Why not talk to Mr. Emerson about this?"
    lun "..."
    lun "I don't have the power to get rid of that law." # removed the "s" at the end of "powers" and replaced "break" with "get rid of" (since, as far as I know, "breaking the law" means something different from what was most likely meant)
    lun "But I bet your music can wake our people up! It's completely different from what Mr. Emerson usually writes!"
    lun "He writes for the new generations, while you write for the older generations."
    lun "I can only follow directions from the music he writes for me. Only you can follow your own directions."
    lun "Look, just pick one song that you wrote and play it tonight!"  # removed the second "just" and "for"
    lun "Everyone will see how wonderful you can be in the future!"
    lu "But…"
    lun "I’ll be there to guide you until the very end."
    lun "It’s a promise!"
    lu "T-thank you very much."
    "Sighing in relief, she didn't have to be alone in this."
    "Lately, her father had been avoiding her. Perhaps he didn't want to talk about her upcoming position as the new Aria Goddess."
    "It made her feel left out, almost as if she never existed at his side again." # replaced the first period with a comma and decapitalized "almost"
    "After a century being together as a family, their relationship seemed to have… dispelled, like an old phoenix fading away to be reborn again." # added a comma after "dispelled", replaced "as" with "like", and replaced "would fade" with "fading away"
    lun "After you perform for us…"
    lun "Mr. Emerson is planning to make a big feast for you, but you’re still not used to eating our chef’s food."
    lun "You always go to that woman’s house or even your father’s house for your daily meals."
    lun "*Sigh* Goddess, I worry about you sometimes."
    lu "(Why does everyone have to say that?)"
    lun "At least enjoy the food once in a while! It’s always delicious with one of their finest wines!"
    lu "I…"
    lu "I don’t know."
    lu "I don't want them to be lonely or be hungry alone."
    lun "You always say that... At least join me for a little meal once in a while! It’ll be great!" 
    lun "Just think about it! You, me, the Emerson family, gathered with all the famous knights for wonderful dinner nights!"
    lun "I'm sure you'll enjoy every meal the chefs will serve you!"
    lu "..."
    lu "I…"
    hide lun1
    hide lu1

    menu:
        "I'd rather eat with my family and friends, though.":
            show lu1 at left
            show lun1 at right
            lun "Oh, I completely understand."
            lun "I always miss the times when my family and I would always eat together."
            lu "(Liar. I can see that from the look of your face.)"
            lu "What about your family?"
            lun "...!"
            lun "..."
            lu "Luna, did I say something wrong?"
            lun "..."
            lun "Oh no. You didn't say anything wrong."
            lun "It's just that… my father and I are usually busy at times."
            lun "We don't usually have a lot of time to talk."
            lun "We had this conversation before, remember?"
            lu "...!"    
            lu "(Goddess! How can I not remember?!)"
            lu "Sorry!"
            lun "Don’t worry about it, Lucia. I have you and the Emerson family!"
            jump cheese_talk

        "I really don't like the food...":
            show lu1 at left
            show lun1 at right
            lun "What???? I love their food!"
            lun "It’s completely different from what I eat every day!"
            lun "Oh~ The roast beef the chefs would make would always come so savory and tender!" 
            lun "Not compared to my father’s cooking. It would always come out dry and bland!"
            lu "Well, you should be grateful that your father is committed to cooking for you!"
            lun "Oh, Lucia… you don’t know what he cooks everyday…"
            lun "It’s… ah…"
            lun "You don’t want to know."
            jump cheese_talk

        "I would like for you to eat with my family and friends for once!":
            show lu1 at left
            show lun1 at right
            lun "Me?! Joining your family?"
            lu "Yes! I’m sure my father won’t mind!"
            lu "We can build a campfire and sing lots of different songs together!"
            lu "I’m sure you have many songs to share too! Your voice is really amazing!" 
            lu "So powerful and operatic! My voice is nothing compared to yours!"
            lu "I wish I can be just like you!"
            lun "…"
            lu "…"
            lu "Did I… say something wrong?"
            lun "Hehe! No, it's nothing."
            jump cheese_talk
            
    label cheese_talk:
    lun "Hmm~ I wonder what the Emerson family will serve today?"
    lun "Is there going to be cheese? I would love to have some of their delicious cheese again!"
    lun "What was it again? Mozz? It does taste great with some tomato, basil, olive oil..." 
    lu "…"
    lu "(Luna... at least talk about what's bothering you."
    lu "(I'm your secondary goddess and your friend. Do you not trust me?)"
    
    stop music fadeout 0.5
    play music "audio/Transparent_Casual.ogg"
    scene castle_entrance with Dissolve (1.0)
    
    hide lun1
    hide lu1
    "After that, Lucia and Luna walked towards the castle’s entrance."
    "They were greeted by the guards formally, and then, they opened the gate for them."
    show lun1 at right
    show lu1 at left
    lun "Lucia, would you like to use the time to find a song for you to perform?"
    lu "I'd love to!"
    ty "A song from Miss Crimson? I look forward to hearing it soon!"
    lu "Oh, Tyrus!"
    lu "What are you doing here?"
    ty "I just returned from my daily stroll."
    lun "With your new friend?" # replaced "From" with "With"
    ty "H-how did you know?"
    lun "Oh, come on, Tyrus! Everyone is talking about it!" # added a comma after "Oh"
    lun "You've been smiling a lot lately. Was it because of him?"
    ty "..."
    lu "(Tee-hee! He looks so cute whenever he blushes!)" # added "ed" to the end of "blush"
    ty "*Ahem!*"
    ty "Please allow me to apologize for not attending your concert, Miss Luna."
    lun "Oh no, it's all right!"
    lun "It was scheduled at the very last minute! You don't need to apologize!"
    lun "Is someone here to escort you back to your room, though?"
    ty "...Not really." 
    lu "Guards! Weren’t you supposed to help him?!"
    lun "Now, now, Lucia…" 
    lun "I’m sure he can call a servant from this very distance."
    lu "But what if he were in danger?"
    lu "He can hear what’s approaching him, but he can’t SEE what it is!"
    ty "Lucia, please. Don't make a scene."
    ty "That was a joke."
    "………………" #pause for a bit
    
    pause 1.0
    
    lun "Ahahaha!"
    lu "Ouch…"
    lu "Luna, I don’t get it."
    lun "You don’t have to."
    lu "Ah!"
    "Suddenly, a huge bird came behind Tyrus."
    "His shadow completely covered the little bird, who stood up calmly and took the servant’s huge wing!"
    ty "It was good to greet you two again. Now, if you'll excuse me."
    lu "(Goddess… I should get used to this by now. Both Mr. and Mrs. Emerson must have really wanted to protect him...)"
    lu "…"
    lun "Oh, don’t be so hard on him. He’s growing up to become a great knight to the Emerson family."
    lu "But… he’s unable to move around the castle without assistance. He can’t even see how beautiful Cunabula is…"
    lun "You shouldn’t worry about him that much. He will adapt himself in the future." 
    lun "You should worry about your... spirit possessing you ever since you were a child."
    lu "…"
    lu "Must you remind me of that?"
    lun "I'm sorry, but you have to face it."
    lun "Remember what I said to you last night?"
    hide lun1
    hide lu1

    menu:
        "Lucia shook her head":
            show lu1 at left
            lu "..."
            show lun1 at right
            lun "It’s all right, I can remind you."
            jump you_are_what_you_are

        "Lucia nodded her head":
            show lun1 at right
            lun "Are you sure? What did I say last night?"
            show lu1 at left
            lu "Oh, uhh..."
            lun "You have to be honest with me, Lucia."
            jump you_are_what_you_are
    
    label you_are_what_you_are:
    lun "You are what you are, Lucia. You can change yourself, or someone else will change you."
    lun "Just know that you are one of us."
    lun "And that spirit-"
    jump Azure_intro
   

label Azure_intro:
    
    stop music fadeout 0.5
    play music "audio/Transparent_Childs_Song_3.ogg"
    
    lg "Goddess Luna! Goddess Luna!"
    "Both women were shaken up by the sudden call of two children running towards her."
    "Not looking at Lucia, she smiled at them. She had gotten used to the fact that other children wouldn't look up to her either."
    "They don't seem to be the ones Lucia would frequently see in the classroom she would visit." 
    "They seemed to be wearing uniforms rather than their casual clothing."
    hide lu1
    lg "Miss Aria Goddess. Can you take this?"
    lun "Of course!"
    lb "Hey! Didn’t I say I should go first?!"
    lg "Oh really? Didn’t Mom say I should always go first?!"
    lb "And why is that?!"
    lg "'Cause I’m a lady! Don’t you even remember the code in this nest?" # added an apostrophe to the beginning of "Cause"
    lg "All men should respect all female birds and goddesses becau-"
    lb "Quiet, you! I don’t want to hear about this again!"
    lg "Hey! Don’t push me!"
    lun "Oh my goddess…"
    "Luna began to sigh heavily, and she shook her head at them."
    show lufull1 at left
    "This is not a good sign…"
    "Luna is not the type of person who could handle children!"
    "Nobody knows why, not even Lucia. Luna never liked ’misbehaving’ children even when she was a young child herself." # removed "before"
    lu "Children, please! Stop fighting!"
    "Just when Lucia was about to crouch down, her shoulder was grasped by a soft hand."
    hide lun1
    show lunfull1 at right
    lun "Lucia, let me handle this."
    lu "Are you-"

    stop music fadeout 0.5

    lun "It’s all right. They don’t seem to be ‘obedient’ enough to listen to you."
    lu "(Oh no… I've got a bad feeling about this!)"
    hide lufull1
    hide lunfull1
    show lun1
    "Luna crouched down and gave them a friendly smile."
    lun "Now, you two are a family. Why must you fight?"

    play music "audio/Transparent_Despair_.ogg"

    lb "We’re not family."
    "The little boy crossed his arms and turned his back away from the little girl."
    lg "You’re just jealous because Mom loves me more!"
    lb "You don’t have priorities! I’m stronger than you are!"
    lg "Oh yeah! Well, I can be an Aria Goddess when I grow up! And you can’t just because you’re a boy!"
    lb "Shut up!"
    lb "You've been nothing but a nuisance in my life!"
    lb "I hate you! I wish you were never born!"
    lb "I wish you never existed in the first place!"
    hide lun1
    show lu1
    lu "…!"
    lu "(Goddess… that’s so cruel…)"
    lu "(How could he say that to this poor little girl?)" # replaced "can" with "could" and the first "this" with "that"
    hide lu1
    show lun1 at right
    lun "This is why I dislike children…"
    lun "Always so immature!"
    show lu1 at left
    lu "Luna…"
    "How long has it been since she saw her this way?"
    "For so long, she had seen many good sides of her." 
    "However… there lies a beast inside of her. It sleeps inside of her, peacefully… until the night gets noisy…"
    "It now releases itself from Luna's body..."
    lu "No, Luna. Please don't do this to them..."
    hide lu1
    hide lun1
    lg "Goddess gracious! You're so noisy!"
    lg "Watch and learn, stupid boy!"
    "The little girl approached Luna and bowed formally to her." 
    lg "I apologize, my lady. Please excuse my rowdy little brother, for he is not worthy of your presence." # replaced "to be in" with "of"
    lg "Perhaps he is not worthy of existing in this world at all." # replaced "to exist" with "of existing"
    lb "Grrr!!!"
    "The little boy began to crush his gift…"
    "Crushing Lucia’s chest as well."
    lg "Please accept my gift as a token of my gratitude."
    "Luna smiled innocently, pretending to not notice the boy's reaction." 
    show lun1
    lun 'You speak well. Then I shall humbly accept your gift.'  
    lun "And maybe you’re right, that boy is not worth my presence anyway." 
    show lu1 at left
    lu 'Luna!'
    lu "(Goddess! I should be used to this by now! But the way she treats the other children... it's just not fair!)" # replaced "get" with "be" and adding "by" between "this" and "now"
    hide lu1
    lg "I’m so glad you agree with me!"
    lg "Come on, stupid boy! We’re going home, and I’m going to tell Mom that you pushed me!"
    lb "…"
    "He sprinted out of the area, not looking back at the three female individuals with only one that showed pity."
    hide lun1
    show lufull1 
    lu "Poor boy… Why does he have to be treated that way?"
    lu "Is it because that little girl is taking advantage of the rules? For all female birds to be respected?"
    lu "Why?"
    hide lufull1
    lg "Oh, so the stupid boy decides to run? What a coward!" 
    lg "Please excuse me."
    lun "I hope to see you again!"
    "The little girl smiled widely."
    lg "Thank you very much, my goddess!"
    "Then she skipped out of the scene, leaving Lucia’s boiling anger to finally be released."
    show lu1 at left
    lu "What the heck was that?!"
    show lun1 at right
    lun "Lucia, please don’t scream in front of the others. That's very immature of you."
    lu "How could you say that to this poor little boy?!" 
    lu "You could at least be a little nicer to him!" 
    lun "I wish I could, but…"
    lun "Somehow, I can’t stand children… and I can’t take back what I just said."
    lun "Maybe you can… tend to him for me?"
    hide lun1
    hide lu1

    menu:
        "Why don’t you tend to him yourself?":
            show lu1 at left
            lu "Why don't you do it yourself?!"
            show lun1 at right
            lun "He’s already mad at me."
            lun "I can’t just talk to him like this…"
            lu "(Liar! You’re just looking for an excuse to not talk to him at all!)"
            jump negative_voice_intro

        "O-okay, I’ll be right back.":
            show lu1 at left
            lu "O-okay, I’ll be right back."
            show lun1 at right
            lun "Sorry, I’ll wait for you in the castle."
            lu "Yes, ma’am."
            jump negative_voice_intro

label negative_voice_intro:
    hide lun1
    hide lu1
    scene center with Dissolve (1.0)
    show lu1
    lu "Poor boy… where could he be?"
    lg "Are you Lucia Lock Crimson? Luna’s secondary goddess?"
    stop music fadeout 0.5
    hide lu1
    show lufull1
    lu "Ah!"
    lu "Oh, it's you."

    play music "audio/Transparent_Childs_Song_3.ogg"
    
    "She really needs to stop doing that."
    "Getting scared by little things out of nowhere."
    "The child was tilting her head, perhaps wondering why Lucia is like that."
    
    hide lufull1
    show lu1
    lu "*Ahem!* How may I help you?"
    lg "Please forgive me for taking up your time, but…"
    lg "Will you accept this gift for me?"
    lu "Oh! You have one for me too?"
    lu "No one has given me one before!"
    lg "Of course! Why would I exclude you from our home?"
    "*Exclude her from their home?* Those words stung her. Perhaps this little girl has a lot to learn."
    "She never learned of her past… her childhood… her mistakes…"
    lg "My lady?"
    lu "!"    
    "Snapped back to reality, Lucia instantly thought of something to say to the little girl…"
    hide lu1

    menu:
        "I don’t know":
            show lu1
            lu "I don't know."
            lg "What do you mean you don’t know?"
            lg "Look at yourself! You’re a beautiful bird who wishes to become just like Luna!"
            lg "Think about the benefits you can get when you work with her!"
            jump cookie_choices      

        "Children love me more, I suppose?":
            show lu1
            lu "Children love me more, I suppose?"
            lg "I noticed!"
            lg "You know that most of my friends are around my age. They would talk about you very often!"
            lg "Of course, my parents would often recognize Luna just because she has been their Aria Goddess for so many centuries."
            lg "I suppose a little change would be nice, right?"
            jump cookie_choices

            
        "I guess I’m just too different for my people.":
            show lu1
            lu "I guess I’m just too different for my people."
            lg "Luna has been a goddess for quite a long time. My parents were pretty young when she got started…"
            lg "Do you know how old she is right now?"
            lu "I don’t know… every time I tried to ask, she would change the subject."
            lu "I’m already 316 years old myself, so… I’m a very young woman right now."
            lg "Teehee! I’m already 50 years old, and I’m still young!"
            jump cookie_choices
    
    label cookie_choices:
    lg "Anyways, here! It’s a bunch of cookies I made for you and Luna!"
    lu "Oh, uhh…"
    lu "(You didn't have to tell me what it was.)"

    stop music fadeout 0.5
    scene black 
    "You shouldn't take those, Lucia." #000000
    scene center
    show lu1
    lu "...!"
    lu "No... it can't be!"
    hide lu1
    scene black
    "Do you want to die so much, Lucia?" #000000
    scene center
    show lu1
    lu "No… not you again!"

    play music "audio/Transparent_Suspicions.ogg"

    lg "My lady? Are you alright?"
    lu "I’m- I’m fine…"
    lg "Are you sure? You look really pale."
    lu "Oh, really?"
    hide lu1
    scene black
    "What if these cookies are dangerous?" #000000
    show lu1
    lu "…!"
    lu "(Please… don’t do this to me! This little girl will be very sad if I don’t take them!)"
    "Don't take them! These cookies are not worth anything!" #000000
    "Those things will kill you!"
    lu "Stop it! Just shut up already!"
    scene center
    show lu1
    lg "My lady, are you okay?"
    "Citizen" "Little girl! Little girl! I suggest you stay away from this woman!"
    lg "What, why?"
    "Citizen" "Trust me, okay?!"
    lu "Please... please... please…"
    lu "I’m not sick… I’m not sick… I’m not sick…"
    lu "(But what if it’s right? It did get me out of trouble a bunch of times before…)"
    lu "(It saved me from a spear that was launched in my direction by accident once.)" # replaced the "ing" at the end of "launching" with "ed" and added "that was" before it
    lu "(But... I got in trouble once for putting in the wrong music sheet for Luna's daily performance.)"
    lu "(I can choose whatever, but it will affect my 'ending'.)"
    lu "All right, Lucia. Calm down…"
    lu "(Breathe in... breathe out..."
    lu "(No! It's not working! No!)"
    lu "(What should I do?! I should just say something right now or else!)"
    hide lu1

    menu:
        "Take them":
            show lu1
            lu "I’m… sorry…"
            lg "What?"
            lu "I was acting very strange earlier. I shall humbly accept your gift."
            lg "Really?! Thank you!"
            lg "I hope you like them!"
            lu "…"
            $ take_cookies = True
            jump the_boy
        
        "Don't take them":
            show lu1
            lu "I can’t take these!" 
            lg "What, why?"
            lu "Just take them back, please!" 
            "Citizen" "Come, little girl! Leave her!"
            lg "But-"
            "Citizen" "Let's go!"
            lg "No, wait! You don’t understand!"
            $ take_cookies = False
            jump the_boy

    label the_boy:
    lu "…"
    lu "Goddess, does this thing have to ruin everything again?"
    "Lucia could suddenly hear the loud whispers of her people…"
    "Is she doing it again?"
    "She just screamed at that little girl!"
    "What a horrible bird she is!"
    lu "(Please… just stop… I hate this!)"
    lu "(Why can’t you just set me free? So I can bring smiles to my people again?)"
    hide lu1
    "Her knees slammed down on the ground, and she placed her hands onto her head."
    scene black with Dissolve (1.0)
    "Those haunting voices blending with the ones inside her continued to abuse her mind."
    "Even when she was having a bright future…"
    "This curse… it was too much for her to handle…"
    unknown "My lady!"

    stop music fadeout 0.5
    scene center
    show lu1
    lu "!"
    "Suddenly, Lucia’s skirt was being tugged from one side."
    "She looked down…"
    "A child… a little boy that possessed such rare lavender eyes that were not as bright as hers."
    lu "(When and where did he come from? How did he get here?)"
    lu "(And most of all… did he actually approach me?)"
    lb "Let’s go somewhere else."
    "The child grasped her wrist and pulled her off the ground."
    "Soon, she began to run. The loud whispers and the voices had suddenly vanished…"
    "What was going on?"
    hide lu1
    jump kid_talk

label kid_talk:

    play music "audio/Transparent_Casual.ogg"
    
    scene classroom with dissolve
    show lufull1
    lu "Oh, isn’t that the place I…"
    lb "I’m surprised you don’t even recognize me."
    lb "You know, I used to sit back here."
    hide lufull1
    show lu1
    lu "Oh… I usually don’t look at that area."
    lu "Sorry."
    lb "…"
    if take_cookies:
        lb "Aren't you going to eat those?"
        "He pointed at the cookie box." # replaced "to" with "at"
        lu "Oh, uhh…"
        lu "I'll save those for later."
        lb "Really? I wouldn't suggest eating them at all. Those are rosemary cookies. Do you know how gross that is?"
        lu "Rosemary… cookies?"
        lu "I hate rosemary."
        lu "Luna loves them though!"
        lb "Don't eat them. Trust me."
        jump rumors        
    else:
        lb "Oh? You didn't take the rosemary cookies?"
        lu "Rosemary cookies?"
        lb "Oh."
        lb "Never mind."
        lb "It's best that you didn't take them. It's gross."
        lu "I would... agree." 
        lu "(Ugh, rosemary... I hate rosemary.)"
        jump rumors

label rumors:

    lb "Anyways, I heard strange rumors about you."
    lb "You always seem so happy every day, but you would always show a different side."
    lb "It looks like I was able to see it today."
    lb "Is that why everyone treats you differently?"
    "Lucia can't help but nod her head." 
    "She can't deny that... everyone always hated that." 
    "It was something Lucia was already used to being treated as every day…" # replaced "is" with "was"
    lb "It sucks, doesn’t it? When people start spreading rumors, they’re going to listen to more than one person at a time."
    lb "They don't want to listen to you."
    lu "Well, there is one thing we can confirm."
    lu "I'm a crazy bird."
    lb "Well, we can confirm something else too."
    lb "Luna, our current Aria Goddess, is no good with children."
    lb "And yet, they still honor her as their goddess. Not exactly you, even though you two share the Goddess' soul."
    lu "You're right..."
    lu "I guess I'm just not right for them."
    lb "Do you think I'm a bad kid?"
    lu "Huh? Where is this coming from?"
    lb "I don't know. I just thought of it a while ago."
    lb "I don't get along with a lot of kids at school. I always get in trouble with the teachers over nothing."
    lb "I also don't get along with my family."
    lb "Does that make me a bad kid?"
    hide lu1
    
    menu:
        "You're not a bad child!":
            show lu1
            lu "You're not a child!"
            lb "Are you certain about that?"
            lu "…"
            lb "I knew it… "
            jump bad_boy

        "Well… you treated your sister very horribly!":
            show lu1
            lu "Well... you treated your sister very horribly!"
            lb "You should have seen the way she treated me too!"
            lb "Those birds are right. You really are a dumb bird."
            lu "I'm sorry, but it's the truth."
            lb "I see… then you're siding with her..."
            jump bad_boy

        "Why not look at yourself?":
            show lu1
            lu "Why not look at yourself?"
            lb "Oh? So you’re attacking me back?"
            lb "Just when I thought you were a better person than that!"
            lb "You sound just like that girl you saw earlier!"
            lb "So I guess you know the results."
            jump bad_boy

    stop music fadeout 0.5

    play music "audio/Transparent_Despair_.ogg"

label bad_boy:
    lb "It’s just as that girl said… I’m not good for anyone…"
    lu "That’s not true!"
    lu "I know you're better than anyone else!"
    lb "Oh yeah? You barely even know me!"
    lb "You know what? Just leave me alone!"
    "The child lowered his head, making her chest tinge heavily in guilt at the harsh truth."
    "He was right; Lucia doesn’t even know this child one bit."
    "She would always say that just to make them feel better, perhaps to make them feel good about themselves…"
    "Children should be positive all the time. They shouldn’t be so negative all the time…"
    "Usually they would feel better when she says that, but… this is the first time she encountered a stubborn child…"
    "Should she leave him alone or not?"
    hide lu1

    menu:
        "No":
            jump no_choice

        "Okay, sorry to bother you.":
            show lu1
            lu "Okay, sorry to bother you."
            $ leave_boy = True
            hide lu1
            show lufull1
            "Lucia got up from her desk and left the classroom."
            jump leave_boy2
            
label leave_boy2:
    hide lufull1
    scene castle_entrance with Dissolve (1.0)
    "She stepped back into a very familiar area." # replaced "Stepping" with "She stepped"
    show lunfull1
    lun "Oh, you're back!"
    "Luna was sitting on the staircase, sipping tea and nibbling her cookies."
    hide lunfull1
    show lu1 
    if take_cookies:
        hide lu1
        show lufull1
        "That reminds her... she left HER cookies in the classroom..."
        lu "Oops!"
        jump backtonormal
    else:
        "That reminds her... she didn't take the girl's cookies."
        lu "..."
        jump backtonormal
        
    label backtonormal:
    show lu1 at left
    lu "Luna. Why are you sipping tea at a place like this?"
    show lun1 at right
    lun "I was waiting for you to get back here. I wanted to show you something." 
    lu "Oh..."
    lu "Luna!"
    lun "Yes?"
    lu "Oh, uhh..."

    menu:
        "About earlier…":
            lu "About earlier… I'm sorry."
            lun "Sorry about what?"
            lun "You have your own opinion, and I have mine."
            lun "Our disagreements would lead to conflict, but we have to learn from each other and work things out together."
            lun "We'll have to start later, though. I have something important to tell you."
            lun "Would you mind talking about this later?"
            lu "I don't mind."
            jump continueon

        "Did you know that these are rosemary cookies?":
            lun "Of course I did. The smell was very strong, but it was very delicious!"
            lun "There's still some left! Would you like some?"
            lu "I'll pass."
            jump continueon

            
label no_choice:
    $ leave_boy = False
    stop music fadeout 1.0
    show lu1
    lu "No."
    lu "I’m not leaving you like this."
    lu "Is there anything I can do for you?"
    lb "What the heck is your problem? Why can’t you just leave me alone?!"
    lu "You shouldn’t say those horrible words to others!"
    lu "How in the world am I going to help you if you’re just going to act this way?!"
    lu "You're... completely selfish!"
    lb "…"
    lu "Oh!"
    lu "I'm sorry! I didn't mean to! My foster father would say that a lot whenever I get angry and-"    
    lb "You sound just like my father…"
    lb "I guess you’re not stupid as that girl is."
    lu "Why are you calling your sister ‘that girl?’"
    lu "Isn't she your family?"
    lb "I’m adopted. All I had was my father, and now he’s gone." 
    lu "..."
    "Now it makes sense… he is an outsider…"
    "It's almost as if… he reminded her of something..."
    lb "I was forced to transfer to another school because of my new parents." # replaced "I'm" with "I was" (at least, I THINK that's correct)
    lb "I hate this place… it's full of stupid, spoiled kids who think they can do anything by having money." # added a comma after "stupid"
    lb "I miss my friends… and most of all, I miss singing with you too."
    lu "…!"
    lu "Singing with me?"
    lb "Yeah, my foster father would often take me to work to let me hear your voice."
    lb "I like the lyrics you wrote. It reflects a lot of my life." # replaced "made" with "wrote" (because you "write" lyrics, right?) and "about" with "of"
    lb "Plus, my foster father is a widower. It's always hard to see him cry at home everyday."
    lb "You might not remember him, but I remember you wrote music and sang for him."
    lb "The look on his face was brilliant."
    lb "If it weren't for you, then my dad would have never recovered from his long sorrow from the loss of my mother."
    lb "I haven't had the chance to thank you yet."
    lu "It's nothing! I actually write music daily just to cope with many servants' sorrows!"
    lu "It's what I do!"
    lb "Really? Other birds say you can write any music for them, and it would sound good."
    lb "Even your lyrics would fit their current feelings too, even when they are relaxing in some flower field or something." 
    lb "Your songs are different from what Mr. Emerson usually writes. His are nothing but boring traditional music..."
    lb "Yours just talks about how to live on even when there are sad times."
    lu "(Oh really? Is that what children think about?)"
    lu "(That makes me feel so...)"
    lu "(Happy!)"
    lb "Maybe it’s fine for me to not go back anyway."
    lb "After being so angry at her again, I bet she’s going to act all whiny and stuff just to get her parents to believe her." # removed "in"
    lb "Again, they're going to punish me for this."
    lu "…"
    lb "I have nothing, and I have nowhere else to go. I was born alone, and I’ll always be alone."
    lb "I might as well survive alone for the rest of eternity."  
    lb "Maybe it was a bad idea to approach you…"
    lb "See ya…"
    lu "Wait!"
    lb "What?"
    hide lu1
    show lufull1
    lu "How about I tell you a story?"
    lb "A story? Sounds boring."
    lu "What? My stories are not boring!!"
    lu "Come! Come! Sit next to me!"
    lb "*Sigh* Fine."
    lu "I'm sure you'll like this one."
    
    play music "audio/Transparent_Prologue.ogg"
    
    lu "Let's start with here... When I was around your age, I was homeless."
    lu "I had to survive by stealing food and drinking some dirty water that was near me."
    lu "I thought of so many negative things. I had no memories of my parents and my past."
    lu "I even had to deal with a voice in my head saying that someone is going to kill me." # added "ed" to the end of "scream"
    lu "I screamed day and night, annoying the birds around me and even scaring them off."
    lu "I was so scared of myself. I didn't know what was wrong with me."
    lu "No one wanted me, so I had thoughts of dying several times. I tried to cut my wrists with a stick and tried to drown myself as well."
    lu "Nobody would care if I died, but the voices in my head said not to or that someone will kill me." 
    lu "I don’t even know why I couldn't die, but... I still live to see this day…" 
    "She looked down at her bare wrists, which were as clear as the sky."
    "There were no scars around... It was because of her special ability from that ‘place’."
    lu "One day, I snuck inside a cabin. A well-made cabin that seemed to be there for quite a short time." 
    lu "I found myself in an apple garden and ate most of the sweet apples that were freshly grown by a single person."
    lb "Isn’t that the guy who walks around the nest to sell apples everyday?"
    lu "Yes! That person happens to be my foster father!"
    lb "Oh… I heard he had a daughter, but I didn’t know it was you."
    lu "Really? Where did you think I came from?"
    lb "Some royal family or something…"
    lu "Tee-hee! There’s no way I would want to live with them!" 
    lb "You don’t?"
    "Lucia shook her head." 
    lu "You know what happened next? I got caught by him, but I couldn’t run because my body felt so strange at that time."
    lu "I felt something… growing inside of me, but… it was so painful that I fainted."
    lu "After that, I woke up in a soft bed."     
    lu "Then, I saw a beautiful smile shining upon me…"
    lu "The man who called himself Mr. Crimson said if I needed a place to live, then I could live with him!" # replaced "can" with "could"
    lu "He lives alone as he stated that both his wife and daughter were lost forever around 200 years ago."
    lu "He must have been lonely after all these years…"
    lu "Just the way I felt before..."
    lu "After that, we became a happy little family."
    lu "Oh! And I also got really lucky that he was friends with Mr. Emerson too!"  
    lu "That’s how I went through some intense vocal training with him." 
    lu "But… I didn't make it because of my past. I lost all hope until Luna approached me and made me as one with her."
    lu "I guess I must have gotten lucky, right?"
    lu "To meet both my foster father and Luna."
    "The boy nodded his head. His eyes were focused on her the whole time." # replaced "at all times" with "the whole time"
    "It was a good sign for Lucia. He was listening to her the entire time." # removed "for"
    "Even when she was just telling him a below-average story that was titled: ’My past, my life’."
    "Was it really that intriguing to him?"
    "Little boy" "Why are you telling me all this? This has nothing to do with me."
    "Or maybe not…"
    lu "I know, but I really wanted to tell you since you reminded me of myself from before."
    lu "If I had never met my foster father, then I would have ended up just the way you are right now."
    lu "Someone who is lost, apathetic, and even alone."
    lu "You don’t want to be that kind of person, now do you?"
    lb "I hate it when my teachers say that."
    lb "If only they would understand what I always say to them."
    lu "What would you say to them?"
    lb "If you experience a lot of things, then you learn a lot of things."
    lb "You’ll learn more about yourself and others too." # removed "the"
    lu "(That sounds like… something that Luna would say to me.)" # added "like" after "sounds"
    lu "(Perhaps this child is nothing like me after all?)"
    lb "You’ve already experienced being homeless, and it looks like you learned how to survive in the nest without proper shelter, food, and water."
    "Little boy" "That sounds cool."
    lu "How is that cool? It’s not fun being desperate for a normal life every day."
    lb "But you get to learn more about yourself."
    lb "At least you can enjoy the more simple things in life, like watching the sky and watching the knights patrol around the nest."
    lb "Didn’t you ever think about those when you were homeless?"
    lu "I… think so?"
    "Her mind would always scatter when she tried to think about her past."
    "She doesn’t even know why."
    "Perhaps it must have been her imagination or something… or maybe it’s that ‘spirit’ that’s been controlling her after all these years…"
    lb "…"
    lb "Can you teach me how to survive the outside world sometime?"
    "Snapped back to reality, Lucia looked down at the boy and smiled at him."
    lu "You really want to learn how to survive like that?"
    lb "It’s not like that. I want to survive because I want to live for my dad."
    lb "He always says to never let anything stop me."
    lb "I shouldn't let this dumb family stop me from living on for myself more than taking care of their stupid daughter in the future."
    lu "Goddess… if only I could meet your father… if only I knew my real father…"
    lb "Well, don’t let that stop you."
    "The boy stood up from his desk." 
    lb "I should probably go. I don’t want to get in trouble with them. Can I come visit you sometime?"
    "His pale lavender eyes widened in curiosity." 
    "Good, it looks like he’s feeling better already…"
    lu "I’ll be there at the altar soon. You know where to find me."
    lu "May the Cunablian goddesses bless you."
    lb "..." 
    lb "You’re Lucia Lock Crimson, right?"
    lu "Yes, I am."
    "He gave out a small smile."
    lb "I’ll be sure to remember that name."
    "The boy walked out of the classroom, leaving Lucia alone to smile again."
    "She looked around at the empty classroom, remembering the wonderful times she had with the other children before."
    "But this boy… was he here before?"
    lu "I shouldn’t think about this too much! I have to get back to Luna!"
    lu "Let’s take my shoes off and run~"
    hide lufull1
    jump comfort_boy  
    
label comfort_boy:   
    stop music fadeout (0.5)
    scene castle_entrance with Dissolve (1.0)
    play music "audio/Transparent_Casual.ogg"
    show lufull1
    "She stepped back into a very familiar area." # replaced "Stepping" with "She stepped"
    hide lufull1
    show lunfull1
    lun "Oh, you're back!"
    "Luna was sitting on the staircase, sipping tea and nibbling her cookies."
    hide lunfull1
    if take_cookies:
        show lu1 at left
        "That reminds her... she left HER cookies in the classroom..."
        lu "Oops!"
        jump backtonormal
    else:
        "That reminds her... she didn't take the girl's cookies."
        lu "..."
        jump backtonormal
    
    hide lunfull1
    lu "Luna. Why are you sipping tea at a place like this?"
    lun "I was waiting for you to get back here. I wanted to show you something." 
    lu "Luna!"
    lun "Yes?"
    lu "Oh, uhh..."

    menu:
        "About earlier…":
            lu "About earlier… I'm sorry."
            lun "Sorry about what?"
            lun "You have your own opinion, and I have mines."
            lun "Our disagreements would lead to conflict, but we have to learn from each other and work things out together."
            lun "We'll have to start later though. I have something important to tell you."
            lun "Would you mind talking about this later?"
            lu "I don't mind."
            jump continueon

        "Did you know that these are rosemary cookies?":
            lun "Of course I did. The smell was very strong, but it was very delicious!"
            lun "There's still some left! Would you like some?"
            lu "I'll pass."
            jump continueon
   
label continueon:
    
    scene black with Dissolve (1.0)
    #play music "audio/Transparent Lucien's Theme.ogg" ##Not sure yet. You can ignore this part!
    hide lufull1
    "As Luna opened a big door, Lucia was blinded by a bright light, forcing her to unconsciously shut her eyes and place her arm in front of them." # replaced the "s" at the end of "opens" with "ed", "is" with "was", and "around her" with "in front of them"
    lun "Let me take you there, so you can keep your eyes shut."
    "Luna didn’t seem to be bothered by the light. How is she able to handle that awful distraction in minutes?"
    "After Lucia was able to regain her senses, she opened her eyes."
    show lu1 at left
    #lu "A graveyard?"
    
    #THIS PART IS FOR THE DEMO PURPOSE.
    scene center with Dissolve (1.0)
    lu "We're back in this place. It's already completely empty because it's used for scheduled events only."
    lun "…"
    lu "Luna, why are we here?"
    show lun1 at right
    lun "…"
    lun "…"
    lu "Luna, haven't we been here before? How many times?"
    lun "…"
    "This place… both Luna and Lucia had been here a few times before." 
    "It was the place where many former Emerson family members would be lost forever…" 
    "They would kill themselves and dispel here to be with their goddesses." 
    #"Their names were engraved on their tombstones, even their own feathers were piled on heavy rocks." # added "were" between "names" and "engraved", removed the "to" at the end of "onto", and replaced "are" with "were"
    "It's good to remember their colors as most of them were teal with a mixture of black."
    "It's the Emersons' traditional color they had for generations. They even wear the colors on their armor and clothing too." # replaced "from" with "on"
    lu "Hmm… it's still a pretty odd color, right, Luna?"
    lun "..."
    "Strange… whenever Lucia would suddenly shout something out, Luna would smile at her or say something too." 
    lu "Luna?"
    lu "(What’s wrong with her?!)"
    lun "…"
    "Her face remained calm and steady, not making a wink or even making a movement from her body." # replaced the "s" at the end of "remains" with "ed"
    #"She stood firm… moving her eyes from one tombstone to another."
    lun "No one would come here as frequently as I do."
    lu "Don't we usually come here together?"
    lun "Yes, but I would always come here often after work."
    lu "Why?"
    lun "The Emersons' loyalty towards their goddess is very strong." # switched the apostrophe and the s at the end of "Emersons'" around   
    lun "They would do anything to join their goddess in the lost realm." 
    "She looked at Lucia."
    lun "Why do you think they are the creators of the Umbrien weapons?"
    lu "Umbrien? *Gulp*"
    lu "Aren’t those weapons the ones that can kill a bird and a goddess?"
    lun "Yes, they would kill themselves with those weapons."
    lun "To protect their goddess in death, leaving their offspring to stay with their next goddess as well." 
    lu "I’ve heard of it, but there is nothing we can do about it." # replaced "this" with "it"
    lu "Every time I do, I would feel so sad for the children." # separated "everytime" into two words
    lu "To hear about the parents leaving their children…"
    lun "..."
    lun "Your reaction is the same as everyone else's." 
    lun "However, there was nothing anyone could do about this."
    #added details
    lun "Not even the Emerson's deputies either."
    lu "Why does the Emerson family need deputies for themselves?"
    lu "They are here to protect the Aria Goddesses. Can't they just protect themselves?"
    lun "That is correct, but they are here for extra protections to the Emerson family."
    lun "Don't you know about this? Mr. Emerson's grandfather was a victim of a 'forbidden spell.'"
    lu "A forbidden spell?"
    lun "Ah..."
    
    if tome_taken:
        lun "I see you have brought an old history book with you."
        lun "May I see it?"
        "Lucia handed the book to Luna. Then, she took a good look at it."
        "As she flipped each page, Luna's expression never changed. Lucia couldn't tell what she was thinking." # replaced "each page flipped on" with "she flipped each page"
        lun "Ah-ha! There it is!"
        lun "It says here that he was alone in his room, drinking a cup of tea and he then swallowed something."
        lun "He took no concern of it until a great pain surrounded his body, even trying to talk and sing was very painful for him to bear."
        lun "As soon as he went to the healer, it was too late. Something had quickly swelled inside his throat, blocking his ability to breath."
        lun "Investigators found something that was inside of him."
        lun "A flower, and a bunch of vines that surrounded his body."
        lu "Ewww... didn't he felt all of that?"
        lun "Nobody knows. He's known to mask his pains and feelings."
        lun "Rumors say that a mysterious Nosirian female bird served him that tea."
        lun "No one knows about her whereabout ever since."
        lun "The surviving family members say that they should get their own deputy to protect the family until the end."
        lu "Oh, right. I heard the first one was a woman though!"
        lu "The one who uhh..."
        lu "Sorry. I shouldn't talk about this in here."
        lun "It's okay, Lucia."
        lun "May I borrow this for a bit?"
        lu "O-of course!"
        lu "(I don't exactly need it anyway.)"        
    else:
        lun "……………"
        lu "Wha-what?"
        lun "It's nothing. The tome..."
        lu "Tome?"
        lun "If only we had one, then I would have pointed that summary on what happened to him."
        lu "Oh, sorry."
        lu "(Maybe I should have taken it in the first place.)"
        lun "It okay, Lucia. I can tell you about it."
        lun "Each tome says that he was drinking a cup of tea and he swallowed something."
        lun "He took no concern of it until he felt a great amount of pain from his throat, trying to talk and sing was very painful."
        lun "As soon as he went to the healer, it was too late. Something had swelled his throat, blocking his ablity to breath."
        lun "Investigators found something that was inside of him."
        lun "A flower, and a bunch of vines that surrounded his body."
        lu "Ewww... didn't he felt all of that?"
        lun "Nobody knows. He's known to masked his pains and feelings."
        lun "Rumors say that a mysterious Nosirian female bird served him that tea."
        lun "No one knew about her whereabout ever since."
        lu "Oh, right. I heard the first one was a woman though!"
        lu "The one who uhh..."
        lu "Sorry. I shouldn't talk about this in here."
        lun "It's okay, Lucia."
        
    lun "Anyways, all of our tomes say that all Emerson families are known as loyal protectors to all Cunablian people and goddesses."
    lun "So many of them have dispelled themselves to save their home."
    lu "What are you talking about, Luna? We have all this time to protect Cunabula."
    lu "Sure, we only have one life to spare from now on, but at least we lived for a purpose!" # replaced "with" with "for"
    lun "Lucia."
    lu "Yes?"
    #lun "Did you… noticed something about these graves?"

    #menu:
      #  "Does each grave only have the Emerson names?":
      #      lun "You're on the right track, but what else?"
      #      jump no_names
            
      # "The line up is off?":
            #lun "Not exactly..."
            #jump no_names
            
        #"I don't know.":
            #lun "Just say something, Lucia."
            #jump no_names

label no_names:
    #lun "After all these centuries of being an Aria Goddess, my name will never be engraved on one of these tombstones."
    #lun "Even yours as well…"
    #"Then she looked at Lucia. Her body began to shiver as her bright eyes went suddenly dark."
    lun "Tell me. Do you still want to be an Aria Goddess?"

    stop music fadeout 1.0
    lu "What? What are you talking about?"
    lu "Stop saying that nonsense, Luna! Being an Aria Goddess has been my dream for a very long time!"
    lu "What are you getting at?"

    play music "audio/Transparent_Despair_.ogg"
    lun "Even though you will be recognized when you're alive, you won't be recognized when you are lost forever."
    lun "Is that what you want? Even when our lives are shortened by possessing the goddess' soul?"
    lun "Even when it's only half of her soul, our lives are much shorter than they were before."
    lu "Stop! I don’t want to hear it anymore!"
    lu "Luna! What are you doing?! I just want to be an Aria Goddess!"
    lu "I don't care if my life has been shortened! I just want to be with my people for the rest of my days!"
    lu "Is that too much to ask?!"
    show lun1 at right
    lun "..."
    lun "If you wish to cease your position, tell me right here and now."
    lun "Will it be eternal life? Or everlasting death? You know we are no longer phoenixes. We live long, but we don’t live forever."
    lun "We only have one life to spare, never to be reborn as any other birds out there."
    "What is she talking about?"
    "Is she playing games with her?"
    "This isn’t right… this isn’t right at all…"
    hide lu1
    show lu1 at left
    lu "Luna, don’t you remember the first time we met?"
    lu "We became Aria Goddesses of our own free will."
    lu "If we are committed to it, then we should stay like this until the day we die!"
    lu 'Why are you making me drop this position now?'  
    lun "You really don't know anything yet…"
    lu "No! It’s you that doesn’t know anything! You’ve been an Aria Goddess for 500 years!"
    lu "You’re staying in Cunabula for a purpose! Never to leave, always there to protect so many Cunablians' lives!" # switched the apostrophe and the s at the end of "Cunablian's" around
    lun "You’re right. There is a purpose for me to stay in Cunabula for the rest of my time."
    lun "I want you to hear me out…"
    lu "No! You listen to me!"
    lu "You gave me half of your soul just to make me your secondary goddess!"
    lu "I can’t just take it back! I would go back to being a worthless being again!"
    lu "You just wanted it back, did you?!" # replaced "now do" with "did"
    lun "That’s not what I’m saying!"
    lun "Please, you need to listen to me!"
    lu "No! I… just need some time to think! I’m sorry!"
    "Confused, she ran out of the door, going back to the entrance."
    scene castle_entrance with Dissolve (1.0)
    "All she could hear was the sudden evil laughter echoing in her head."
    scene black 
    "See, Lucia? I told you so! You can’t escape from reality! You’ll never be like her, no matter what she does for you!" #000000 # replaced "did to" with "does for" (at least, I THINK that's correct)
    lu "Shut up! I don’t want to hear it!"
    lu "You’re… you’re just here to possess me again!"
    lun "No, it can’t be! Lucia! Can you hear me?!"
    "Don’t you remember, my dear?" #000000
    "I… am... you!" #000000
    scene castle_entrance
    lu "Noooooo! Leave me alone!"
    "Screaming out of nowhere, she caught the attention of all the servants at the entrance."
    "Some showed worried expressions, while others shook their heads and walked away."
    "Lucia was already used to this."
    "Actually… she should…"
    "The feeling of her people judging her as a complete freak."
    "Yes…"
    "It was something she should handle by herself."
    "It was her own condition, her problem, her life…"
    unknown "Miss, are you all right?"
    lu "...!"
    "Suddenly, a gentle voice reached towards her."
    "Looking up, she saw a man offering his hand at her."
    "His gentle eyes looking straight at her made her chest tinged."
    "Those eyes... how long has someone looked at her that way?"
    "With such concern to a complete stranger?"
    'Servant' "Sir, I wouldn’t suggest you talk to this woman."
    unknown "Why shouldn’t I? She needs some help, right?"
    'Servant' "She can handle herself. Move along, sir."
    unknown "Now, now... Is there a reason why would I want to ignore such a pretty bird like her?"
    lun "It's because she is Cunabula’s secondary goddess, outsider."
    show lunfull1 with Dissolve (1.0)
    lun "You mustn’t think of her as a regular bird."
    lun "She is associated with the Emerson family, and she will be working alongside me for a very long time."
    unknown "You’re… a goddess? You’re not wearing their crest."
    lun "Only a full-fledged goddess can wear the symbol."
    hide lunfull1
    show lufull1 at right
    lu "Of course… only a goddess can wear it."
    show lunfull1 at left
    lun "Lucia, please! Just listen to-"
    lu "No! You’ve been saying these same words for the last two centuries!"
    lu "Who would want to listen to your perfect little self!"
    lu "You're so selfish all the time!"
    lu "All you care about is yourself!"
    lun "...!"
    scene black
    hide lufull1
    hide lunfull1
    lu "(Stupid Luna! She always says that everything is going to be fine in her way, but it’s not!)"
    lu "(I waited for so long to become an Aria Goddess, and now she wants me to drop it?! What kind of a friend is she?!)"
    lu "(She might as well disappear forever!)"
    "........................."
    
    scene black with Dissolve (1.0)
    stop music fadeout 0.5
    
    scene castle_entrance with Dissolve (1.0)
    show lun1
    lun "Oh no…"
    lun "Things have turned for the worst."
    ty "Goddess Luna, would you like for me to get a knight to escort her back?"
    unknown "No… let her go."
    lun "Mr. Emerson!"
    ty "Father!"
    ty "What about the performance?"
    des "I’m afraid it has already been cancelled."
    des "..."
    lun "Mr-"
    des "Luna, come to my study room. I wish to discuss this with you, but first, I shall take my son back to his room." 
    des "We will discuss your punishment for going out without my permission."
    ty "..."
    ty "Yes, sir." 
    lun "…"
    lun "Yes, Mr. Emerson."
    "And so, everyone went back to work. As if nothing happened…"
    scene black with Dissolve (1.0)
    "......................."

    scene CH1_P2 with Dissolve (1.0)
    pause 
    
    scene pathwaynight with Dissolve (1.0)
    
    "Knight" "You there! Are you or are you not that woman that betrayed the Emerson family?"
    show temp1
    unknown "Another one? Jeez! When are you guys going to get over that?!"
    "A woman holding a heavy bag of wooden logs was stopped by a couple of knights…" 
    "AGAIN for the third time this week."
    "Just running into them is a complete waste of her time after being exhausted from work every day…"
    'Knight' "Answer my question! Are you or are you not that woman who-"
    'Knight #2' "Wait a minute! I heard she birthed two children, and one disappeared."
    'Knight #2' "Meanwhile, the other followed her mother’s path…"  
    'Knight #2' "A survivor… a new complete failure in life."
    'Knight #2' "How did they escape the death penalty for their atrocious crimes?"
    'Knight #2' "It’s quite a mystery…"
    unknown "Believe what you like! Now quit wasting my time, and mind your own damn business!" 
    unknown "I’m outta here!"
    unknown "(Ugh! Again with this crap! For goddess sake, this bag is really heavy!" 
    "It’s going to hurt my good wing, for goddess sake! Better get home soon.)"
    hide temp1
    show tempfull1
    t "My name is Tempest Skye."
    t "As you can see, I’m just a regular commoner heading home with a heavy bag that contains a lot of firewood for cooking and warmth."  
    t "Why is this woman in a red dress holding a heavy bag by herself?"
    t "That's what everyone would say behind my back…"
    t "At least someone would just help me instead of just staring at me..."
    t "Staring at this crooked wing of mine..."
    "……………"
    stop music fadeout 0.5
    
    show camp with Dissolve (1.0)
    
    play music "audio/Transparent_Tempest_Cabin_3_.ogg"
    
    hide tempfull1
    "As Tempest walked towards the familiar, hidden place where no Cunablian birds would ever bother her."
    "It would lead to a old, broken cabin that lays in this nest for many centuries."
    "Never to be moved or cleaned from the lack of funds to maintain it."
    show temp1
    t "*Sigh* if only that incident from a century ago never happened."
    t "Oh well! What's done is done. What's lost is lost!"
    t "Let's see what else the future got for me!"
    "Throwing down her heavy bag near her fire pit."
    t "...?"
    "Strange, the fire pit is already lit."
    "It can’t be…"
    t "(Those brown eyes, that pink dress, and that giant flower on her ponytail.)"
    t "Lucia?"
    hide temp1
    show lufull1 at right
    lu "Welcome back!"
    show tempfull1 at left
    t "You’re early!"
    "Usually, she doesn't come here at this time..."
    hide tempfull1
    show temp1 at right
    "Strange..."
    "Every day and night, this woman would come over to make delicious home-cooked meals for Tempest and herself."
    "Always bringing fresh ingredients from the Emersons' chefs and farmers." 
    "She would say that she’s not used to eating ‘royal’ food."
    "She prefers to eat home-cooked meals because everything is made of ‘love’."
    "Blech… love…"
    "Tempest would like to spit that out of her mouth if she ever says that…"
    t "So, what’s cooking?"
    show lu1 at left
    lu "Your favorite! Butternut squash stew!"
    "Tempest looked over a giant basket that was right behind her."
    t "How much did you bring?"
    lu "Don’t look!"
    t "How much did you bring again?"
    lu "Just enough for tonight’s dinner?"
    t "Liar!"
    lu "Okay! Okay! I brought plenty of food for you to eat for a little while!"
    lu "These are very easy to cook with just one arm! Look here! I cut plenty of butternut squashes for our next daily meals!"
    t "Really? Jeez!"
    t "How many times do I have to tell you? I can take care of myself!"
    lu "But who else is going to help you with that broken wing of yours?"
    "Oh, goddess. Here we go again…"
    hide lu1
    hide temp1

    menu:
        "I hate it when you always say that!":
            show temp1 at right
            t "I hate it when you always say that!"
            show lu1 at left
            lu "I’m sorry."
            lu "I just can’t stand seeing you like this!"
            t "I know... I know…"
            t "I just can’t stand the fact that you always make a fuss about it!"
            t "Stupid Lucia… if only you could understand…"
            jump thank_you
        
        "I don’t wanna talk about this...":
            show temp1 at right
            t "I don't wanna talk about this..."
            show lu1 at left
            lu "…"
            lu "Sorry, I worry about you a lot."
            t "Look, worry about yourself."
            t "You've got something to do later, so make sure you take care of that first!"
            jump thank_you
        
        "Let me repeat myself! I can take care of myself!":
            show temp1 at right
            t "Let me repeat myself! I can take care of myself!"
            show lu1 at left
            lu "You can’t fly anymore! You can’t even wield an axe anymore!"
            t "Don’t remind me… Miss Faker…"
            lu "…!"
            t "Yeah, I heard the rumors." 
            t "People say you took half of Luna’s soul just so you can have the power to rule Cunabula!"
            t "You wouldn’t have the same benefits as she’s having right now!"
            jump nomorearguing

label nomorearguing:
    
    t "Goddamn it, Lucia. You’re making me do this again…" # combined "God damn" into one word
    lu "..."
    lu "What are we doing? We’re fighting already?"

    menu:
        "You started it":
            lu "Yes… I did."
            lu "Let’s set the meals up, okay?" 
            jump thank_you

        "Sorry":
            lu "It’s okay, Tempest. I started the fight in the first place."
            lu "Let’s set the meals up, okay?"
            jump thank_you 

label thank_you:
    t "Oh, Lucia…"
    lu "Hm?"
    t "Uh…"
    t "..."
    t "Thanks for coming over today."
    lu "…"
    "Lucia’s face turned red." 
    "The look on her face looks like those red bell peppers that’s on top of the basket."
    "It’s kind of cute… just seeing her like this makes her want to hurl, though."
    lu "C-come on! The soup isn’t going to fill itself up!"
    t "Yeah, yeah…"
scene black with Dissolve (1.0)
"................."
scene camp with Dissolve (1.0)
"As dinner got started, Tempest’s stomach grumbled loudly as soon as Lucia handed the bowl to her."
#CG starts
show temp1 at right
show lu1 at left
t "Ah!"
t "Stew time!"
t "*Gulp, Gulp, Gulp*"
lu "Tempest! You’re a lady! You should use a spoon!"
t "What? I’m hungry!"
t "Plus, you made my favorite! Butternut squash stew! I love butternut squash!"
t "It tastes so sweet! It's almost like I’m eating my favorite desserts again!"
lu "You should at least watch your health."
t "…"
lu "Teeheehee!"
t "Hahahaha!"
"It was a typical day between the two of them."
"They would sit in the same spot, watch the fire to keep the stew warm, and talk about many different topics that would come from their heads."
"How did it come to this? Tempest doesn’t know…"
"Lucia came over to her cabin to introduce herself, and then, this happened." # replaced "in" with "to"
"Just meeting Lucia made her life a little better…"
"Tempest never would have guessed… if it weren’t for her, then she wouldn’t be able to get a job and eat delicious meals every day." # separated "everyday" into two words
"Who would have thought it would come to this…"
t "Hey."
lu "Yes?"
t "How long have we been together?"
lu "Hmmm... I don't know. How long do you think it was?"
hide lu1
hide temp1
    
menu:
    "A lonnnnnggg time?":
        show temp1 at right
        t "A lonnnnggg time?"
        show lu1 at left
        lu "Tee-hee! It's actually not very long!"
        jump  Aria_Goddesses1
    "A century?":
        show lu1 at left
        lu "Yep!"
        lu "Goddess, has it been that long already?"
        show temp1 at right
        t "More like time just flies away so fast!" # replaced "it" with "time" (and removed some spaces that were there before "More")
        lu "Ah, yes. It's been a great century... yes."
        jump  Aria_Goddesses1
    "Fifty years?":
        show lu1 at left
        lu "Close! You're halfway there!"
        jump  Aria_Goddesses1

label Aria_Goddesses1:
    hide lu1 
    show temp1 at right
    t "Has it been that long already?"
    t "I guess I still remember the day we first met." # replaced "time" with "day"
    t "It was right after the Emerson family broke my wing."
    t "You were waiting right here, lighting the fire pit and making my favorite stew."
    t "I was at a loss for words when a complete stranger knew where I lived, but you were really stubborn. You wouldn't let me go out for a week!"
    lu "Of course! If you ever messed with the Emerson family, then your situation would be much worse than just a broken wing!"
    t "Yep. It would have sucked if I ever lost my second one."
    t "You know, if it weren't for you, then I would have never set my next goals in life."
    t "You fed me, assisted my needs, and even paid for my meals!"
    t "I might not be able to repay you."
    t "You know why? I'm going to leave Cunabula and start a new life!"
    t "So… this might be our last meal together."
    t "Considering that today was your last day of training."
    t "..."
    t "Wait a minute… what the hell are you doing back here?"
    show lu1 at left
    lu "..."
    t "Lucia?"
    lu "..."
    t "Hey!"
    lu "Oh, sorry! Did you say something?"
    t "You weren’t eating this whole time? It doesn’t taste good when it gets cold."
    lu "O-oh! Yes, sorry…"
    lu "…"
    t "..."
    t "(Something is wrong, and I should get to the bottom of this!)"
    t "(But… what can I say to her?)"
    hide lu1
    hide temp1
    
    menu:
        "Something is up, and you better tell me or else!":
            show lu1 at left
            lu "As aggressive as usual, Tempest."
            lu "I don’t know if you’ll be able to understand what I’m going through right now."
            jump talk_time 
                            
        "Come on, Lucia. Talk to me, what’s wrong?":
            show lu1 at left
            lu "…"
            lu "Thank you for your kindness, Tempest."
            lu "After years of being together… I see that you have become even more worried about me."
            lu "I suppose I’ll talk."
            jump talk_time

label talk_time:                               
    lu "Today… was to be my last day as an Aria Goddess."
    show temp1 at right
    t "Of course it was, then why are you back here?!"
    lu "Uhh…"
    lu "You know Luna?"
    t "…"
    hide lu1
    hide temp1

    menu:
        "No":
            show lu1 at left
            lu "Oh, you don’t remember her? I thought you met her a couple times already?"
            lu "She’s the one that gave me half of her soul in order to keep our nest balanced."
            jump talk_time2 

        "Yes":
            show lu1 at left
            lu "Okay, just wanted to make sure."
            jump talk_time2 

label talk_time2:

    lu "She… said something that doesn’t seem… right to me."
    lu "She said that I shouldn’t have become an Aria Goddess in the first place."
    lu "Isn’t that weird? At the very last minute? Just what in the world was she thinking?"
    show temp1 at right
    t "She thinks you’re not fit to be one?"
    lu "Maybe… I… don’t know. She kept blabbering about a lot of stuff that I couldn’t understand."
    lu "If only my father and I had some money before, then maybe I would have had some idea what she wanted to say to me."
    lu "Maybe if I knew about Cunabula’s history and such…"
    "Her bowl slipped out of her hands, spilling the cold stew onto the grassy ground."
    "Tempest paid no mind to it. She wanted to focus on Lucia, who was already sobbing hysterically with her hands slammed onto her face."
    "She sobbed hysterically, with her hands slammed into her eyes."
    lu "Goddess, she’s right! I’m not fit to become one!"
    lu "I have no beauty, no knowledge of my history, and this spirit that possessed me still lingers inside me!"
    lu "If only I’d never taken that soul, then my people would have been happy without me around!"
    lu "They would have never criticized me a lot or even thought that a crazy bird would rule this nest someday!"
    lu "Even half of that soul is not enough! But what would the entire soul do to me?!"
    lu "I thought I was already protecting Cunabula by connecting with my people’s hearts by singing!"
    lu "But Mr. Emerson would say I need that certain ‘item’ to ‘really’ protect this nest."
    lu "Face it, Tempest, I’m nothing…"
    t "Are we going to deal with that crap again?"
    lu "Huh?"
    t "What are you? Some kind of a joke?"
    t "I thought you were way better than that!"
    t "Instead, you’re just whining about that spirit trying to control you over and over and over again?!"
    t "This is getting ridiculous, Lucia! How are you going to help yourself if you’re just going to end up like this?"
    t "You’re so selfish!"
    lu "...!"
    "Lucia’s eyes widened, and the tears streaming down went faster than before."
    lu "Sniff… sniff… This spirit…"
    lu "It scares me to death…"
    lu "Every day, whenever I wake up, I always hope that it’ll never come."
    lu "I tried to control it by pretending that it wasn’t there."
    lu "But I don’t know why it keeps coming back to me… this goddess soul is perhaps not working." 
    t  "Goddess… at least even with my temper too!"
    t "*Sigh*"
    t  "Look, I wouldn’t blame you for what you’re feeling right now."
    t  "I know you’re scared, but I don’t know much about your situation. You have to deal with it yourself."
    lu "I know, but… it would just come back to me over and over again."
    lu "Just whenever I get scared or stressed. That’s not what an Aria Goddess should do…"
    t "All right, educate me."
    lu "What?"
    t "You heard me! Tell me more about Aria Goddesses, now that you’re blabbering about things that I don’t even understand!"
    lu "Oh, sorry... I don’t exactly know everything, but I can try…"
    t "Then tell me more about…"
    hide temp1
    hide lu1
    jump Aria_Goddesses2

label Aria_Goddesses2:
    menu:
        "What do you do as an Aria Goddess in training?":
            show lu1 at left
            show temp1 at right
            lu "Well, most of the time, I would walk with Luna and observe what she would do to help her people."
            lu "She prays, heals their wounds if needed, and even sings on top of that stage too." # replaced "most of all, I would see her sing" with "even sings" (I don't know. I just feel like the entire sentence flows better that way.)
            lu "Oh, and what’s more fun is that she would use her magic to make everyone happy!"
            t "Magic, huh? Magic doesn’t come from our wings."
            lu "I know that! That’s why we do an exchange!"
            t "An exchange?"
            t "Tell me more about that."
            lu "You don’t remember seeing that from the history books? Everyone knows about that!"
            lu "All birds who wish to become a goddess will have to sacrifice their wings and their current soul to earn their divine magic!"
            t "Oh, right."
            "Of course she hasn’t… she wanted to see if Lucia can handle this stuff that was coming to her in the future."
            "She unconsciously touched her left shoulder that was covered by her cloak."
            "It was crooked and unnatural."
            "Would Lucia survive like this in the future?"
            "Unable to fly, unable to protect herself?"
            lu "Tempest, are you okay? Does your wing hurt?"
            t "Huh?"
            "Lost in thought, Lucia happened to be sitting much more closer to her."
            "Enough for their eyes to be close…"
            t "It’s fine!"
            "Tempest abruptly pushed her away and turned her head to the other side."
            "Were her eyes really that pretty? Tempest’s heart began to beat fast."
            t "Sorry about that. Can we move on?"
            lu "…"
            lu "Okay."
            hide temp1
            hide lu1
            jump Aria_Goddesses2
        
        "The item":
            show lu1 at left
            show temp1 at right
            lu "This item… it was already stolen a century ago."
            t "Oh, that."
            t "Yeah, I don't want to talk about that." # removed "one"
            lu "I knew you wouldn't want to talk about THAT again." 
            t "Wouldn't Luna know about that item?"
            lu "She would, but I doubt she would tell me more about it."
            t "Why not? Aren't you her secondary goddess?"
            lu "She still hides things from me, Tempest. She's selfish herself, and that's what she is."
            t "Wow, harsh. Did you two get yourselves in a bad fight?"
            lu "Forget what I said."
            t "What, seriously?"
            hide temp1
            hide lu1
            jump Aria_Goddesses2

        "What do Aria Goddesses do?":
            show lu1 at left
            show temp1 at right
            lu "Most of the time, we would pray and sing for our people."
            lu "We’re just here to keep Cunabula alive."
            t "Well, that sounds boring! What’s so good about that?"
            lu "It’s for Cunabula’s survival, Tempest!"
            lu "I was offered this position to become a better person! I took it on my own will!"
            lu "I want to keep Cunabula safe!"
            t "Even when you have to sacrifice so much for the others? They wouldn't appreciate your endurance in becoming one."
            lu "It doesn't matter to me, Tempest. I chose to do this, so don't back me down now!"
            t "Don’t regret your choice then!"
            lu "I will never regret my choice."
            hide temp1
            hide lu1
            jump Aria_Goddesses2

        "That’s enough":
            show lu1 at left
            show temp1 at right
            t "I guess that’s about it, then."
            t "You already dropped your bowl on the ground."
            lu "Oh, yes."
            "Lucia's stomach grumbled, making her face turn red."
            t "Hahaha!"
            lu "What are you laughing at?"
            t "Here! Why not take my bowl instead?"
            lu "Uhhh… Isn't that yours?"
            t "Oh come on! I didn't use a spoon for that one!"
            t "Here! I'll clean it!"
            lu "Tempest! Don't use your dress!"
            lu "I brought some napkins to wipe it down!"
            t "(Good, she's feeling better now.)"
            t "(But for Luna to tell her that she's not quite right for the job at this time and day?)" # removed the period and decapitalized "at"
            t "(How strange...)"
            lu "Oh, right! We have to save some stew for him!"
            t "For who?"
            jump Tempest_father
        
label Tempest_father:

    stop music fadeout 0.5

    unknown "You sure don’t know how to make things easier for me, huh, Tempest?" # replaced the period with a comma and decapitalized "huh"
    t "…"
    t "Shit."
    "Just the voice she didn’t want to hear…"
    
    play music "audio/Transparent_Suspicions.ogg"
    
    ms "Empty again?"
    "Tempest glared at the man holding a cheap alcohol bottle, with his back leaned on the door and his arms crossed."
    "How long was he standing here?!"
    hide lu1
    show lufull1 at left
    lu "Mr. Skye! Where were you?! Your portion is about to get cold!"
    hide temp1
    show tempfull1 at right
    t "Hey, shut it!"
    hide tempfull1
    hide lufull1
    ms "Happy as usual, huh?"
    ms "So, you’re skipping your last day?"
    show lu1 at left
    show temp1 at right
    lu "I did, but I'll make up for it very soon! As soon as I leave, sir!"
    lu "I'm also sorry that we didn’t get to talk for around a century."
    lu "It looks like you’re… doing very well!"
    t "Lucia! Shut it!"
    hide lu1
    ms "Well? Then, I might as well tell you this."
    ms "You sound pretty hesitant for someone who whores around with that big smile of yours."
    lu "What?"
    ms "I thought you always wanted to be an Aria Goddess?"
    ms "Then why are you confessing that the bitch is driving you away already?" # replaced "if" with "that"
    lu "What?! Are you referring to Luna?!"
    hide temp1 
    show tempfull1 at right
    "Tempest stood from her seat. This might get crazy later…"
    hide tempfull1
    hide lu1
    ms "Maybe she does want her powers back?"
    ms "Come to think about it, why is she trying to take your position away?"
    ms "Was it that they might have thought they made a mistake in choosing you to become their new waste of life for the nest?"
    t "That’s enough!"
    ms "Oh, yeah? Well, what are you going to do with that one little wing of yours?" # replaced "about" with "with"
    ms "You're nothing without your second one!"
    show temp1 at right
    t "...!"
    "His words were harsh, but his morals were absolute. Tempest couldn't open her mouth again to keep arguing with him."
    "Her mouth remained shut, ignoring Lucia, who was staring at her with worried eyes."
    show lu1 at left
    lu "..."
    "She eventually looked at Mr. Skye, who was still standing there, smirking to himself for shutting Tempest up." 
    "He must have been so proud of himself. It made Tempest want to punch him in the face."
    lu "Mr. Skye… you changed… was it really because of what happened a century ago?"
    t "…!"
    "Tempest’s body began to shiver."
    "And then… she grasped both of her fists…"
    t "(This feeling…)"
    t "(Shit!)"
    lu "I’m sorry you didn’t get to see her again, but I promise you! I will free you and your daughter!"
    lu "Just you wait! Until I become an Aria Goddess!"
    lu "The Emerson family will assist me, and soon everything will go back to normal!"
    lu "Of course, I'll tell them to help you with anything! They'll do anything for every being in Cunabula! That's for sure!"
    t "So is this your purpose for coming here?"
    t "To piss me off?!"
    scene black
    "Unconsciously, Tempest lifted her hand and formed it into a fist."
    lu "..!"
    "She hit something…"
    "It was something soft and plump."
    "She doesn’t know what it was… but she didn’t care."
    "Her anger was taking over her already."
    
    play music "audio/Transparent_Despair_.ogg"
    
    t "Haven’t we suffered enough?!"
    t "Do you not listen to the rumors?!"
    t "My mother, the former deputy of the Emerson family, betrayed them!"
    t "You think they're going to forgive her so easily?!"
    "She finally opened her eyes, and then her eyes widened."
    ms "Jeez… since when did you have that much strength?" # replaced "get" with "have"
    "Her fist was on her father’s stomach. Her face began to sweat."
    "Perhaps he was enduring the extreme pain that must have been lingering through him." # replaced "around" with "through"
    "He was standing behind Lucia… protecting her from the great strength of a former warrior who once wielded a giant axe…" # replaced "that" with "who"
    scene camp with Dissolve (1.0)
    show lu1
    lu "..."
    "Lucia was in complete shock. It was written all over her face."
    "She slowly backed away…"
    lu "I should go home and get a good night's sleep." 
    lu "Make sure you let your father have some stew too!"
    hide lu1
    show temp1
    t  "Lucia, wait!"
    t  "Goddamn it!"
    ms "*Cough! Cough!*"
    t "You…"

    menu: 
        "You dumbass!":
            show tempfull1
            t "You dumbass! Why?!" # removed the "ly" at the end of "completely"
            ms "Watch your language, young lady."
            ms "Goddess… how long has it been since I felt this much pain?"
            jump anothererrorfixtwo 

        "Why?":
            show tempfull1
            t "Why?"
            ms "Don’t ask me, kid. At least you maintained your strength well."
            jump anothererrorfixtwo 
       
label anothererrorfixtwo:
    hide tempfull1
    show temp1
    "Her father slowly stood up, grunting and pressing his stomach. He must be in a lot of pain…"
    t "We should get you to a healer soon! Damn it, if only Lucia was still here!"
    ms "It’s fine! Save the money for yourself."
    t "But-"
    ms "Just do as I say!"
    "As soon as the old door closed, Tempest let out a huge roar." # replaced "gave" with "let"
    t "Great. Now everything is fucked up!"
    t "Again…"
    "Tired from all the drama that was going on, Tempest slammed her back on the cold grass," 
    "Not caring about how the bugs were about to crawl around her."
    t "…"
    "She closed her eyes, letting the darkness take over her." 
    unknown "Tempest!"
    t "Mother?"
    unknown "What are you doing here?" 
    t "I don’t know. Just chilling, I guess."
    unknown "Just chilling? Why are you not training?"
    t "I can’t train anymore, Mom! Did you not remember what happened to my wing?!"
    t "It was because I had your back, and what do I get in return?!"
    unknown "I don't know… I don't know… I promise I'll make it up to you! I promise!"
    t "Those were the last words her mother said to her."
    "What could that mean? Tempest thought to herself for a long, long time."
    "Until she eventually stopped thinking."
    t "I might as well take a itty bitty nap……."

    
    stop music fadeout 0.1
    
    "AHHHHHHHHHHHHHHHHHHHHH!!!!!"
    
    play music "audio/Transparent_Suspicions.ogg"
    
    hide temp1
    show tempfull1
    t "What in the-?!"
    t "It came from around here!"  
    hide tempfull1
    scene black 
    t "Oh no… it can't be!"  
    t "(Wait a minute! Should I really be doing this?!)"
    t "(Oh, what are you doing, Tempest?! Someone is in need of help, so you should just go help that bird already!)"
    t "(Sheesh!)"

    
    scene pathwaynight with Dissolve (1.0)
    
    show tempfull1
    t "Goddess, it’s been too long since I’ve done this. Me, holding a weapon while being on-patrol like this."
    t "…"
    t "I shouldn’t think about that now. I should focus on this!"
    t "All right… you got this…"
    hide tempfull1
    show temp1
    t "Wait a minute… am I smelling…"
    t "Blood?"
    t "Goddess! What in the world?!"
    "A gruesome display laid right in front of her eyes."
    "Blood was scattered around the place. It painted the dirty ground with redness, as if flowers were scattered on the ground." 
    "A woman who was face down wore a beautiful dress, containing many pieces of jewelry around her…"
    "Wait... that dress…"
    "No way!"
    t "Goddess, no! No, no, no! It can’t be!"
    t "It can’t be her!"
    unknown "You, I shall take you in under suspicions of murder."
    t "What the-?!"
    t "Hey, why the heck are you grabbing my arms?!"
    t "I didn’t do it! I swear!" 
    unknown "Oh yeah? Well, you were standing right near it with that bloody axe of yours!"
    t "Hey! My axe is clean! Bar none!"
    t "(Shit! Just what the hell is going on here?!)"
    t "(I didn’t kill her! I swear to all goddesses!)"
    scene black with Dissolve (1.0)
    "Most of all… that hand bracelet…"
    "It can’t be…"
    pause
    scene black
    "Thank you for playing the demo!"
    "Please sign the google form for feedbacks and suggestions to help improve the next demo."
    #jump chpt_2
