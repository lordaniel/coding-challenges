gets.chomp
a = gets.chomp.split(" ").map(&:to_i)

h = Hash.new(0)
a.each { |x| h[x] += 1 }
h = h.sort_by { |k, v| v }.reverse
k, v = h.first
v = a.size - v

puts v
if v > 0
  base_pos = a.index(k)
  range = base_pos..0
  (range.first).downto(range.last).each do |i|
    if a[i] != k
      puts "#{a[i] < k ? 1 : 2} #{i+1} #{i+2}"
    end
  end

  for i in base_pos..a.size-1
    if a[i] != k
      puts "#{a[i] < k ? 1 : 2} #{i+1} #{i}"
    end
  end
end
