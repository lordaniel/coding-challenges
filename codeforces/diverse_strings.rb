alphabet = "abcdefghijklmnopqrstuvwxyz"
t = gets.to_i

t.times do
  word = gets.chomp
  puts alphabet.include?(word.chars.sort.join) ? "Yes" : "No"
end
