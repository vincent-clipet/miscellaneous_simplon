grades = []


# Handle input values
while grades.size < 9 do
	puts ">>> Enter a grade (0<=>20)      [#{grades.size}/9]"
	input = gets.chomp
	if input.to_i.to_s != input 			then puts ">>> #{input} is not a number !" 		; next end
	if input.to_i < 0 || input.to_i > 20	then puts ">>> #{input} should be 0 <=> 20 !" 	; next end
	grades << input.to_i
end
puts "\n>>> Notes : #{grades}"


# Process
avg = grades.sum / grades.size.to_f
puts ">>> Average = #{avg}"
puts ">>> Congrats !" if avg > 15

