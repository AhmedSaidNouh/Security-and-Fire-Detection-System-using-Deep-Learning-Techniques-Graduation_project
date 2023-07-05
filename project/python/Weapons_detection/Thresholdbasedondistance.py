# Threshold technique
def run_threshold_based_distance(matches):
    sum = 0
    for m1 in matches:
        sum = sum + m1.distance

    if(len(matches)==0):
        return matches

    threshold = sum / len(matches)
    newMatches = []
    for m1 in matches:
        if (m1.distance > threshold):
            newMatches.append(m1)
    return newMatches
