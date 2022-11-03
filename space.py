#speed of light in meters per second
sol = 299792458

#seconds in an hour
sih = 3600

#hours in a day
hid = 24

#days in a year accounting for leap
diy = 365.25

#light year in meters
lym = sol*3600*hid*diy

#astronomical unit
au = 149597870700

#distances relative to earth & diameters
#source: https://www.jpl.nasa.gov/edu/pdfs/scaless_reference.pdf
sun = [0, 1391400000]
mercury = [0.39, 4879000]
venus = [0.72, 12104000]
earth = [1, 12756000]
mars = [1.52, 6792000]
jupiter = [5.2, 142984000]
saturn = [9.54, 120536000]
uranus = [19.2, 51118000]
neptune = [30.06, 49528000]

planets = [mercury, venus, earth, mars, jupiter, saturn, uranus, neptune]
pltxt = ["mercury", "venus  ", "earth  ", "mars   ", "jupiter", "saturn ", "uranus ", "neptune"]

print(" ")
print("***********************************************************************************")
print(" ")
print("This app displays the time it takes light to reach each planet in the solar system from the surface of the Sun")

cursor = 0

while cursor < len(planets):
	print(" ")
	x = planets[cursor]
	y = x[0]
	z = y * au
	ly = z / sol
	h = str(int(ly // 3600))
	m = str(int((ly%3600) // 60))
	s = str(int((ly%3600) % 60))
	if int(h) < 10:
		h = "0" + h
	if int(m) < 10:
		m = "0" + m
	if int(s) < 10:
		s = "0" + s
	clock = h + ":" + m + ":" + s
	print(pltxt[cursor] + " > " + str(clock))
	cursor = cursor + 1

print(" ")
print("***********************************************************************************")