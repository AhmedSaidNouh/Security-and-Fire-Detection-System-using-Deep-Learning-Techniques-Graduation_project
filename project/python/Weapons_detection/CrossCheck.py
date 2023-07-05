# CrossCheck technique
def run_cross_check(matches1, matches2):
    newMatches = []
    for m1 in matches1:
        for m2 in matches2:
            if (m1.queryIdx == m2.trainIdx) and (m2.queryIdx == m1.trainIdx):
                newMatches.append(m1)
    return newMatches
