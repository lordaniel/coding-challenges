gets.chomp
a = gets.chomp.split(" ").map(&:to_i)
even = a.select(&:even?).sort
odd = a.select(&:odd?).sort

elements_sum = 0
even_size_diff = even.size - odd.size - 1
odd_size_diff = odd.size - even.size - 1

elements_sum = even[0..even_size_diff-1].reduce(0, :+) if even_size_diff > 0 
elements_sum = odd[0..odd_size_diff-1].reduce(0,:+) if odd_size_diff > 0 

puts elements_sum
