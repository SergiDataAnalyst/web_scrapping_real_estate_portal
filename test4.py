from sede_catastro import extract_cat_code
from playwright.sync_api import sync_playwright

## note, convert to main,

catastral_code_list = [
    "9166306CG7096N0003RS",
    "8494409CF8989S0001XG",
    "8494012CF8989S0001YG",
    "5172018CF8957S0001AG",
    "0840034DF0904S0001EX",
    "2864019DF0926S0001GK",
    "6871011CG8067S0001GS",
    "8215001CF9981N0001BZ",
    "3733227CG8033S0033WQ",
    "4139025CG8043N0014IU",
    "6629204CG8062N0001YA",
    "6436401CG8063N0111PG",
    "7037119CG8073N0014XL",
    "6734110CG8063S0004AH",
    "6436401CG8063N0070WU",
    "5042410CG9254S0001LW",
    "3299008DG0139G0006QT",
    "3405303DG0230A0004YI",
    "1701003DG0210A0004HM",
    "2701204DG0220A0005QT",
    "2499401DG0129G0009BR",
    "2602007DG0220A0004OR",
    "3608086DG0230A0003JU",
    "1701003DG0210A0008BR",
    "2298302DG0129G0002YB",
    "002100600DG01A0001GK",
    "8730046DG0283S0026LD",
    "8510212DG0381S0005OG",
    "3937701CG9333N0013HY",
    "5641713DG0154S0001TJ",
    "5036603DG0153N0001XG",
    "0875727DF1907N0001PI",
    "0680303DF1908S0001LP",
    "7876617DF0777N0001HF",
    "4812409DF1741D0008MD",
    "4305205DF1740E0011XT",
    "4714802DF1741C0009KT",
    "3193309DF1639C0003BA",
    "4912804DF1741B0011OK",
    "4512115DF1741B0003AD",
    "4912815DF1741B0142FB",
    "4612815DF1741B0004OF",
    "4908201DF1740H0357LY",
    "5011205DF1751A0004QO",
    "3611722DF1731B0002ZI",
    "0853111DF1805S0001LM",
    "0657101DF1805N0005LL",
    "3783705DF2738D0017BI",
    "3393944DF2739C0008PP",
    "3095322DF2739E0004PQ",
    "3296234DF2739E0042PR",
    "2783504DF2728D0008UZ",
    "3393952DF2739C0013AS",
    "3296211DF2739E0003FM",
    "3393952DF2739C0021HJ",
    "2993405DF2729D0038YD",
    "2993405DF2729D0043IG",
    "3398233DF2739G0025GA",
    "2892909DF2729E0007BM",
    "2085208DF2728E0014IP",
    "3094434DF2739C0004ZY",
    "3296221DF2739E0004OQ",
    "3595513DF2739F0026OE",
    "2698116DF2729H0006ME",
    "2597711DF2729F0005RU",
    "3598107DF2739H0037SY",
    "3296226DF2739E0003UM",
    "3393943DF2739C0003LT",
    "3393903DF2739C0034LR",
    "3300901DF2830A0029FB",
    "3598126DF2739H0007HI",
    "2085403DF2728E0007DY",
    "3296237DF2739E0020ZA",
    "3393938DF2739C0016AG",
    "3398204DF2739G0002WJ",
    "3398202DF2739G0062ED",
]


if __name__ == "__main__":
    with sync_playwright() as playwright:
        extract_cat_code(playwright, catastral_code_list)
