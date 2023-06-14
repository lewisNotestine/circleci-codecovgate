import os
from sys import argv


def getcoveragepct(filepath):
    with open(filepath, 'r') as f:
        return float(f.readline())


def compare_test_coverage(localbranch_pct_filepath, mainbranch_pct_filepath):
    """
    """
    print(f'localbranch filepath is {localbranch_pct_filepath}')
    print(f'main branch filepath is {mainbranch_pct_filepath}')

    if not os.path.exists(mainbranch_pct_filepath):
        raise ValueError("no code coverage for main branch")

    # problem if this happens
    if not os.path.exists(localbranch_pct_filepath):
        raise ValueError("no code coverage metric found for branch")

    local_covg_pct = getcoveragepct(localbranch_pct_filepath)
    main_covg_pct = getcoveragepct(mainbranch_pct_filepath)

    print(f"local branch code coverage pct is {local_covg_pct}")
    print(f"main coverage pct is {main_covg_pct}")

    if local_covg_pct < main_covg_pct:
        raise ValueError(f"insufficient code coverage in feature branch {local_covg_pct}. Main branch has {main_covg_pct}")


if __name__ == '__main__':
    localbranch_pct_filepath = argv[1]
    mainbranch_pct_filepath = argv[2]
    compare_test_coverage(localbranch_pct_filepath, mainbranch_pct_filepath)