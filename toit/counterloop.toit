main:
  startTime := Time.now.ms-since-epoch
  endTime := startTime + 10000
  count := 0
  while Time.now.ms-since-epoch < endTime:
    count += 1
  print "Count: $count"