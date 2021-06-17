# Uncomment this when you reach the "Use the Force" section
train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1


# Write your code below: 

##### TEMPS #####
def f2c(ftemp):
  ctemp = (ftemp - 32) * (5/9)
  return ctemp

def c2f(ctemp):
  ftemp = (ctemp * (9/5)) + 32
  return ftemp

f100c = f2c(100)
print(f100c)

c100f = c2f(0)
print(c100f)

##### FORCE #####

def getForce(mass, acceleration=9.81):
  force = mass*acceleration
  return force

def getEnergy(mass, c=3*10**8):
  energy = (mass * c)**2
  return energy

trainForce = getForce(train_mass, train_acceleration)
print("The GE train suppplies", trainForce, "Newtons of force.")

bomb_energy = getEnergy(bomb_mass)
print("A 1kg bomb supplies", bomb_energy, "Joules.")

##### WORK #####

def getWork(mass, acceleration, distance):
  work = getForce(mass, acceleration) * distance
  return work

train_work = getWork(train_mass, train_acceleration, train_distance)
print("The GE train does", train_work, "Joules of work over", train_distance, "meters.")
