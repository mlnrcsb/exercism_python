def to_rna(dna_strand):
    rna_mapping = {'G': 'C', 'C': 'G', 'T': 'A', 'A': 'U'}
    return ''.join(rna_mapping[nucleotide] for nucleotide in dna_strand)