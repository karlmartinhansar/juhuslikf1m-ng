import random

def funktsiooninimi(vahemik):
    aeg = round(random.uniform(vahemik[0], vahemik[1]), 3)
    return aeg

print(funktsiooninimi([47, 59]))



nimekiri = ["Lewis", "Valtteri", "Max", "George", "Karl"]
ajad = []

for nimi in nimekiri:
    sekt1 = funktsiooninimi([23, 26])
    sekt2 = funktsiooninimi([23, 26])
    sekt3 = funktsiooninimi([23, 26])
    ajad.append([nimi, sekt1, sekt2, sekt3])

for aeg in ajad:
    print(aeg[0], aeg[1], aeg[2], aeg[3])


for aeg in ajad:
    print(f"{aeg[0]:<10} {aeg[1]} {aeg[2]} {aeg[3]}")


print(f"{'Nimi':<10} {'Aeg':<10} {'S1':<10} {'S2':<10} {'S3':<10}")
for aeg in ajad:
    aeg_summa = sum(aeg[1:])
    print(f"{aeg[0]:<10} {aeg_summa:<10.3f} {aeg[1]:<10.3f} {aeg[2]:<10.3f} {aeg[3]:<10.3f}")


def aja_vormindamine(aeg):
    tund = int(aeg / 3600)
    minut = int((aeg % 3600) / 60)
    sekund = int(aeg % 60)
    tuhanded = int((aeg % 1) * 1000)
    return f"{tund:02d}:{minut:02d}:{sekund:02d}.{tuhanded:03d}"

print(f"{'Nimi':<10} {'Aeg':<15} {'S1':<10} {'S2':<10} {'S3':<10}")
for aeg in ajad:
    aeg_summa = sum(aeg[1:])
    aeg_formatted = aja_vormindamine(aeg_summa)
    print(f"{aeg[0]:<10} {aeg_formatted:<15} {aeg[1]:<10.3f} {aeg[2]:<10.3f} {aeg[3]:<10.3f}")


ajad_sorted = sorted(ajad, key=lambda x: x[1])

for aeg in ajad_sorted:
    aeg_summa = sum(aeg[1:])
    aeg_formatted = aja_vormindamine(aeg_summa)
    print(f"{aeg[0]:<10} {aeg_formatted} {aeg_summa:<10.3f}")



def voi_aeg():
    aegade_summa = 0
    for i in range(10):
        aeg = funktsiooninimi([23, 26])
        aegade_summa += aeg
    return aegade_summa

print(aja_vormindamine(voi_aeg()))



ringid = 10
sonum = []

for nimi in nimekiri:
    ajad_summa = 0
    ringide_vigade_nimekiri = []
    for i in range(ringid):
        viga = ""
        if random.randint(0, 9) == 2:
            sekt1 = funktsiooninimi([30, 90])
            sekt2 = funktsiooninimi([30, 90])
            sekt3 = funktsiooninimi([30, 90])
            viga = "Jah"
        else:
            sekt1 = funktsiooninimi([23, 26])
            sekt2 = funktsiooninimi([23, 26])
            sekt3 = funktsiooninimi([23, 26])
        ringi_aeg = sekt1 + sekt2 + sekt3
        ajad_summa += ringi_aeg
        if viga:
            ringide_vigade_nimekiri.append(i+1)
    sonum.append([nimi, ajad_summa, ringide_vigade_nimekiri])

sonum_sorted = sorted(sonum, key=lambda x: x[1])

print(f"{'Nimi':<10} {'Koguaeg':<15} {'Vead':<10}")
for s in sonum_sorted:
    nimi = s[0]
    aeg_formatted = aja_vormindamine(s[1])
    vead_formatted = str(s[2])
    print(f"{nimi:<10} {aeg_formatted:<15} {vead_formatted:<10}")



ringid = 10
sonum = []

for nimi in nimekiri:
    ajad_summa = 0
    ringide_vigade_nimekiri = []
    for i in range(ringid):
        viga = ""
        if random.randint(0, 9) == 2:
            sekt1 = funktsiooninimi([30, 90])
            sekt2 = funktsiooninimi([30, 90])
            sekt3 = funktsiooninimi([30, 90])
            viga = "Jah"
        else:
            sekt1 = funktsiooninimi([23, 26])
            sekt2 = funktsiooninimi([23, 26])
            sekt3 = funktsiooninimi([23, 26])
        ringi_aeg = sekt1 + sekt2 + sekt3
        ajad_summa += ringi_aeg
        if viga:
            ringide_vigade_nimekiri.append(i+1)
    sonum.append([nimi, ajad_summa, ringide_vigade_nimekiri])

sonum_sorted = sorted(sonum, key=lambda x: x[1])

for i, s in enumerate(sonum_sorted):
    if i == 0:
        aeg_base = s[1]
    vahe_formatted = aja_vormindamine(s[1] - aeg_base)
    nimi = s[0]
    aeg_formatted = aja_vormindamine(s[1])
    vead_formatted = str(s[2])
    print(f"{nimi:<10} {aeg_formatted:<15} {vahe_formatted} {vead_formatted:<10}")



ringid = 10
sonum = []

for nimi in nimekiri:
    ajad_summa = 0
    ringide_vigade_nimekiri = []
    for i in range(ringid):
        viga = ""
        if random.randint(0, 9) == 2:
            sekt1 = funktsiooninimi([30, 90])
            sekt2 = funktsiooninimi([30, 90])
            sekt3 = funktsiooninimi([30, 90])
            viga = "Jah"
        else:
            sekt1 = funktsiooninimi([23, 26])
            sekt2 = funktsiooninimi([23, 26])
            sekt3 = funktsiooninimi([23, 26])
        ringi_aeg = sekt1 + sekt2 + sekt3
        ajad_summa += ringi_aeg
        if viga:
            ringide_vigade_nimekiri.append(i+1)
    sonum.append([nimi, ajad_summa, ringide_vigade_nimekiri])

sonum_sorted = sorted(sonum, key=lambda x: x[1])

for i, s in enumerate(sonum_sorted):
    ringid_formatted = str(s[2])
    if ringid_formatted == "[]":
        ringid_formatted = ""
    else:
        ringid_formatted = ringid_formatted[1:-1]
    nimi = s[0]
    aeg_formatted = aja_vormindamine(s[1])
    print(f"{nimi:<10} {aeg_formatted:<15} {ringid_formatted}")


ringid = 10
sonum = []

for nimi in nimekiri:
    ajad_summa = 0
    ringide_vigade_nimekiri = []
    for i in range(ringid):
        viga = ""
        if random.randint(0, 9) == 2:
            sekt1 = funktsiooninimi([30, 90])
            sekt2 = funktsiooninimi([30, 90])
            sekt3 = funktsiooninimi([30, 90])
            viga = "Jah"
        else:
            sekt1 = funktsiooninimi([23, 26])
            sekt2 = funktsiooninimi([23, 26])
            sekt3 = funktsiooninimi([23, 26])
        ringi_aeg = sekt1 + sekt2 + sekt3
        ajad_summa += ringi_aeg
        if viga:
            ringide_vigade_nimekiri.append(i+1)
    sonum.append([nimi, ajad_summa, ringide_vigade_nimekiri])

sonum_sorted = sorted(sonum, key=lambda x: x[1])

for i, s in enumerate(sonum_sorted):
    ringid_formatted = str(s[2])
    if ringid_formatted == "[]":
        ringid_formatted = ""
    else:
        ringid_formatted = ringid_formatted[1:-1]
    nimi = s[0]
    aeg_formatted = aja_vormindamine(s[1])
    if i == 0:
        vahe_formatted = ""
    else:
        vahe_formatted = aja_vormindamine


ajad_sorted = sorted(ajad, key=lambda x: x[1])
sonum_sorted = sorted(sonum, key=lambda x: x[1])

def save_results_to_file(ajad_sorted, sonum_sorted):
    with open("Result.txt", "w") as f:
        f.write("Kokkuvõte\n\n")
        f.write("Ajavahe tabel:\n")
        f.write(f"{'Nimi':<10} {'Koguaeg':<15} {'Vahe':<15} {'Vea ringid':<10}\n")
        for i, s in enumerate(ajad_sorted):
            vahe_formatted = aja_vormindamine(s[1] - ajad_sorted[0][1]) if i != 0 else ""
            vead_formatted = str(s[2]) if s[2] else ""
            f.write(f"{s[0]:<10} {aja_vormindamine(s[1]):<15} {vahe_formatted:<15} {vead_formatted:<10}\n")
        f.write("\nRingide tabel:\n")
        f.write(f"{'Nimi':<10} {'Koguaeg':<15} {'Vea ringid':<25}\n")
        for s in sonum_sorted:
            ringid_formatted = str(s[2])[1:-1] if s[2] else ""
            f.write(f"{s[0]:<10} {aja_vormindamine(s[1]):<15} {ringid_formatted:<25}\n")

    print("Tulemused salvestatud faili Result.txt")

save_results_to_file(sonum_sorted, ajad_sorted)