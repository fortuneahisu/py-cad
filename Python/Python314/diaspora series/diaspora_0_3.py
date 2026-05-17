import matplotlib.pyplot as plt
import numpy as np

# 1. Setup Time (0 to 200 minutes)
time = np.linspace(0, 200, 1000)

# 2. Define the "Flip Point" (When we plug it in)
FLIP_POINT = 100


# 3. Create the Life Cycle Logic
def battery_cycle(t):
    """Simulates the battery life cycle based on the time 't'."""
    if t <= FLIP_POINT:
        # DISCHARGE PHASE (Your "Perfect Zero" Math)
        # Using your calculated constant 21.66
        val = 10.1 - (np.exp(t / 21.6679) * 0.1)
    else:
        # RECHARGE PHASE (Logarithmic - it slows down as it fills)
        # We start from 0 and climb back to 10.
        time_since_plugged_in = t - FLIP_POINT
        val = 10 * (1 - np.exp(-time_since_plugged_in / 25))
    return np.clip(val, 0, 10.1)


# Apply the logic to every point in time
battery_life = [battery_cycle(t) for t in time]

# 4. Visualization
plt.figure(figsize=(10, 6), facecolor="black")
ax = plt.gca()
ax.set_facecolor("black")

plt.plot(time, battery_life, color="#00FFCC", lw=3, label="Lithium Cycle")
plt.axvline(x=FLIP_POINT, color="white", linestyle="--", label="Plugged In")

# Aesthetics
plt.title("Battery Life Cycle: From Dead to Full", color="white", fontsize=18)
plt.ylabel("Voltage / Capacity", color="white")
plt.xlabel("Time (Minutes)", color="white")
plt.grid(color="gray", linestyle=":", alpha=0.4)
plt.tick_params(colors="white")
plt.legend()
plt.show()
