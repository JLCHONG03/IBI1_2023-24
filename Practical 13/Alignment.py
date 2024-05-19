#import the necessary libraries
import blosum as bl

seq1 = open("C:\\Users\\JL CHONG\\Desktop\\IBI1\\IBI1_2023-24\\Practical 13\\SLC6A4_HUMAN.fa","r")
seq2 = open("C:\\Users\\JL CHONG\\Desktop\\IBI1\\IBI1_2023-24\\Practical 13\\SLC6A4_MOUSE.fa","r")
seq3 = open("C:\\Users\\JL CHONG\\Desktop\\IBI1\\IBI1_2023-24\\Practical 13\\SLC6A4_RAT.fa","r")
#extract the gene sequence from the file
def extract_sequence(file):
    seq = ""
    for line in file:
        if line.startswith('>'):
            continue
        else:
            seq += line.strip()
    return (seq)
            
human_seq = extract_sequence(seq1)
mouse_seq = extract_sequence(seq2)
rat_seq = extract_sequence(seq3)
#calculate the difference in the human and mouse sequence and the percentage identical of the human and mouse sequence
distance_between_human_and_mouse = 0
for i in range(len(human_seq)):
    if human_seq[i] != mouse_seq[i]:
        distance_between_human_and_mouse += 1
print("Difference between human and mouse sequence is:", distance_between_human_and_mouse)
percentage_identical = ((len(human_seq) - distance_between_human_and_mouse) / len(human_seq))*100
print("The percentage identical between human and mouse sequence is: " + str(percentage_identical) + "%")
#calculate the difference in the human and rat sequence and the percentage identical of the human and rat sequence
distance_between_human_and_rat = 0
for i in range(len(human_seq)):
    if human_seq[i] != rat_seq[i]:
        distance_between_human_and_rat += 1
print("Difference between human and rat sequence is:", distance_between_human_and_rat)
percentage_identical = ((len(human_seq) - distance_between_human_and_rat) / len(human_seq))*100
print("The percentage identical between human and rat sequence is: " + str(percentage_identical) + "%")
#calculate the difference in the mouse and rat sequence and the percentage identical of the mouse and rat sequence
distance_between_mouse_and_rat = 0
for i in range(len(mouse_seq)):
    if mouse_seq[i] != rat_seq[i]:
        distance_between_mouse_and_rat += 1
print("Difference between mouse and rat sequence is:", distance_between_mouse_and_rat)
percentage_identical = ((len(mouse_seq) - distance_between_mouse_and_rat) / len(mouse_seq))*100
print("The percentage identical between mouse and rat sequence is: " + str(percentage_identical) + "%")  

import blosum as bl
#by using the BLOSUM62 matrix
matrix = bl.BLOSUM(62)
#calculate the alignment score for the human and mouse sequence
alignment_between_human_and_mouse_sequence = 0
for i in range(len(human_seq)):
    human_aa = human_seq [i]
    mouse_aa = mouse_seq [i]
    alignment = matrix[human_aa][mouse_aa]
    alignment_between_human_and_mouse_sequence += alignment
print("The alignment between human and mouse sequence:", alignment_between_human_and_mouse_sequence)
#calculate the alignment score for the human and rat sequence
alignment_between_human_and_rat_sequence = 0
for i in range(len(human_seq)):
    human_aa = human_seq [i]
    rat_aa = rat_seq [i]
    alignment = matrix[human_aa][rat_aa]
    alignment_between_human_and_rat_sequence += alignment
print("The alignment between human and rat sequence:", alignment_between_human_and_rat_sequence)
#calculate the alignment score for the mouse and rat sequence 
alignment_between_mouse_and_rat_sequence = 0
for i in range(len(mouse_seq)):
    mouse_aa = mouse_seq [i]
    rat_aa = rat_seq [i]
    alignment = matrix[mouse_aa][rat_aa]
    alignment_between_mouse_and_rat_sequence += alignment
print("The alignment between mouse and rat sequence:", alignment_between_mouse_and_rat_sequence)


        