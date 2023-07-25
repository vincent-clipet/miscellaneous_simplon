CHARS = (("0".."9").to_a + ("A".."F").to_a).join

number = ARGV[0].to_i
ret = []

while number > 0 do
  remainder = CHARS[number % 16]
  number /= 16
  ret << remainder
end

puts ret.join.reverse
