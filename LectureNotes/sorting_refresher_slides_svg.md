---
marp: true
theme: default
paginate: true
header: "Algorithms Refresher — Sorting Algorithms"
footer: "Algorithms Course — Lesson 2"
---

# 🧮 Algorithms Refresher  
## Sorting Algorithms

**Insertion Sort · Merge Sort · QuickSort**

---

# 🎯 Lesson Goals

- Refresh key sorting algorithms:
  - **Insertion Sort**
  - **Merge Sort**
  - **QuickSort**
- Understand:
  - Basic idea
  - Step-by-step process
  - Time complexity
  - When to use each

---

# 📥 Insertion Sort — Idea

- Works like sorting playing cards in your hand.
- Builds the sorted list one element at a time.
- Each new element is **inserted** into its correct position in the already sorted portion.

---

# 🧩 Insertion Sort — Pseudocode

```text
for i = 1 to n-1:
    key = A[i]
    j = i - 1
    while j >= 0 and A[j] > key:
        A[j+1] = A[j]
        j = j - 1
    A[j+1] = key
```

---

# 🖼️ Insertion Sort — Visualization (SVG)

<!-- Inline SVG: three-step array transformation -->
<div style="text-align:center">
<svg width="700" height="140" xmlns="http://www.w3.org/2000/svg">
  <!-- Step labels -->
  <text x="40" y="20" font-size="14">Start</text>
  <text x="260" y="20" font-size="14">After inserting 1</text>
  <text x="480" y="20" font-size="14">Final</text>

  <!-- First array -->
  <g transform="translate(20,30)">
    <rect x="0" y="0" width="80" height="30" fill="none" stroke="#333"/>
    <text x="40" y="20" text-anchor="middle" font-size="14">3</text>
    <rect x="90" y="0" width="80" height="30" fill="none" stroke="#333"/>
    <text x="130" y="20" text-anchor="middle" font-size="14">1</text>
    <rect x="180" y="0" width="80" height="30" fill="none" stroke="#333"/>
    <text x="220" y="20" text-anchor="middle" font-size="14">2</text>
    <rect x="270" y="0" width="80" height="30" fill="none" stroke="#333"/>
    <text x="310" y="20" text-anchor="middle" font-size="14">4</text>
  </g>

  <!-- Second array -->
  <g transform="translate(240,30)">
    <rect x="0" y="0" width="80" height="30" fill="none" stroke="#333"/>
    <text x="40" y="20" text-anchor="middle" font-size="14">1</text>
    <rect x="90" y="0" width="80" height="30" fill="none" stroke="#333"/>
    <text x="130" y="20" text-anchor="middle" font-size="14">3</text>
    <rect x="180" y="0" width="80" height="30" fill="none" stroke="#333"/>
    <text x="220" y="20" text-anchor="middle" font-size="14">2</text>
    <rect x="270" y="0" width="80" height="30" fill="none" stroke="#333"/>
    <text x="310" y="20" text-anchor="middle" font-size="14">4</text>
  </g>

  <!-- Third array -->
  <g transform="translate(460,30)">
    <rect x="0" y="0" width="80" height="30" fill="none" stroke="#333"/>
    <text x="40" y="20" text-anchor="middle" font-size="14">1</text>
    <rect x="90" y="0" width="80" height="30" fill="none" stroke="#333"/>
    <text x="130" y="20" text-anchor="middle" font-size="14">2</text>
    <rect x="180" y="0" width="80" height="30" fill="none" stroke="#333"/>
    <text x="220" y="20" text-anchor="middle" font-size="14">3</text>
    <rect x="270" y="0" width="80" height="30" fill="none" stroke="#333"/>
    <text x="310" y="20" text-anchor="middle" font-size="14">4</text>
  </g>
</svg>
</div>

Step-by-step:
1. Insert `1` before `3` → `[1,3,2,4]`  
2. Insert `2` before `3` → `[1,2,3,4]`  
3. `4` already in place.

---

# ⏱️ Insertion Sort — Analysis

| Case | Comparisons | Time Complexity |
|------|--------------|----------------|
| Best (sorted input) | n-1 | **O(n)** |
| Average | ~n²/4 | **O(n²)** |
| Worst (reversed) | n²/2 | **O(n²)** |

✅ Simple, adaptive, in-place.  
❌ Slow for large datasets.

---

# ⚙️ Merge Sort — Idea

- **Divide and Conquer**:
  1. Divide the list into halves.
  2. Recursively sort each half.
  3. Merge the two sorted halves.

---

# 🧩 Merge Sort — Pseudocode

```text
merge_sort(A):
    if len(A) <= 1:
        return A
    mid = len(A) // 2
    left = merge_sort(A[:mid])
    right = merge_sort(A[mid:])
    return merge(left, right)
```

---

# 🔗 Merge Step — Visualization (SVG)

<div style="text-align:center">
<svg width="700" height="200" xmlns="http://www.w3.org/2000/svg">
  <!-- Root array -->
  <text x="20" y="20" font-size="13">[8 3 5 2 9 1]</text>

  <!-- Split arrows -->
  <line x1="120" y1="25" x2="220" y2="60" stroke="#333" stroke-width="1"/>
  <line x1="220" y1="60" x2="320" y2="95" stroke="#333" stroke-width="1"/>

  <!-- Left subtree -->
  <g transform="translate(180,50)">
    <text x="0" y="0" font-size="12">[8 3 5]</text>
    <line x1="20" y1="5" x2="-20" y2="35" stroke="#333"/>
    <line x1="20" y1="5" x2="60" y2="35" stroke="#333"/>
    <text x="-40" y="55" font-size="12">[8]</text>
    <text x="60" y="55" font-size="12">[3 5]</text>
    <text x="60" y="75" font-size="12">→ [3 5]</text>
  </g>

  <!-- Right subtree -->
  <g transform="translate(380,50)">
    <text x="0" y="0" font-size="12">[2 9 1]</text>
    <line x1="20" y1="5" x2="-20" y2="35" stroke="#333"/>
    <line x1="20" y1="5" x2="60" y2="35" stroke="#333"/>
    <text x="-40" y="55" font-size="12">[2]</text>
    <text x="60" y="55" font-size="12">[9 1]</text>
    <text x="60" y="75" font-size="12">→ [1 9]</text>
  </g>

  <!-- Final merge -->
  <text x="260" y="170" font-size="13">Merge → [1 2 3 5 8 9]</text>
</svg>
</div>

---

# ⏱️ Merge Sort — Analysis

| Case | Time Complexity | Space |
|------|------------------|--------|
| Best | O(n log n) | O(n) |
| Average | O(n log n) | O(n) |
| Worst | O(n log n) | O(n) |

✅ Guaranteed O(n log n).  
❌ Requires extra space.  
📦 Stable and predictable.

---

# ⚡ QuickSort — Idea

- Also **Divide and Conquer**, but smarter splitting:
  1. Choose a **pivot**.
  2. Partition array into:
     - smaller than pivot
     - pivot
     - larger than pivot
  3. Recursively sort the partitions.

---

# 🧩 QuickSort — Pseudocode

```text
quick_sort(A, low, high):
    if low < high:
        p = partition(A, low, high)
        quick_sort(A, low, p-1)
        quick_sort(A, p+1, high)
```

---

# 🔀 Partitioning — Visualization (SVG)

<div style="text-align:center">
<svg width="700" height="120" xmlns="http://www.w3.org/2000/svg">
  <text x="20" y="18" font-size="13">Start: [5 2 9 1 5 6] (pivot = 5)</text>

  <!-- Before partition -->
  <g transform="translate(20,30)">
    <rect x="0" y="0" width="60" height="28" fill="none" stroke="#333"/><text x="30" y="18" text-anchor="middle">5</text>
    <rect x="70" y="0" width="60" height="28" fill="none" stroke="#333"/><text x="100" y="18" text-anchor="middle">2</text>
    <rect x="140" y="0" width="60" height="28" fill="none" stroke="#333"/><text x="170" y="18" text-anchor="middle">9</text>
    <rect x="210" y="0" width="60" height="28" fill="none" stroke="#333"/><text x="240" y="18" text-anchor="middle">1</text>
    <rect x="280" y="0" width="60" height="28" fill="none" stroke="#333"/><text x="310" y="18" text-anchor="middle">5</text>
    <rect x="350" y="0" width="60" height="28" fill="none" stroke="#333"/><text x="380" y="18" text-anchor="middle">6</text>
  </g>

  <text x="20" y="75" font-size="13">After partitioning around 5 → [2 1 5 5 6 9]</text>

  <!-- After partition -->
  <g transform="translate(20,80)">
    <rect x="0" y="0" width="60" height="28" fill="none" stroke="#333"/><text x="30" y="18" text-anchor="middle">2</text>
    <rect x="70" y="0" width="60" height="28" fill="none" stroke="#333"/><text x="100" y="18" text-anchor="middle">1</text>
    <rect x="140" y="0" width="60" height="28" fill="none" stroke="#333"/><text x="170" y="18" text-anchor="middle">5</text>
    <rect x="210" y="0" width="60" height="28" fill="none" stroke="#333"/><text x="240" y="18" text-anchor="middle">5</text>
    <rect x="280" y="0" width="60" height="28" fill="none" stroke="#333"/><text x="310" y="18" text-anchor="middle">6</text>
    <rect x="350" y="0" width="60" height="28" fill="none" stroke="#333"/><text x="380" y="18" text-anchor="middle">9</text>
  </g>
</svg>
</div>

---

# ⏱️ QuickSort — Analysis

| Case | Time Complexity | Notes |
|------|------------------|--------|
| Best | O(n log n) | balanced splits |
| Average | O(n log n) | expected |
| Worst | O(n²) | unbalanced (e.g. sorted input with bad pivot) |

✅ Fast in practice, in-place.  
❌ Unstable; needs good pivot strategy.

---

# 🎯 Summary — Sorting Algorithms

| Algorithm | Best | Average | Worst | Stable | In-place |
|------------|-------|----------|--------|----------|-----------|
| Insertion | O(n) | O(n²) | O(n²) | ✅ | ✅ |
| Merge | O(n log n) | O(n log n) | O(n log n) | ✅ | ❌ |
| Quick | O(n log n) | O(n log n) | O(n²) | ❌ | ✅ |

---

# 💡 Visual Comparison (SVG)

<div style="text-align:center">
<svg width="700" height="100" xmlns="http://www.w3.org/2000/svg">
  <text x="20" y="20" font-size="13">Insertion — simple (small n)</text>
  <text x="20" y="40" font-size="13">Merge — guaranteed O(n log n)</text>
  <text x="20" y="60" font-size="13">Quick — fast on average</text>
</svg>
</div>

---

# 🧠 Key Takeaways

- **Insertion Sort** — simple, good for small or nearly sorted data.  
- **Merge Sort** — consistent, stable, predictable.  
- **QuickSort** — usually fastest, in-place.

---

# 🧩 Exercises — Conceptual

1. What makes Merge Sort’s time complexity always O(n log n)?  
2. Why does QuickSort’s performance degrade for already sorted input?  
3. For small arrays (n < 10), which algorithm would you use and why?  
4. Which algorithm is stable, and why does stability matter?  

---

# 🧮 Exercises — Practical

### 1. Trace Insertion Sort on:
`[8, 3, 5, 4, 6]`  
Show each step of the insertion.

### 2. Trace Merge Sort on:
`[7, 2, 9, 4]`  
Show the recursive splits and merges.

### 3. QuickSort Partitioning
Given `[4, 9, 2, 6, 1, 5]` and pivot = 4,  
show the partitioned array after one partition step.

---

# 🏁 End of Lesson

✅ Reviewed: Insertion, Merge, QuickSort  
🧩 Practiced: tracing and analysis  
📘 Next: **Lower bounds of sorting** and **non-comparison sorts**.

---
