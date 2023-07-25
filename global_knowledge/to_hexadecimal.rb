# La version 'triche' en 1 ligne pour Victor
# puts gets.chomp.to_i.to_s(16)



CHARS = (("0".."9").to_a + ("A".."F").to_a).freeze

def hexstring(i)
	return CHARS[i % 16]
end


def to_hex(number)

	quotient = number
	ret = []

	while quotient > 0 do
		reste = hexstring(quotient % 16)
		quotient = quotient / 16
		ret << reste
	end

	return ret.join.reverse
end

puts to_hex(ARGV[0].to_i)
