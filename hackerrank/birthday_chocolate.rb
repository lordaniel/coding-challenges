def birthday(s, d, m)
  st = Array.new(s.size)
  st[0] = s[0..m-1].sum
  ways = st[0] == d ? 1 : 0
  for i in 1..(s.size-m)
    st[i] = st[i-1] - s[i-1] + s[i+m-1]
    ways += 1 if st[i] == d
  end
  return ways
end
