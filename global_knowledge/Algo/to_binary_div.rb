def to_binary(number)
	
	quotient = number
	ret = []

	while quotient > 0 do
		reste = quotient % 2
		quotient = quotient / 2
		ret << reste
	end
	
	return ret.join.reverse
end

puts to_binary(ARGV[0].to_i)