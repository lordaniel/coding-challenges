STDOUT.sync = true

t = gets.to_i
t.times do |index|
  n, d = gets.chomp.split(" ").map(&:to_i)
  max_time = 0.0
  d.times do
    k, s = gets.chomp.split(" ").map(&:to_i)
    k_time = (n - k) / (s * 1.0)
    max_time = k_time if k_time > max_time
  end
  puts "Case ##{index + 1}: #{n / max_time}"
end
