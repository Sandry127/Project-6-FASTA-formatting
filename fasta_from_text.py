# Assignment: Read input text file and convert into a properly formatted FASTA file.
# Ask for the input filename so this program can be reused with other files.
input_file = input("Enter the input text file name: ")
# Opened the file 'with' to make sure the file closes automatically when done.
with open(input_file, 'r') as f:
    accession = f.readline().strip()
    gene = f.readline().strip()
    species = f.readline().strip()
    sequence = f.readline().strip().upper() # To make sure all the bases are uppercase.
# To create a FASTA header which should start with '>' followed by its accession, gene, and species.
header = f">{accession} {gene} [{species}]"
# To break the sequence every 60 characters, fitting FASTA format.
# Join all the wrapped sequence lines into one final sequence.
fasta_seq = ""
for i in range(0, len(sequence), 60):
    fasta_seq += sequence[i:i+60] + "\n"
# Choose an output filename and use .fasta
output_file = "output.fasta"
# Write everything including the header and the formatted sequence into the FASTA file and end with a new line.
with open(output_file, "w") as f:
    f.write(header + "\n" + fasta_seq)
# Print message to confirm success and where to find the result.
print("FASTA file created successfully:", output_file)