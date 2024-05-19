import re
seq = 'ATGCAATCGGTGTGTCTGTTCTGAGAGGGCCTAA'
count_of_repeat_elements = 0
if re.findall(r'GTGTGT',seq):
    count_of_repeat_elements +=1
    print(count_of_repeat_elements)
if re.findall(r'GTCTGT',seq):
    count_of_repeat_elements +=1
    print(count_of_repeat_elements)
