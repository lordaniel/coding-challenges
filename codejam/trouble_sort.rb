STDOUT.sync = true

def trouble_sort(array)
  a = []
  b = []
  c = []
  array.each_with_index { |val, i| i%2==1 ? a.push(val) : b.push(val) }
  a.sort!
  b.sort!
  for i in 0..(a.size + b.size - 1)
    i%2==1 ? c[i] = a.shift : c[i] = b.shift
    return i-1 if i>0 && c[i-1] > c[i]
  end
  return -1
end

t = gets.to_i
t.times do |index|
  n = gets.to_i
  array = gets.chomp.split(' ').map(&:to_i)
  out = trouble_sort(array)
  puts "Case ##{index+1}: #{out == -1 ? 'OK' : out}"
end
