def powersOfTwo n
  a = []
  b = 12
  while n > 0
    t = 2**b
    if t <= n
      n -= t
      a.push t
    end
    b -= 1
  end
  a.reverse
end
