# ******************************************** Manipulación de archivos ***********************************************************************
# leer archivo
"""
with open("testt.txt", "r") as archivo:
    contenido = archivo.read()
    print(contenido) """

# escribir en archivo
contentt = """
Hey you, out there in the cold
Getting lonely, getting old
Can you feel me?
Hey you, standing in the aisles
With itchy feet and fading smiles
Can you feel me?
Hey you, don't help them to bury the light
Don't give in without a fight

Hey you out there on your own
Sitting naked by the phone
Would you touch me?
Hey you with you ear against the wall
Waiting for someone to call out
Would you touch me?
Hey you, would you help me to carry the stone?
Open your heart, I'm coming home

But it was only fantasy
The wall was too high
As you can see
No matter how he tried
He could not break free
And the worms ate into his brain

Hey you, out there on the road
Always doing what you're told
Can you help me?
Hey you, out there beyond the wall
Breaking bottles in the hall
Can you help me?
Hey you, don't tell me there's no hope at all
Together we stand, divided we fall
"""

filld =  open("testt.txt","w")
filld.write(contentt)

