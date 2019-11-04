class FastA:
    def __init__(self):
        self.data = []
        self.sequences = []
        self.sequence_names = []
        self.number_of_contigs = 0
        
        
    def __iter__(self):
        self.counter = 0
        return self
    
    def __next__(self):
        if (self.counter < self.number_of_contigs):
            self.counter += 1
        else:
            raise StopIteration
        return (self.sequences[self.counter - 1])

    def ReadFastA(self, filename):

        try:
            with open(filename) as f_handle:
                self.data = list(f_handle)
        except IOError:
            print("Could not open file...")
            print("Check that the file path and name is correct...")
        else:
            f_handle.closed

        line = 0
        first = 0
        items_in_list = len(self.data)

        # Step through the read lines
        # If it start with a '>' it is a title line
        # No '>' means a sequence line
        # Keep on appending sequences to the current sequence until you hit the next title line

        while (line < items_in_list):
            if (self.data[line][0] == ">"):
                self.sequence_names.append(self.data[line][1:].rstrip('\n'))
                self.number_of_contigs += 1
                first = 1
            else:
                if (first == 1):
                    self.sequences.append(self.data[line].rstrip('\n'))
                    first = 0
                else:
                    self.sequences[self.number_of_contigs - 1] = self.sequences[self.number_of_contigs - 1] + self.data[
                        line].rstrip('\n')
            line += 1
        return self.number_of_contigs

    def NumberOfContigs(self):
        return (self.number_of_contigs)

    def GetContigLengths(self):
        # Get the length of each sequence

        contig_length = []
        number_of_contigs = self.NumberOfContigs()
        for i in range(0, number_of_contigs):
            contig_length.append(len(self.contig_sequence[i]))
        return (contig_length)

    def GetContigSequence(self, index):
        if ((index >= 0) & (index < self.number_of_contigs)):
            return (self.sequences[index])
        else:
            return ("")

    def GetContigLength(self, index):
        return (len(self.sequences[index]))

    def GetContigName(self, index):
        if ((index >= 0) & (index < self.number_of_contigs)):
            return (self.sequence_names[index])
        else:
            return ("")

    def GetSequenceNamesList(self):
        return (self.sequence_names)

    def GetSequencesList(self):
        return (self.sequences)

    def WriteFastA(self, filename, sequence_names, sequence, number_of_sequences):

        line_length = 80
        f = open(filename, 'w')
        for i in range(0, number_of_sequences):
            f.write(">" + sequence_names[i] + "\n")
            number_of_80_bp_rows = int(len(sequence[i]) / line_length)
            bases_in_final_row = int(len(sequence[i]) % line_length)
            for row in range(1, number_of_80_bp_rows + 1):
                f.write(sequence[i][(row - 1) * line_length:(row * line_length)] + "\n")
            f.write(sequence[i][
                    number_of_80_bp_rows * line_length:number_of_80_bp_rows * line_length + bases_in_final_row + 1] + "\n")
        f.close()