def sdnf_sknf(x1s: dict, x2s: dict, x3s: dict, f):
    sknf = []
    sdnf = []

    conjugationElements = []
    disjunctionElements = []

    for index, x1 in enumerate(x1s):
        x2 = x2s[index]
        x3 = x3s[index]

        conjugationElementX1 = None
        conjugationElementX2 = None
        conjugationElementX3 = None

        disjunctionElementX1 = None
        disjunctionElementX2 = None
        disjunctionElementX3 = None

        if x1 == '1':
            conjugationElementX1 = f' не x1'
        elif x1 == '0':
            conjugationElementX1 = f' x1'

        if x2 == '1':
            conjugationElementX2 = f' не x2'
        elif x2 == '0':
            conjugationElementX2 = f' x2'

        if x3 == '1':
            conjugationElementX3 = f' не x3'
        elif x3 == '0':
            conjugationElementX3 = f' x3'

        conjugationElements.insert(0, f'| {conjugationElementX1}*{conjugationElementX2}*{conjugationElementX3} |')

        if x1 == '0':
            disjunctionElementX1 = f' не x1'
        elif x1 == '1':
            disjunctionElementX1 = f' x1'

        if x2 == '0':
            disjunctionElementX2 = f' не x2'
        elif x2 == '1':
            disjunctionElementX2 = f' x2'

        if x3 == '0':
            disjunctionElementX3 = f' не x3'
        elif x3 == '1':
            disjunctionElementX3 = f' x3'

        disjunctionElements.insert(0, f'| {disjunctionElementX1}*{disjunctionElementX2}*{disjunctionElementX3} |')

        if f[index] == '0':
            if (index + 1) == len(x1s):
                sknf.append(f"({conjugationElementX1} V {conjugationElementX2}V {conjugationElementX3})")
            else:
                sknf.append(f"({conjugationElementX1} V {conjugationElementX2} V {conjugationElementX3}) * ")
        elif f[index] == '1':
            if (index + 1) == len(x1s):
                sdnf.append(f"{disjunctionElementX1} * {disjunctionElementX2} * {disjunctionElementX3}")
            else:
                sdnf.append(f"{disjunctionElementX1} * {disjunctionElementX2} * {disjunctionElementX3} V ")

    return {
        "sdnf": ''.join(sdnf),
        "sknf": ''.join(sknf),
        "conjugationElements": '\n'.join(conjugationElements),
        "disjunctionElements": '\n'.join(disjunctionElements)
    }
