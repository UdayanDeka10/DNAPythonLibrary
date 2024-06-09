

class DNASeq(object):
    __seq: list
    __key = object()
    
    
    def __init__(self, key: object, readableSeq: list) -> None:
        '''
        Makes an instance of DNASeq given a list of nitrogen bases
        '''
        assert(DNASeq.__key == key), \
            "Can only create object with DNASeq.initStringDNASeq() or DNASeq.initEmptyDNASeq()"
        self.__seq = readableSeq
    
    def __str__(self) -> str:
        '''
        Gives a string representation of object's DNA sequence
        Return:
            str: DNA Sequence
        '''
        return str.upper(self.seq.__str__())

    @classmethod
    def initListDNASeq(cls, readableSeq: list) -> "DNASeq":
        if not isinstance(readableSeq, list):
            raise TypeError("readableSeq must be of type list")
        '''
        make an instance of DNASeq from user given list sequence of bases.
        anything that is not a character in "AaCcTtGg" is ignored and not added to the instance. 
    
        Parameters:
            readableSeq (list): Given list of ACTG or any permutation thereof
        Return:
            DNASeq: an instance of DNASeq
        '''
        return DNASeq(DNASeq.__key, readableSeq)

    @classmethod
    def initStringDNASeq(cls, readableSeq: str) -> "DNASeq":
        if not isinstance(readableSeq, str):
            raise TypeError("readableSeq must be a string")
        ''' 
        make an instance of DNASeq from user given string sequence of bases.
        anything that is not a character in "AaCcTtGg" is ignored and not added to the instance. 
    
        Parameters:
            readableSeq (str): Given string of ACTG or any permutation thereof
        Return:
            DNASeq: an instance of DNASeq
        '''
        DNAToArr = []
        acceptableBases = ["A", "a", "c", "C", "T", "t", "G", "g"]
        readableSeq.strip()
        for base in readableSeq:
            if base in acceptableBases:
                if base == "T" or base == "t":
                    DNAToArr.append("U")
                else:
                    DNAToArr.append(base.upper())
        return DNASeq(DNASeq.__key, DNAToArr)
    
    @classmethod
    def initEmptyDNASeq(cls) -> "DNASeq":
        '''
        Gives an instance of DNASeq with no sequence

        Parameters:
            None
        Return:
            DNASeq: Instance of DNASeq 
        '''
        return DNASeq(DNASeq.__key, [])
    
    def getSequence(self) -> list:
        '''
        Returns a the DNA Sequence

        Parameters:
            None
        Return:
            List of bases in DNA Sequence
        '''
        return self.__seq
    
    def append(cls, base):
        base = str(base)
        if not base in ["A", "a", "c", "C", "T", "t", "G", "g"]:
            raise ValueError("Invalid base")
        '''
        Adds a base to the end of the DNA Sequence
        Parameters:
            None
        Return:
            None
        '''
        if base == "T" or base == "t":
            cls.seq += "U"
        else:
            cls.seq += base

    def concat(cls, otherSeq: "DNASeq"):
        if not isinstance(otherSeq, DNASeq):
            raise TypeError("otherSeq must be of type DNASeq")
        '''
        Concatenates two DNA Sequences
        
        Parameters:
            otherSeq (DNASeq): DNA sequence to be added at the end of this sequence
        Return:
            None
        '''     
        cls.__seq += otherSeq.__seq

    
    def reverse(self):
        '''
        Reverses the DNA sequence

        Parameters:
            None
        Return:
            None
        '''
        list.reverse(self.seq)

    def complement(self):
        '''
        Complements DNA Sequence
        
        Parameters:
            None
        Return:
            None
        '''
        for base in range(len(self.seq)):
            if self.seq[base] == "A" or self.seq[base] == "T":
                self.seq[base] = "T" if self.seq[base] == "A" else "T"
            elif self.seq[base] == "C" or self.seq[base] == "G":
                self.seq[base] = "G" if self.seq[base] =="C" else "G"
    
    def reverseComplement(self):
        '''
        Reverses and complemements this DNA Sequence

        Parameters: 
            None
        Return:
            None
        '''

        self.reverse()
        self.complement()
    
    def __str__(self) -> str:
        '''
        Returns string of bases

        Parameters:
            None
        Return:
            String DNA Sequence
        '''
        return self.__seq.__str__().replace(",", "").replace(" ", "").replace("[", "").replace("]", "").replace("'", "")



    


