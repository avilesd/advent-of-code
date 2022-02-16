import pandas as pd

index_of_space = lambda srs: [i.find(" ") for i in srs]

def main():
    data = pd.read_csv("input_data", header=None)
    data.rename(columns={0:"instructions"}, inplace=True)
    data["i_number"] = data["instructions"].str[-2:]

    data["i_number"] = (data["i_number"].astype("int"))

    ver_sum = 0
    hor_sum = 0

    for i in range(0, data.shape[0]):
        if data.iloc[i, 0].find("forward") != -1:
            hor_sum += data.iloc[i, 1]
        if data.iloc[i, 0].find("down") != -1:
            ver_sum += data.iloc[i, 1]
        if data.iloc[i, 0].find("up") != -1:
            ver_sum -= data.iloc[i, 1]

    print("ver_sum={}, hor_sum={}. Multiplied results in={}".format(ver_sum, hor_sum, ver_sum*hor_sum))


    print(data.head(5))

if __name__ == "__main__":
    main()