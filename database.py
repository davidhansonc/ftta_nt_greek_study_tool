import pandas as pd
import os

if __name__ == "__main__":
    # Greek data
    gk_cols = ["book", "chapter", "verse", "nestle1904"]
    gk_df = pd.read_csv("./database_creation/verses/nestle1904/nestle1904.csv", delimiter="|", names=gk_cols, header=None, usecols=range(4), lineterminator="\n")
    gk_df.nestle1904 = gk_df.nestle1904.str.replace("\r", "")
    print(f"Greek table length: {len(gk_df)}")

    # recovery version data
    rcv_cols = ["book", "chapter", "verse", "recovery_version"]
    rcv_df = pd.read_csv("./database_creation/verses/recovery_version/rcv.csv", delimiter="|", names=rcv_cols, header=None, usecols=range(4), lineterminator="\n")
    rcv_df.recovery_version = rcv_df.recovery_version.str.replace("\r", "")
    print(f"RcV table length: {len(rcv_df)}")

    # fill table with combined data
    total_df = pd.merge(rcv_df, gk_df, how="outer", on=["book", "chapter", "verse"]).fillna("-")
    print(f"Total length: {len(total_df)}")
    print(total_df)


    total_df.to_csv("./combined_verse_table.csv", sep='|', index=False)