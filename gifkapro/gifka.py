import random
from tkinter import *


WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
BAR_WIDTH = 10
BAR_SPACING = 2
CANVAS_BG_COLOR = 'white'
BAR_COLORS = ['blue', 'green']


class SortVisualizer(Tk):
    def __init__(self):
        super().__init__()
        self.title("Визуализация алгоритмов сортировки")
        self.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")


        self.canvas = Canvas(self, width=WINDOW_WIDTH, height=WINDOW_HEIGHT - 100, bg=CANVAS_BG_COLOR)
        self.canvas.pack()


        button_frame = Frame(self)
        button_frame.pack(pady=10)
        Button(button_frame, text="Bubble Sort", command=self.bubble_sort).pack(side=LEFT, padx=5)
        Button(button_frame, text="Quick Sort", command=self.quick_sort).pack(side=LEFT, padx=5)
        Button(button_frame, text="Selection Sort", command=self.selection_sort).pack(side=LEFT, padx=5)
        Button(button_frame, text="Insertion Sort", command=self.insertion_sort).pack(side=LEFT, padx=5)


        self.array = [random.randint(10, WINDOW_HEIGHT // 2) for _ in range(WINDOW_WIDTH // (BAR_WIDTH + BAR_SPACING))]
        self.draw_array()

    def draw_array(self, color_positions=None):
        """Отображаем массив в виде столбчатых диаграмм."""
        self.canvas.delete('all')
        x_start = 0
        for i, value in enumerate(self.array):
            bar_color = BAR_COLORS[i % len(BAR_COLORS)]

            if color_positions is not None and i in color_positions:
                bar_color = 'red'

            # Рисуем полоску
            self.canvas.create_rectangle(
                x_start, WINDOW_HEIGHT - value,
                         x_start + BAR_WIDTH, WINDOW_HEIGHT,
                fill=bar_color
            )
            x_start += BAR_WIDTH + BAR_SPACING

    def bubble_sort(self):
        """Метод пузырьковой сортировки с анимацией."""
        n = len(self.array)
        for i in range(n):
            swapped = False
            for j in range(0, n - i - 1):
                if self.array[j] > self.array[j + 1]:
                    self.array[j], self.array[j + 1] = self.array[j + 1], self.array[j]
                    swapped = True


                self.update()
                self.after(100)
                self.draw_array([j, j + 1])

            if not swapped:
                break
        self.draw_array()

    def quick_sort(self):
        """Быстрая сортировка (рекурсивная версия) с анимацией."""

        def partition(arr, low, high):
            pivot = arr[(low + high) // 2]
            i = low - 1
            j = high + 1
            while True:
                i += 1
                while arr[i] < pivot:
                    i += 1
                j -= 1
                while arr[j] > pivot:
                    j -= 1
                if i >= j:
                    return j
                arr[i], arr[j] = arr[j], arr[i]
                self.update()
                self.after(100)
                self.draw_array([i, j])

        def qsort(arr, low, high):
            if low < high:
                pi = partition(arr, low, high)
                qsort(arr, low, pi)
                qsort(arr, pi + 1, high)

        qsort(self.array, 0, len(self.array) - 1)
        self.draw_array()

    def selection_sort(self):
        """Сортировка выбором с анимацией."""
        n = len(self.array)
        for i in range(n):
            min_idx = i
            for j in range(i + 1, n):
                if self.array[min_idx] > self.array[j]:
                    min_idx = j

            # Меняем минимальный элемент и текущий элемент местами
            self.array[i], self.array[min_idx] = self.array[min_idx], self.array[i]

            # Отображение промежуточного состояния
            self.update()
            self.after(100)
            self.draw_array([min_idx, i])

        self.draw_array()

    def insertion_sort(self):
        """Сортировка вставками с анимацией."""
        n = len(self.array)
        for i in range(1, n):
            key = self.array[i]
            j = i - 1
            while j >= 0 and key < self.array[j]:
                self.array[j + 1] = self.array[j]
                j -= 1
                self.update()
                self.after(100)
                self.draw_array([i, j + 1])
            self.array[j + 1] = key

        self.draw_array()



if __name__ == "__main__":
    app = SortVisualizer()
    app.mainloop()