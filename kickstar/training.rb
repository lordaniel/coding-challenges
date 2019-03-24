STDOUT.sync = true
t = gets.to_i
t.times do |index|
  n, p = gets.split(" ").map(&:to_i)
  s = gets.split(" ").map(&:to_i).sort

  st = Array.new(n)
  st[p-1] = (0..p-1).reduce(0) { |x, v| x += s[p-1] - s[v] }
  m = st[p-1]

  for i in p..n-1
    st[i] = s[i-p] - s[i-1]  + st[i-1] + (s[i] - s[i-1]) * (p-1)
    m = st[i] if st[i] < m
  end
  puts "Case ##{index+1}: #{m}"
end
