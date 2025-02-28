from solutions.CHK.products import Product, MultiOfferProduct

ALLOWED_SKUS = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

PRODUCT_CATALOG = {
    'A': MultiOfferProduct('A', 50, [(3, 130), (5, 200)]),
    'B': Product('B', 30, 2, 45),
    'C': Product('C', 20),
    'D': Product('D', 15),
    'E': Product('E', 40),
    'F': Product('F', 10, 3, 20),
    'G': Product('G', 20),
    'H': MultiOfferProduct('H', 10, [(5, 45), (10, 80)]),
    'I': Product('I', 35),
    'J': Product('J', 60),
    'K': Product('K', 80, 2, 150),
    'L': Product('L', 90),
    'M': Product('M', 15),
    'N': Product('N', 40),
    'O': Product('O', 10),
    'P': Product('P', 50, 5, 200),
    'Q': Product('Q', 30, 3, 80),
    'R': Product('R', 50),
    'S': Product('S', 30),
    'T': Product('T', 20),
    'U': Product('U', 40, 3, 80),
    'V': MultiOfferProduct('V', 50, [(2, 90), (3, 130)]),
    'W': Product('W', 20),
    'X': Product('X', 90),
    'Y': Product('Y', 10),
    'Z': Product('Z', 50)
}



