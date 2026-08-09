import pandas as pd


def main():
    print("Hello from pandas-practice!")

columns = ["Name", "Age", "Hight"]
data = [
    ["Ted", 22, 175],
    ["Allen", 25, 180],
    ["Jack", 25, 180],
]
df = pd.DataFrame(data=data, columns=columns)

if __name__ == "__main__":
    main()
