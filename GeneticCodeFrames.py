from DNASeq import DNASeq
class GeneFrame(object):
    geneLookUp = {"UUU" : "F", "UUC" : "F", "UUA" : "L", "CUU" : "L", "CUC" : "L",
                  "CUA" : "L", "CUG" : "L", "AUU" : "I", "AUC" : "I", "AUA" : "I", 
                  "GUU" : "V", "GUC" : "V", "GUA" : "V", "UCU" : "S", "UCC" : "S",
                  "UCA" : "S", "UCG" : "S", "CCU" : "P", "CCC" : "P", "CCA" : "P",
                  "CCG" : "P", "ACU" : "T", "ACC" : "T", "ACA" : "T", "ACG" : "T", 
                  "GCU" : "A", "GCC" : "A", "GCA" : "A", "GCG" : "A", "CAA" : "Q",
                  "UAU" : "Y", "UAC" : "Y", "CAU" : "H", "CAC" : "H", "AAG" : "K",
                  "CAG" : "Q", "AAU" : "N", "AAC" : "N", "AAA" : "K", "UGU" : "C",
                  "GAU" : "D", "GAC" : "D", "GAA" : "E", "GAG" : "E", "CGA" : "R",
                  "UGC" : "C", "UGG" : "W", "CGU" : "R", "CGC" : "R", "AGG" : "R",
                  "CGG" : "R", "AGU" : "S", "AGC" : "S", "AGA" : "R", "GGA" : "G",
                  "GGU" : "G", "GGC" : "G", "GGG" : "G", "AUG" : "M", "UAA" : "*",
                  "UAG" : "*", "UGA" : "*", "GUG" : "V", "UUG" : "L"}
    __aminoSeq: list = []

    __key: object = object()
    
    def __init__(self, key: object, other: DNASeq) -> None:
        assert(key == self.__key), \
            "Can only create geneFrames with geneFrame.initListGeneFrame() or geneFrame.initStringGeneFrame()"

        '''
        Initialize a geneFrame by translating a DNASeq to its corresponding codons

        Parameters:
            other (DNASeq): DNASeq to be translated
        Return:
            None
        '''
        self.aminoSeq = []
        translateMe = other.__str__().replace("T", "U")
        upTo = len(translateMe) - (len(translateMe) % 3)
        for x in range(0, upTo, 3):
            print("range: " + str(x) + " to " + str(x+3))
            self.__aminoSeq.append(self.geneLookUp.get(translateMe[x: x + 3]))
                
    @classmethod
    def initEmptyGeneFrame(cls) -> "GeneFrame":
        '''
        Initialize an empty geneFrame

        Parameters:
            None
        Return:
            Empty GeneFrame
        '''
        return GeneFrame(GeneFrame.__key, DNASeq.initEmptyDNASeq())
    
    @classmethod
    def initListGeneFrame(cls, bases: list) -> "GeneFrame":
        '''
        Initialize a geneFrame with a list of nitorgen bases

        Parameters:
            bases (list): List of nitrogen bases ACTG or any permutation thereof
        Returns:
            An instance of the translated amino acids from given DNA sequence
        '''
        return GeneFrame(GeneFrame.__key, DNASeq.initListDNASeq(bases))
    
    @classmethod 
    def initDNASeqGeneFrame(cls, dnaSeq: "DNASeq"):
        '''
        Initializes a Gene Frame with a DNA Sequence

        Parameters:
            dnaSeq (DNASequence): DNA Sequence to be translated to a gene frame
        Return:
            Instance of GeneFrame
        '''
        return GeneFrame(cls.__key, dnaSeq)
    
    def getAminoSequence(self) -> str:
        '''
        Return the string representation of amino sequence

        Parameters:
            None
        Return:
            String amino sequence
        '''
        return self.__aminoSeq.__str__().replace(",", "").replace(" ", "").replace("[", "").replace("]", "").replace("'", "")

    def swapFrames(self, codon1, codon2, offset = 0):
        if offset > 2 or offset < 0:
            raise IndexError("Offset must be 0, 1, or 2")
        '''
        Swap the given codon with the replacement starting at offset 0,1, or 2

        Parameters:
            offset (int): The startng index of search
            codon1 (str): Codon to be swapped
            codon2 (str): Codon to be swapped with
        '''
        leftOver = self.getAminoSequence()[0 : offset]
        result = self.getAminoSequence()[offset : ]
        return leftOver + codon2.join(part.replace(codon2, codon1) for part in result.split(codon1))
    
    def reverse(self):
        '''
        Reverse amino sequence

        Parameters:
            None
        Return:
            Reversed amino sequence
        '''
        self.__aminoSeq = self.__aminoSeq[::-1]
        return self.__aminoSeq
    
    def codReadFramePredict(self, maxLen: int, minLen: int):
        '''
        Create a list of codon reading frames

        Parameters:
            maxLen (int): Maximum length of reading frame
            minLen (int): Minimum length of reading frame
        Return:
            List of geneticCodeFrames that start with M and end with *
        '''
        result = []
        runningFrame = []
        for codon in self.__aminoSeq:
            if runningFrame[0] == "M":
                runningFrame.append(codon)
            elif codon == "M":
                runningFrame.append(codon)
            if codon == "*":
                runningFrame.append(codon)
                if len(runningFrame) <= maxLen and len(runningFrame) >= minLen:
                    result.append(GeneFrame.initEmptyGeneFrame())
                    result[len(result) - 1].__aminoSeq = runningFrame
                    runningFrame = []
        return result
            

