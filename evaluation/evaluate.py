

import shlex
import subprocess
import numpy as np

def run_test(power):
  command = shlex.split(
    "/usr/bin/time -v ./coolsort {}".format(power))
  output = subprocess.run(
    command, stderr=subprocess.PIPE).stderr.decode('utf-8')
  time: float = None
  for line in output.split("\n"):
    if "User" in line:
        time = float(line.strip().split(" ")[3])
  if time is None:
    print("No User Time in:")
    print(output)
    raise Exception
  return time

if __name__ == "__main__":
  n_tests = 1000
  # for power in range(15, 27):
  power = 15
  times = []
  for i in range(n_tests):
    print("\rRunning test {}/{} pow={}".format(i+1, n_tests, power), end="")
    times.append(run_test(power))
  print("\rpow={} complete:                 ".format(power))

  print(" Mean: {}\n SD: {}".format(
    np.mean(times), np.std(times)))


# print(output)

