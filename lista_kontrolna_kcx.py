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
       ['1', 'Kontrola wizualna', '1.1', 'Identyfikacja, naklejka z nr. fab ','13'],
       ['' , '', '1.2', 'Tab. znaminowa, inne nalepki', '23'],
       ['', '' , '1.3', 'Tab. klasa energetyczna, ozn króćów', '33'],
       ['', '', '1.4', 'Estetyka, silikonowanie, rysy ', '44'],
       ['', '', '1.5', 'Kapturki srub NW, znaczki uziemień', '54'],
       ['', '', '1.6', 'Izolacja, uszczelki', '64'],
       ['', '', '1.7', 'Filtry', '74'],
       ['', '', '1.8', 'Wanna-szczelność-silikon-malowanie', '84'],
       ['2', 'Próby ruchowe', '2.1', 'Bypass-montaż-działanie-szczelność', '94'],
       ['', '', '2.2', 'Wentylatory-montaż-działanie', '104'],
       ['', '', '2.3', 'Czujniki temperatur-montaż-działanie', '105'],
       ['', '', '2.4', 'Montaż rozdzielnicy-wpięcie płytki ', '106'],
       ['', '', '2.5', 'Nagrzewnica-montaż-działanie-alarm', '107'],
       ['', '', '2.6', 'Drzwi-zamki-mntaż-oznacznia-rączki', '108'],
       ['', '', '2.7', 'Wydatek', '109'],
       ['', '', '2.8', 'Szczelność', '110'],
       ['3', 'Kompletacja', '3.1', 'Osłona rozdzielnicy-znak ostrzegawczy' , '109'],
       ['', '', '3.2', 'DTRka, karta produktu' , '110'],
       ['', '', '3.3', 'Oznaczenie KJ' , '112'],
       ['4', 'Uwagi', '', '' , '113'],
       ['5', 'Nr zlecenia', '', '' , ''],
       ['',  'Nr seryjny', '', '' , ''],
       ['',  'Typ urządzenia', '', '' , ''],
       ['',  'Data badania KJ', '', '' , ''],
       ['',  'Kontroler KJ', '', '' , ''],
       ['6',  'Ocena końcowa', '', '' , ''],


       ]



t=Table(data,4*[1.3*inch], 29*[0.3*inch])
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
                       ('SPAN',(0,3),(0,10)),#
                       ('SPAN',(1,3),(1,10)),#
                       ('SPAN',(0,11),(0,18)),#
                       ('SPAN',(1,11),(1,18)),#
                       ('SPAN',(0,19),(0,21)),#
                       ('SPAN',(1,19),(1,21)),#
                       ('SPAN',(2,22),(3,22)),
                       ('SPAN',(2,23),(4,23)),
                       ('SPAN',(0,23),(0,27)),
                       ('SPAN',(2,24),(4,24)),
                       ('SPAN',(2,25),(4,25)),
                       ('SPAN',(2,26),(4,26)),
                       ('SPAN',(2,27),(4,27)),
                       ('SPAN',(2,28),(4,28)),
                       ('SPAN',(2,29),(4,29)),
                       ('FONT',(0,0),(-1,-1),'DejaMono'),
                       ('FONTSIZE',(2,1),(2,4),12),
                       ('FONTSIZE',(2,0),(2,4),10),

                       ]))

t._argW[0]=0.5*inch
t._argW[1] = 1.5*inch
t._argW[2] = 0.5*inch
t._argW[3] = 3.2*inch
t._argW[4] = 1.*inch
t._argH[1]=0.4*inch
t._argH[22]=0.5*inch
t._argH[28]=0.5*inch
elements.append(t)
# write the document to disk
doc.build(elements)