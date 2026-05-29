# 🇯🇵 Coding Country Flags: Japan

A Python Turtle Graphics project that draws the flag of Japan — the **Nisshōki** (日章旗) — programmatically, featuring the white rectangular field and the centered crimson red disc (*Hinomaru*).

---

## 📸 Preview

The program renders a white flag (ratio 2:3) with a crimson sun disc centered on a dark `#1A1A1A` background for visual contrast.

---

## 🚀 Getting Started

### Prerequisites

- Python 3.x (Turtle is part of the standard library — no extra installs needed)

### Run the Script

```bash
python japan_flag.py
```

A window will open and animate the flag drawing in real time. **Click anywhere on the window to close it.**

---

## 🛠️ How It Works

| Step | What It Does |
|------|-------------|
| **1. Canvas Setup** | Creates a 700×500 window with a dark background |
| **2. White Rectangle** | Draws the flag base using the official 2:3 width-to-height ratio (450×300 px) |
| **3. Red Disc** | Draws the *Hinomaru* centered at `(0, 0)` with a radius of 90 px |
| **4. Finish** | Hides the turtle cursor and waits for a click to exit |

---

## 🎨 Colors Used

| Element | Color | Hex Code |
|---------|-------|----------|
| Background | Dark Gray | `#1A1A1A` |
| Flag Base | Pure White | `#FFFFFF` |
| Sun Disc | Crimson Red | `#BC002D` |

> `#BC002D` is the **official crimson** specified in Japan's national flag law (*Act on National Flag and Anthem*, 1999).

---

## 📐 Flag Specifications

- **Aspect Ratio:** 2:3 (height : width)
- **Disc Diameter:** 3/5 of the flag's height
- **Disc Position:** Perfectly centered on the flag

---

## 📁 Project Structure

```
japan_flag/
└── japan_flag.py   # Main script
└── README.md       # This file
```

---

## 💡 Extending the Project

- 🌍 Draw flags of other countries using the same Turtle approach
- 🎞️ Record the animation using a screen recorder for short coding videos
- 🖼️ Export to an image using `screen.getcanvas().postscript()` and convert with Pillow

---

## 📜 License

This project is open source and free to use for educational purposes.
