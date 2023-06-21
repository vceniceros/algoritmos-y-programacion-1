
def leer_info(ejs, default):
    linea = ejs.readline()
    return linea.rstrip().split(',') if linea else default

FIN = 'fin'
ultimo = [FIN, "0"]

movsbane = open("../data/MoviBANE.csv","rt")
movshb = open("../data/MoviHB.csv","rt")
movssuc = open("../data/MoviSUC.csv","rt")

movstotal = open("../data/MoviTOT.csv", "wt")

bane_cta, bane_importe = leer_info(movsbane, ultimo)
hb_cta, hb_importe = leer_info(movshb, ultimo)
suc_cta, suc_importe = leer_info(movssuc, ultimo)

total = 0
while bane_cta != FIN or hb_cta != FIN or suc_cta != FIN:
    tot_cta = 0
    men = min(hb_cta, bane_cta, suc_cta)  # min es una función de python
    print('cta:', men)
    while bane_cta == men and bane_cta != FIN:
        tot_cta += float(bane_importe)
        bane_cta, bane_importe = leer_info(movsbane, ultimo)
    while hb_cta == men and hb_cta != FIN:
        tot_cta += float(hb_importe)
        hb_cta, hb_importe = leer_info(movshb, ultimo)
    while suc_cta == men and suc_cta != FIN:
        tot_cta += float(suc_importe)
        suc_cta, suc_importe = leer_info(movssuc, ultimo)
    print ('Total por cta.:', tot_cta)
    movstotal.write("{},{}\n".format(men, str(tot_cta)))
    total += tot_cta
print ('Total gral.:', total)

movsbane.close()
movshb.close()
movssuc.close()
movstotal.close()

