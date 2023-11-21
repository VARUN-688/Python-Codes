import pandas as pd
def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    m=pd.merge(employee,department,left_on="departmentId",right_on="id",left_index=False)
    df=pd.DataFrame({"name_y":[],"name_x":[],"salary":[]})
    m=m.groupby("id_y")
    for i,j in m:
        df=pd.concat([df,(j.loc[j.salary==j.salary.max(),['name_y','name_x','salary']])],ignore_index=True)
    df=df.rename(columns={"name_y":"Department","name_x":"Employee","salary":"Salary"})
    return df
# df={"headers": {"Employee": ["id", "name", "salary", "departmentId"], 
#                 "Department": ["id", "name"]}, 
#     "rows": {"Employee": [[1, "Joe", 70000, 1], 
#                           [2, "Jim", 90000, 1], 
#                           [3, "Henry", 80000, 2],
#                           [4, "Sam", 60000, 2],
#                           [5, "Max", 90000, 1]], 
#              "Department": [[1, "IT"], [2, "Sales"]]}}
# print(department_highest_salary(df))
    
