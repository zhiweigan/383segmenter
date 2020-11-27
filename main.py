from music21 import *

c = converter.parse('mozart.mxl')

out = [0, 1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1, 1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 6, 6, 6,
       7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 16, 16, 17, 17, 18, 18, 19, 19, 20, 20, 21, 21,
       22, 22, 23, 23, 24, 24, 3, 3, 3, 3, 3, 3, 3, 3, 3, 25, 25, 26, 26, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 27, 27, 28, 28,
       28, 28, 29, 29, 30, 30, 28, 28, 31, 31, 32, 32, 33, 33, 34, 34, 35, 35, 36, 36, 37, 37, 38, 38, 39, 39, 40, 40]
i = 0
for measure in c.parts[0]:
    if i == 0:
        i += 1
        continue
    #     measure[0].lyric = out[i]
    if type(measure) == stream.Measure:
        measure.getElementsByClass(['Note', 'Rest', 'Chord'])[0].lyric = out[i]
    #         measure.getElementsByClass(['Note', 'Rest', 'Chord'])[0].lyric = ""

    i += 1

def find_major_segments(section1, section2):
    pass

bounds = [(0, 34), (35, 64), (65, 96), (97, 128)]
segments = [set([])] * len(bounds)
similar = {0:(0,34), 2:(65, 96)}

for i in similar.keys():
    for j in similar.keys():
        if not i < j: continue

        one = similar[i]
        two = similar[j]

        longchunks = []
        currentChunk = out[0]
        length = 0
        for k in range(one[0], one[1]+1):
            if length >= 8:
                longchunks.append(out[k])
            if out[k] == currentChunk:
                length += 1
            else:
                length = 0
                currentChunk = out[k]

        chunknums = set([])
        for k in range(two[0], two[1]+1):
            if out[k] in longchunks:
                chunknums.add(out[k])

        segments[i] = segments[i].union(chunknums)
        segments[j] = segments[j].union(chunknums)

sectionmap = {}
alphabet = "ABCDEFGHJIJKLMNOPQRSTUVWXYZ"
output = ""
iter = 0
for se in segments:
    if len(se) == 0:
        output += alphabet[iter]
        iter += 1
    for elem in se:
        if elem not in sectionmap:
            sectionmap[elem] = alphabet[iter]
            output += alphabet[iter]
            iter += 1
        else:
            output += sectionmap[elem]

print(output)

# c.show()