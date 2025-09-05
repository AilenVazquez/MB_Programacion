import time

seg = 0
min = 0
hora = 0
    
while seg < 5 and min < 5 and hora < 5 :
    seg += 1
    time.sleep(0.5)
    print(hora,':',min,':',seg)
    
    if seg == 5:
        seg = 0
        min += 1
        
        if min == 5:
            min = 0
            hora += 1
    