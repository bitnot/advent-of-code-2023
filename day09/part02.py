import sys

def predict_prev(metric: [int]) -> int:
    first_col = [metric[0]]
    last_col = [metric[-1]]
    values = metric
    while  last_col[-1]:
        diffs = [k-j for j,k in zip(values, values[1:])]
        first_col.append(diffs[0])
        last_col.append(diffs[-1])
        # print(f"metric={metric}, diffs={diffs}, first_col={first_col}")
        values = diffs
    x = first_col[-1]
    for y in reversed(first_col[:-1]):
        x = y - x
    return x

if __name__ == "__main__":
    lines = sys.stdin.readlines()
    metrics = [[int(x) for x in line.strip().split()] for line in lines]
    # print([predict_prev
    #(m) for m in metrics])
    print(sum(predict_prev
(m) for m in metrics))
