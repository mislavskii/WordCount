import os
from pprint import pprint

from word_counter_ppt import WordCounter as WC
path = r'F:\User\Earn\Translate\Eng\Stories\Value\Processed'

all_files = sorted(os.listdir(path))
pprint(all_files)
print()

source_files = [path + '/' + file for file in all_files if 'eng.' not in file.lower()]
out_files = [path + '/' + file for file in all_files if 'eng.' in file.lower()]


total_count = 0
for in_file, out_file in zip(source_files, out_files):
    print(in_file, out_file, sep='\n')
    in_eng_count, out_eng_count = WC(in_file), WC(out_file)
    in_eng_count.count_words()
    out_eng_count.count_words()
    print(in_eng_count.en, out_eng_count.en, sep='\n')
    count = out_eng_count.en_count - in_eng_count.en_count
    print(count, end='\n\n')
    total_count += count


print(total_count * 1.3)
