import re

duplicate_genes = open("C:\\Users\\JL CHONG\\Desktop\\IBI1\\IBI1_2023-24\\Practical 8\\Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa","r")
new_gene_file = open("C:\\Users\\JL CHONG\\Desktop\\IBI1\\IBI1_2023-24\\Practical 8\\duplicate_genes.fa","w")
gene_name = ""
gene_sequence = ""
isTargetGene = False
for line in duplicate_genes:
    if line.startswith('>'):
        if len(gene_sequence) > 0:
            if isTargetGene:
                new_gene_file.write(gene_sequence)
            gene_sequence = ""
            isTargetGene = False   
        if 'duplication' in line:
            gene_name = re.search(r'>(.*?)\s',line)
            new_gene_file.write(gene_name.group())
            new_gene_file.write('\n')
            isTargetGene = True
    else:
        gene_sequence += line   
if len(gene_sequence) > 0:
    if isTargetGene:
        new_gene_file.write(gene_sequence)
        
        
#with open("C:\\Users\\JL CHONG\\Downloads\\Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa") as f:
 #   isTargetGene = False
  #  gene_sequence = ""
   # for line in f:
    #    if line.startswith('>'):
     #       if len(gene_sequence) > 0:
      #          if isTargetGene:
       #             print(gene_sequence)
        #        gene_sequence = ""
         #       isTargetGene = False

            # We do this in case there are two "description:"
          #  description = line.split("description:")
           # description.pop(0)
            #description = "".join(description)

            # WARNING: This will also match words like "nonduplication" (which is not a word, but you get the idea)
            #if "duplication" in description:
             #   isTargetGene = True
              #  print(line.split(" ")[0])
        #else:
         #   gene_sequence += line.strip()
    #if len(gene_sequence) > 0:
    #    if isTargetGene:
     #       print(gene_sequence)


