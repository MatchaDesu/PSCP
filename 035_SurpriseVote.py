"surprising"
def main(vote,most):
    "main"
    x = most-max(0, vote-2*most)
    if x > 2:
        print("Surprising")
    else:
        print("Not surprising")
main(float(input()),float(input()))
