import random

names = ['Karl', 'Joosep', 'Romet', 'Marius', 'Hendrik'] # sõitjad listis
laps = 10 # võistluse pikkus
filename = 'Result.txt' # failinimi
file_header = 'Ring;Nimi;Aeg;Sektor1;Sektor2;Sektor3;Viga\n' # faili esimene rida
results = [] #  tühi list ehk kogu võistluse info
minimum = 23 #väikseim sektori aeg
maximum = 26 # suurim sektori aeg
fastest_lap = ['Unknown', 999] # kiirema ringi sõitja ja aeg
# kolme sektori kiiremad ajad eraldi
three_sectors = [['Unknown', 999], ['Unknown', 999], ['Unknown', 999]]
sectors_data = [] #ühe ringi kolm sektorit (globaalne muutuja)


def random_sector_time(mini, maxi):
    """ Juhuslik sektori aeg ette antud vahemikus k.a. """
    thousandth = random.randint(0, 999) / 1000
    return random.randint(mini, maxi) + thousandth


def one_lap_time(mini, maxi, driver_name):
    """ Ühele sõitjale ühe ringi aeg (tagastatakse) s.h sektori ajad (globl.)"""
    this_total = 0 # sektorid kokku liidetuna
    sectors_data.clear() #tühjenda sektori aegade massiivi. Globaalne
    for z in range(3): # kolme sektori tegemiseks
        this_sector = random_sector_time(mini, maxi) # ühe sektori aeg
        if this_sector < three_sectors[z][1]: # kas on uus kiireim sektor
            three_sectors[z][0] = driver_name # sektori sõitja nimi
            three_sectors[z][1] = this_sector # uus sektori aeg
        this_total += this_sector # liidame sektori aja kogu ajale
        sectors_data.append(this_sector) # sektori kaupa
    return this_total # tagasta ringi aeg


def is_fastest_lap(driver_name, fastest_data):
    """ kas on kiireima ringi aeg ja sõitja . väljastuse juures vaja."""
    if driver_name == fastest_data[0]:
        return sec2time(fastest_data[1]) # kiireim ring vorminta
    else:
        return "" #pole kiireima ringi aeg

def sec2time(sec, n_msec=3):
    ''' Convert seconds to 'D days, HH:MM:SS.FFF' '''
    #https://stackoverflow.com/questions/775049/how-do-i-convert-seconds-to-hours-minutes-and-seconds
    if hasattr(sec,'__len__'):
        return [sec2time(s) for s in sec]
    m, s = divmod(sec, 60)
    h, m = divmod(m, 60)
    d, h = divmod(h, 24)
    if n_msec > 0:
        pattern = '%%02d:%%02d:%%0%d.%df' % (n_msec+3, n_msec)
    else:
        pattern = r'%02d:%02d:%02d'
    if d == 0:
        return pattern % (h, m, s)
    return ('%d days, ' + pattern) % (d, h, m, s)


if __name__ == '__main__':
    f = open(filename, 'w', encoding='utf-8') # ava fail üle kirjutamiseks
    f.write(file_header) # kirjuta fail päis
    for name in names: # kõikide isikutega tuleb teha allolev tegevus
        lap_times = 0 # nullime isiku ringide arvu
        errors = [] #siia tulevad vigased/koperdamiste ringide numbrid
        for lap in range(laps): # hakkame sõitjale "ringe tegema"
            error = False # pole vigane/kopertatud ring
            if random.randint(0, 9) == 2: # see on kopertatud ring
                # ühe ringi aeg arvutatakse teisiti
                lap_times += one_lap_time(30, 90, 'Uknown')
                errors.append(lap+1)
                error = True
            else:
                this_lap = one_lap_time(minimum, maximum, name)
                if this_lap < fastest_lap[1]:
                    fastest_lap[0] = name # uue kiirema ringi sõitja
                    fastest_lap[1] = this_lap
                    lap_times += this_lap # liidame ringi aja kogu sõidu ajale
            line = ';'.join([str(lap+1)] + [name] + [str(sum(sectors_data))] +
                            [str(sectors_data[0])] + [str(sectors_data[1])] +
                            [str(sectors_data[2])] + [str(error)])
            f.write(line + '\n')
        results.append([name, lap_times, errors])
    f.close() # sulge fail et saaks hiljem uuesti avada

    results = sorted(results, key=lambda x: x[1])
    print(results)

    #näita info konsooli
    for idx, person in enumerate(results):
        if idx > 0:
            difference = sec2time(person[1] - results[0][1])
            # nimi, kogu erinevus esimesega ringid, kiireim ringi aeg
            print(person[0].ljust(10), sec2time(person[1], 3), difference, person[2], is_fastest_lap(person[0], fastest_lap))
        else:
            print(person[0].ljust(10), sec2time(person[1], 3), person[2], is_fastest_lap(person[0], fastest_lap))

    print('Sektorite parimad')
    total = 0
    for idx, driver in enumerate(three_sectors):
        total += driver[1]
        print('sektor', (idx+1), driver[0].ljust(10), sec2time(driver[1]))
    print('unelmate ring', sec2time(total))