# -*- coding: utf-8 -*-

import curses

dogdance1=[[
' ▄','▄','▄', #3
'▄▄▄▄','▄','▄', #6
'▄'],[' ',' ', #9
'        ',  '▄','▄'],#12
[' ','  ' , '▄',#15
'  ','▄','    ',#18
'▄▄',  '▄▄     '],[ ' ',#21
' ','▄',' ',#24
' ','▄',' ',#27
'▄',  '       ','▄▄▄▄▄▄',#30
'▄'],[' ','  ',#33
'▄▄▄▄','            ',' ',#36
'▀'],[' ','                  ',#39
' '],[' ','                 ', #42
'▄',  '▀'],[' ',#45
' ','  ','▄▄  ▄▄▄▄  ▄▄  ', #48
' '],[' ',  ' ',#51
' ','▄','▀▀',#54
'▄','▀','   ▀',#57
'▄',  '▀',' ',#60
' ',  ' ','▄',#63
'▀'],['  ','▀             ▀']]#66

dog1pallete=[
        [1,3,1, #3
        3,1,3,#6
        1],[1,3,#9
        2,3,1], #12
        [4,2,3, #15
        2,3,2, #18
        3,1],[4, #21
        2,2,2, #24
        4,3,2, #27
        2,2,3, #30
        1],[4,2, #33
        3,2,4, #36
        1],[4,2, #39
        4],[4,2, #42
        2,1],[1, #45
        4,2,2, #48
        4],[1,4, #51
        2,2,1, #54
        2,1,1, #57
        2,1,1, #60
        4,2,2, #63
        1],[1,1]] #6

dogdance2=[[
' ▄','▄','▄', #3
'▄▄▄▄','▄','▄',#6
'▄'],[' ',' ',#9
'        ','▄','▄'],[ #12
' ',' ',' ', #15
'▄','  ','▄',#18
'    ','▄▄','▄▄', #21
'  ','▄','▄', #24
'▄'],[' ',' ', #27
'▄',' ',' ▄', #30
' ▄      ',' ','▄▄▄', #33
' ',' ','   '],[' ', #36
'  ','▄▄▄▄','            ', #39
' ',' '],[' ','                  ',#42
' '],[' ','                 ▄', #45
'▀'],[' ',' ', #48
'  ▄▄  ▄▄▄▄  ▄▄  ',' '],[' ', #51
'▀','▄','▀', #54
' ',' ',' ▄', #57
'▀  ',' ',' ▄', #60
'▀▀','▄','▀ '],[ #63
'      ▀     ▀    ']]#64
dog2pallete=[[1,3,1, #3
        3,1,3, #6
        1],[1,3, #9
        2,3,1],[ #12
        4,2,2, #15
        3,2,3, #18
        2,3,1, #21
        1,1,3, #24
        1],[4,2, #27
        2,2,3, #30
        2,2,3, #33
        2,3,1],[3, #36
        2,3,2, #39
        3,1],[3,2, #42
        3],[3,2, #45
        1],[1,3, #48
        2,3],[1, #51
        1,2,1, #54
        1,3,2, #57
        1,3,2, #60
        1,2,1],[ #63
        1]] #64

def draw_dog1(scr,posx,posy):
    i = 0
    width = posx
    for code,num in zip(dogdance1,dog1pallete):
        for st,pair in zip(code,num):
            scr.addstr(posy,width,st,curses.color_pair(pair))
            width=width+(len(st.decode('utf-8')))
        posy=posy+1
        width=posx

def draw_dog2(scr,posx,posy):
    i = 0
    width = posx
    for code,num in zip(dogdance2,dog2pallete):
        for st,pair in zip(code,num):
            scr.addstr(posy,width,st,curses.color_pair(pair))
            width=width+(len(st.decode('utf-8')))
        posy=posy+1
        width=posx

#def main():
#    i = 1
#    for code,num in zip(dogdance2,dog2pallete):
#        for st,pair in zip(code,num):
#            #print st
#            print len(st.decode('utf-8'))
#            #i = i + 1
#        #print "-------------------"
#        #print len(code),len(num)
#
#if __name__ == "__main__":
#    main()
