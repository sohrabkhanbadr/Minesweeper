 در اینجا توضیح ساده و دوستانه‌ای از کد بازی Minesweeper به زبان پایتون آورده شده است:

### کتابخانه‌های مورد استفاده:
```python
import tkinter as tk  # برای ایجاد رابط کاربری
import random  # برای ایجاد موقعیت‌های تصادفی
```

### کلاس Minesweeper:
```python
class Minesweeper:
```
این کلاس اصلی بازی را تعریف می‌کند.

### تابع `__init__`:
```python
    def __init__(self, root, rows, cols, mines):
        self.root = root
        self.rows = rows
        self.cols = cols
        self.mines = mines
        self.buttons = [[None for _ in range(cols)] for _ in range(rows)]
        self.mine_positions = set()
        self.create_widgets()
        self.place_mines()
        self.calculate_numbers()
```
این تابع، وقتی که شیء بازی ایجاد می‌شود، اجرا می‌شود و کارهای زیر را انجام می‌دهد:
- تنظیمات اولیه مثل تعداد ردیف‌ها، ستون‌ها و مین‌ها را ذخیره می‌کند.
- یک ماتریس از دکمه‌ها برای شبکه بازی ایجاد می‌کند.
- موقعیت مین‌ها را به صورت یک مجموعه خالی تعریف می‌کند.
- توابع `create_widgets`، `place_mines` و `calculate_numbers` را صدا می‌زند.

### تابع `create_widgets`:
```python
    def create_widgets(self):
        for r in range(self.rows):
            for c in range(self.cols):
                button = tk.Button(self.root, width=2, height=1, command=lambda r=r, c=c: self.reveal(r, c))
                button.bind("<Button-3>", lambda e, r=r, c=c: self.toggle_flag(r, c))
                button.grid(row=r, column=c)
                self.buttons[r][c] = button
```
این تابع دکمه‌های مربوط به هر سلول از شبکه بازی را ایجاد می‌کند:
- دکمه‌ها را در جایگاه مناسب در شبکه قرار می‌دهد.
- برای دکمه‌ها دو رویداد تعریف می‌کند: کلیک چپ (برای فاش کردن) و کلیک راست (برای قرار دادن پرچم).

### تابع `place_mines`:
```python
    def place_mines(self):
        while len(self.mine_positions) < self.mines:
            r = random.randint(0, self.rows - 1)
            c = random.randint(0, self.cols - 1)
            self.mine_positions.add((r, c))
```
این تابع موقعیت مین‌ها را به صورت تصادفی انتخاب می‌کند تا زمانی که تعداد مین‌ها به تعداد مشخص شده برسد.

### تابع `calculate_numbers`:
```python
    def calculate_numbers(self):
        self.numbers = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        for r, c in self.mine_positions:
            for dr in (-1, 0, 1):
                for dc in (-1, 0, 1):
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < self.rows and 0 <= nc < self.cols and (nr, nc) not in self.mine_positions:
                        self.numbers[nr][nc] += 1
```
این تابع تعداد مین‌های اطراف هر سلول را محاسبه می‌کند و آنها را در ماتریس `numbers` ذخیره می‌کند.

### تابع `reveal`:
```python
    def reveal(self, r, c):
        if (r, c) in self.mine_positions:
            self.buttons[r][c].config(text='*', background='red')
            self.game_over()
        else:
            self.buttons[r][c].config(text=self.numbers[r][c] if self.numbers[r][c] > 0 else '', relief=tk.SUNKEN, state=tk.DISABLED)
```
این تابع وقتی که یک سلول توسط کاربر فاش می‌شود، اجرا می‌شود:
- اگر سلول حاوی مین باشد، بازی تمام می‌شود.
- اگر سلول حاوی مین نباشد، تعداد مین‌های اطراف آن سلول نمایش داده می‌شود.

### تابع `toggle_flag`:
```python
    def toggle_flag(self, r, c):
        current_text = self.buttons[r][c].cget('text')
        if current_text == '':
            self.buttons[r][c].config(text='F')
        elif current_text == 'F':
            self.buttons[r][c].config(text='')
```
این تابع به کاربر اجازه می‌دهد تا با کلیک راست روی سلول‌ها پرچم قرار دهد یا پرچم را بردارد.

### تابع `game_over`:
```python
    def game_over(self):
        for r, c in self.mine_positions:
            self.buttons[r][c].config(text='*', background='red')
        print("Game Over!")
```
این تابع وقتی که بازی به پایان می‌رسد (یعنی کاربر روی مین کلیک می‌کند)، همه مین‌ها را نمایش می‌دهد.

### اجرای بازی:
```python
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Minesweeper")
    game = Minesweeper(root, 10, 10, 10)  # 10x10 grid with 10 mines
    root.mainloop()
```
این قسمت برنامه را اجرا می‌کند:
- یک پنجره جدید با عنوان "Minesweeper" ایجاد می‌کند.
- بازی Minesweeper را با شبکه 10x10 و 10 مین راه‌اندازی می‌کند.
- برنامه را در یک حلقه رویداد tkinter اجرا می‌کند تا پنجره باز بماند.

این کد ساده و پایه‌ای برای بازی Minesweeper است که می‌تواند با افزودن ویژگی‌های بیشتر گسترش یابد.