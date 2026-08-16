import pandas as pd
def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    merged = pd.merge(employee,employee, left_on="managerId", right_on="id", suffixes=("", "_mgr"))
    result = merged[merged["salary"] > merged["salary_mgr"]][["name"]]
    result.columns = ["Employee"]
    return result