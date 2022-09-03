
import matplotlib.pyplot as plt
import numpy as np

cool_means = np.array([
  0.0002, #12
  0.0004, #13
  0.00085, #14
  0.0018, #15
  0.004, #16
  0.008, #17
  0.0168, #18
  0.0358, #19
  0.0756, #20
  0.172, #21
  0.369, #22
  0.794, #23
  2.85, #24
  6.12, #25
  12.56, #26
])
cool_sds = np.array([
  0.0, #12
  0.0, #13
  0.0, #14
  0.0, #15
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
])

merge_means = np.array([
  0.00032, #12
  0.00068, #13
  0.00144, #14
  0.00302, #15
  0.007, #16
  0.0137, #17
  0.0278, #18
  0.0595, #19
  0.133, #20
  0.299, #21
  0.643, #22
  1.483, #23
  3.11, #24
  6.48, #25
  13.47, #26
])
merge_sds = np.array([
  0.0, #12
  0.0, #13
  0.0, #14
  0.0, #15
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
])

insertion_means = np.array([
  0.029, #12
  0.12, #13
  0.49, #14
  2.01, #15
  7.94, #16
  64.3, #17
])
insertion_sds = np.array([
  0.0032, #12
  0.001, #13
  0.003, #14
  0.03, #15
  0.05, #16
  0.1, #17
])

MIN = 12

plt.xscale("log")

xs = np.array([pow(2, i) for i in range(MIN, 27)])

baseline = np.array([1.0 for _ in range(MIN, 27)])

ratios = np.array([(x / y if y != 0.0 else 0.0) for x, y in zip(cool_means, merge_means)])

err_ratios = np.array([(x * y) / (z * w) for x, y, z, w in zip(cool_sds, merge_sds, cool_means, merge_means)])

insertion_xs = np.array([pow(2, i) for i in range(MIN, 18)])

plt.xlim([pow(2, MIN), pow(2, 26)])
plt.xticks(
  [pow(2, x) for x in range(MIN, 27)],
  [x for x in range(MIN, 27)])
plt.minorticks_off()
line_cool, _, _ = plt.errorbar(xs, cool_means).lines
# plt.fill_between(xs, cool_means - cool_sds, cool_means + cool_sds, alpha=0.2)
line_merge, _, _ = plt.errorbar(xs, merge_means).lines
# plt.fill_between(xs, merge_means - merge_sds, merge_means + merge_sds, alpha=0.2)

line_insertion, _, _ = plt.errorbar(insertion_xs, insertion_means).lines
# plt.fill_between(insertion_xs, insertion_means - insertion_sds, insertion_means + insertion_sds, alpha=0.2)
plt.ylim([0.0, 15.0])
# plt.xticks(
#   [x * 10_000_000 for x in range(0, 7)],
#   [str(x * 10) for x in range(0, 7)])


# plt.ylim([0.0, 1.1])
# line_ratios, _, _ = plt.errorbar(xs, ratios).lines
# line_baseline, = plt.plot(xs, baseline)
# plt.fill_between(xs, ratios - err_ratios, ratios + err_ratios, alpha=0.2)
# plt.yticks(
#   [x / float(10) for x in range(11)],
#   [x * 10 for x in range(11)])


plt.grid(which="both", axis="y")
plt.grid(which="major", axis="x")

plt.xlabel("log2(# of ints in array)")
plt.ylabel("Time (s)")

plt.legend(
  [line_insertion, line_cool, line_merge],
  ["Insertion Sort", "Cool Sort", "Merge Sort"],
  loc="upper right")

plt.savefig('out.png', dpi=300)

plt.show()







