#攝氏溫度轉換成華氏溫度
#讓使用者輸入攝氏溫度，最後顯示華氏溫度

flo_Cel = float(input('請輸入攝氏溫度: '))
flo_Fah = flo_Cel * 9 / 5 + 32
print('華氏溫度: ', flo_Fah)