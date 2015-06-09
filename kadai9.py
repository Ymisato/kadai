
#練習問題9.1
fin = open('words.txt')
for line in fin:
    word = line.strip()
    if (20<=len(word)):
        print word  
"""
実行結果
counterdemonstration
counterdemonstrations
counterdemonstrators
hyperaggressivenesses
hypersensitivenesses
microminiaturization
microminiaturizations
representativenesses
"""

