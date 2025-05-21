mood={"happy":("\U0001F60A","Sound's great!"),"sad":("\U0001F622","It's okay"),"angry":("\U0001F620","You are turning red"),"excited":("\U0001F929","Great"),"tired":("\U0001F634","Relax for a while")}
usermood=input("How are you feeling today?").strip().lower()
if usermood in mood:
    emoji=mood[usermood][0]
    message=mood[usermood][1]
else:
    emoji="\U0001F914"
    message="Oops,I can't figure out your mood,but I hope you have a great day!"
print(f"Emoji: {emoji}")
print(f"Message: {message}")