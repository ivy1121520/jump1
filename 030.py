# -*- coding: utf8 -*-
import turtle               # 匯入turtle套件，允許我們使用turtle指令
window = turtle.Screen()        # 產生畫布以進行畫圖
window.bgcolor("lightgreen")# 設定畫布底色為淺綠色

marry = turtle.Turtle()         # 建立一個海龜turtle，它的名字叫marry
marry.color("hotpink")          # 設定畫筆顏色為粉紅色
marry.pensize(5)                        # 設定畫筆粗細為5個像素

def j(t,size):
    for i in range(4):
        t.forward(size)
        t.left(90)

for i in range(5):
    j(marry,50)
    marry.penup()
    marry.forward(100)
    marry.pendown()

window.exitonclick()                    # 等待使用者關閉視窗    # 等待使用者關閉
