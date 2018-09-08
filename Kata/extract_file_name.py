class FileNameExtractor:
    
	#Inputs:
	#1231231223123131_FILE_NAME.EXTENSION.OTHEREXTENSION
	#1_This_is_an_otherExample.mpg.OTHEREXTENSIONadasdassdassds34
	#1231231223123131_myFile.tar.gz2

	#Outputs
	#FILE_NAME.EXTENSION
	#This_is_an_otherExample.mpg
	#myFile.tar
	
	
	
	
	def extract_file_name(dirty_file_name):
        split_name = dirty_file_name.split(".")
        ignore_last_extension = split_name[:-1]
        file_name = ignore_last_extension[0].split("_",1)[1]
        extension = ignore_last_extension[1]

        return file_name + "." + extension