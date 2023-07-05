# David lowe's technique
def run_david_lowes(matches):
    newMatches = []
    for m in matches:
        distance1 = m[0].distance
        distance2 = m[1].distance
        if ((distance1 / distance2) < 0.75):
            newMatches.append(m[0])
    return newMatches