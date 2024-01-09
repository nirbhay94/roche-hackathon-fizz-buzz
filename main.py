from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root(int1: Union[int, None] = None,int2: Union[int, None] = None,limit: Union[int, None] = None,str1: Union[str, None] = None,str2: Union[str, None] = None):
    rangeLimit = range(1,limit+1)
    myList = list(rangeLimit)
    for i in rangeLimit:
        # replace int1int2 with str1str2
        if (isMultiple(myList[i-1],int1) and isMultiple(myList[i-1],int2)):
        	myList[i-1] = str1+str2
        	continue

        # replace int1 with str1
        if isMultiple(myList[i-1],int1):
        	myList[i-1] = str1
        	continue

        # replace int2 with str2
        if isMultiple(myList[i-1],int2):
        	myList[i-1] = str2
        	continue

    return ','.join(map(str,myList))

def isMultiple(num,  check_with):
        return num % check_with == 0;

