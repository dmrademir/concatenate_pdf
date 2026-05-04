from PyPDF2 import PdfWriter

merger = PdfWriter()

# Lista de arquivos que você quer juntar
arquivos = ["document1.pdf", "document2.pdf", "document3.pdf"]
capa = "capa_intermediaria.pdf"

for pdf in arquivos:
    # Adiciona o document principal
    merger.append(pdf)
    # Adiciona a capa logo após (exceto talvez no último, se desejar)
    merger.append(capa)

with open("resultado_final.pdf", "wb") as f:
    merger.write(f)

merger.close()

