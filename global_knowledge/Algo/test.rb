C='0123456789ABCDEF';i=ARGV[0].to_i;r=[];(r<<C[i%16];i/=16)while i>0;puts r.join.reverse
























































# CHARS = (("0".."9").to_a + ("A".."F").to_a).join
# number = ARGV[0].to_i
# ret = []

# while number > 0 do
#   ret << CHARS[number % 16]
#   number /= 16
# end

# puts ret.join.reverse

