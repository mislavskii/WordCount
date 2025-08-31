from word_counter_ppt import WordCounter as WC, count

path_1 = r'D:\Earn\Translate\English\Atelier\sparkling wine\Перевод 3.pptx'
path_2 = r'D:\Earn\Translate\English\Atelier\sparkling wine\Перевод 3 ENG.pptx'

source = WC(path_1)
source.count_words()

output = WC(path_2)
output.count_words()

print(source.ru_count)
print(count(path_1))
