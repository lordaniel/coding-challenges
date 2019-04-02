def allLongestStrings a
  a.reduce([]) do |r, v|
    f = r.first&.size.to_i
    v.size > f ? [v] : v.size == f ? r.push(v) : r
  end
end
