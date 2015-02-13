#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd

df = pd.read_excel("./_data/cityfixitdata.xlsx")

df["NumThroughApp"] = df.NumRequests*(df["%ReportedBySeeClickFix"]*.01)

df[
        ["ProblemType",
        "NumRequests",
        "Year",
        "%ReportedBySeeClickFix",
        "NumThroughApp"]
    ].\
            to_csv("./_data/cityfixitdata.csv", index=False)
