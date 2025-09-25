# utils.py
import random
import difflib

BASES = "ATGC"

# Amino acid codon mapping for Level 3
CODON_TABLE = {
    "AUG": "Met",
    "UUU": "Phe",
    "UUC": "Phe",
    "GAA": "Glu",
    "GAG": "Glu",
    "UUA": "Leu",
    "UUG": "Leu",
    "CUU": "Leu",
    "CUC": "Leu",
    "CUA": "Leu",
    "CUG": "Leu",
    "AUU": "Ile",
    "AUC": "Ile",
    "AUA": "Ile",
    "GUU": "Val",
    "GUC": "Val",
    "GUA": "Val",
    "GUG": "Val"
}

def generate_dna(length=6, count=1):
    """Generate one or more random DNA sequences."""
    return [''.join(random.choice(BASES) for _ in range(length)) for _ in range(count)]

def get_complement(dna):
    comp_map = {'A':'T','T':'A','G':'C','C':'G'}
    return ''.join(comp_map[base] for base in dna)

def introduce_mutations(dna, num_mutations=1):
    dna_list = list(dna)
    positions = random.sample(range(len(dna_list)), min(num_mutations, len(dna_list)))
    for pos in positions:
        current_base = dna_list[pos]
        dna_list[pos] = random.choice([b for b in BASES if b != current_base])
    return ''.join(dna_list)

def generate_random_mrna(num_codons=3, count=1):
    sequences = []
    for _ in range(count):
        sequences.append(' '.join(random.choice(list(CODON_TABLE.keys())) for _ in range(num_codons)))
    return sequences

def translate_mrna_to_protein(mrna_seq):
    codons = mrna_seq.split()
    amino_acids = [CODON_TABLE.get(codon, "???") for codon in codons]
    return '-'.join(amino_acids)
