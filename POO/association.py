from classesmodules import Writer
from classesmodules import Pen
from classesmodules import TypeWriter

writer = Writer('joaozinho')
pen = Pen('Bic')
machine = TypeWriter()

writer.tool = machine
writer.tool.writing()

del writer
print(pen.brand)
machine.writing()
