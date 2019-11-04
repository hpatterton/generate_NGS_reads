from class_FastA import FastA
from class_FastQ import FastQ
from class_Convert_Sequence import ConvertSequence

if __name__ == "__main__":
	
	# Enter the full path to the fasta format file that you want to use to generate
	# randomly positioned NGS reads
	
	input_filename = "C:\\Users\\hpatterton\\Downloads\\S288C_reference_genome_Current_Release\\S288C_reference_genome_R64-2-1_20150113\\S288C_reference_sequence_R64-chromosome_names.fasta"
	
	# Enter the other read parameters: 	minimum NGS read length
	#									maximum NGS read length
	#									sequence depth
	
	minimum_read_length = 100
	maximum_read_length = 100
	sequence_depth = 1
	
	input_file = FastA()
	number_of_sequences = input_file.ReadFastA(input_filename)
	print("sequences =",number_of_sequences)
	convert_sequence = ConvertSequence()
	path,*remainder = input_filename.rpartition('\\')
	for index,sequence in enumerate(input_file):
		list_of_fragments = convert_sequence.GenerateSequenceReadFragments(sequence,minimum_read_length,maximum_read_length,sequence_depth)
		list_of_names = []
		for i in range(0,len(list_of_fragments)):
			list_of_names.append(input_file.GetContigName(index)+'_'+str(i))
		out_file = input_file.GetContigName(index)
		out_file = path + '\\' + out_file + '.fastq'
		output_file = FastQ()
		output_file.WriteFastQ(out_file, list_of_names, list_of_fragments, len(list_of_fragments), quality='')
		print('written '+str(len(list_of_fragments))+' sequences to',out_file)
		