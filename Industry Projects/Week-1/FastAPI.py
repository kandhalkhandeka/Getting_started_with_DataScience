import json
from pathlib import Path

import fastapi
import uvicorn
import typing
from fastapi import FastAPI, File, UploadFile
from borb.pdf.document import Document
from borb.pdf.pdf import PDF
from borb.toolkit.text.simple_text_extraction import SimpleTextExtraction



app = FastAPI()

pdf_file =''

@app.get('/')
def home(): 
    return {'Data' : 'HELLO!'}


@app.post('/Total-amount-extractor/{file}')




def main(file):
    f=open("xyz.txt","w")
    d: typing.Optional[Document] = None
    l: SimpleTextExtraction = SimpleTextExtraction()
    with open(file, "rb") as pdf_in_handle:
        d = PDF.loads(pdf_in_handle, [l])


    assert d is not None
    f.write(l.get_text_for_page(0))


    if __name__ == "__main__":
        main()
    f.close()


    with open('xyz.txt') as f:
        contents = f.read()


    import re

    result = re.findall(r"[-+]?\d*\.\d+", contents)
#print(result)

    Total_amount= max(result,key=lambda x:float(x))
    print("Total Amount:",Total_amount)  
#Total_amount=max(list1)

    return({"Data" : [file,Total_amount]})



