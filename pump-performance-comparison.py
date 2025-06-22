import matplotlib.pyplot as plt

# Theoretical data
flow_theoretical = [0, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1424]
head_theoretical = [None, 209.91, 209.9567031, 209.9338537, 209.6622491, 209.1321933, 207.0220637, 
                    202.2152848, 194.8147593, 183.7576375, 169.7584209, 154.0021374, 136.1393233, 
                    116.7233238, 96.81216554, None]
bowl_power_theoretical = [23.36692317, 26.38115149, 28.67758735, 31.14755367, 34.00631172, 38.19671698,
                          41.42346532, 44.60958066, 47.79471496, 49.92024436, 50.98238991, 52.04451105,
                          53.10667629, 54.11510601, 55.23090931, 55.23090931]
npshr_theoretical = [0.265, 0, None, 5.576317535, 6.372110861, 6.372342927, 7.965138577, 8.761647992, 
                     9.558166292, 11.15118651, 12.74913406, 15.13093363, 18.3181586, 22.30225468, 
                     28.66199697, None]
efficiency_theoretical = [None, 20.941, 37.85133563, 52.03451165, 62.95488272, 71.03968985, 76.85437857,
                          81.14961469, 83.75275052, 84.7560677, 83.762557, 80.85911432, 76.3929529,
                          69.57347311, 61.33620766, None]

# Experimental data
flow_experimental = [1582.839821, 1495.305392, 1415.559274, 1344.736101, 1256.983935]
head_experimental = [152.2899759, 137.0609783, 123.8319808, 112.6029832, 99.37398558]
bowl_power_experimental = [29.23056691, 31.34680704, 37.43099744, 40.47309264, 46.55728304]
npsha_experimental = [-23.62329085, -21.35777673, -19.38939268, -17.71827771, -15.74910771]
efficiency_experimental = [205.7604319, 163.1327779, 116.8477339, 93.34936856, 66.94306962]

# Plotting in a 2x2 grid
fig, axs = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Comparison of Theoretical and Experimental Pump Performance', fontsize=16)

# Plot 1: Flow vs. Head
axs[0, 0].plot(flow_theoretical, head_theoretical, 'bo-', label='Theoretical Head', markersize=5)
axs[0, 0].plot(flow_experimental, head_experimental, 'ro-', label='Experimental Head', markersize=5)
axs[0, 0].set_xlabel('Flow (U.S. gallons per minute)')
axs[0, 0].set_ylabel('Head (feet)')
axs[0, 0].legend()
axs[0, 0].grid(True)

# Plot 2: Flow vs. Bowl Power
axs[0, 1].plot(flow_theoretical, bowl_power_theoretical, 'bo-', label='Theoretical Bowl Power', markersize=5)
axs[0, 1].plot(flow_experimental, bowl_power_experimental, 'ro-', label='Experimental Bowl Power', markersize=5)
axs[0, 1].set_xlabel('Flow (U.S. gallons per minute)')
axs[0, 1].set_ylabel('Bowl Power (bhp)')
axs[0, 1].legend()
axs[0, 1].grid(True)

# Plot 3: Flow vs. NPSH (NPSHR for theoretical and NPSHA for experimental)
axs[1, 0].plot(flow_theoretical, npshr_theoretical, 'bo-', label='Theoretical NPSHR', markersize=5)
axs[1, 0].plot(flow_experimental, npsha_experimental, 'ro-', label='Experimental NPSHA', markersize=5)
axs[1, 0].set_xlabel('Flow (U.S. gallons per minute)')
axs[1, 0].set_ylabel('NPSH (feet)')
axs[1, 0].legend()
axs[1, 0].grid(True)

# Plot 4: Flow vs. Efficiency
axs[1, 1].plot(flow_theoretical, efficiency_theoretical, 'bo-', label='Theoretical Efficiency', markersize=5)
axs[1, 1].plot(flow_experimental, efficiency_experimental, 'ro-', label='Experimental Efficiency', markersize=5)
axs[1, 1].set_xlabel('Flow (U.S. gallons per minute)')
axs[1, 1].set_ylabel('Efficiency (%)')
axs[1, 1].legend()
axs[1, 1].grid(True)

# Adjust layout and show plot
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()
