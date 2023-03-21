#!/usr/bin/env python

from bs4 import BeautifulSoup as soup
from time import sleep

global bkg_color

print()

ack_state = input('''I do not own any C18s so I only can guarantee 
    (take that word very loosely) this to work on Ruby2 and Topaz. Cool? Answer y or n: ''')

while ack_state != 'y':
    ack_state = input('''I do not own any C18s so I only can guarantee 
    (take that word very loosely) this to work on Ruby2 and Topaz. Cool? Answer y or n: ''')
    print()
    pass

scrn_move = input(
        '''- Did you move the old screencfg&regNum=101 into the folder this script is running from? You can do it now 
        then answer y or n: ''')

while scrn_move != 'y':
    scrn_move = input(
        '''- Did you move the old screencfg&regNum=101 into the folder this script is running from? You can do it now 
        then answer y or n: ''')
    print()
    pass

# Global Btn Counter for ID in 53+
btn_counter = 0
fill_btns = []
func_btns = []

# Start of XML
new_xml = ['''<?xml version="1.0" encoding="UTF-8"?><sc:panelCfg creationDate="2021-06-18T21:48:40-04:00" 
    xmlns:vs="urn:vfi-sapphire:vs.2001-10-01" xmlns:sc="urn:vfi-sapphire:sc.2018-11-29" 
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">''']


# Make Total fill btns for blank spaces
def fill_btn(fill_list):
    # print("Making some fill buttons!")
    global btn_counter, fill_btns
    for x in range(1, 8):
        if x in fill_list:
            pass
        else:
            btn_counter += 1
            btn = '''<functionButton buttonId="{0}"><labelText id="1"/><labelText 
            id="2"/><color>#99CCFF</color><labelColor>#FFFFFF</labelColor><softkeyType>TOT</softkeyType
            ></functionButton>'''.format(
                btn_counter)
            new_xml.append(btn)
            if btn_counter == 63:
                new_xml.append('</itemPanel>')
            # print('fill button for {0}'.format(btn_counter))


def color_convert(color):
    global bkg_color
    if color == '1':
        bkg_color = '#993300'
    elif color == '2':
        bkg_color = '#60ADFF'
    elif color == '3':
        bkg_color = '#00FF00'
    elif color == '4':
        bkg_color = '#CC99FF'
    elif color == '5':
        bkg_color = '#930090'
    elif color == '6':
        bkg_color = '#FFFF00'
    elif color == '8':
        bkg_color = '#999999'
    elif color == '9':
        bkg_color = '#004793'
    elif color == '10':
        bkg_color = '#33CCCC'
    elif color == '11':
        bkg_color = '#008000'
    elif color == '12':
        bkg_color = '#99CCFF'
    elif color == '13':
        bkg_color = '#FFD700'
    elif color == '14':
        bkg_color = '#FFE4C4'
    elif color == '15':
        bkg_color = '#FF6600'
    elif color == '16':
        bkg_color = '#FFB000'
    elif color == '17':
        bkg_color = '#FF0000'
    elif color == '18':
        bkg_color = '#FFFF99'
    elif color == '19':
        bkg_color = '#CCFFCC'
    elif color == '20':
        bkg_color = '#00FFFF'
    elif color == '21':
        bkg_color = '#A13669'
    elif color == '22':
        bkg_color = '#0000FF'
    elif color == '23':
        bkg_color = '#C0C0C0'
    elif color == '24':
        bkg_color = '#00CCFF'
    elif color == '25':
        bkg_color = '#3366FF'
    elif color == '26':
        bkg_color = '#2FFFBE'
    elif color == '27':
        bkg_color = '#00F081'
    else:
        print(" - I don't know what color that is for the color conversion.....")
        sleep(2)


# Convert 51 and lower btns to 53+
def convert_btns():
    print(" - Running main conversion to new Base 53 panelcfg!")
    sleep(2)
    global btn_counter, func_btns, bkg_color
    oldxml = soup(oldfile, 'xml')
    for screen in oldxml.find(name='screencfg').parent.findAll(name='screen'):
        screenId = screen.get('id')
        print(" - Converting screen {screenId}".format(**vars()))
        sleep(2)
        new_xml.append('''<itemPanel name="Screen {0}">'''.format(screenId))
        btn_counter = 0
        if screenId == '1':
            rstart = 3
            rstop = 12
        else:
            rstart = 1
            rstop = 10
        for r in range(rstart, rstop):
            fill_list = []
            for c in range(1, 9):
                if c == 8:
                    fill_btn(fill_list)
                else:
                    for btn in screen.findAll(name='row', string='{r}'.format(**vars())):
                        btnType = btn.parent.parent.name
                        if btnType == 'fuelButton':
                            pass
                        else:
                            try:
                                #row = btn.text
                                #col = btn.find_next_sibling(name='col', text='{c}'.format(**vars())).text
                                fill_list.append(c)
                                text1 = btn.findNext(name='textLine1').text.replace('&', '')
                                text2 = btn.findNext(name='textLine2').text
                                color = btn.findNext(name='clrGrfxCombo_ID').text
                                color_convert(color)
                                lbl_color = '#000000'
                                btn_counter += 1
                                if btnType == 'functionButton':
                                    softkeyType = btn.findNext(name='softkeyType').text
                                    # print(screenId, row, col, btn_counter, btnType, text1, text2, bkg_color, softkeyType)
                                    btn = '''<functionButton buttonId="{0}"><labelText id="1">{1}</labelText><labelText id="2">{2}</labelText><color>{3}</color>
                                    <labelColor>{4}</labelColor><softkeyType>{5}</softkeyType></functionButton>'''.format(
                                        btn_counter, text1, text2, bkg_color, lbl_color, softkeyType)
                                    new_xml.append(btn)
                                elif btnType == 'pluButton':
                                    upc = btn.findNext(name='upc').text
                                    modifier = btn.findNext(name='modifier').text
                                    # print(screenId, row, col, btn_counter, btnType, text1, text2, bkg_color, upc, modifier)
                                    btn = '''<pluButton buttonId="{0}" inactive="false"><labelText id="1">{1}</labelText><labelText id="2">{2}</labelText><color>{3}</color>
                                    <labelColor>{4}</labelColor><vs:pluNum><upc encoding="A">{5}</upc><modifier>{6}</modifier></vs:pluNum></pluButton>'''.format(
                                        btn_counter, text1, text2, bkg_color, lbl_color, upc, modifier)
                                    new_xml.append(btn)
                                elif btnType == 'mopButton':
                                    itemId = btn.findNext(name='itemId').text
                                    # print(screenId, row, col, btn_counter, btnType, text1, text2, bkg_color, itemId)
                                    btn = '''<mopButton buttonId="{0}" inactive="false"><labelText id="1">{1}</labelText><labelText id="2">{2}</labelText><color>{3}</color>
                                    <labelColor>{4}</labelColor><itemId>{5}</itemId></mopButton>'''.format(btn_counter,
                                                                                                           text1, text2,
                                                                                                           bkg_color,
                                                                                                           lbl_color,
                                                                                                           itemId)
                                    new_xml.append(btn)
                                elif btnType == 'depButton':
                                    itemId = btn.findNext(name='itemId').text
                                    # print(screenId, row, col, btn_counter, btnType, text1, text2, bkg_color, itemId)
                                    btn = '''<depButton buttonId="{0}" inactive="false"><labelText id="1">{1}</labelText><labelText id="2">{2}</labelText><color>{3}</color>
                                    <labelColor>{4}</labelColor><itemId>{5}</itemId></depButton>'''.format(btn_counter,
                                                                                                           text1, text2,
                                                                                                           bkg_color,
                                                                                                           lbl_color,
                                                                                                           itemId)
                                    new_xml.append(btn)
                                elif btnType == 'menuButton':
                                    itemId = btn.findNext(name='itemId').text
                                    # print(screenId, row, col, btn_counter, btnType, text1, text2, bkg_color, itemId)
                                    btn = '''<menuButton buttonId="{0}" inactive="false"><labelText id="1">{1}</labelText><labelText id="2">{2}</labelText><color>{3}</color>
                                    <labelColor>{4}</labelColor><itemId>{5}</itemId></menuButton>'''.format(btn_counter,
                                                                                                            text1,
                                                                                                            text2,
                                                                                                            bkg_color,
                                                                                                            lbl_color,
                                                                                                            itemId)
                                    new_xml.append(btn)
                                else:
                                    print(" - Thats a weird button, doesn't equal menu, mop, dept, or plu")
                                    sleep(5)
                                    # itemId = btn.findNext(name='itemId').text
                                    # print(screenId, row, col, btn_counter, btnType, text1, text2, color, itemId)
                                    # btn = ''''''
                                    # new_xml.append(btn)
                                    # btns['btn{screenId}{row}{col}'.format(**vars())] = {'btnType': btnType, 'text1': text1, 'text2': text2, 'color': color, 'itemId': itemId}
                                if btn_counter == 63:
                                    new_xml.append('</itemPanel>')
                            except Exception as e:
                                # print(e)
                                pass


with open("./screencfg&regNum=101.xml", "r") as f:
    oldfile = f.read()
print(" - Reading the old screencfg for Reg101!")
sleep(2)
convert_btns()
new_xml.append('</sc:panelCfg>')
with open("./panelcfg.xml", "w+") as p:
    p.write("".join(new_xml))
print("Done")
sleep(5)
exit()

# print("".join(new_xml))