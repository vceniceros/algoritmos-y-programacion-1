def leer_info(ejs, default):
   linea = ejs.readline()
   return linea.rstrip().split(',') if linea else default.split(',')

max = "999999"
ultimo = max+",0"

movsbane = open("../data/MoviBANE.csv", 'rt')
movshb = open("../data/MoviHB.csv", 'rt')
movssuc = open("../data/MoviSUC.csv", 'rt')

bane_cta, bane_importe = leer_info(movsbane, ultimo)
hb_cta, hb_importe = leer_info(movshb, ultimo)
suc_cta, suc_importe = leer_info(movssuc, ultimo)

total_gral = 0
while bane_cta != max or hb_cta != max or suc_cta != max:
    tot_cta = 0
    men = min(hb_cta, bane_cta, suc_cta) # min es una función de python
    print('cta:', men)
    while bane_cta == men:
        tot_cta += float(bane_importe)
        bane_cta, bane_importe = leer_info(movsbane, ultimo)
    while hb_cta == men:
        tot_cta += float(hb_importe)
        hb_cta, hb_importe = leer_info(movshb, ultimo)
    while suc_cta == men:
        tot_cta += float(suc_importe)
        suc_cta, suc_importe = leer_info(movssuc, ultimo)
    print('Total por cta.:', tot_cta)
    total_gral += tot_cta
print('Total gral.:', total_gral)

movsbane.close()
movshb.close()
movssuc.close() 