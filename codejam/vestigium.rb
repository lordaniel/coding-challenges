STDOUT.sync = true

t = gets.to_i
t.times do |x|
  n = gets.to_i
  matrix = []
  k, r, c = [0, 0, 0]

  n.times do |i|
    matrix << gets.chomp.split(" ").map(&:to_i)
    r += 1 unless matrix.last.uniq.count ==  matrix.last.count
    k += matrix.last[i]
  end

  matrix.transpose.each { |col| c += 1 unless col.uniq.count == col.count}

  puts "Case ##{x + 1}: #{k} #{r} #{c}"
end
