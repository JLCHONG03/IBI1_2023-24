#import necessary libraries
import re
#ask the user to input the repetitive sequence
user_input = input("Please choose a repetitive sequence\nGTGTGT or GTCTGT: ").strip().upper()
repetitive_sequence = re.escape(user_input)
count_of_repeat_sequence = 0
gene_name = ""
gene_sequence = ""
isTargetGene = False

input_file_path = "C:\\Users\\JL CHONG\\Desktop\\IBI1\\IBI1_2023-24\\Practical 8\\duplicate_genes.fa"
output_file_path = f"C:\\Users\\JL CHONG\\Desktop\\IBI1\\IBI1_2023-24\\Practical 8\\{user_input}_duplicate_genes.fa"
#loop the file
#extract the gene name and the gene sequence
#new file write the extracted gene name and the gene sequence
#add the count by one when the repetitive sequence was encountered in the gene sequence
#new file write the count
with open(input_file_path, "r") as read_file, open(output_file_path, "w") as write_file:
    for line in read_file:
        if line.startswith('>'):
            if isTargetGene == True:
                write_file.write(gene_name)
                write_file.write(gene_sequence)
                write_file.write(f"Count of {user_input}: {count_of_repeat_sequence}\n")
            gene_name = line
            gene_sequence = ""
            isTargetGene = False
        else:
            gene_sequence += line
            # Check if the repetitive sequence is present in the current line
            if re.findall(repetitive_sequence, line):
                isTargetGene = True
                count_of_repeat_sequence = len(re.findall(repetitive_sequence, line))
if isTargetGene:
        write_file.write(gene_name)
        write_file.write(gene_sequence)
        write_file.write(f"Count of {user_input}: {count_of_repeat_sequence}\n")

print(f"Processed genes with {user_input}. Output written to {output_file_path}")
                    
                    
                     
                    
            
            
        
        
            
            
