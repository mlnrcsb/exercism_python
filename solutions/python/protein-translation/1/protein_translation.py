def proteins(strand):
    acid_trans = {'Methionine': ['AUG'], 'Phenylalanine': ['UUU', 'UUC'], 'Leucine': ['UUA', 'UUG'], 'Serine': ['UCU', 'UCC', 'UCA', 'UCG'], 'Tyrosine': ['UAU', 'UAC'], 'Cysteine': ['UGU', 'UGC'], 'Tryptophan': ['UGG']}
    stops = ['UAA', 'UAG', 'UGA']

    result = []

    for i in range(0,len(strand), 3):
        codon = strand[i] + strand[i + 1] + strand[i + 2]
        if codon in stops:
            return result
        for acid, codons in acid_trans.items():
            if codon in codons:
                result.append(acid)
    return result