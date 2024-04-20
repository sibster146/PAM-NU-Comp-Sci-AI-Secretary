import ClassCode as code

def speak(paragraph):
    avatar = "greeter"
    code.purge(avatar)
    code.resetTriggers()

    trigger = code.paragraphSpeak(paragraph, avatar, "Free Trigger")

    print("The speaker has begun.")

    code.waitUntilOver(trigger)

    print("The speaker has ended.")

#speak()