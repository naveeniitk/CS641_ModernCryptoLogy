def coppersmith_howgrave_univariate(pol, modulus, beta, mm, tt, XX):
    dd = pol.degree()
    nn = dd * mm + tt

    polZ = pol.change_ring(ZZ)
    x = polZ.parent().gen()

    # compute polynomials
    gg = []
    for ii in range(mm):
        for jj in range(dd):
            gg.append((x * XX) ** jj * modulus ** (mm - ii) * polZ(x * XX) ** ii)
    for ii in range(tt):
        gg.append((x * XX) ** ii * polZ(x * XX) ** mm)

    # construct lattice B
    BB = Matrix(ZZ, nn)

    for ii in range(nn):
        for jj in range(ii + 1):
            BB[ii, jj] = gg[ii][jj]

    # LLL
    BB = BB.LLL()

    # transform shortest vector in polynomial
    new_pol = 0
    for ii in range(nn):
        new_pol += x ** ii * BB[0, ii] / XX ** ii

    # factor polynomial
    potential_roots = new_pol.roots()

    # test roots
    roots = []
    for root in potential_roots:
        if root[0].is_integer():
            result = polZ(ZZ(root[0]))
            if gcd(modulus, result) >= modulus ^ beta:
                roots.append(ZZ(root[0]))

    return roots


e = 5
N = 84364443735725034864402554533826279174703893439763343343863260342756678609216895093779263028809246505955647572176682669445270008816481771701417554768871285020442403001649254405058303439906229201909599348669565697534331652019516409514800265887388539283381053937433496994442146419682027649079704982600857517093
C = 23701787746829110396789094907319830305538180376427283226295906585301889543996533410539381779684366880970896279018807100530176651625086988655210858554133345906272561027798171440923147960165094891980452757852685707020289384698322665347609905744582248157246932007978339129630067022987966706955482598869800151693
# RSA known parameters
ZmodN = Zmod(N);


def break_RSA(p_str, max_length_M):
    global e, C, ZmodN

    p_binary_str = ''.join(['{0:08b}'.format(ord(x)) for x in p_str])

    for length_M in range(0, max_length_M + 1, 4):  # size of the root

        # Problem to equation (default)
        P. < M > = PolynomialRing(ZmodN)  # , implementation='NTL')
        pol = ((int(p_binary_str, 2) << length_M) + M) ^ e - C
        dd = pol.degree()

        # Tweak those
        beta = 1
        epsilon = beta / 7
        mm = ceil(beta ** 2 / (dd * epsilon))
        tt = floor(dd * mm * ((1 / beta) - 1))
        XX = ceil(N ** ((beta ** 2 / dd) - epsilon))

        roots = coppersmith_howgrave_univariate(pol, N, beta, mm, tt, XX)

        if roots:
            print("Root is :", ' {0:b}'.format(roots[0]))
            return

    print('No solution found\n')


if __name__ == "__main__":
    print("The padding p using the hexadecimal numbers is : ", end="")

    a = [["59", "6f", "75", "20", "73", "65", "65", "20"], ["61", "20", "47", "6f", "6c", "64", "2d", "42"],
         # numbers found when we type commands exit1-exit4
         ["75", "67", "20", "69", "6e", "20", "6f", "6e"],
         ["65", "20", "63", "6f", "72", "6e", "65", "72"], ["2e", "20", "49", "74", "20", "69", "73", "20"],
         ["74", "68", "65", "20", "6b", "65", "79", "20"],
         ["74", "6f", "20", "61", "20", "74", "72", "65"], ["61", "73", "75", "72", "65", "20", "66", "6f"]]
    for i in range(8):
        for j in range(8):
            bytes_object = bytes.fromhex(a[i][j])
            ascii_string = bytes_object.decode("ASCII")
            print(ascii_string, end="")
    b = ["75", "6e", "64", "20", "62", "79"]
    for i in range(6):
        bytes_object = bytes.fromhex(b[i])
        ascii_string = bytes_object.decode("ASCII")
        print(ascii_string, end="")
    print()

    break_RSA("You see a Gold-Bug in one corner. It is the key to a treasure found by", 300)

    b = "0100001001000000011010000111010101100010010000010110110000100001"
    print("Password : ", end="")
    for i in range(0, 64, 8):
        x = b[i:i + 8]
        y = int(x, 2)
        print(chr(y), end="")
    print()
