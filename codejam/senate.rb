STDOUT.sync = true

PARTIES = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

t = gets.to_i
t.times do |index|
  n = gets.to_i
  list = gets.split(" ").each_with_index.map do |x, i| 
           {val: x.to_i, party: PARTIES[i]}
         end
  
  print "Case ##{index+1}:"
  while !list.empty? do
    list.sort_by! { |hsh| hsh[:val] }.reverse!
    s = list.reduce(0) { |acc, x| acc + x[:val] }
    out = " #{list[0][:party]}"
    if s > 1 && s != 3
      pos = 1
      pos = 0 if list[0][:val] >= list[1][:val] + 2
      out = out + "#{list[pos][:party]}"
      list[pos][:val] -= 1
    end
    list[0][:val] -= 1
    print out
    list = list.select { |x| x[:val] > 0 }
  end
  puts ""
end
