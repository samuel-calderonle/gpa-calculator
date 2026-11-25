# 🌴 High School GPA Calculator

A sleek, custom-weighted GPA calculator built with Python and Streamlit for high school students taking Regular, Honors, AP, and Dual Enrollment courses.

🔗 **Live App:** [Launch GPA Calculator](https://getgpa.streamlit.app)

---

## Features
* **Custom District Weighting:** Calculates both Unweighted (4.0 scale) and Weighted GPAs (`+0.04` per credit for Honors, `+0.08` per credit for AP/Dual Enrollment).
* **Flexible Credit Support:** Supports half-credit (`0.5`), full-year (`1.0`), and college Dual Enrollment (`3.0+`) courses.
* **Private Browser Storage:** Automatically saves your schedule locally in your browser's `localStorage` so your classes stay saved across refreshes without needing an account.
* **Custom Neon UI:** Built with a custom dark-mode theme and interactive grade slider.

## Preview
![App Screenshot](preview.png)

## Built With
* **Python 3**
* **[Streamlit](https://streamlit.io)** — Web UI framework
* **`streamlit-local-storage`** — Client-side persistence

## Run Locally
1. Clone the repository:
   ```bash
   git clone https://github.com
   cd high-school-gpa-calculator
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Launch the app:
   ```bash
   streamlit run app.py
   ```
