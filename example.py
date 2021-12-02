from tile import Model, Shape

BLUE = 0x477984
ORANGE = 0xEEAA4D
RED = 0xC03C44

model = Model()
model.append(Shape(6, fill=RED))
a = model.add(0, range(6), 4, fill=ORANGE)
surface = model.render()
surface.write_to_png('output1.png')
b = model.add(a, 1, 3, fill=BLUE)
surface = model.render()
surface.write_to_png('output2.png')
c = model.add(a, 2, 6, fill=RED)
surface = model.render()
surface.write_to_png('output3.png')
model.repeat(c)
surface = model.render()
surface.write_to_png('output4.png')
