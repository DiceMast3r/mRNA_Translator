stop_codon = ["UAA", "UAG", "UGA"]
amino_acid = ["Ala", "Arg", "Asn", "Asp", "Cys", "Glu", "Gln", "Gly", "His", "Ile", "Leu", "Lys",
              "Met", "Phe", "Pro", "Ser", "Thr", "Trp", "Tyr", "Val"]
codon_U = ["UUU", "UUC", "UUA", "UUG",
           "UCU", "UCC", "UCA", "UCG",
           "UAU", "UAC", "UAA", "UAG",
           "UGU", "UGC", "UGA", "UGG"]
codon_C = ["CUU", "CUC", "CUA", "CUG",
           "CCU", "CCC", "CCA", "CCG",
           "CAU", "CAC", "CAA", "CAG",
           "CGU", "CGC", "CGA", "CGG"]
codon_A = ["AUU", "AUC", "AUA", "AUG",
           "ACU", "ACC", "ACA", "ACG",
           "AAU", "AAC", "AAA", "AAG",
           "AGU", "AGC", "AGA", "AGG"]
codon_G = ["GUU", "GUC", "GUA", "GUG",
           "GCU", "GCC", "GCA", "GCG",
           "GAU", "GAC", "GAA", "GAG",
           "GGU", "GGC", "GGA", "GGG"]
translated_amino_acid = []

codon_in = input("Enter mRNA Codon: ")
codon_txt = [(codon_in[i:i + 3]) for i in range(0, len(codon_in), 3)]
for r in range(0, len(codon_txt)):
    if codon_txt[r] == "AUG":
        translated_amino_acid.append(amino_acid[12])
        r += 1
    elif codon_txt[r] == ("UUU" or "UUC"):
        translated_amino_acid.append(amino_acid[13])
        r += 1
    elif codon_txt[r] == ((("UUA" or "UUG") or ("CUU" or "CUA")) or ("CUG" or "CUC")):
        translated_amino_acid.append(amino_acid[10])
        r += 1
    elif codon_txt[r] == ((("UCU" or "UCA") or ("UCC" or "UCG")) or ("AGU" or "AGC")):
        translated_amino_acid.append(amino_acid[15])
        r += 1
    elif codon_txt[r] == ("UAU" or "UAC"):
        translated_amino_acid.append(amino_acid[18])
        r += 1
    elif codon_txt[r] == ("UGU" or "UGC"):
        translated_amino_acid.append(amino_acid[4])
        r += 1
    elif codon_txt[r] == "UGG":
        translated_amino_acid.append(amino_acid[17])
        r += 1
    elif codon_txt[r] == (("CCU" or "CCC") or ("CCA" or "CCG")):
        translated_amino_acid.append(amino_acid[14])
        r += 1
    elif codon_txt[r] == ("CAU" or "CAC"):
        translated_amino_acid.append(amino_acid[8])
        r += 1
    elif codon_txt[r] == ("CAA" or "CUG"):
        translated_amino_acid.append(amino_acid[6])
        r += 1
    elif codon_txt[r] == ((("CGU" or "CGC") or ("CGA" or "CGG")) or ("AGA" or "AGG")):
        translated_amino_acid.append(amino_acid[1])
        r += 1
    elif codon_txt[r] == (("AUU" or "AUC") or "AUA"):
        translated_amino_acid.append(amino_acid[9])
        r += 1
    elif codon_txt[r] == (("ACU" or "ACC") or ("ACA" or "ACG")):
        translated_amino_acid.append(amino_acid[16])
        r += 1
    elif codon_txt[r] == ("AAU" or "AAC"):
        translated_amino_acid.append(amino_acid[2])
        r += 1
    elif codon_txt[r] == ("AAA" or "AAG"):
        translated_amino_acid.append(amino_acid[11])
        r += 1
    elif codon_txt[r] == (("GUU" or "GUC") or ("GUA" or "GUG")):
        translated_amino_acid.append(amino_acid[19])
        r += 1
    elif codon_txt[r] == (("GCU" or "GCC") or ("GCA" or "GCG")):
        translated_amino_acid.append(amino_acid[0])
        r += 1
    elif codon_txt[r] == ("GAU" or "GAC"):
        translated_amino_acid.append(amino_acid[3])
        r += 1
    elif codon_txt[r] == ("GAA" or "GAG"):
        translated_amino_acid.append(amino_acid[5])
        r += 1
    elif codon_txt[r] == (("GGU" or "GGC") or ("GGA" or "GGG")):
        translated_amino_acid.append(amino_acid[7])
        r += 1
    elif codon_txt[r] == (("UAG" or "UAA") or "UGA"):
        translated_amino_acid.append("Stop")
        r += 1

print("Amino acid sequence: " + " ".join(translated_amino_acid))
