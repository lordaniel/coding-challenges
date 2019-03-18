STDOUT.sync = true

def calc_damage(seq)
  actual_d = 1
  acc_d = 0
  seq.each_char { |c|  c == "C" ? actual_d *= 2 : acc_d += actual_d }
  return acc_d
end

def hack(s, seq)
  hack_times = 0
  while seq.include?("CS") do
    pos = seq.rindex("CS")
    tmp = seq[pos+1]
    seq[pos+1] = seq[pos]
    seq[pos] = tmp
    hack_times += 1
    return hack_times if s >= calc_damage(seq)
  end
  return "IMPOSSIBLE"
end

t = gets.to_i
t.times do |index|
  shield, seq = gets.chomp.split(" ")
  shield = shield.to_i
  print "Case ##{index + 1}: "
  if shield >= calc_damage(seq)
    puts 0
  else
    puts hack(shield, seq)
  end
end
