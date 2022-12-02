import turtle
import functools

Characters = { #Vie ; Atk ; Def ; Speed

    "Test" : (200, "TestAtk", 2, 30, "None"), 
    "Test-2" : (200, "TestAtk", 2, 30, "None") 
} 


Atks = {

    "TestAtk" : (40, "Gauche", "ExtremeDroite")
}

Types = {
    "Gauche" : "ExtremeDroite",
    "Droite" : "ExtremeGauche",
    "ExtremeDroite" : "None",
    "ExtremeGauche" : "None",
    "None" : "None"
}

Coords = {

    "Player" : (-100, -100),
    "Enemies" : (100, 100),
}


gameState = -1
PlayerCharacter = "Test"
EnemiCharacters = "Test-2"

myScreen = turtle.Screen

# ========================== Setup du turtle ==================================


superEcran = turtle.Screen() # ont recupere la fenetre et ont la stocke pour plus tard =D
superTortue = turtle.Turtle()


def SetupTurtle() :

    """
    Setup la tortue ainsi que l'écran | peu etre metre un input pour demander la taille de la fenetre et ça couleur 
    """

    superEcran.title("Chargement...")


    superEcran.setup(width=600, height=600) # IMPORTANT RESO CARRE car sinon les coord ne marcheront po 
    superEcran.bgcolor("pink")

    superTortue.hideturtle()
    superTortue.pencolor("white")
    superTortue.fillcolor("red")
    superTortue.color("white")
    superTortue.penup()

    # Setup La position des Enemies et du player 
    #// Pas fini

    superTortue.goto(Coords["Player"])
    superTortue.write("Player", font=("Arial", 36, "bold"), align="center")

    superTortue.goto(Coords["Enemies"])
    superTortue.write("Enemies", font=("Arial", 36, "bold"), align="center")

    


    superEcran.title("Jeu en cour")


    global gameState
    gameState = 0


SetupTurtle()

turtle.done()