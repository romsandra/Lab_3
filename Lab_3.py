stuff_dict = {
    'в': (3, 25), 'п': (2, 15), 'б': (2, 15), 'а': (2, 20),
    'и': (1, 5), 'н': (1, 15), 'т': (3, 20), 'о': (1, 25),
    'ф': (1, 15), 'д': (1, 10), 'к': (2, 20), 'р': (2, 20)
}
cost = int(stuff_dict['и'][1])
volm = int(stuff_dict['и'][0])
del stuff_dict['и']
key_str = '[и] '* volm
check = stuff_dict.copy()


def get_selected_items_list(V, area, value, n=len(stuff_dict), A=4):
    res = V[n][A]
    a = A
    totarea = 0
    items_list = []

    for i in range(n, 0, -1):
        if res <= 0:
            break
        if res == V[i - 1][a]:
            continue
        else:
            items_list.append((area[i - 1], value[i - 1]))
            totarea += area[i - 1]
            res -= value[i - 1]
            a -= area[i - 1]

    selected_stuff = []

    for search in items_list:
        for key, value in stuff_dict.items():
            if value == search:
                selected_stuff.append(key)

    return res, totarea, items_list, selected_stuff


def get_memtable(area, value, A=4, n=len(stuff_dict)):
    V = [[0 for a in range(A+1)]
        for i in range(n+1)]
    for i in range(n+1):
        for a in range(A+1):
            if i == 0 or a == 0:
                V[i][a] = 0
            elif area[i-1] <= a:
                V[i][a] = max(value[i-1] + V[i-1][a-area[i-1]], V[i-1][a])
            else:
                V[i][a] = V[i-1][a]       
    return V


def get_area_and_value(stuffdict):
    area = []
    value = []

    for item in stuffdict:
        area.append(stuffdict[item][0])
        value.append(stuffdict[item][1])

    return area, value


area, value = get_area_and_value(stuff_dict)
V = get_memtable(area,value,4,len(stuff_dict))
data = get_selected_items_list(V,area,value)
for i in data[3]:
    if i in stuff_dict:
        del stuff_dict[i]
area, value = get_area_and_value(stuff_dict)
V = get_memtable(area,value,4-volm,len(stuff_dict))
data1 = get_selected_items_list(V,area,value,len(stuff_dict),4-volm)

surv = 20
for i in data1[2]:
    surv+= i[1]*2
for i in data[2]:
    surv+= i[1]*2
surv += cost
item = {}
for key, value in check.items():
    surv=surv - value[1]
i = 0

duple={}
for key,value in check.items():
    for item in data[2]:
        if value == item and not(key in duple):
            duple[key]=0
            i+=value[0]
            print(('['+key+'] ')*value[0],end='')
            if(i == 4):
                break
    if i == 4:
        break
print()
i = 0
for key,value in check.items():
    for item in data1[2]:
        if value == item and not(key in duple):
            duple[key]=0
            i+=value[0]
            print(('['+key+'] ')*value[0],end='')
            if(i == 4 -volm):
                break
    if i == 3-volm:
        break


print(key_str)

print('Итоговые очки выживания: ', surv)

print("Том сможет выжить" if surv>0 else "Том не сможет выжить")
