import random
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def swap(A, i, j):

    if i != j:
        A[i], A[j] = A[j], A[i]
        
def bubble_sort(A):

    if len(A) == 1:
        return

    swapped = True
    for i in range(len(A) - 1):
        if not swapped:
            break
        swapped = False
        for j in range(len(A) - 1 - i):
            if A[j] > A[j + 1]:
                swap(A, j, j + 1)
                swapped = True
            yield A
            
if __name__ == "__main__":

    N = int(input("Enter number of integers: "))
    A = [x + 1 for x in range(N)]
    random.seed(time.time())
    random.shuffle(A)

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.set_title("Bubble Sort")
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

    generator = bubble_sort(A)

    anim = animation.FuncAnimation(fig, func=update_fig, fargs=(bar_rects, iteration), frames=generator, interval=30, repeat=False)
    plt.show()
