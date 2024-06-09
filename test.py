from DNASeq import DNASeq
from GeneticCodeFrames import GeneFrame

trialDNA = DNASeq.initStringDNASeq("AACGTGATG")
trialGene = GeneFrame.initListGeneFrame(["A", "A", "C", "G", "T", "G", "A", "T", "G"])
print(trialGene.getAminoSequence())




