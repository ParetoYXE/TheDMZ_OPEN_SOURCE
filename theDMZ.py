import pygame,random
pygame.init()


gameDisplay = pygame.display.set_mode((900,900))
pygame.display.set_caption('The DMZ')
pygame.font.init() # you have to call this at the start, 
                   # if you want to use this module.
myfont = pygame.font.SysFont('VCR_OSD_MONO', 20)
clock = pygame.time.Clock()

quit = False




#DECLARE GLOBAL ARRAYS HERE

entities = []
env = []









#DECLARE GLOBAL STAT DISPLAY VARIABLES HERE

selectedStr = 0
selectedDex = 0
selectedCon = 0
selectedInt = 0 
selectedCha = 0 
selectedCyber = 0
selectedHp = 0
selectedTo = 0
selectedLe = 0
selectedInf = 0



#LOAD IMAGES HERE

npcImage = pygame.image.load("npc.png")
brushImage = pygame.image.load("brush.png")
houseImage = pygame.image.load("house.png")







class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location




class ENV():
	def __init__(self):
		self.name = ''
		self.x = 0
		self.y = 0
		self.value = 0
		self.state = ''
		self.ownership = ''
		self.image = ''



class NPC():
	def __init__(self):
		self.name = ''
		self.age = ''
		self.str = 0
		self.dex = 0
		self.con = 0
		self.int = 0
		self.char = 0 
		self.cyber = 0
		self.hp = 0
		self.to = 0
		self.le = 0
		self.inf = 0
		self.x = 0
		self.y = 0
		self.image ="npc"
		self.width = 10
		self.height = 10

player = NPC()

player.str = random.randint(3,18)
player.dex = random.randint(3,18)
player.con = random.randint(3,18)
player.int = random.randint(3,18)
player.char = random.randint(3,18)
player.cyber = random.randint(3,18)
player.hp = random.randint(3,18)
player.to = random.randint(3,18)
player.le = random.randint(3,18)
player.inf = random.randint(3,18)



def generateENV():

	genENV = ENV()

	if(random.randint(1,10) < 3):
		genENV.image ="house"
	else:
		genENV.image ="brush"
	genENV.x = random.randint(100,800)
	genENV.y = random.randint(100,800)

	return genENV

def generateNPC():
	genNPC = NPC()

	genNPC.str = random.randint(3,18)
	genNPC.dex = random.randint(3,18)
	genNPC.con = random.randint(3,18)
	genNPC.int = random.randint(3,18)
	genNPC.char = random.randint(3,18)
	genNPC.cyber = random.randint(3,18)
	genNPC.hp = genNPC.str + genNPC.con
	genNPC.to = (genNPC.str + genNPC.con) / 2
	genNPC.le = (genNPC.char + genNPC.int) / 2
	genNPC.inf = (genNPC.cyber + genNPC.char) / 2
	genNPC.x = random.randint(100,800)
	genNPC.y = random.randint(100,800)

	return genNPC


def drawStats():
	strText = myfont.render('STR: ' + str(selectedStr), False, (0, 0, 0))
	dexText = myfont.render('DEX: ' + str(selectedDex), False, (0, 0, 0))
	conText = myfont.render('CON: ' + str(selectedCon), False, (0, 0, 0))
	intText = myfont.render('INT: ' + str(selectedInt), False, (0, 0, 0))
	charText = myfont.render('CHAR: ' + str(selectedCha),False, (0, 0, 0))
	cyberText = myfont.render('CYBER: ' + str(selectedCyber),False, (0, 0, 0))
	hpText = myfont.render('HP: ' + str(selectedHp),False, (0, 0, 0))
	toText = myfont.render('TOUGH: ' + str(selectedTo),False, (0, 0, 0))
	leText = myfont.render('LEAD: ' + str(selectedLe),False, (0, 0, 0))
	infText = myfont.render('INFL: ' + str(selectedInf),False, (0, 0, 0))

	gameDisplay.blit(strText,(0,800))
	gameDisplay.blit(dexText,(0,820))
	gameDisplay.blit(conText,(0,840))
	gameDisplay.blit(intText,(0,860))
	gameDisplay.blit(charText,(0,880))
	gameDisplay.blit(cyberText,(60,800))
	gameDisplay.blit(hpText,(60,820))
	gameDisplay.blit(toText,(60,840))
	gameDisplay.blit(leText,(60,860))
	gameDisplay.blit(infText,(60,880))


def updateStats(NPC):
	global selectedStr,selectedDex,selectedCon,selectedInt,selectedInf,selectedCha,selectedCyber,selectedHp,selectedLe,selectedInf,selectedTo

	selectedStr = NPC.str
	selectedDex = NPC.dex
	selectedCon = NPC.con
	selectedInt = NPC.int 
	selectedCha = NPC.char
	selectedCyber = NPC.cyber
	selectedHp = NPC.hp
	selectedTo = NPC.to
	selectedLe = NPC.le
	selectedInf = NPC.inf

def drawNPCS():
	for i in entities:
		if i.image == "npc":
			gameDisplay.blit(npcImage,(i.x,i.y))


def drawEnv():
	for i in env:
		if i.image == "brush":
			gameDisplay.blit(brushImage,(i.x,i.y))
		elif i.image == "house":
			gameDisplay.blit(houseImage,(i.x,i.y))

def mouseCollisionDetection(pos):
	for i in entities:
		if(i.x <= pos[0] < i.x + i.width):
			if(i.y <= pos[1] <= i.y + i.height):
				updateStats(i)






for i in range(10):
	genNPC = generateNPC()
	entities.append(genNPC)


for i in range(30):
	genENV = generateENV()
	env.append(genENV)



entities.append(player)


while not quit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
        	pos = pygame.mouse.get_pos()
        	mouseCollisionDetection(pos)



    gameDisplay.fill([255, 255, 255])
    drawNPCS()
    drawEnv()
    drawStats()
    pygame.display.update()
    clock.tick(60)


pygame.quit()
quit()
