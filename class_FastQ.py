class FastQ:
    def __init__(self):
        self.data = []
        self.sequences = []
        self.sequence_names = []
        self.quality = []
        self.number_of_contigs = 0

    def ReadFastQ(self, filename):

        try:
            with open(filename) as f_handle:
                self.data = list(f_handle)
        except IOError:
            print("Could not open file...")
            print("Check that the file path and name is correct...")
        else:
            f_handle.close()

        line = 0
        first = 0
        items_in_list = len(self.data)

        while (line < items_in_list):
            if ((self.data[line][0] == '@') & (first == 0)):
                self.sequence_names.append(self.data[line][1:].rstrip('\n'))
                self.number_of_contigs += 1
                first = 1
                line += 1
            if (((self.data[line][0] == 'G') | (self.data[line][0] == 'A') | (self.data[line][0] == 'T') | (
                self.data[line][0] == 'C')) & first == 1):
                self.sequences.append(self.data[line][:].rstrip('\n'))
                line += 1
            if ((self.data[line][0] == '+') & (first == 1)):
                line += 1
            if (first == 1):
                self.quality.append(self.data[line][:].rstrip('\n'))
                first = 0
                line += 1
        return (self.number_of_contigs)

    def IsFastQ(self, number_of_lines, data):
        if ((data[0][0] == '@') & (data[2][0] == '+')):
            return (True)
        else:
            return (False)

    def GetNumberOfSequences(self):
        return (self.number_of_contigs)

    def GetSequenceName(self, index):
        return (self.sequence_names[index])

    def GetSequence(self, index):
        return (self.sequences[index])

    def GetSequenceNameList(self):
        return (self.sequence_names)

    def GetSequenceList(self):
        return (self.sequences)

    def GetQuality(self, index):
        return (self.quality[index])

    def WriteFastQ(self, outputfilename, sequence_names, sequences, number_of_sequences, quality=''):
        f = open(outputfilename, "w")
        for i in range(0, number_of_sequences):
            f.write("@" + sequence_names[i] + "\n")
            f.write(sequences[i] + "\n+\n")
            f.write("F" * len(sequences[i]) + "\n")
        f.close()