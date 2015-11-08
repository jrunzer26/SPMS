

#include "RFIDTag.h"

/*
Returns the identification of the tag.
*/
int RFIDTag::getID(int i){
	return rfidTag[i];
}

/*
Chances a part of the identification of the tag
@param i the location of the identification to be replaced
@param id the new identification to replace the old id.
*/
void RFIDTag::setID(int i,int id){
	rfidTag[i] = id;
}

/*
Creates an RFIDTag by initializing the identification.
*/
RFIDTag::RFIDTag(int array[4]){
	
	for(int i = 0; i < 4; i++){
		rfidTag[i] = array[i];
	}
	
}




