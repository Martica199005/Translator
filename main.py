import googletrans
from googletrans import Translator

translator= Translator()

#result=translator.translate('Hola como estas')
result = translator.translate('Hola como estas', src='es', dest='ro')

print(result.src)
print(result.dest)
print(result.origin)
print(result.text)
print(result.pronunciation)