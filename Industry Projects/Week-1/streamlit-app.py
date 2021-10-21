import streamlit as st
import streamlit.components.v1 as stc
from PIL import Image











img = Image.open('pic.png')

st.image(img, width = 200)

st.title('Invoice Data Extractor')
st.markdown("""
This app extracts the total amount data from any kind of invoice!

""")

import typing
from borb.pdf.document import Document
from borb.pdf.pdf import PDF
from borb.toolkit.text.simple_text_extraction import SimpleTextExtraction


st.header("Document Files")
pdf_file = st.file_uploader("Upload Document", type=["pdf"])
kk=st.button("Process")
@st.cache		



#if pdf_file is not None:
         
         
def main(pdf_file):
    f=open("xyz.txt","w")
    d: typing.Optional[Document] = None
    l: SimpleTextExtraction = SimpleTextExtraction()
    with open(pdf_file, "r") as pdf_in_handle:
        d = PDF.loads(pdf_in_handle, [l])
        stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))


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
            
            return Total_amount 
    

if kk==True:
    Total_amount=main(pdf_file)
    st.write(Total_amount)





   
