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

data= [['Logo','','Montaż aparatów KCX            ZP3 SKOWARCZ' ],
       ['','','Lista kontrolna czynnoŚci sprawdzających KCX'],
       ['Lp', 'Operacja', 'Lp', 'Wytyczne', 'Ocena'],
       ['1', '10', '1.1', '12','13'],
       ['' , '', '1.2', '22', '23'],
       ['', '' , '1.3', '32', '33'],
       ['', '', '1.4', '43', '44'],
       ['', '', '1.5', '53', '54'],

       ]



t=Table(data,4*[1.3*inch], 8*[0.3*inch])
t.setStyle(TableStyle([('ALIGN',(0,0),(-2,-2),'CENTER'),

                       #('VALIGN',(0,0),(0,-1),'TOP'),
                       #('TEXTCOLOR',(0,0),(0,-1),colors.blue),
                       ('ALIGN',(0,0),(-1,-1),'CENTER'),
                       ('VALIGN',(0,0),(-1,-1),'MIDDLE'),
                       #('TEXTCOLOR',(0,-1),(-1,-1),colors.green),
                       ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
                       ('BOX', (0,0), (-1,-1), 0.25, colors.black),
                       ('SPAN',(3,0),(4,0)),
                       ('SPAN',(2,1),(4,1)),
                       ('SPAN',(2,0),(4,0)),
                       ('SPAN',(0,0),(1,1)),
                       ('SPAN',(0,3),(0,7)),
                       ('SPAN',(1,3),(1,7)),
                       ('FONT',(0,0),(-1,-1),'DejaMono'),
                       ('FONTSIZE',(2,1),(2,4),12),
                       ('FONTSIZE',(2,0),(2,4),10),

                       ]))

t._argW[0]=0.5*inch
t._argW[1] = 1.5*inch
t._argW[2] = 0.5*inch
t._argW[3] = 3*inch
t._argW[4] = 1.5*inch
t._argH[1]=0.5*inch
elements.append(t)
# write the document to disk
doc.build(elements)