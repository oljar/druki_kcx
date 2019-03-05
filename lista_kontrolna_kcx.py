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

data= [['Nagłówek 1','','',''],
       ['10', '11', '12', '13', '14','15'],
       ['20', '21', '22', '23', '24','16'],
       ['30', '31', '32', '33', '34','24'],
       ['30', '31', '32', '33', '34','24'],]



t=Table(data,5*[1*inch], 5*[0.4*inch])
t.setStyle(TableStyle([('ALIGN',(0,0),(-2,-2),'CENTER'),
                       ('TEXTCOLOR',(1,1),(-2,-2),colors.red),
                       ('VALIGN',(0,0),(0,-1),'TOP'),
                       ('TEXTCOLOR',(0,0),(0,-1),colors.blue),
                       ('ALIGN',(0,-1),(-1,-1),'CENTER'),
                       ('VALIGN',(0,0),(-1,-1),'MIDDLE'),
                       ('TEXTCOLOR',(0,-1),(-1,-1),colors.green),
                       ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
                       ('BOX', (0,0), (-1,-1), 0.25, colors.black),
                       ('SPAN',(0,0),(0,2)),
                       ('SPAN',(1,0),(5,0)),
                       ('FONT',(0,0),(-1,-1),'DejaMono'),
                       ]))

t._argW[0]=2.5*inch
t._argW[1] = 0.5*inch
t._argW[2] = 1*inch
t._argH[0]=1*inch
elements.append(t)
# write the document to disk
doc.build(elements)