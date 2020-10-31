import pygame, random, math
pygame.init()




gameDisplay = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
pygame.display.set_caption('The DMZ')
pygame.font.init() # you have to call this at the start, 
                   # if you want to use this module.
myfont = pygame.font.SysFont('VCR_OSD_MONO', 40,)
clock = pygame.time.Clock()

w, h = pygame.display.get_surface().get_size()

quit = False

overWorld = []
localMap = [0,60,0,50]
mapX = math.floor(w * 1/4)
mapY = math.floor(h * 1/5)

hutImage = pygame.image.load("Hut.png")
treeImage = pygame.image.load("tree.png")
bannerImage = pygame.image.load("Banner.png")
playerImage = pygame.image.load("player.png")
waterImage = pygame.image.load("water.png")
marshImage = pygame.image.load("marshLand.png")
grassImage = pygame.image.load("grass.png")
settlementImage = pygame.image.load("Settlement.png")
npcImage = pygame.image.load("npc.png")



playerLocation = [20,20]
stats = {"Strength":0,"Dexterity":0,"Constitution":0,"Intelligence":0,"Charisma":0,
		 "Cyber":0,"HP":0,"Toughness":0,"Influence":0,"Leadership":0}


entities = []



class entity:

	def __init__():
		self.s = 0
		self.d = 0
		self.c = 0
		self.i = 0
		self.ch = 0
		self.cy = 0
		self.hp = 0
		self.t = 0 
		self.inf = 0
		self.l = 0

		
def genMap():
	for i in range(700):
		line = []
		lineE = []
		for j in range(400):
			line.append(random.randint(1,1600))
			lineE.append(0)
		overWorld.append(line)
		entities.append(lineE)
	for i in range(600):
		for j in range(300):
			#Seed river
			if(overWorld[i][j] == 401):
				northSouth = False
				count = 0
				direction = 0
				pivot = 0
				for k in range(random.randint(10,50)):
					twist = (random.randint(0,10))
					if(twist < 2):
						direction = random.randint(1,2)
						pivot = k
						
					if(j+k<len(overWorld[i])):
						if(direction == 1):
							overWorld[i+k][j+pivot+random.randint(0,1)] = 400
						elif(direction == 2):
							overWorld[i+pivot+random.randint(0,1)][j+k] = 400


			#Seed lake
			if(overWorld[i][j]==406):
				for k in range(100):
					overWorld[i+random.randint(1,5)][j+random.randint(1,5)] = 400
					overWorld[i+random.randint(1,5)][j+random.randint(1,5)] = 400
			#Seed Marsh
			if(overWorld[i][j]==400):
				if(overWorld[i][j-1] != 400):
					overWorld[i][j-1] = 605
				if(overWorld[i][j+1] != 400):
					overWorld[i][j+1] = 605
				if(overWorld[i-1][j] != 400):
					overWorld[i-1][j] = 605
				if(overWorld[i+1][j] != 400):
					overWorld[i+1][j] = 605
			
			#seed settlements
			if(overWorld[i][j] == 405):
				city = False
				for l in range(20):
					if((overWorld[i-l][j] == 400) or (overWorld[i+l][j] == 400) or (overWorld[i][j-l] == 400) or (overWorld[i][j+l] == 400)):
						print("city")
						entities[i][j] = 1
						city = True
						for k in range(random.randint(10,50)):
							overWorld[i+random.randint(-5,5)][j+random.randint(-5,5)] = 1
						break
				if(not city):
					for k in range(random.randint(3,10)):
						overWorld[i+random.randint(-4,3)][j+random.randint(-3,3)] = 1

	print(entities)

def renderStats():
	Y = 0
	for i in stats:
		textsurface = myfont.render(i + ": "+str(stats[i]), False, (255, 255, 255))
		gameDisplay.blit(textsurface,(w*3/4,h*1/4+Y))
		Y+=40


def renderLocalMap():
	tileX = mapX
	tileY = mapY
	for i in range(localMap[2],localMap[3]):
		tileX = mapX
		for j in range(localMap[0],localMap[1]):
			if(i == playerLocation[1] and j == playerLocation[0]):
				gameDisplay.blit(playerImage,(tileX,tileY))
			else:
				if(overWorld[i][j]>1200):
					gameDisplay.blit(treeImage,(tileX,tileY))
				elif(overWorld[i][j] == 400):
					gameDisplay.blit(waterImage,(tileX,tileY))
				elif(overWorld[i][j]==405):
					gameDisplay.blit(settlementImage,(tileX,tileY))
				elif(overWorld[i][j]==1):
					gameDisplay.blit(hutImage,(tileX,tileY))
				elif(overWorld[i][j]==605):
					gameDisplay.blit(marshImage,(tileX,tileY))
				else:
					gameDisplay.blit(grassImage,(tileX,tileY))

				if(entities[i][j]==1):
					gameDisplay.blit(npcImage,(tileX,tileY))



			tileX +=16
		tileY+=16


genMap()
renderLocalMap()



while not quit:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			quit = True
		elif event.type == pygame.MOUSEBUTTONDOWN:
			pos = pygame.mouse.get_pos()
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				quit = True
			elif event.key == pygame.K_d:
				localMap[0]+=1
				localMap[1]+=1
				playerLocation[0]+=1
			elif event.key == pygame.K_w:
				if(localMap[2]>0):
					localMap[2]-=1
					localMap[3]-=1
					playerLocation[1]-=1
			elif event.key == pygame.K_s:
				if(localMap[3]<=700):
					localMap[2]+=1
					localMap[3]+=1
					playerLocation[1] +=1
			elif event.key == pygame.K_a:
				if(localMap[0]>0):
					localMap[0] -=1
					localMap[1] -=1
					playerLocation[0]-=1


	gameDisplay.fill([0,0,0])
	renderLocalMap()
	renderStats()
	pygame.display.update()
	clock.tick(60)



pygame.quit()



