import PyPDF2
import os
pdf_list=["1.pdf","2.pdf","3.pdf"]
merger=PyPDF2.PdfMerger()
for pdf in pdf_list:
    if os.path.exists(pdf):
        merger.append(pdf)
    else:
        print(f"{pdf}  bulunmadı")
    

merger.write("birleSik.pdf")
    
merger.close()   
