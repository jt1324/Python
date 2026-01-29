text = 'Curso em Video Python'
text2 = '   Aprenda Python  '

print(text[9])
print(text[9:13])
print(text[9:21:2])
print(text[:5])
print(text[12:])
print(text[9::3])
print(len(text))
print(text.count('o'))
print(text.count('o',0,13))
print(text.find('deo'))
print(text.find('Android'))
print('Curso' in text)
print(text.replace('Python', 'Android'))
print(text.upper())
print(text.lower())
print(text.capitalize())
print(text.title())
print(text.split())
print('-'.join(text.split()))

# text 2
print(text2.strip()) # remove space outside
print(len(text2))
print(len(text2.strip()))
print(text2.rstrip()) 
print(text2.lstrip())

# long text
print("""That’s where these 10 prompts come in. If you use them smartly, 
ChatGPT can act like your personal coding buddy: teaching you, 
correcting you and even giving you interview practice.""")