STDOUT.sync = true

t = gets.to_i
t.times do |x|
  s = gets.chomp
  last_digit, pending_parenthesis = 0, 0
  sp = ""

  s.each_char do |c|
    digit = c.to_i
    if digit > last_digit
      diff = digit - last_digit
      sp += "(" * diff
      pending_parenthesis += diff
    end
    if digit < last_digit
      diff = last_digit - digit
      sp += ")" * diff
      pending_parenthesis -= diff
    end
    sp += c
    last_digit = digit
  end

  sp += ")" * pending_parenthesis if pending_parenthesis > 0

  puts "Case ##{x+1}: #{sp}"
end
