#ifndef RFIDTag_h
#define RFIDTag_h


class RFIDTag{
  public:
    RFIDTag(int array[]);
    int getID(int i);
	void setID(int i,int id);
  private:
	int rfidTag[4] = {0,0,0,0};
};

#endif