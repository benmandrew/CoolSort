
import matplotlib.pyplot as plt
import numpy as np

cool_means = [
  # 0.0, #15
  0.00241, #16
  0.0101, #17
  0.0245, #18
  0.0553, #19
  0.126, #20
  0.283, #21
  0.619, #22
  1.34, #23 1.39
  2.85, #24 2.87
  6.12, #25
  12.56, #26
]
cool_sds = [
  # 0.0, #15
  0.0042, #16
  0.0039, #17
  0.005, #18
  0.005, #19
  0.006, #20
  0.009, #21
  0.012, #22
  0.019, #23
  0.067, #24
  0.388, #25
  0.181, #26
]

merge_means = [
  # 0.0, #15
  0.00429, #16
  0.0145, #17
  0.031, #18
  0.066, #19
  0.146, #20
  0.317, #21
  0.689, #22
  1.483, #23
  3.11, #24
  6.48, #25
  13.47, #26
]
merge_sds = [
  # 0.0, #15
  0.00495, #16
  0.0039, #17
  0.005, #18
  0.006, #19
  0.014, #20
  0.0099, #21
  0.012, #22
  0.021, #23
  0.049, #24
  0.073, #25
  0.11, #26
]

insertion_means = [
  0.486, #15
  1.90, #16
  7.73, #17
  30.7, #18
]
insertion_sds = [
  0.019, #15
  0.037, #16
  0.275, #17
  0.426, #18
]

MIN = 16

xs = [pow(2, i) for i in range(MIN, 27)]

baseline = [1.0 for _ in range(MIN, 27)]

ratios = np.array([(x / y if y != 0.0 else 0.0) for x, y in zip(cool_means, merge_means)])

err_ratios = np.array([(x * y) / (z * w) for x, y, z, w in zip(cool_sds, merge_sds, cool_means, merge_means)])

plt.xscale('log')
plt.ylim([0.0, 1.1])
plt.xlim([pow(2, MIN), pow(2, 26)])

plt.yticks(
  [x / float(10) for x in range(11)],
  [x * 10 for x in range(11)])
plt.xticks(
  [pow(2, x) for x in range(MIN, 27)],
  [x for x in range(MIN, 27)])
plt.minorticks_off()
# plt.plot(xs, cool_means)
# plt.plot(xs, merge_means)
plt.errorbar(xs, ratios)
plt.plot(xs, baseline)

plt.fill_between(xs, ratios - err_ratios, ratios + err_ratios, alpha=0.2)

plt.grid(which="both", axis="y")
plt.grid(which="major", axis="x")

plt.xlabel("log2(# of ints in array)")
plt.ylabel("Relative time (%)")

plt.savefig('out.png', dpi=300)

plt.show()







