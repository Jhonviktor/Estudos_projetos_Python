from reportlab.pdfgen import canvas

def GeneratePDF(Lista):
    try:
        nome_pdf = input("Infome o nome do PDF: ")
        pdf = canvas.Canvas('{}.pdf'.format(nome_pdf))
        x = 720
        for nome, idade in lista.items():
            x -= 20
            pdf.drawString(247,x, '{} : {}'.format(nome,idade))
        pdf.setTitle(nome_pdf)
        pdf.setFont('Melvetica-Oblique', 14)
        pdf.drawString(245,270, 'Lista de Clientes')
        pdf.setFont('Melvetica-Bold', 12)
        pdf.drawString(245,724, 'Nome e Idade')
        pdf.Save()
        print('{}.pdf criado com sucesso!'.format(nome_pdf))
    except:
        print('Erro ao gerar {}.pdf'.format(nome_pdf))
lista = {'Felipe': '24','Jose':'42','Maria':'22','Eduardo':'31'}

GeneratePDF(lista)        
