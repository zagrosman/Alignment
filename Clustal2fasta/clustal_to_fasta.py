# Import necessary modules
import argparse

# Parse command-line arguments
parser = argparse.ArgumentParser(description='Convert Clustal Omega alignment output to Fasta format')
parser.add_argument('input', help='Input file in Clustal Omega format (.aln)')
parser.add_argument('output', help='Output file in Fasta format (.fasta)')
args = parser.parse_args()

# Read in input file
with open(args.input, 'r') as infile:
    # Skip header lines
    for line in infile:
        if line.startswith('CLUSTAL') or line.startswith('#'):
            continue
        else:
            break
    # Parse alignment data
    seqs = {}
    for line in infile:
        if line.strip() == '':
            continue
        else:
            fields = line.split()
            if fields[0] not in seqs:
                seqs[fields[0]] = fields[1]
            else:
                seqs[fields[0]] += fields[1]

# Write output file in Fasta format
with open(args.output, 'w') as outfile:
    for id, seq in seqs.items():
        outfile.write('>' + id + '\n')
        outfile.write(seq + '\n')

