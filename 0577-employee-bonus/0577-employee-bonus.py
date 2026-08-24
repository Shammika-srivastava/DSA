import pandas as pd

def employee_bonus(employee: pd.DataFrame, bonus: pd.DataFrame) -> pd.DataFrame:
    df = pd.merge(employee,bonus,on='empId',how='left')
    print(df)
    final = df[(df['bonus']<1000) | df['bonus'].isnull()] 
    print(final)
    return final[['name','bonus']]

    #     # Merge Employee with Bonus
    # df = employee.merge(bonus, on="empId", how="left")

    # # Filter condition: bonus < 1000 OR bonus is null
    # result = df[(df["bonus"].isna()) | (df["bonus"] < 1000)][["name", "bonus"]]
    # return result