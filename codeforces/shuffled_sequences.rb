gets.chomp
a = gets.chomp.split(" ").map(&:to_i).sort

inc = [a.shift]
dec = []
a = a.reduce([]) do |acc, x|
      x > inc.last ? inc.push(x) : acc.push(x)
      acc
    end

a.reverse!

dec.push(a.shift) if a.size > 0
a = a.reduce([]) do |acc, x|
      x < dec.last ? dec.push(x) : acc.push(x)
      acc
    end

if a.size == 0
  puts "YES"
  puts inc.size
  inc.each_with_index { |x, i| print " " if i > 0; print x }
  print "\n"
  puts dec.size
  dec.each_with_index { |x, i| print " " if i > 0; print x }
  print "\n"
else
  puts "NO"
end
