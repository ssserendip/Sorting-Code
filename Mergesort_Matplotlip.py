import random
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def swap(A, i, j):

    if i != j:
        A[i], A[j] = A[j], A[i]

def merge_sort(A, start, end):

    if end <= start:
        return

    mid = start + ((end - start + 1) // 2) - 1
    yield from merge_sort(A, start, mid)
    yield from merge_sort(A, mid + 1, end)
    yield from merge(A, start, mid, end)
    yield A

def merge(A, start, mid, end):
    
    merged = []
    leftIdx = start
    rightIdx = mid + 1

    while leftIdx <= mid and rightIdx <= end:
        if A[leftIdx] < A[rightIdx]:
            merged.append(A[leftIdx])
            leftIdx += 1
        else:
            merged.append(A[rightIdx])
            rightIdx += 1

    while leftIdx <= mid:
        merged.append(A[leftIdx])
        leftIdx += 1

    while rightIdx <= end:
        merged.append(A[rightIdx])
        rightIdx += 1

    for i, sorted_val in enumerate(merged):
        A[start + i] = sorted_val
        yield A
        
if __name__ == "__main__":

    N = int(input("Enter number of integers: "))

    A = [x + 1 for x in range(N)]
    random.seed(time.time())
    random.shuffle(A)

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.set_title("Merge Sort")
    ax.axis('off')

    bar_rects = ax.bar(range(len(A)), A, align="edge")
    ax.set_xlim(0, N)
    ax.set_ylim(0, int(1.07 * N))
    text = ax.text(0.02, 0.95, "", transform=ax.transAxes)

    iteration = [0]

    def update_fig(A, rects, iteration):
        for rect, val in zip(rects, A):
            rect.set_height(val)
        iteration[0] += 1
        text.set_text("# of operations: {}".format(iteration[0]))

    generator = merge_sort(A, 0, len(A) - 1)

    anim = animation.FuncAnimation(fig, func=update_fig, fargs=(bar_rects, iteration), frames=generator, interval=30, repeat=False)
    plt.show()