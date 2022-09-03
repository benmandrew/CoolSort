

import shlex
import subprocess
import numpy as np



def run_test(executable, power):
  command = shlex.split(
    "/usr/bin/time -v ./bin/{} {}".format(executable, power))
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
  
  executable = "mergesort"
  print("Executable: '{}'".format(executable))
  for power in range(12, 19):
    times = []
    # for i in range(n_tests):
      # print("\rRunning test {}/{} pow={}".format(i+1, n_tests, power), end="")
      # times.append(run_test(executable, power))
    # print("\rpow={} complete:                 ".format(power))
    time = run_test(executable, power) / 2000.0
    print("pow: {} - time: {}".format(power, time))
    # print(" Mean: {}\n SD: {}".format(
    #   np.mean(times), np.std(times)))


# print(output)

