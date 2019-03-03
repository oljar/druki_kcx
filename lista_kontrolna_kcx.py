# -*- coding: utf-8 -*-
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, inch
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle,Paragraph
#from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.styles import getSampleStyleSheet


pdfmetrics.registerFont(TTFont('DejaMono', 'DejaVuSansMono.ttf'))



doc = SimpleDocTemplate("simple_table_grid1.pdf", pagesize=A4 )

styleSheet = getSampleStyleSheet()

style = styleSheet['BodyText']
P=Paragraph('This is a very silly example',style)

elements = []

data= [['Nagłówek','','',''],
       ['10', '11', '12', '13', '14'],
       ['20', '21', '22', '23', '24'],
       ['30', '31', '32', '33', '34']]
t=Table(data,5*[1*inch], 4*[1*inch])
t.setStyle(TableStyle([('ALIGN',(0,0),(-2,-2),'CENTER'),
                       ('TEXTCOLOR',(1,1),(-2,-2),colors.red),
                       ('VALIGN',(0,0),(0,-1),'TOP'),
                       ('TEXTCOLOR',(0,0),(0,-1),colors.blue),
                       ('ALIGN',(0,-1),(-1,-1),'CENTER'),
                       ('VALIGN',(0,0),(-1,-1),'MIDDLE'),
                       ('TEXTCOLOR',(0,-1),(-1,-1),colors.green),
                       ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
                       ('BOX', (0,0), (-1,-1), 0.25, colors.black),
                       ('SPAN',(0,0),(-1,0)),
                       ('FONT',(0,0),(-1,-1),'DejaMono'),
                       ]))

t._argH[1]=1.5*inch
elements.append(t)
# write the document to disk
doc.build(elements)