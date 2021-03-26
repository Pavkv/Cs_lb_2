n = int(input("Write amount of variables: "))
matrix = [[0] * n for _ in range(2**n)]
value = []
for i in range(2**n):
    s = i
    while s:
        value.insert(0, s % 2)
        s //= 2
    for j in range(n):
        while len(value) < n:
            value.insert(0, 0)
        matrix[i][j] = value[j]
    value.clear()
for i in range(2**n):
    f = int(input(f"{matrix[i]}: "))
    matrix[i].append(f)
numofunit = []
numofunits = [[] * n for _ in range(n+1)]
for i in range(len(matrix)):
    if matrix[i][-1] == 1:
        count = 0
        for j in range(n):
            if matrix[i][j] == 1:
                count += 1
        numofunit.append(int(i))
        numofunits[count].append(i)
im1 = []
for i in range(len(numofunits)-1):
    for j in numofunits[i]:
        for x in numofunits[i+1]:
            c = ''
            count = 0
            for z in range(n):
                if matrix[j][z] == matrix[x][z]:
                    c += str(matrix[j][z])
                elif matrix[j][z] != matrix[x][z]:
                    c += '-'
                    count += 1
                    num = z
            if count == 1:
                im1.append(c)
    continue
im2 = []
if n >= 4:
    for f in range(2, n-1):
        for i in range(len(im1)):
            for j in range(i+1, len(im1)):
                c = ''
                count = 0
                for z in range(len(im1[i])):
                    if im1[i][z] == im1[j][z]:
                        c += str(im1[i][z])
                    elif im1[i][z] != im1[j][z]:
                        c += '-'
                        count += 1
                if count == f-1:
                    im2.append(c)
else:
    im2 = im1
im = []
for i in im1:
    for j in im2:
        c = ''
        count = 0
        for z in range(n):
            if i[z] == j[z]:
                c += str(i[z])
            elif i[z] != j[z]:
                c += '-'
                count += 1
        if count != 1:
            im.append(i)
a = 0
while a != len(im)-1:
    b = a + 1
    if im[a] == im[b]:
        del im[b]
        a -= 1
    else:
        a += 1
if len(im) > n:
    IM = [[] * n for _ in range(n)]
    for i in range(len(im)-1):
        for j in range(i+1, len(im)):
            f = 0
            s = 0
            for z in range(n):
                if im[i][z].isdigit():
                    f += int(im[i][z])
                if im[j][z].isdigit():
                    s += int(im[j][z])
            if f == s and im[i] not in IM and len(IM[f]) == 0:
                IM[f].append(im[i])
    im.clear()
    for i in range(len(IM)):
        for j in IM[i]:
            im.append(j)
m = [[0] * len(numofunit) for _ in range(len(im))]
for i in range(len(im)):
    for j in numofunit:
        count = 0
        for z in range(n):
            if str(matrix[j][z]) != im[i][z]:
                count += 1
        if count == 1:
            f = numofunit.index(j)
            m[i][f] = 1
row = [[0] * 2 for _ in range(len(numofunit))]
column = [[0] * 2 for _ in range(len(m))]
for i in range(len(m)):
    for j in range(len(numofunit)):
            column[i][0] += m[i][j]
            column[i][1] = i
            for x in range(i + 1, len(m)):
                if column[x][0] > column[i][0]:
                    column[x][0] = column[i][0]
                    column[x][1] = i
                    column[i][0] = column[x][0]
                    column[i][1] = x
for x in range(len(column)):
    i = column[x][1]
    for j in range(len(numofunit)):
            if m[i][j] == 1 and row[j][0] != 1:
                row[j][0] = 1
                row[j][1] = i
output = []
for i in range(len(m)):
    c = ''
    for j in range(len(row)):
        if row[j][1] == i and str(im[i]) not in output:
            c = str(im[i])
    output.append(c)
letters = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'
lett = list(map(str, letters.split()))
end = ''
for i in range(len(output)):
    c = ''
    for z in range(n):
        if output[i][z] == '1':
            c += lett[z]
        elif output[i][z] == '0':
            c += f'!{lett[z]}'
    if i != len(output)-1:
        end += f'{c}+'
    else:
        end += c
# print(*[' '.join(map(str,e)) for e in m], sep='\n')
print(end)