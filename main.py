from epidemic_models import SIRModel
import matplotlib.pyplot as plt
import numpy as np

m = SIRModel(0.00218, 0.5, 5000, 1, 0, 0.05)

time_frame = m.run(100)

plt.plot(time_frame, m.S_history, color = "black", label = "Susceptible")
plt.plot(time_frame, m.I_history, color = "red", label = "Infected")
plt.plot(time_frame, m.R_history, color = "green", label = "Recovered")
plt.title(f"COVID-19 SIR Model R_0 = {m.R0()}")
plt.legend()
plt.xlabel("Month")
plt.ylabel("# of People")
plt.show()