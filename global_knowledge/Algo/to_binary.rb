def to_binary(number)
	ret = []
	(0..30).to_a.reverse.each do | index |
		bit_max_value = 2 ** index
		if number < bit_max_value then
			ret << 0
		else
			ret << 1
			number -= bit_max_value
		end
	end
	return ret.map(&:to_s).join("")
end

puts to_binary(ARGV[0].to_i)
