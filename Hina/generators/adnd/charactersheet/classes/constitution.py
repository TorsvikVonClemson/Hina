def roll(con):
    mod=[]
    if con==1:
        mod.append("-3")
        mod.append("25%")
        mod.append("30%")
        mod.append("-2")
        mod.append("nil")
    elif con==2:
        mod.append("-2")
        mod.append("30%")
        mod.append("35%")
        mod.append("-1")
        mod.append("nil")
    elif con==3:
        mod.append("-2")
        mod.append("35%")
        mod.append("40%")
        mod.append("0")
        mod.append("nil")
    elif con==4:
        mod.append("-1")
        mod.append("40%")
        mod.append("45%")
        mod.append("0")
        mod.append("nil")
    elif con==5:
        mod.append("-1")
        mod.append("45%")
        mod.append("50%")
        mod.append("0")
        mod.append("nil")
    elif con==6:
        mod.append("-1")
        mod.append("50%")
        mod.append("55%")
        mod.append("0")
        mod.append("nil")
    elif con==7:
        mod.append("0")
        mod.append("55%")
        mod.append("60%")
        mod.append("0")
        mod.append("nil")
    elif con==8:
        mod.append("0")
        mod.append("60%")
        mod.append("65%")
        mod.append("0")
        mod.append("nil")
    elif con==9:
        mod.append("0")
        mod.append("65%")
        mod.append("70%")
        mod.append("0")
        mod.append("nil")
    elif con==10:
        mod.append("0")
        mod.append("70%")
        mod.append("75%")
        mod.append("0")
        mod.append("nil")
    elif con==11:
        mod.append("0")
        mod.append("75%")
        mod.append("80%")
        mod.append("0")
        mod.append("nil")
    elif con==12:
        mod.append("0")
        mod.append("80%")
        mod.append("85%")
        mod.append("0")
        mod.append("nil")
    elif con==13:
        mod.append("0")
        mod.append("85%")
        mod.append("90%")
        mod.append("0")
        mod.append("nil")
    elif con==14:
        mod.append("0")
        mod.append("88%")
        mod.append("92%")
        mod.append("0")
        mod.append("nil")
    elif con==15:
        mod.append("+1")
        mod.append("90%")
        mod.append("94%")
        mod.append("0")
        mod.append("nil")
    elif con==16:
        mod.append("+2")
        mod.append("95%")
        mod.append("96%")
        mod.append("0")
        mod.append("nil")
    elif con==17:
        mod.append("+2(+3)")
        mod.append("97%")
        mod.append("98%")
        mod.append("0")
        mod.append("nil")
    elif con==18:
        mod.append("+2(+4)")
        mod.append("99%")
        mod.append("100%")
        mod.append("0")
        mod.append("nil")
    elif con==19:
        mod.append("+2(+5)")
        mod.append("99%")
        mod.append("100%")
        mod.append("1")
        mod.append("nil")
    elif con==20:
        mod.append("+2(+5)**")
        mod.append("99%")
        mod.append("100%")
        mod.append("+1")
        mod.append("1/6")
    elif con==21:
        mod.append("+2(+6)***")
        mod.append("99%")
        mod.append("100%")
        mod.append("+2")
        mod.append("1/5")
    elif con==22:
        mod.append("+2(+6)***")
        mod.append("99%")
        mod.append("100%")
        mod.append("+2")
        mod.append("1/4")
    elif con==23:
        mod.append("+2(+6)****")
        mod.append("99%")
        mod.append("100%")
        mod.append("+3")
        mod.append("1/3")
    elif con==24:
        mod.append("+2(+7)****")
        mod.append("99%")
        mod.append("100%")
        mod.append("+3")
        mod.append("1/2")
    elif con==25:
        mod.append("+2(+7)****")
        mod.append("100%")
        mod.append("100%")
        mod.append("+4")
        mod.append("1")
    return mod
