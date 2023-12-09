import sys

def predict_next(metric: [int]) -> int:
    last_col = [metric[-1]]
    values = metric
    while  last_col[-1]:
        diffs = [k-j for j,k in zip(values, values[1:])]
        last_col.append(diffs[-1])
        # print(f"metric={metric}, diffs={diffs}, last_col={last_col}")
        values = diffs

    return sum(last_col)

if __name__ == "__main__":
    lines = sys.stdin.readlines()
    metrics = [[int(x) for x in line.strip().split()] for line in lines]
    # print([predict_next(m) for m in metrics])
    print(sum(predict_next(m) for m in metrics))
