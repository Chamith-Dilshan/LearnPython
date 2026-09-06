def hanoi_solver(n):
    """
    Solves the Tower of Hanoi puzzle and returns a string of all moves.

    Args:
        n (int): Number of disks

    Returns:
        str: String with starting arrangement and all moves, each on a new line.
             Rods are represented as lists separated by spaces.
    """

    # Initialize the three rods
    source = list(range(n, 0, -1))  # [n, n-1, ..., 2, 1]
    auxiliary = []
    destination = []

    # Store all states
    states = [f"{source} {auxiliary} {destination}"]

    def solve(num_disks, src, dest, aux):
        """Recursive helper to solve Tower of Hanoi."""
        if num_disks == 1:
            # Move disk from source to destination
            disk = src.pop()
            dest.append(disk)
            states.append(f"{source} {auxiliary} {destination}")
            return

        # Move n-1 disks from source to auxiliary using destination
        solve(num_disks - 1, src, aux, dest)

        # Move the largest disk from source to destination
        disk = src.pop()
        dest.append(disk)
        states.append(f"{source} {auxiliary} {destination}")

        # Move n-1 disks from auxiliary to destination using source
        solve(num_disks - 1, aux, dest, src)

    # Solve the puzzle
    solve(n, source, destination, auxiliary)

    # Return all states as a single string, one per line
    return "\n".join(states)


# Test it
if __name__ == "__main__":
    print(hanoi_solver(3))

"""
Let's break down the recursion step-by-step. This is actually a beautiful algorithmic pattern once you understand it.

---

## The Key Insight

**To move n disks from source to destination**, you don't think about moving all n disks at once. Instead, you break it into **three smaller subproblems**:

1. **Move n-1 disks** from source to auxiliary (using destination as a helper)
2. **Move the largest disk** from source to destination (the one disk you can move directly)
3. **Move n-1 disks** from auxiliary to destination (using source as a helper)

This is the **recursive pattern**. Each time you call `solve()`, you're solving a smaller version of the same problem.

---

## Visual Example: n = 3

Let me trace through `hanoi_solver(3)` in detail.

### Initial Setup
```
Source:      Auxiliary:    Destination:
  [3]          []            []
  [2]
  [1]
```

We need to move all 3 disks to Destination.

---

### The Recursive Breakdown

```
solve(3, source, destination, auxiliary)
│
├─ Step 1: solve(2, source, auxiliary, destination)
│          "Move 2 disks from source to auxiliary using destination"
│
├─ Step 2: Move disk 3 from source to destination
│          (The largest disk moves directly)
│
└─ Step 3: solve(2, auxiliary, destination, source)
           "Move 2 disks from auxiliary to destination using source"
```

Let's expand **Step 1** — `solve(2, source, auxiliary, destination)`:

```
solve(2, source, auxiliary, destination)
│
├─ Step 1.1: solve(1, source, destination, auxiliary)
│            "Move 1 disk from source to destination"
│
├─ Step 1.2: Move disk 2 from source to auxiliary
│
└─ Step 1.3: solve(1, destination, auxiliary, source)
             "Move 1 disk from destination to auxiliary"
```

And **Step 1.1** — `solve(1, source, destination, auxiliary)` hits the **BASE CASE**:

```python
if num_disks == 1:
    disk = src.pop()      # Remove disk 1 from source
    dest.append(disk)     # Add disk 1 to destination
    states.append(...)    # Record this state
    return                # Stop recursing
```

---

## Complete Trace for n = 3

Let me show **exactly** what happens at each recursive level:

### Level 1: `solve(3, source, destination, auxiliary)`

```
Before Step 1: source=[3,2,1]  auxiliary=[]  destination=[]

Step 1: Call solve(2, source, auxiliary, destination)
        "Move 2 disks from source to auxiliary, using destination"
        ↓ (Recursing deeper...)
```

### Level 2: `solve(2, source, auxiliary, destination)`

```
Before Step 1.1: source=[3,2,1]  auxiliary=[]  destination=[]

Step 1.1: Call solve(1, source, destination, auxiliary)
          "Move 1 disk from source to destination"
          ↓ (Recursing deeper...)
```

### Level 3: `solve(1, source, destination, auxiliary)` — BASE CASE!

```
num_disks == 1, so:
  disk = src.pop()        → disk=1, source=[3,2]
  dest.append(disk)       → destination=[1]
  Record: source=[3,2]  auxiliary=[]  destination=[1]
  RETURN (stop recursing, go back up)
```

**State 1:** `[3, 2] [] [1]`

---

### Back to Level 2: `solve(2, source, auxiliary, destination)` — Step 1.2

```
Now that solve(1, ...) returned, we continue:

Step 1.2: Move disk 2 from source to auxiliary
  disk = src.pop()        → disk=2, source=[3]
  dest.append(disk)       → auxiliary=[2]
  Record: source=[3]  auxiliary=[2]  destination=[1]
```

**State 2:** `[3] [2] [1]`

Then Step 1.3:

```
Step 1.3: Call solve(1, destination, auxiliary, source)
          "Move 1 disk from destination to auxiliary"
          ↓ (Recursing deeper...)
```

### Level 3 again: `solve(1, destination, auxiliary, source)` — BASE CASE!

```
num_disks == 1, so:
  disk = src.pop()        → disk=1, destination=[]
  dest.append(disk)       → auxiliary=[2,1]
  Record: source=[3]  auxiliary=[2,1]  destination=[]
  RETURN
```

**State 3:** `[3] [2, 1] []`

---

### Back to Level 1: `solve(3, source, destination, auxiliary)` — Step 2

```
Now that solve(2, source, auxiliary, destination) returned,
we can move the largest disk:

Step 2: Move disk 3 from source to destination
  disk = src.pop()        → disk=3, source=[]
  dest.append(disk)       → destination=[3]
  Record: source=[]  auxiliary=[2,1]  destination=[3]
```

**State 4:** `[] [2, 1] [3]`

Then Step 3:

```
Step 3: Call solve(2, auxiliary, destination, source)
        "Move 2 disks from auxiliary to destination, using source"
        ↓ (Recursing deeper...)
```

### Level 2 again: `solve(2, auxiliary, destination, source)`

This follows the same pattern as before:

```
Step 1: solve(1, auxiliary, source, destination)
        → Disk 1 moves from auxiliary to source
        Record: [1]  []  [3]
        
Step 2: Move disk 2 from auxiliary to destination
        Record: [1]  []  [3, 2]
        
Step 3: solve(1, source, destination, auxiliary)
        → Disk 1 moves from source to destination
        Record: []  []  [3, 2, 1]
```

**States 5-7:**
- `[1] [2] [3]`
- `[1] [] [3, 2]`
- `[] [] [3, 2, 1]` ✅

---

## The Call Stack Visualization

Here's what the **call stack** looks like as the recursion goes deeper:

```
solve(3, src, dest, aux)
  └─ solve(2, src, aux, dest)
       └─ solve(1, src, dest, aux)      ← BASE CASE HIT
       ← Returns to solve(2)
     ← Returns to solve(3)
  └─ [Move disk 3]
  └─ solve(2, aux, dest, src)
       └─ solve(1, aux, src, dest)      ← BASE CASE HIT
       ← Returns to solve(2)
     ← Returns to solve(3)
   ← Returns to main
```

---

## Why This Works: The Logic

**The genius is**: once you've moved the top n-1 disks to the auxiliary rod, the largest disk is **free to move** directly to the destination. You don't have to worry about the n-1 disks above it anymore—they're out of the way!

Then once the largest disk is on the destination, you need to move those n-1 disks on top of it, using the now-empty source as a helper.

```
BEFORE:          MIDDLE:          AFTER:
Src  Aux  Dest   Src  Aux  Dest   Src  Aux  Dest
 3           →   →    3   ∅   →   ∅           3
 2           →  (2)  ( )  [3] →   ∅    2      3
 1           →   1    1           1    (1)    (2,1)
                                       
Step 1:       Step 2:            Step 3:
Move n-1      Move largest       Move n-1
to Aux        to Dest            to Dest
```

---

## Code Breakdown: What Each Part Does

```python
def solve(num_disks, src, dest, aux):
    if num_disks == 1:
        # ✅ BASE CASE: Move 1 disk (stop recursing)
        disk = src.pop()
        dest.append(disk)
        states.append(...)
        return
    
    # ✅ RECURSIVE CASE 1: Move n-1 disks OUT OF THE WAY
    solve(num_disks - 1, src, aux, dest)
    
    # ✅ MOVE THE BIGGEST DISK (it's now free!)
    disk = src.pop()
    dest.append(disk)
    states.append(...)
    
    # ✅ RECURSIVE CASE 2: Move the n-1 disks ON TOP
    solve(num_disks - 1, aux, dest, src)
```

---

## Key Points to Remember

| Concept | Explanation |
|---------|-------------|
| **Base case (n=1)** | Move 1 disk directly—no recursion needed |
| **Recursive case (n>1)** | Break into 3 steps: move n-1 away, move 1 disk, move n-1 back |
| **Parameter swapping** | Notice how `destination`, `auxiliary`, `source` swap roles in each call |
| **Depth** | For n=3, recursion goes **3 levels deep** before hitting the base case |
| **Total calls** | `solve(3)` makes 7 calls total: solve(3), solve(2) twice, solve(1) four times |
| **Moves** | Each base case (when n=1) **produces one move**. With n=3, we hit the base case 4 times = 4 moves... wait, actually 7 moves total including non-base-case moves |

---

Does this make it clearer? Try tracing through `hanoi_solver(2)` yourself to solidify the pattern!
"""
