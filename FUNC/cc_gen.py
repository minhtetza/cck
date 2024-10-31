import traceback
def checkLuhn(cardNo):
    try:
        nDigits = len(cardNo)
        nSum = 0
        isSecond = False
        for i in range(nDigits - 1, -1, -1):
            d = ord(cardNo[i]) - ord('0')
            if (isSecond == True):
                d = d * 2
            nSum += d // 10
            nSum += d % 10
            isSecond = not isSecond
        if (nSum % 10 == 0):
            return "pass"
        else:
            return "fail"
    except Exception as e:
        tb = traceback.format_exc()
        with open("error_logs.txt", "a") as f:
            f.write(tb + "\n")


def cc_gen(total):
    try:
        cc = total[0]
        mes = total[1]
        ano = total[2]
        cvv = total[3]
        if mes != "x" and len(mes) == 1:
            mes = "0" + mes

        if ano != "x" and len(ano) == 2:
            ano = "20" + ano
        import random
        amount = 1
        genrated = 0
        while (genrated < amount):
            genrated += 1
            s = "0123456789"
            l = list(s)
            random.shuffle(l)
            result = ''.join(l)
            result = cc + result
            if cc[0] == "3":
                ccgen = result[0:15]
            else:
                ccgen = result[0:16]
            if mes == 'x':
                mesgen = random.randint(1, 12)
                if len(str(mesgen)) == 1:
                    mesgen = "0" + str(mesgen)
            else:
                mesgen = mes
            if ano == 'x':
                anogen = random.randint(2024, 2035)
            else:
                anogen = ano
            if cvv == 'x':
                if cc[0] == "3":
                    cvvgen = random.randint(1000, 9999)
                else:
                    cvvgen = random.randint(100, 999)
            else:
                cvvgen = cvv
            if (ccgen, mesgen, anogen, cvvgen):
                lista = f"{ccgen}|{mesgen}|{anogen}|{cvvgen}"

        return lista
    except Exception as e:
        tb = traceback.format_exc()
        with open("error_logs.txt", "a") as f:
            f.write(tb + "\n")


def luhnccgen(total,amt):
    try:
        allcc = ""
        for i in range(amt):
            while True:
                gen = cc_gen(total)
                split = gen.split("|")
                cc = split[0]
                if checkLuhn(cc) == "fail":
                    continue
                else:
                    allcc += f"{gen}\n"
                    break
        return allcc
    except Exception as e:
        tb = traceback.format_exc()
        with open("error_logs.txt", "a") as f:
            f.write(tb + "\n")

def ccgen_amt(total):
    try:
        allcc = ""
        for i in range(15):
            gennned = luhnccgen(total)
            allcc += f"{gennned}\n"
        return allcc
    except Exception as e:
        tb = traceback.format_exc()
        with open("error_logs.txt", "a") as f:
            f.write(tb + "\n")